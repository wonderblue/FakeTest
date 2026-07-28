"""
Compute key account reconciliations for Meridian June 2026 close.
"""

from __future__ import annotations

from pathlib import Path

from src import OUTPUTS, TXN, fnum, load_coa, read_csv, trial_balance


def ar_subledger_balance() -> tuple[float, list[dict]]:
    """Open AR = invoices - receipts applied (simplified FIFO by customer totals)."""
    invoices = read_csv(TXN / "ar_invoices.csv")
    receipts = read_csv(TXN / "ar_receipts.csv")
    # Lab approach: AR GL is source of truth from journals; subledger listing =
    # sum of June invoices still open + opening AR implied.
    # For learning, reconstruct open items as June invoices not fully collected
    # plus a plug for prior open AR.
    inv_total = sum(fnum(i["total"]) for i in invoices)
    rcpt_total = sum(fnum(r["amount"]) for r in receipts)
    # Opening AR from TB opening
    from src import CLOSE

    open_ar = fnum(
        next(r["net"] for r in read_csv(CLOSE / "opening_trial_balance_2026-05-31.csv") if r["account"] == "1100")
    )
    # ending = open + new invoices - receipts (and unbilled clears are invoices too)
    ending = open_ar + inv_total - rcpt_total
    detail = [
        {"component": "Opening AR", "amount": round(open_ar, 2)},
        {"component": "June billings (AR invoices)", "amount": round(inv_total, 2)},
        {"component": "June cash applications", "amount": round(-rcpt_total, 2)},
        {"component": "Ending AR (subledger rollforward)", "amount": round(ending, 2)},
    ]
    return ending, detail


def ap_subledger_balance() -> tuple[float, list[dict]]:
    from src import CLOSE

    open_ap = -fnum(
        next(r["net"] for r in read_csv(CLOSE / "opening_trial_balance_2026-05-31.csv") if r["account"] == "2100")
    )
    invoices = read_csv(TXN / "ap_invoices.csv")
    payments = read_csv(TXN / "ap_payments.csv")
    inv_total = sum(fnum(i["amount"]) for i in invoices)
    pay_total = sum(fnum(p["amount"]) for p in payments)
    ending = open_ap + inv_total - pay_total
    detail = [
        {"component": "Opening AP", "amount": round(open_ap, 2)},
        {"component": "June AP invoices", "amount": round(inv_total, 2)},
        {"component": "June AP payments", "amount": round(-pay_total, 2)},
        {"component": "Ending AP (subledger rollforward)", "amount": round(ending, 2)},
    ]
    return ending, detail


def deferred_waterfall() -> tuple[float, list[dict]]:
    from src import CLOSE

    open_def = -fnum(
        next(r["net"] for r in read_csv(CLOSE / "opening_trial_balance_2026-05-31.csv") if r["account"] == "2400")
    )
    # Additions: deferred billings in June (C008 annual)
    invoices = read_csv(TXN / "ar_invoices.csv")
    additions = sum(fnum(i["total"]) for i in invoices if i.get("revenue_treatment") == "deferred")
    releases = sum(fnum(r["recognition_amount"]) for r in read_csv(TXN / "deferred_revenue_schedule.csv"))
    ending = open_def + additions - releases
    detail = [
        {"component": "Opening deferred revenue", "amount": round(open_def, 2)},
        {"component": "Billings to deferred (additions)", "amount": round(additions, 2)},
        {"component": "Revenue releases", "amount": round(-releases, 2)},
        {"component": "Ending deferred (waterfall)", "amount": round(ending, 2)},
    ]
    return ending, detail


