# The Finance Process Universe

Every company runs the same **economic loop**: spend money to create value, sell that value, collect cash, record what happened, and report it. Finance organizes that loop into **end-to-end (E2E) process cycles**. Different firms use slightly different acronyms; the substance is the same.

## One-roof map

```text
                         ┌─────────────────────────────────────┐
                         │           STRATEGY / FP&A            │
                         │     Budget → Forecast → Report       │
                         └─────────────────┬───────────────────┘
                                           │ targets & variance
     ┌──────────────┐    ┌─────────────────▼───────────────────┐    ┌──────────────┐
     │  HIRE→RETIRE │    │         RECORD → REPORT (R2R)        │    │ TREASURY/CASH│
     │   (H2R/Payroll)──►│  Journals · Accruals · Recons · FS   │◄───│  Bank · FX   │
     └──────────────┘    └────────▲───────────────▲────────────┘    └──────────────┘
                                  │               │
              ┌───────────────────┘               └───────────────────┐
              │                                                       │
     ┌────────┴────────┐                                   ┌─────────┴────────┐
     │ PROCURE → PAY   │                                   │  ORDER → CASH    │
     │ P2P / AP / PTP  │                                   │  O2C / AR / OTC  │
     │ Buy & pay vendors│                                   │ Sell & collect   │
     └────────┬────────┘                                   └─────────┬────────┘
              │                                                       │
     ┌────────┴────────┐                                   ┌─────────┴────────┐
     │ ACQUIRE→RETIRE  │                                   │ REVENUE ACCOUNTING│
     │ Fixed Assets    │                                   │ ASC 606 / IFRS 15 │
     └─────────────────┘                                   └──────────────────┘
```

## Acronym decoder (what people actually say)

| You hear | Formal name | Alias | What it means |
|----------|-------------|-------|---------------|
| **R2R / R to R** | Record to Report | Close & report | Capture events → books → statements |
| **P2P / PTP** | Procure to Pay | Purchase to Pay | Buy goods/services → pay vendors |
| **AP** | Accounts Payable | — | Sub-process / subledger of P2P |
| **O2C / OTC** | Order to Cash | Quote to Cash (Q2C) | Win order → fulfill → invoice → collect |
| **AR** | Accounts Receivable | — | Sub-process / subledger of O2C |
| **B2C** | *(ambiguous!)* | — | In retail: Business-to-Consumer sales model. In finance slang sometimes confused with O2C. **Not** a core GL cycle. |
| **H2R** | Hire to Retire | Record to Pay (payroll) | Hire → compensate → exit |
| **A2R / FA** | Acquire to Retire | Capex / Fixed Assets | Buy asset → depreciate → dispose |
| **I2C / STC** | Inventory to Cash / Source to Consume | Inventory cycle | Buy/make stock → issue → COGS |
| **T&E** | Travel & Expense | — | Employee spend → reimburse (often under P2P) |
| **IC** | Intercompany | — | Trading / loans / settlements between entities |
| **Tax** | Tax accounting | Provision / compliance | Current & deferred tax, filings |
| **Treasury** | Cash & liquidity | Bank to book | Cash positioning, FX, debt, investments |
| **B2R** | Budget to Report | FP&A | Plan → forecast → variance vs actuals |

## How the cycles feed R2R

R2R does **not** create most business activity. It **absorbs** activity from other cycles and turns it into trustworthy ledgers and reports.

| Source cycle | Typical subledger | What hits the GL | What R2R must do with it |
|--------------|-------------------|------------------|--------------------------|
| O2C / AR | AR subledger | Revenue, deferred revenue, AR, cash, bad debt | Tie AR subledger → GL; revenue cut-off; deferred waterfalls |
| P2P / AP | AP subledger | Expense, prepaid, inventory/GRNI, AP, cash | Tie AP → GL; accruals for unbilled; GRNI aging |
| H2R | Payroll | Salary, benefits, taxes, accruals | Payroll clearing recon; bonus/leave accruals |
| FA / A2R | Fixed asset register | Capex, depreciation, disposals | FA register → GL; CIP capitalization |
| Treasury | Bank / cash book | Cash, FX gains/losses, interest | Bank reconciliations; cash flow statement |
| IC | IC matching | IC AR/AP, revenue/expense | Match, eliminate, settle |
| Tax | Tax engine / workbook | Tax expense, deferred tax, payable | Provision vs TB; deferred schedules |

## Subledger → General Ledger → Statements

```text
Operational event
      │
      ▼
Subledger posting (AR, AP, FA, Payroll, Bank)
      │  (automated accounting rules / SLA)
      ▼
General Ledger (natural account + dimensions)
      │
      ├─► Trial Balance
      ├─► Account reconciliations
      ├─► Adjusting journals (accruals, reclass, estimates)
      └─► Financial statements + management packs
```

**Rule of thumb:** If you cannot drill from a financial-statement line to a business event (invoice, receipt, payroll run, asset), the process design is broken.

## Meridian CloudWorks scope

This lab models a mid-market **B2B SaaS + professional services** company so you can see:

1. Subscription billing and **deferred revenue** (O2C + revenue accounting)
2. Vendor spend and **AP accruals** (P2P)
3. Payroll and bonus accruals (H2R)
4. Laptops/servers and **depreciation** (FA)
5. Bank activity and **bank recon** (Treasury)
6. Month-end **R2R close** that pulls it all together

Next: [01 — Company overview](01-company-overview.md)
