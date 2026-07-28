# Meridian CloudWorks — Company Overview

## Who we are (synthetic)

| Attribute | Value |
|-----------|-------|
| Legal name | Meridian CloudWorks, Inc. |
| Entity code | MCW-US |
| HQ | Austin, TX |
| Industry | B2B SaaS + implementation services |
| Fiscal year | Calendar (Jan–Dec) |
| Reporting currency | USD |
| Accounting basis | US GAAP (ASC 606 revenue) |
| ERP (conceptual) | Cloud ERP with AR/AP/GL/FA + billing system |
| Lab period | **June 2026** month-end close (with May opening balances) |

## Business model

Meridian sells two things:

1. **Nimbus Platform** — multi-tenant SaaS (annual or monthly subscriptions). Cash often collected upfront → **contract liability / deferred revenue**.
2. **Forge Services** — implementation and advisory billed T&M or fixed-fee milestones → **revenue when performed** (or over time under ASC 606).

This mix is intentional: it forces deferred revenue, unbilled AR (contract assets), accrued expenses, and clean cut-off — the classic R2R pain points.

## Organizational dimensions (posting model)

Every GL posting carries:

| Dimension | Example | Purpose |
|-----------|---------|---------|
| Entity | MCW-US | Legal books |
| Natural account | 4100 SaaS Revenue | What |
| Cost center | CC-400 Customer Success | Who owns P&L |
| Product line | PL-SAAS / PL-SVC | Margin analysis |
| Project | PRJ-1042 Acme rollout | Services WIP / profitability |
| Intercompany | (blank or partner entity) | IC matching |

## People & scale (synthetic snapshot)

| Metric | Approx. |
|--------|---------|
| Employees | 48 |
| Active customers | 25 |
| Active vendors | 18 |
| Monthly SaaS ARR run-rate | ~$4.8M ARR |
| June 2026 revenue (target) | ~$520–560k |
| Bank accounts | Operating + Payroll |

## Systems landscape (finance systems thinking)

```text
CRM / CPQ ──► Billing ──► AR ──┐
                               ├──► GL ──► Consolidation/Reporting
Procurement ─► AP ─────────────┘      ▲
Payroll provider ─────────────────────┤
Bank feeds ───────────────────────────┤
Fixed asset register ─────────────────┘
```

For transformation / AI work, ask of each arrow:

1. Who is the **system of record**?
2. What is the **control total** at the handoff?
3. How do we **reconcile** source → subledger → GL?
4. What exceptions need human judgment?

## Lab learning path

1. Read [00 — Process universe](00-process-universe.md)
2. Study [02 — Chart of accounts](02-chart-of-accounts.md)
3. Walk [03 P2P](03-p2p-procure-to-pay.md) → [04 O2C](04-o2c-order-to-cash.md) → [05 R2R](05-r2r-record-to-report.md)
4. Practice [06 Reconciliations](06-reconciliations.md) and [07 Accounting treatments](07-accounting-treatments.md)
5. Connect to [08 Systems thinking](08-finance-systems-thinking.md) and [09 AI & finance transformation](09-ai-finance-transformation.md)
6. Run the Python close demo (`python -m src.r2r_close`)
