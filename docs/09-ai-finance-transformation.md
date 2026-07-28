# AI & Finance Transformation — Where to Start

This lab exists so you can practice **core accounting first**, then spot where AI actually helps.

## Start from scratch — core areas (priority order)

1. **Chart of accounts & dimensions** — without this, AI classifies garbage  
2. **O2C + revenue** — cash, deferred, ASC 606 schedules  
3. **P2P + AP** — spend integrity, accruals  
4. **R2R close orchestration** — calendars, journals, recons  
5. **Cash / bank** — liquidity truth  
6. **Payroll & FA** — recurring automated postings  
7. **FP&A bridge** — actuals → forecast narrative  

## High-ROI AI use cases (mapped to Meridian)

| Process | AI use case | Human still owns |
|---------|-------------|------------------|
| P2P | Invoice OCR + coding suggestions | Policy, fraud, new vendors |
| O2C | Cash application matching | Disputes, concessions |
| R2R | Auto-match recon items; anomaly on TB flux | Estimates, certify |
| Rev | Contract obligation extraction draft | ASC 606 judgments |
| FP&A | Variance narrative draft | Business story |
| Controls | Duplicate payment / odd journal detection | Investigation |

## Anti-patterns

- Automating reclass journals instead of fixing source coding  
- “AI plug” to force bank recon to zero  
- Skipping subledger-GL ties because a dashboard “looks right”  
- Training models on unclean historical closes  

## Transformation sequence (practical)

```text
Standardize process → Clean master data → Stabilize integrations
    → Measure close/recon KPIs → Automate deterministic work
    → Add AI on exceptions → Continuous accounting (soft close daily)
```

## How to use this repo for learning

1. Read process docs in `docs/`  
2. Inspect CSVs in `data/` — follow one customer and one vendor end-to-end  
3. Run `python -m src.generate_data` then `python -m src.r2r_close`  
4. Read generated statements in `outputs/`  
5. Modify an accrual in data and re-run to see FS impact  
6. Sketch an AI agent that proposes cash application matches from `ar_invoices` + `bank_transactions`  

## Glossary quick hits

See [glossary.md](glossary.md).
