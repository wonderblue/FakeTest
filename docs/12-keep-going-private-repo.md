# Keep Going — Private Repo Setup & Roadmap

This environment **cannot create a new GitHub repository** (the agent’s GitHub token is read-only for repo creation). You create the private repo once in your account; everything below is copy-paste ready.

---

## Part A — Create a private GitHub repo and move Meridian into it

### Option 1 — GitHub website (simplest)

1. Open [https://github.com/new](https://github.com/new)
2. Set:
   - **Repository name:** `meridian-finance-lab` (or any name you like)
   - **Visibility:** **Private**
   - **Do not** add README / .gitignore / license (you already have them)
3. Click **Create repository**
4. On your machine (or Codespaces), run:

```bash
# Clone THIS current project branch (or download the PR branch)
git clone -b cursor/meridian-finance-learning-lab-cab0 \
  https://github.com/wonderblue/FakeTest.git meridian-finance-lab
cd meridian-finance-lab

# Point at your NEW private repo (replace YOUR_USER)
git remote rename origin upstream-faketest   # optional: keep old remote
git remote add origin https://github.com/YOUR_USER/meridian-finance-lab.git

# Optional: start clean history on main
git checkout -b main
git push -u origin main
```

### Option 2 — GitHub CLI on your machine

```bash
# Install gh if needed, then login
gh auth login

# Create private empty repo under your user
gh repo create meridian-finance-lab --private --source=. --remote=origin

# If you are still inside FakeTest, better: copy files first
mkdir -p ~/code && cd ~/code
git clone -b cursor/meridian-finance-learning-lab-cab0 \
  https://github.com/wonderblue/FakeTest.git meridian-finance-lab
cd meridian-finance-lab
gh repo create meridian-finance-lab --private --source=. --remote=origin --push
```

### Option 3 — Fresh folder from PR files only

```bash
mkdir meridian-finance-lab && cd meridian-finance-lab
git init
# copy all files from the FakeTest PR branch into this folder
git add .
git commit -m "Initial import: Meridian CloudWorks finance learning lab"
gh repo create meridian-finance-lab --private --source=. --remote=origin --push
```

### After the private repo exists

1. Confirm visibility: GitHub → **Settings → General → Danger Zone** shows Private  
2. Invite only people you want: **Settings → Collaborators**  
3. Clone URL for daily work:

```bash
git clone https://github.com/YOUR_USER/meridian-finance-lab.git
cd meridian-finance-lab
python3 -m src.r2r_close
python3 -m src.validate
```

You can leave the FakeTest PR as-is or close it once the private repo is the source of truth.

---

## Part B — How to keep learning / extending the lab

Work in small loops: **learn a concept → change one thing in data → re-run close → explain the FS impact**.

### Weekly rhythm (suggested)

| Week focus | What to do in the repo |
|------------|------------------------|
| 1. Language | Read docs 00–07; complete traces in `docs/10-end-to-end-traces.md` |
| 2. O2C depth | Add a multi-year contract, credit memo, or partial cash app; re-run validate |
| 3. P2P depth | Add 3-way match failure, GRNI, or duplicate invoice scenario |
| 4. R2R depth | Build a Day-by-day close checklist CSV with owners/SLAs |
| 5. Multi-entity | Add `MCW-UK` entity + simple intercompany + elimination JE |
| 6. FP&A | Add budget CSV; variance bridge vs actuals in `outputs/` |
| 7. Controls | Document SOX-lite RCMs (risk-control matrix) for AR/AP/cash |
| 8. AI layer | Build a small matcher script: suggest AR cash apps from bank lines |

### Concrete next builds (pick any)

1. **July period** — roll June closing TB into July opening; practice continuous close  
2. **Aging reports** — AR/AP aging buckets (0–30, 31–60, 61–90, 90+)  
3. **Revenue bridge** — Billings → Deferred → Revenue waterfall dashboard (Markdown/CSV)  
4. **Flux analysis** — BS/P&L MoM commentary template filled from TB deltas  
5. **Inventory / COGS** — only if you change the business model  
6. **Tax stub** — simple income-tax provision (Dr tax expense / Cr tax payable)  
7. **BlackLine-style recon statuses** — preparer / reviewer / ages / auto-certify rules  
8. **AI cash application prototype** — score matches between `bank_transactions` and open `ar_invoices`

### Guardrails so the lab stays trustworthy

Every change must still pass:

```bash
python3 -m src.r2r_close
python3 -m src.validate
```

Rules:

- Debits = credits always  
- Control accounts tie (AR, AP, bank, deferred, FA, prepaid, accruals)  
- Prefer fixing **source data** over “plug” journals  
- Document new scenarios in `docs/` when you add them  

### Branching model for your private repo

```text
main                 # always validates
feature/july-close   # experiments
feature/ai-cash-app
```

```bash
git checkout -b feature/july-close
# edit data / src
python3 -m src.validate
git add -A && git commit -m "Add July close skeleton"
git push -u origin feature/july-close
# open PR into main on YOUR private repo
```

---

## Part C — Cursor / AI workflow on the private repo

1. Open the private repo in Cursor  
2. Point agents at `docs/11-learning-path-from-scratch.md` as context  
3. Ask for **one scenario at a time**, e.g.  
   - “Add a customer credit memo for C012 and show AR + revenue impact”  
   - “Generate AR aging from open invoices and receipts”  
4. Always require the agent to re-run `python3 -m src.validate`  

Good prompt template:

```text
In the Meridian finance lab, add <scenario>.
Update synthetic data + journals so control accounts still tie.
Re-run src.r2r_close and src.validate.
Document the accounting treatment in docs/07 or a new short doc.
```

---

## Part D — What “done” looks like for transformation skills

You are progressing when you can explain, without notes:

1. Why billing ≠ revenue for SaaS  
2. How P2P accruals protect cut-off  
3. How a bank recon timing difference works  
4. How every statement line drills to a business event  
5. Where AI helps (exceptions) vs where judgment stays (estimates, certify)

Then you are ready to map the same spine onto a real ERP (NetSuite, SAP, Dynamics, etc.).

---

## Quick reference

| Item | Location |
|------|----------|
| Learning path | `docs/11-learning-path-from-scratch.md` |
| Process map | `docs/00-process-universe.md` |
| Run close | `python3 -m src.r2r_close` |
| Prove ties | `python3 -m src.validate` |
| Outputs | `outputs/` |
| Current PR (FakeTest) | https://github.com/wonderblue/FakeTest/pull/2 |