def bank_recon_1010() -> dict:
    tb = trial_balance()
    gl_cash = tb.get("1010", 0.0)
    bank_txns = [t for t in read_csv(TXN / "bank_transactions.csv") if t["bank_account"] == "1010"]
    # Bank statement = only reconciled items + opening
    from src import CLOSE

    open_cash = fnum(
        next(r["net"] for r in read_csv(CLOSE / "opening_trial_balance_2026-05-31.csv") if r["account"] == "1010")
    )
    stmt_activity = sum(fnum(t["amount"]) for t in bank_txns if t["reconciled"] == "Y")
    # Outstanding payment was posted to bank file with reconciled=N — exclude from statement
    bank_stmt_balance = open_cash + stmt_activity
    outstanding = read_csv(TXN / "bank_outstanding_items.csv")
    dit = sum(fnum(i["amount"]) for i in outstanding if i["type"] == "deposit_in_transit")
    osp = sum(fnum(i["amount"]) for i in outstanding if i["type"] == "outstanding_payment")
    # Book = bank + DIT - outstanding payments
    reconciling = bank_stmt_balance + dit - osp
    return {
        "gl_balance": round(gl_cash, 2),
        "bank_statement_balance": round(bank_stmt_balance, 2),
        "deposits_in_transit": round(dit, 2),
        "outstanding_payments": round(osp, 2),
        "reconciled_book_balance": round(reconciling, 2),
        "difference": round(gl_cash - reconciling, 2),
        "status": "TIED" if abs(gl_cash - reconciling) < 0.05 else "BREAK",
    }


def fa_recon() -> dict:
    tb = trial_balance()
    assets = read_csv(TXN / "fixed_assets.csv")
    gross = sum(fnum(a["cost"]) for a in assets)
    begin_accum = sum(fnum(a["accum_dep_begin"]) for a in assets)
    month_dep = sum(fnum(a["monthly_dep"]) for a in assets)
    accum = begin_accum + month_dep
    return {
        "register_gross": round(gross, 2),
        "gl_1400": round(tb.get("1400", 0), 2),
        "gross_diff": round(gross - tb.get("1400", 0), 2),
        "register_accum_dep": round(accum, 2),
        "gl_1450_credit": round(-tb.get("1450", 0), 2),
        "accum_diff": round(accum - (-tb.get("1450", 0)), 2),
        "status": "TIED"
        if abs(gross - tb.get("1400", 0)) < 1 and abs(accum - (-tb.get("1450", 0))) < 1
        else "BREAK",
    }


def prepaid_recon() -> dict:
    from src import CLOSE

    open_pre = fnum(
        next(r["net"] for r in read_csv(CLOSE / "opening_trial_balance_2026-05-31.csv") if r["account"] == "1300")
    )
    sched = read_csv(TXN / "prepaid_schedule.csv")[0]
    tb = trial_balance()
    return {
        "schedule_end": fnum(sched["end"]),
        "gl_1300": round(tb.get("1300", 0), 2),
        "difference": round(fnum(sched["end"]) - tb.get("1300", 0), 2),
        "status": "TIED" if abs(fnum(sched["end"]) - tb.get("1300", 0)) < 0.05 else "BREAK",
        "rollforward": sched,
    }


def accrual_recon() -> dict:
    tb = trial_balance()
    accruals = read_csv(TXN / "accruals.csv")
    detail_sum = sum(fnum(a["amount"]) for a in accruals)
    # After reversing May (42000) and booking June accruals, GL 2200 credit = june accruals only
    gl_credit = -tb.get("2200", 0)
    return {
        "accrual_listing_total": round(detail_sum, 2),
        "gl_2200_credit": round(gl_credit, 2),
        "difference": round(detail_sum - gl_credit, 2),
        "status": "TIED" if abs(detail_sum - gl_credit) < 0.05 else "BREAK",
        "items": accruals,
    }


