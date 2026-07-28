# Order-to-Cash (O2C) / Accounts Receivable

## Purpose

Convert customer demand into **recognized revenue**, **receivables**, and **collected cash** — under ASC 606 — and feed a clean AR + revenue picture into R2R.

## Process spine

```text
Lead → Quote → Credit check → Contract/Order → Fulfill / Grant access
    → Bill → Recognize revenue (may differ from billing!) → Collect → Apply cash
```

## Critical distinction: billing ≠ revenue

| Concept | Meaning | Balance sheet |
|---------|---------|---------------|
| **Billed** | Invoice issued to customer | Dr AR / Cr Deferred or Revenue |
| **Recognized** | Earned under ASC 606 | Revenue on P&L |
| **Collected** | Cash received | Dr Cash / Cr AR (or unapplied) |
| **Deferred revenue** | Cash/bill ahead of earning | Liability 2400 |
| **Unbilled AR** | Earned ahead of billing | Asset 1200 |

## ASC 606 five steps (applied simply)

1. Identify contract with customer  
2. Identify performance obligations (SaaS access vs implementation)  
3. Determine transaction price  
4. Allocate price to obligations  
5. Recognize when (or as) obligations satisfied  

**Meridian pattern:**

- SaaS: recognize **ratably over subscription term**
- Services: recognize **as delivered** (hours or milestones)

## Double-entry patterns

### Annual SaaS billed upfront ($120,000 for 12 months)

**On invoice / cash:**
```text
Dr  Accounts Receivable 1100          120,000
   Cr  Deferred Revenue 2400                  120,000
```

**Each month (recognize 1/12):**
```text
Dr  Deferred Revenue 2400              10,000
   Cr  SaaS Revenue 4100                       10,000
```

### Services T&M invoice when earned

```text
Dr  Accounts Receivable 1100           25,000
   Cr  Services Revenue 4200                   25,000
```

### Cash application

```text
Dr  Cash 1010                          25,000
   Cr  Accounts Receivable 1100                25,000
```

### Unbilled services (earned, not yet billed)

```text
Dr  Unbilled AR 1200                   8,000
   Cr  Services Revenue 4200                    8,000
```
*(Reverse/reclass when billed.)*

## What R2R inherits from O2C

- AR subledger = GL 1100
- Deferred revenue waterfall = GL 2400
- Revenue cut-off & ASC 606 schedules
- Credit memos, write-offs, reserve (1150)
- Unapplied cash / suspense clearing

## Meridian June lab scenarios

1. Acme Corp annual renewal billed in April → monthly release from deferred
2. New logo billed monthly in arrears
3. Services project with unbilled WIP at month-end
4. Partial payment / short-pay creating open AR item
5. Aging-based bad debt reserve true-up

## KPIs

| KPI | Meaning |
|-----|---------|
| DSO | Days Sales Outstanding |
| Deferred revenue balance | Future SaaS obligation |
| Billings vs revenue | Growth vs recognition timing |
| Collection effectiveness | Cash conversion |

→ Next: [05 R2R](05-r2r-record-to-report.md)
