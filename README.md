# Meridian Finance Learning Lab

Synthetic company for learning **core accounting**, **R2R**, and **finance systems thinking** — with a path into AI / finance transformation.

## What this is

**Meridian CloudWorks, Inc.** — a fictional mid-market B2B SaaS + professional services company closing **June 2026**.

You get:

1. A map of every major finance process under one roof (R2R, P2P/AP, O2C/AR, H2R, FA, Treasury…)
2. A full chart of accounts and master data
3. Reconcilable synthetic transactions (journals, AR, AP, bank, payroll, deferred revenue, accruals)
4. A runnable month-end close that produces statements + reconciliations
5. Docs on accounting treatments, systems thinking, and where AI actually helps

## Quick start

```bash
python -m src.r2r_close      # generate data + run close
python -m src.validate        # prove control accounts tie
```

Outputs land in `outputs/`.

## Learn in this order

| Step | Doc |
|------|-----|
| 0 | [docs/11-learning-path-from-scratch.md](docs/11-learning-path-from-scratch.md) — start here if new to accounting |
| 1 | [docs/00-process-universe.md](docs/00-process-universe.md) — acronyms & cycles |
| 2 | [docs/01-company-overview.md](docs/01-company-overview.md) |
| 3 | [docs/02-chart-of-accounts.md](docs/02-chart-of-accounts.md) |
| 4 | [docs/03-p2p-procure-to-pay.md](docs/03-p2p-procure-to-pay.md) |
| 5 | [docs/04-o2c-order-to-cash.md](docs/04-o2c-order-to-cash.md) |
| 6 | [docs/05-r2r-record-to-report.md](docs/05-r2r-record-to-report.md) |
| 7 | [docs/06-reconciliations.md](docs/06-reconciliations.md) |
| 8 | [docs/07-accounting-treatments.md](docs/07-accounting-treatments.md) |
| 9 | [docs/08-finance-systems-thinking.md](docs/08-finance-systems-thinking.md) |
| 10 | [docs/09-ai-finance-transformation.md](docs/09-ai-finance-transformation.md) |
| 11 | [docs/10-end-to-end-traces.md](docs/10-end-to-end-traces.md) — follow C008 & V002 |

## Repo layout

```text
docs/           Concept guides (start here)
data/master/    CoA, customers, vendors, employees
data/transactions/  Journals + subledgers
data/close/     Opening TB + close calendar
src/            Generator, close, recons, statements
outputs/        Generated FS + reconciliation pack
```

## Design goals

- **Books balance** (debits = credits)
- **Control accounts tie** (AR/AP/bank/deferred/FA/prepaid/accruals)
- **Billing ≠ revenue** shown clearly via deferred revenue
- **Realistic close artifacts** you would see in ERP + BlackLine-style recon work

## License

See LICENSE (upstream demo license retained for fork heritage).
