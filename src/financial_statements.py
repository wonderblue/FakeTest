"""
Build trial balance, P&L, balance sheet, and cash flow for June 2026 close.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from src import CLOSE, OUTPUTS, ROOT, TXN, fnum, load_coa, read_csv, signed_for_fs, trial_balance

PERIOD = "2026-06"


def is_pnl(account: str, coa: dict) -> bool:
    t = coa.get(account, {}).get("type", "")
    return t in {"Revenue", "Expense", "Other Income", "Other Expense"}


def build_statements() -> dict:
    coa = load_coa()
    tb = trial_balance("2026-06")

    # TB rows
    tb_rows = []
    for acct in sorted(tb.keys()):
        if acct not in coa or coa[acct]["type"] == "Header":
            continue
        net = tb[acct]
        debit = net if net > 0 else 0.0
        credit = -net if net < 0 else 0.0
        tb_rows.append(
            {
                "account": acct,
                "name": coa[acct]["name"],
                "type": coa[acct]["type"],
                "debit": round(debit, 2),
                "credit": round(credit, 2),
                "net": round(net, 2),
            }
        )

    dr = sum(r["debit"] for r in tb_rows)
    cr = sum(r["credit"] for r in tb_rows)

    # Income statement
    revenue = {}
    expenses = {}
    other = {}
    for acct, net in tb.items():
        if acct not in coa or coa[acct]["type"] == "Header":
            continue
        t = coa[acct]["type"]
        amt = signed_for_fs(acct, net, coa)
        if t == "Revenue":
            revenue[acct] = amt
        elif t in {"Expense", "Other Expense"}:
            expenses[acct] = amt
        elif t == "Other Income":
            other[acct] = amt

    total_rev = sum(revenue.values())
    total_exp = sum(expenses.values())
    total_other = sum(other.values())
    net_income = total_rev - total_exp + total_other

    # Balance sheet — roll NI into retained earnings for presentation
    assets = {}
    liabilities = {}
    equity = {}
    for acct, net in tb.items():
        if acct not in coa or coa[acct]["type"] == "Header":
            continue
        if is_pnl(acct, coa):
            continue
        t = coa[acct]["type"]
        amt = signed_for_fs(acct, net, coa)
        if t in {"Asset", "Contra-Asset"}:
            # Contra-asset shown as negative asset / credit
            if t == "Contra-Asset":
                assets[acct] = -amt  # allowance/accum dep reduce assets
            else:
                assets[acct] = amt
        elif t == "Liability":
            liabilities[acct] = amt
        elif t == "Equity":
            equity[acct] = amt

    equity["3200"] = equity.get("3200", 0.0) + net_income

    total_assets = sum(assets.values())
    total_liab = sum(liabilities.values())
    total_eq = sum(equity.values())

    # Indirect cash flow (simplified)
    # Cash change from TB vs opening
    open_tb = {r["account"]: fnum(r["net"]) for r in read_csv(CLOSE / "opening_trial_balance_2026-05-31.csv")}
    cash_begin = open_tb.get("1010", 0) + open_tb.get("1020", 0)
    cash_end = -(-tb.get("1010", 0)) + -(-tb.get("1020", 0))  # net debit-positive
    cash_end = tb.get("1010", 0) + tb.get("1020", 0)
    # Opening was stored with debit positive for assets in net field
    delta_cash = cash_end - cash_begin

    def delta(acct: str) -> float:
        # change in debit-positive balance
        return tb.get(acct, 0.0) - open_tb.get(acct, 0.0)

    # Working capital adjustments (increase in asset = use of cash)
    # Sign convention: positive = source of cash. For assets, -Δ; for liabilities/contra, -Δ
    # also works because liability increases make Δ more negative.
    cfo_adjustments = {
        "net_income": net_income,
        "add_back_depreciation": -delta("1450"),
        "add_back_bad_debt_provision": -delta("1150"),
        "change_in_ar": -delta("1100"),
        "change_in_unbilled_ar": -delta("1200"),
        "change_in_prepaid": -delta("1300"),
        "change_in_ap": -delta("2100"),
        "change_in_accrued_expenses": -delta("2200"),
        "change_in_accrued_payroll": -delta("2300"),
        "change_in_deferred_revenue": -delta("2400"),
        "change_in_sales_tax_payable": -delta("2500"),
    }
    # For liabilities, open_tb net is negative (credit). Increase in liability = more negative delta.
    # Cash from increase in liability = -(delta) when delta is debit-positive convention:
    # e.g. AP open -156000, end -180000, delta -24000 → cash +24000 = -delta. Good.
    # For assets: AR open +412500, end +450000, delta +37500 → cash -37500 = -delta. Good.
    # Depreciation: accum dep open -98000, end -103739, delta -5739 → -delta = +5739. Good.

    cfo = sum(cfo_adjustments.values())
    # Capex = increase in FA gross
    capex = -max(delta("1400"), 0.0)
    cfi = capex
    # Financing none
    cff = 0.0
    # Plug reconciling difference into CFO other for learning transparency
    implied = cfo + cfi + cff
    plug = delta_cash - implied
    cfo_adjustments["other_reconciling"] = plug
    cfo = sum(v for k, v in cfo_adjustments.items())

    statements = {
        "period": PERIOD,
        "trial_balance_balanced": abs(dr - cr) < 0.05,
        "trial_balance_debits": round(dr, 2),
        "trial_balance_credits": round(cr, 2),
        "income_statement": {
            "revenue": {k: round(v, 2) for k, v in revenue.items()},
            "total_revenue": round(total_rev, 2),
            "expenses": {k: round(v, 2) for k, v in expenses.items()},
            "total_expenses": round(total_exp, 2),
            "other_income": {k: round(v, 2) for k, v in other.items()},
            "net_income": round(net_income, 2),
        },
        "balance_sheet": {
            "assets": {k: round(v, 2) for k, v in assets.items()},
            "total_assets": round(total_assets, 2),
            "liabilities": {k: round(v, 2) for k, v in liabilities.items()},
            "total_liabilities": round(total_liab, 2),
            "equity": {k: round(v, 2) for k, v in equity.items()},
            "total_equity": round(total_eq, 2),
            "total_liabilities_and_equity": round(total_liab + total_eq, 2),
            "balances": abs(total_assets - (total_liab + total_eq)) < 1.0,
        },
        "cash_flow_indirect": {
            "cash_beginning": round(cash_begin, 2),
            "cash_ending": round(cash_end, 2),
            "net_change": round(delta_cash, 2),
            "operating": {k: round(v, 2) for k, v in cfo_adjustments.items()},
            "operating_total": round(cfo, 2),
            "investing": {"capex": round(cfi, 2)},
            "financing": {"total": round(cff, 2)},
        },
        "trial_balance": tb_rows,
    }
    return statements


def render_markdown(stmt: dict) -> str:
    coa = load_coa()
    is_ = stmt["income_statement"]
    bs = stmt["balance_sheet"]
    cf = stmt["cash_flow_indirect"]
    lines = [
        f"# Meridian CloudWorks — Financial Statements ({stmt['period']})",
        "",
        "## Income Statement",
        "",
        "| Account | Amount |",
        "|---------|--------|",
    ]
    for a, v in is_["revenue"].items():
        lines.append(f"| {a} {coa[a]['name']} | ${v:,.2f} |")
    lines.append(f"| **Total Revenue** | **${is_['total_revenue']:,.2f}** |")
    lines.append("| | |")
    for a, v in is_["expenses"].items():
        lines.append(f"| {a} {coa[a]['name']} | ${v:,.2f} |")
    lines.append(f"| **Total Expenses** | **${is_['total_expenses']:,.2f}** |")
    if is_["other_income"]:
        lines.append("| | |")
        for a, v in is_["other_income"].items():
            lines.append(f"| {a} {coa[a]['name']} | ${v:,.2f} |")
    lines += [
        "| | |",
        f"| **Net Income** | **${is_['net_income']:,.2f}** |",
        "",
        "## Balance Sheet",
        "",
        "### Assets",
        "",
        "| Account | Amount |",
        "|---------|--------|",
    ]
    for a, v in bs["assets"].items():
        lines.append(f"| {a} {coa[a]['name']} | ${v:,.2f} |")
    lines += [
        f"| **Total Assets** | **${bs['total_assets']:,.2f}** |",
        "",
        "### Liabilities",
        "",
        "| Account | Amount |",
        "|---------|--------|",
    ]
    for a, v in bs["liabilities"].items():
        lines.append(f"| {a} {coa[a]['name']} | ${v:,.2f} |")
    lines.append(f"| **Total Liabilities** | **${bs['total_liabilities']:,.2f}** |")
    lines += [
        "",
        "### Equity",
        "",
        "| Account | Amount |",
        "|---------|--------|",
    ]
    for a, v in bs["equity"].items():
        name = coa.get(a, {}).get("name", a)
        if a == "3200":
            name = "Retained Earnings (incl. current NI)"
        lines.append(f"| {a} {name} | ${v:,.2f} |")
    lines += [
        f"| **Total Equity** | **${bs['total_equity']:,.2f}** |",
        f"| **Total Liab. + Equity** | **${bs['total_liabilities_and_equity']:,.2f}** |",
        f"| BS balances | {'YES' if bs['balances'] else 'NO — investigate'} |",
        "",
        "## Cash Flow (Indirect, simplified)",
        "",
        f"- Cash beginning: **${cf['cash_beginning']:,.2f}**",
        f"- Cash ending: **${cf['cash_ending']:,.2f}**",
        f"- Net change: **${cf['net_change']:,.2f}**",
        "",
        "### Operating",
        "",
        "| Item | Amount |",
        "|------|--------|",
    ]
    for k, v in cf["operating"].items():
        lines.append(f"| {k} | ${v:,.2f} |")
    lines += [
        f"| **Operating total** | **${cf['operating_total']:,.2f}** |",
        "",
        f"Investing (capex): ${cf['investing']['capex']:,.2f}",
        "",
        f"TB balanced: {stmt['trial_balance_balanced']} "
        f"(Dr ${stmt['trial_balance_debits']:,.2f} / Cr ${stmt['trial_balance_credits']:,.2f})",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    stmt = build_statements()
    (OUTPUTS / "financial_statements_june_2026.json").write_text(json.dumps(stmt, indent=2))
    md = render_markdown(stmt)
    (OUTPUTS / "financial_statements_june_2026.md").write_text(md)

    # Also write TB csv
    import csv

    with (OUTPUTS / "trial_balance_june_2026.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["account", "name", "type", "debit", "credit", "net"])
        w.writeheader()
        for r in stmt["trial_balance"]:
            w.writerow(r)

    print(md)
    print("\nWrote outputs/financial_statements_june_2026.md")


if __name__ == "__main__":
    main()
