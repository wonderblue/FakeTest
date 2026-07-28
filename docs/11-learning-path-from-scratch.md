# Core Accounting Starter Map

If you are entering finance / AI-for-finance from scratch, start here.

## Layer 1 — Language (1 sitting)

- Debit / credit and normal balances
- Asset = Liability + Equity
- Accrual vs cash
- Subledger vs general ledger
- Billing vs revenue vs cash

Read: `00-process-universe.md`, `glossary.md`, `07-accounting-treatments.md`

## Layer 2 — Process cycles (the “one roof”)

| Cycle | You must be able to explain |
|-------|-----------------------------|
| O2C / AR | Order → invoice → collect; deferred revenue |
| P2P / AP | PO → invoice → pay; accruals & prepaid |
| R2R | Close calendar, journals, recons, statements |
| H2R | Payroll expense & clearing |
| FA | Capitalize vs expense; depreciation |
| Treasury | Bank recon |
| FP&A | Actuals vs budget (conceptual in this lab) |

## Layer 3 — Systems thinking

For every flow: system of record → control total → recon → statement line.

Read: `08-finance-systems-thinking.md`

## Layer 4 — Hands-on Meridian

```bash
python3 -m src.r2r_close
python3 -m src.validate
```

Then complete traces in `10-end-to-end-traces.md`.

## Layer 5 — Transformation / AI

Only after Layers 1–4: `09-ai-finance-transformation.md`.

Ask of every AI idea: **Which control total does it protect or replace?**
