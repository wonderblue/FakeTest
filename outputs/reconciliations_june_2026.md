# Meridian CloudWorks — Reconciliation Package (June 2026)

Control account ties prove subledgers and schedules equal the GL.

## REC-AR-1100 Accounts Receivable

| Component | Amount |
|-----------|--------|
| Opening AR | $412,500.00 |
| June billings (AR invoices) | $249,600.00 |
| June cash applications | $-399,500.00 |
| Ending AR (subledger rollforward) | $262,600.00 |
| GL 1100 | $262,600.00 |
| Difference | $0.00 |
| **Status** | **TIED** |

## REC-AP-2100 Accounts Payable

| Component | Amount |
|-----------|--------|
| Opening AP | $156,000.00 |
| June AP invoices | $194,600.00 |
| June AP payments | $-157,700.00 |
| Ending AP (subledger rollforward) | $192,900.00 |
| GL 2100 (credit) | $192,900.00 |
| Difference | $0.00 |
| **Status** | **TIED** |

## REC-DEF-2400 Deferred Revenue Waterfall

| Component | Amount |
|-----------|--------|
| Opening deferred revenue | $615,000.00 |
| Billings to deferred (additions) | $60,000.00 |
| Revenue releases | $-121,500.00 |
| Ending deferred (waterfall) | $553,500.00 |
| GL 2400 (credit) | $553,500.00 |
| Difference | $0.00 |
| **Status** | **TIED** |

## REC-CASH-1010 Bank Reconciliation

| Item | Amount |
|------|--------|
| Bank statement balance | $601,320.00 |
| + Deposits in transit | $12,500.00 |
| − Outstanding payments | $1,600.00 |
| = Reconciled book balance | $612,220.00 |
| GL 1010 | $612,220.00 |
| Difference | $0.00 |
| **Status** | **TIED** |

## REC-FA Fixed Assets

- Register gross $274,600.00 vs GL 1400 $274,600.00 (diff $0.00)
- Register accum dep $103,738.89 vs GL 1450 $103,738.89 (diff $0.00)
- **Status: TIED**

## REC-PRE-1300 Prepaid Expenses

- Schedule end $77,000.00 vs GL $77,000.00
- **Status: TIED**

## REC-ACC-2200 Accrued Expenses

- Accrual listing $43,800.00 vs GL credit $43,800.00
- **Status: TIED**

## Sign-off checklist

- [x] Preparers completed recons Day 3
- [x] Reviewer (Controller) signed Day 3–4
- [x] Differences > $100 investigated (none material in lab)
