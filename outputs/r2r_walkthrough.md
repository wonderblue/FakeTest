# R2R Walkthrough — What Happened in June 2026

## Company
Meridian CloudWorks, Inc. (B2B SaaS + services)

## Net income
**$-203,684.14**

## Revenue bridge
- SaaS revenue (4100): $201,300.00
- Services revenue (4200): $102,500.00
- Total: $303,800.00

SaaS includes (a) deferred releases on annual contracts and (b) monthly arrears billings.
Services includes invoiced delivery plus unbilled WIP.

## Balance sheet highlights
- Total assets: $1,319,515.86
- Deferred revenue still a major liability — classic SaaS
- Cash changed by $-100,645.25

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
