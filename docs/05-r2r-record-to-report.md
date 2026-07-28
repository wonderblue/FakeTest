# Record-to-Report (R2R)

## Purpose

Turn **all** operational activity into **complete, accurate, timely** books and reports leadership and auditors can trust.

R2R is the **control center**, not the sales or buying engine. Weak P2P/O2C becomes R2R firefighting.

## Six-step close spine (Meridian Day 1–5)

| Day | Focus | Examples |
|-----|-------|----------|
| **-2 to 0** | Operational cutoffs | Last invoices, receipts, payroll feed, bank feed |
| **1** | Subledger completion + recurring | Depreciation, deferred revenue release, reverse prior accruals |
| **2** | Accruals & revals | AP accruals, bonus accrual, prepaid amortization |
| **3** | Reconciliations | Bank, AR, AP, deferred, payroll clearing |
| **4** | Analytical review | Flash P&L, BS flux, KPI pack |
| **5** | Certify & lock | Soft close → hard close → publish |

## What “comes into” R2R

```text
From O2C:  AR TB, billings, cash apps, deferred schedules, credit memos
From P2P:  AP TB, payments, GRNI/accruals, prepaid additions
From H2R:  Payroll journals, employer taxes, PTO/bonus estimates
From FA:   Capex additions, depreciation, disposals
From Bank: Statement activity, FX (N/A in single-currency lab)
From Tax:  Simplified sales tax / income tax provision stub
From FP&A: Budget/forecast for variance commentary (not GL postings)
```

## Journal categories (governance)

| Category | Example | Behavior |
|----------|---------|----------|
| Automated subledger | Customer invoice | System-generated |
| Recurring | Rent, deferred release | Auto, periodic review |
| Accrual | Unbilled vendor, bonus | Often auto-reverse |
| Estimate | Bad debt reserve | Judgment + evidence |
| Reclass | Coding fix | Should trend to zero |
| Top-side | Rare management adj. | Heavy approval |

## Outputs

1. Trial balance  
2. Income statement  
3. Balance sheet  
4. Cash flow (indirect)  
5. Reconciliation package  
6. Close certification checklist  

## Meridian close calendar

See `data/close/close_calendar.csv`. Critical path:

1. AR/AP subledgers final  
2. Deferred revenue monthly release  
3. Depreciation run  
4. Accruals posted  
5. Bank recon signed off  
6. Control account recons  
7. FS package generated  

## Controls mindset (SOX-lite for learning)

- Segregation: preparer ≠ approver for material journals  
- Period lock after certify  
- Evidence retained for accruals & estimates  
- Subledger-to-GL tie-outs with zero unexplained difference  

→ Next: [06 Reconciliations](06-reconciliations.md)
