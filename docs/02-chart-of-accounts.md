# Chart of Accounts (CoA) Design

The CoA is the **spine** of R2R. Bad CoA design creates permanent reclass journals and broken analytics.

## Design principles used here

1. **Natural accounts answer "what"** — asset, liability, equity, revenue, expense.
2. **Dimensions answer "where/why"** — cost center, product, project (not new accounts).
3. **Stable numbering** — ranges by FS caption so rollups are obvious.
4. **Subledger control accounts** — AR, AP, cash, FA have clear control accounts that must tie to subledgers.

## Account ranges (Meridian)

| Range | Type | FS area |
|-------|------|---------|
| 1000–1999 | Assets | Balance sheet |
| 2000–2999 | Liabilities | Balance sheet |
| 3000–3999 | Equity | Balance sheet |
| 4000–4999 | Revenue | Income statement |
| 5000–5999 | COGS / direct cost | Income statement |
| 6000–6999 | Operating expenses | Income statement |
| 7000–7999 | Other income/expense | Income statement |
| 9000–9999 | Memo / statistical (lab only) | Not on FS |

## Control accounts (must reconcile every close)

| Account | Name | Reconciles to |
|---------|------|---------------|
| 1010 | Cash — Operating | Bank statement |
| 1020 | Cash — Payroll | Bank statement |
| 1100 | Accounts Receivable | AR aging / subledger |
| 1150 | Allowance for doubtful accounts | Aging reserve model |
| 1200 | Unbilled AR (contract asset) | Revenue schedule vs billed |
| 1300 | Prepaid expenses | Prepaid rollforward |
| 1400 | Fixed assets — gross | FA register |
| 1450 | Accumulated depreciation | FA register |
| 2100 | Accounts Payable | AP aging / subledger |
| 2200 | Accrued expenses | Accrual schedule |
| 2300 | Accrued payroll & taxes | Payroll reports |
| 2400 | Deferred revenue (contract liability) | Deferred revenue waterfall |
| 2500 | Sales tax payable | Tax filings (simplified) |

## Full CoA

See `data/master/chart_of_accounts.csv` (generated). Sample:

| Account | Name | Type | Normal balance |
|---------|------|------|----------------|
| 1010 | Cash — Operating | Asset | Debit |
| 1100 | Accounts Receivable | Asset | Debit |
| 2100 | Accounts Payable | Liability | Credit |
| 2400 | Deferred Revenue | Liability | Credit |
| 4100 | SaaS Subscription Revenue | Revenue | Credit |
| 4200 | Professional Services Revenue | Revenue | Credit |
| 6100 | Salaries & Wages | Expense | Debit |
| 6200 | Cloud Hosting (COGS-like OpEx) | Expense | Debit |
| 6300 | Software & Tools | Expense | Debit |
| 6400 | Marketing | Expense | Debit |
| 6500 | Depreciation Expense | Expense | Debit |

## Hierarchy example (SaaS revenue)

```text
4000 Net Revenue
 └── 4100 SaaS Subscription Revenue
 └── 4200 Professional Services Revenue
 └── 4300 Other Revenue
```

Management reporting uses **product line** and **cost center** dimensions rather than exploding 4100 into dozens of natural accounts.
