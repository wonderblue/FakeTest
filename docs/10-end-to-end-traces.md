# End-to-End Traces (follow the money)

Use these two walks to connect process cycles → journals → statements.

## Trace A — Customer C008 HarborPoint Energy (O2C → R2R)

**Story:** New annual SaaS deal signed late May, billed June 1 for $60,000, cash collected June 28, revenue recognized ratably ($5,000 in June).

| Step | Artifact | What to open |
|------|----------|--------------|
| 1. Order | Sales order | `data/transactions/sales_orders.csv` filter `C008` |
| 2. Bill | AR invoice | `ar_invoices.csv` — treatment = `deferred` |
| 3. GL bill | Journal | `journal_entries.csv` source `O2C` ref INV… — Dr 1100 / Cr 2400 |
| 4. Collect | Receipt + bank | `ar_receipts.csv`, `bank_transactions.csv` — Dr 1010 / Cr 1100 |
| 5. Recognize | Deferred schedule | `deferred_revenue_schedule.csv` — $5,000 release |
| 6. GL revenue | Journal | source `R2R-REV` — Dr 2400 / Cr 4100 |
| 7. Statement | P&L / BS | June SaaS revenue includes the $5k; BS still holds $55k deferred for C008 |

**Learning point:** Cash and billing hit in June, but only **1/12** is revenue. Deferred revenue is the bridge.

## Trace B — Vendor V002 Northstar CRM Soft (P2P → R2R)

**Story:** Annual CRM license $36,000 paid in June, capitalized as prepaid, amortized $3,000 in June (plus $4,000 amortization of opening prepaid pool = $7,000 total prepaid amort).

| Step | Artifact | Entry |
|------|----------|-------|
| 1. PO | `purchase_orders.csv` | Commitment |
| 2. AP invoice | `ap_invoices.csv` account 1300 | Dr Prepaid / Cr AP |
| 3. Pay | `ap_payments.csv` | Dr AP / Cr Cash |
| 4. Amortize | `prepaid_schedule.csv` + JE `R2R-PRE` | Dr 6300 / Cr 1300 |
| 5. Recon | REC-PRE-1300 | Schedule end = GL 1300 |

**Learning point:** Paying cash ≠ expensing. Matching principle spreads cost over the benefit period.

## Trace C — Bank recon timing difference

1. Open `bank_outstanding_items.csv` — DIT-001 ($12,500) and OS-CHK-001 ($1,600)
2. Open `outputs/reconciliations_june_2026.md` § REC-CASH-1010
3. Prove: `Bank + DIT − Outstanding = GL 1010`

**Learning point:** Books and bank can both be “right” and still differ on a given day.

## Trace D — Month-end accrual

1. Open `accruals.csv` — hosting / marketing / legal / T&E not yet invoiced
2. Find JE source `R2R-ACCR` on 2026-06-30
3. Tie listing total to GL 2200 in reconciliations pack

**Learning point:** R2R completes the period when P2P invoices lag reality.

## After tracing

Re-run:

```bash
python3 -m src.r2r_close
python3 -m src.validate
```

Then read `outputs/r2r_walkthrough.md`.
