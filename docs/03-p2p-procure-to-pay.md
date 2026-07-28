# Procure-to-Pay (P2P) / Accounts Payable

## Purpose

Control **how the company spends** and ensure vendor obligations are complete, accurate, and paid on time — then feed a clean AP subledger into R2R.

## Process spine

```text
Need → Requisition → Approve → Purchase Order → Receive (goods/services)
    → Vendor Invoice → 2/3-way Match → Approve → Schedule → Pay → Reconcile
```

## Double-entry patterns (Meridian)

### 1) PO receipt of services / goods (if GR used)

Often services skip formal GR; Meridian posts on invoice for most OpEx, and accrues at month-end for received-not-invoiced.

### 2) Vendor invoice (expense)

```text
Dr  Expense / Prepaid / Asset     XXX
   Cr  Accounts Payable 2100            XXX
```

### 3) Payment

```text
Dr  Accounts Payable 2100         XXX
   Cr  Cash 1010                        XXX
```

### 4) Month-end AP accrual (received, not invoiced)

```text
Dr  Expense                       XXX
   Cr  Accrued expenses 2200            XXX
```
*(Reverse Day 1 of next month, or true-up when invoice arrives.)*

## Three-way match (when inventory/PO goods exist)

| Document | Asserts |
|----------|---------|
| PO | Authorized price & qty |
| Receipt | Qty actually received |
| Invoice | Vendor bill qty & price |

Mismatch → exception queue (price variance, qty variance, missing receipt).

## What R2R inherits from P2P

- AP trial balance must equal GL 2100
- Open GRNI / accruals must be explainable
- Coding quality (cost center, account) — wrong codes become R2R reclasses
- Cut-off: invoices dated after period but for prior service → accrual or late posting policy

## Meridian June lab scenarios (look for these in data)

1. Cloud hosting invoice from **CloudRail Hosting** (OpEx 6200)
2. Salesforce/CRM tools prepaid annual (1300 Prepaid → amortize)
3. Marketing agency invoice partly accrued
4. Laptop capitalization (FA) vs expense threshold ($2,500 policy)

## KPIs

| KPI | Meaning |
|-----|---------|
| DPO | Days Payable Outstanding |
| % touchless invoices | Automation maturity |
| Exception rate | Match failures |
| Accrual accuracy | Accrual vs actual invoice |

→ Next: [04 O2C](04-o2c-order-to-cash.md)