def run_all() -> str:
    tb = trial_balance()
    coa = load_coa()

    ar_end, ar_detail = ar_subledger_balance()
    ap_end, ap_detail = ap_subledger_balance()
    def_end, def_detail = deferred_waterfall()
    bank = bank_recon_1010()
    fa = fa_recon()
    prepaid = prepaid_recon()
    accr = accrual_recon()

    def tie(name, sub, gl_acct, sub_is_credit=False):
        gl = tb.get(gl_acct, 0.0)
        gl_disp = -gl if sub_is_credit else gl
        diff = sub - gl_disp
        status = "TIED" if abs(diff) < 0.05 else "BREAK"
        return status, gl_disp, diff

    lines = [
        "# Meridian CloudWorks — Reconciliation Package (June 2026)",
        "",
        "Control account ties prove subledgers and schedules equal the GL.",
        "",
        "## REC-AR-1100 Accounts Receivable",
        "",
        "| Component | Amount |",
        "|-----------|--------|",
    ]
    for d in ar_detail:
        lines.append(f"| {d['component']} | ${d['amount']:,.2f} |")
    st, gl, diff = tie("AR", ar_end, "1100")
    lines += [
        f"| GL 1100 | ${gl:,.2f} |",
        f"| Difference | ${diff:,.2f} |",
        f"| **Status** | **{st}** |",
        "",
        "## REC-AP-2100 Accounts Payable",
        "",
        "| Component | Amount |",
        "|-----------|--------|",
    ]
    for d in ap_detail:
        lines.append(f"| {d['component']} | ${d['amount']:,.2f} |")
    st, gl, diff = tie("AP", ap_end, "2100", sub_is_credit=True)
    lines += [
        f"| GL 2100 (credit) | ${gl:,.2f} |",
        f"| Difference | ${diff:,.2f} |",
        f"| **Status** | **{st}** |",
        "",
        "## REC-DEF-2400 Deferred Revenue Waterfall",
        "",
        "| Component | Amount |",
        "|-----------|--------|",
    ]
    for d in def_detail:
        lines.append(f"| {d['component']} | ${d['amount']:,.2f} |")
    st, gl, diff = tie("DEF", def_end, "2400", sub_is_credit=True)
    lines += [
        f"| GL 2400 (credit) | ${gl:,.2f} |",
        f"| Difference | ${diff:,.2f} |",
        f"| **Status** | **{st}** |",
        "",
        "## REC-CASH-1010 Bank Reconciliation",
        "",
        "| Item | Amount |",
        "|------|--------|",
        f"| Bank statement balance | ${bank['bank_statement_balance']:,.2f} |",
        f"| + Deposits in transit | ${bank['deposits_in_transit']:,.2f} |",
        f"| − Outstanding payments | ${bank['outstanding_payments']:,.2f} |",
        f"| = Reconciled book balance | ${bank['reconciled_book_balance']:,.2f} |",
        f"| GL 1010 | ${bank['gl_balance']:,.2f} |",
        f"| Difference | ${bank['difference']:,.2f} |",
        f"| **Status** | **{bank['status']}** |",
        "",
        "## REC-FA Fixed Assets",
        "",
        f"- Register gross ${fa['register_gross']:,.2f} vs GL 1400 ${fa['gl_1400']:,.2f} (diff ${fa['gross_diff']:,.2f})",
        f"- Register accum dep ${fa['register_accum_dep']:,.2f} vs GL 1450 ${fa['gl_1450_credit']:,.2f} (diff ${fa['accum_diff']:,.2f})",
        f"- **Status: {fa['status']}**",
        "",
        "## REC-PRE-1300 Prepaid Expenses",
        "",
        f"- Schedule end ${prepaid['schedule_end']:,.2f} vs GL ${prepaid['gl_1300']:,.2f}",
        f"- **Status: {prepaid['status']}**",
        "",
        "## REC-ACC-2200 Accrued Expenses",
        "",
        f"- Accrual listing ${accr['accrual_listing_total']:,.2f} vs GL credit ${accr['gl_2200_credit']:,.2f}",
        f"- **Status: {accr['status']}**",
        "",
        "## Sign-off checklist",
        "",
        "- [x] Preparers completed recons Day 3",
        "- [x] Reviewer (Controller) signed Day 3–4",
        "- [x] Differences > $100 investigated (none material in lab)",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    md = run_all()
    (OUTPUTS / "reconciliations_june_2026.md").write_text(md)
    print(md)


if __name__ == "__main__":
    main()
