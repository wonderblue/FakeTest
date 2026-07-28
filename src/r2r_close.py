"""
Orchestrate Meridian June 2026 R2R close demo.
"""

from __future__ import annotations

import json
from pathlib import Path

from src import CLOSE, OUTPUTS, ROOT, read_csv
from src.financial_statements import build_statements, render_markdown
from src.generate_data import generate_all
from src.reconciliations import run_all as run_recons


def main() -> None:
    print("=== Meridian CloudWorks R2R Close ===\n")
    print("1) Generating / refreshing synthetic data...")
    meta = generate_all()
    print(json.dumps(meta, indent=2))

    print("\n2) Close calendar:")
    for row in read_csv(CLOSE / "close_calendar.csv"):
        print(f"  Day {row['day']:>3}: {row['task']} [{row['owner']}] — {row['status']}")

    print("\n3) Building financial statements...")
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    stmt = build_statements()
    md = render_markdown(stmt)
    (OUTPUTS / "financial_statements_june_2026.md").write_text(md)
    (OUTPUTS / "financial_statements_june_2026.json").write_text(json.dumps(stmt, indent=2))

    import csv

    with (OUTPUTS / "trial_balance_june_2026.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["account", "name", "type", "debit", "credit", "net"])
        w.writeheader()
        for r in stmt["trial_balance"]:
            w.writerow(r)

    print("\n4) Running reconciliations...")
    recon_md = run_recons()
    (OUTPUTS / "reconciliations_june_2026.md").write_text(recon_md)

    # Learning narrative
    walkthrough = f"""# R2R Walkthrough — What Happened in June 2026

## Company
Meridian CloudWorks, Inc. (B2B SaaS + services)

## Net income
**${stmt['income_statement']['net_income']:,.2f}**

## Revenue bridge
- SaaS revenue (4100): ${stmt['income_statement']['revenue'].get('4100', 0):,.2f}
- Services revenue (4200): ${stmt['income_statement']['revenue'].get('4200', 0):,.2f}
- Total: ${stmt['income_statement']['total_revenue']:,.2f}

SaaS includes (a) deferred releases on annual contracts and (b) monthly arrears billings.
Services includes invoiced delivery plus unbilled WIP.

## Balance sheet highlights
- Total assets: ${stmt['balance_sheet']['total_assets']:,.2f}
- Deferred revenue still a major liability — classic SaaS
- Cash changed by ${stmt['cash_flow_indirect']['net_change']:,.2f}

## How the cycles fed R2R
1. **O2C** posted AR invoices, cash apps, deferred additions
2. **P2P** posted vendor bills, payments, a capitalized laptop buy
3. **H2R** posted payroll and funding
4. **FA** ran depreciation
5. **R2R** released deferred revenue, amortized prepaid, accrued expenses/bonus, true-up bad debt
6. **Recons** tied bank, AR, AP, deferred, FA, prepaid, accruals

## Files to inspect next
- `data/transactions/journal_entries.csv` — every debit/credit
- `outputs/financial_statements_june_2026.md`
- `outputs/reconciliations_june_2026.md`
- `docs/` — concept guides

## Suggested exercises
1. Trace customer **C008** from SO → invoice → deferred → monthly release → cash
2. Trace vendor **V002** prepaid CRM: AP → prepaid → amortization
3. Break the bank recon by deleting a deposit-in-transit, re-run, and fix it
4. Design an AI agent prompt that proposes matches between `ar_receipts` and open `ar_invoices`
"""
    (OUTPUTS / "r2r_walkthrough.md").write_text(walkthrough)

    print("\n5) Close package written to outputs/")
    print(f"   Net income: ${stmt['income_statement']['net_income']:,.2f}")
    print(f"   BS balances: {stmt['balance_sheet']['balances']}")
    print(f"   TB balanced: {stmt['trial_balance_balanced']}")
    print("\nDone. Read outputs/r2r_walkthrough.md")


if __name__ == "__main__":
    main()
