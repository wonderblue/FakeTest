# Finance Systems Thinking

Finance transformation fails when teams automate chaos. Systems thinking means designing **flows, ownership, and controls** before tools or AI.

## The reconcilable spine

Every critical flow needs:

```text
Event → System of record → Subledger → GL → Statement line
              │                │         │
           control total    interface  recon
```

If any hop lacks a control total, month-end becomes archaeology.

## Operating model layers

| Layer | Question | Meridian example |
|-------|----------|------------------|
| Process | What standard work exists? | P2P 3-way match policy |
| Data | What master data is golden? | Customer, vendor, CoA |
| Application | Which system owns the object? | Billing owns invoices |
| Integration | How do we move & prove completeness? | Billing → AR interface hash totals |
| Control | How do we detect failure? | AR→GL daily tie |
| Insight | How do we explain performance? | Billings vs revenue bridge |

## Close as a dependency graph (not a checklist dump)

```text
Bank feed ──┐
AR final ───┼─► Accruals ─► Recons ─► Flash P&L ─► Certify
AP final ───┤
Payroll ────┘
Deferred release ─► Revenue bridge
Depreciation ──────► FA recon
```

Late AR final **blocks** revenue analytics and AR recon. Design SLA backwards from certify date.

## Data model mental map

- **Master data**: customers, vendors, employees, CoA, products, cost centers  
- **Transactional data**: invoices, payments, journals, receipts  
- **Analytical data**: TB, aging, waterfalls, FS, KPIs  

AI features are only as good as master data quality and transaction completeness.

## ERP vs best-of-breed

| Area | Often in ERP | Often specialized |
|------|----------------|-------------------|
| GL, AP, AR, FA | Yes | — |
| Billing / CPQ | Sometimes | Zuora-like, Salesforce CPQ |
| Expense | Sometimes | Concur-like |
| Close / recon | Improving | BlackLine-like |
| Consolidation | Sometimes | OneStream-like |
| Payroll | Rarely | ADP-like |

Integration design > brand names.

## Metrics that prove the system works

| Metric | Healthy signal |
|--------|----------------|
| Close days | Trending down with stable quality |
| Manual journals / TB lines | Falling |
| Unreconciled $ | Near zero before certify |
| Touchless invoice % | Rising |
| Chart of accounts churn | Low |

→ Next: [09 AI & finance transformation](09-ai-finance-transformation.md)
