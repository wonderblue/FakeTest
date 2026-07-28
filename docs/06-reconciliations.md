# Reconciliations

A reconciliation proves an account balance is **complete and accurate** by tying it to an independent source and explaining every difference.

## Anatomy of a good recon

| Element | Question it answers |
|---------|---------------------|
| GL balance | What does the ledger say? |
| Source balance | What does the subledger / bank / schedule say? |
| Timing differences | Known items that will clear next period? |
| Errors | Misposts, duplicates, missing items? |
| Unreconciled | Residual — must be zero or below threshold |
| Sign-off | Who prepared/reviewed, when? |

## Meridian reconciliation set (June 2026)

| ID | Account | Method | Source |
|----|---------|--------|--------|
| REC-CASH-1010 | 1010 Operating cash | Bank recon | Bank statement |
| REC-AR-1100 | 1100 AR | Subledger to GL | AR aging |
| REC-AP-2100 | 2100 AP | Subledger to GL | AP aging |
| REC-DEF-2400 | 2400 Deferred revenue | Waterfall to GL | Deferred schedule |
| REC-FA-1400 | 1400/1450 FA | Register to GL | FA register |
| REC-PRE-1300 | 1300 Prepaid | Rollforward | Prepaid schedule |
| REC-ACC-2200 | 2200 Accruals | Detail listing | Accrual workbook |

## Bank reconciliation pattern

```text
Bank statement ending balance
+ Deposits in transit
− Outstanding checks / payments
± Bank errors
= Book (GL) cash balance
```

## Subledger-to-GL pattern (AR example)

```text
Sum of open AR invoices (aging)
− Credit memos / unapplied credits
± Timing (journals not yet interfaced)
= GL 1100 Accounts Receivable
```

**Difference must be $0** (or documented and cleared).

## Why recons matter for AI / transformation

Automation should:

1. Match high-volume, low-judgment items  
2. Surface **exceptions** with suggested matches  
3. Never “force to zero” without an audit trail  

Human judgment stays on: estimates, unusual timing, fraud indicators, policy calls.

## Lab artifact

Running `python -m src.reconciliations` writes `outputs/reconciliations_june_2026.md` with computed ties from synthetic data.
