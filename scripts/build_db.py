#!/usr/bin/env python3
"""Generate comprehensive finance & accounting learning data for db.json."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def study_plan():
    return [
        {
            "id": 1,
            "day": 1,
            "week": 1,
            "title": "The Accounting Equation",
            "theme": "Foundation",
            "durationMinutes": 60,
            "goals": [
                "Memorize Assets = Liabilities + Equity",
                "Explain what each side of the equation represents",
                "Classify 10 everyday business items into A/L/E",
            ],
            "tasks": [
                {"type": "read", "ref": "module-1", "label": "Read Module 1: The Language of Business"},
                {"type": "flashcards", "deck": "equation", "label": "Drill equation flashcards (20 cards)"},
                {"type": "practice", "ref": "classify-basics", "label": "Classify 15 items into Asset / Liability / Equity"},
                {"type": "quiz", "ref": "quiz-equation", "label": "Take Quiz: Accounting Equation"},
            ],
            "checkpoint": "Without notes, write the equation and define each term in one sentence.",
            "visaUnlock": None,
        },
        {
            "id": 2,
            "day": 2,
            "week": 1,
            "title": "Five Account Types",
            "theme": "Account Mastery",
            "durationMinutes": 75,
            "goals": [
                "Name and define Assets, Liabilities, Equity, Revenue, Expenses",
                "Give 5 examples of each account type",
                "Map every account type back to the equation",
            ],
            "tasks": [
                {"type": "read", "ref": "module-2", "label": "Read Module 2: The Five Account Types"},
                {"type": "flashcards", "deck": "account-types", "label": "Flashcards: account type definitions & examples"},
                {"type": "practice", "ref": "account-sort", "label": "Sort 30 accounts into the five types"},
                {"type": "quiz", "ref": "quiz-account-types", "label": "Take Quiz: Account Types"},
            ],
            "checkpoint": "Draw a map: which account types increase equity? Which decrease it?",
            "visaUnlock": "account-types",
        },
        {
            "id": 3,
            "day": 3,
            "week": 1,
            "title": "Debits and Credits — The Rules",
            "theme": "Debits & Credits",
            "durationMinutes": 90,
            "goals": [
                "Understand debit = left, credit = right (not good/bad)",
                "Memorize DEA-LER normal balances",
                "State increase/decrease rules for all five types",
            ],
            "tasks": [
                {"type": "read", "ref": "module-3", "label": "Read Module 3: Debits & Credits Deep Dive"},
                {"type": "flashcards", "deck": "debit-credit", "label": "Flashcards: normal balances & DEA-LER"},
                {"type": "trainer", "ref": "dc-trainer", "label": "Debit/Credit Trainer — 25 rounds"},
                {"type": "quiz", "ref": "quiz-debits-credits", "label": "Take Quiz: Debits & Credits"},
            ],
            "checkpoint": "Recite DEA-LER and say which side increases for each letter.",
            "visaUnlock": "debits-credits",
        },
        {
            "id": 4,
            "day": 4,
            "week": 1,
            "title": "T-Accounts & Journal Entries",
            "theme": "Recording",
            "durationMinutes": 90,
            "goals": [
                "Draw a T-account and post a simple transaction",
                "Write journal entries in proper form (debit first)",
                "Keep every entry balanced (total debits = total credits)",
            ],
            "tasks": [
                {"type": "read", "ref": "module-4", "label": "Read Module 4: Journals, Ledgers & T-Accounts"},
                {"type": "practice", "ref": "journal-basics", "label": "Write 12 journal entries from narratives"},
                {"type": "flashcards", "deck": "journal", "label": "Flashcards: journal entry patterns"},
                {"type": "quiz", "ref": "quiz-journal", "label": "Take Quiz: Journal Entries"},
            ],
            "checkpoint": "Record: Owner invests $10,000 cash. Buy supplies $500 on account. Pay rent $1,200 cash.",
            "visaUnlock": "journal-entries",
        },
        {
            "id": 5,
            "day": 5,
            "week": 1,
            "title": "The Accounting Cycle — Overview",
            "theme": "Process",
            "durationMinutes": 60,
            "goals": [
                "List the steps of the accounting cycle in order",
                "Distinguish journal vs ledger vs trial balance",
                "Explain why we adjust and close accounts",
            ],
            "tasks": [
                {"type": "read", "ref": "module-5", "label": "Read Module 5: The Accounting Cycle"},
                {"type": "flashcards", "deck": "cycle", "label": "Flashcards: cycle steps & documents"},
                {"type": "practice", "ref": "cycle-order", "label": "Order the cycle steps correctly (3 times)"},
                {"type": "quiz", "ref": "quiz-cycle", "label": "Take Quiz: Accounting Cycle"},
            ],
            "checkpoint": "Name every step from source document to post-closing trial balance.",
            "visaUnlock": None,
        },
        {
            "id": 6,
            "day": 6,
            "week": 1,
            "title": "Accrual vs Cash & Timing",
            "theme": "Recognition",
            "durationMinutes": 75,
            "goals": [
                "Contrast cash basis vs accrual basis",
                "Apply revenue recognition and matching principles",
                "Identify prepaid, accrued, and deferred items",
            ],
            "tasks": [
                {"type": "read", "ref": "module-6", "label": "Read Module 6: Accrual Thinking"},
                {"type": "flashcards", "deck": "accrual", "label": "Flashcards: accruals, deferrals, matching"},
                {"type": "practice", "ref": "timing-cases", "label": "Solve 10 timing / recognition cases"},
                {"type": "quiz", "ref": "quiz-accrual", "label": "Take Quiz: Accrual vs Cash"},
            ],
            "checkpoint": "Explain why paying rent in advance creates a prepaid asset, not an expense yet.",
            "visaUnlock": "accrual-basis",
        },
        {
            "id": 7,
            "day": 7,
            "week": 1,
            "title": "Week 1 Integration Lab",
            "theme": "Integration",
            "durationMinutes": 90,
            "goals": [
                "Complete a mini-set of transactions end-to-end",
                "Build a simple trial balance",
                "Earn or re-test Week 1 mastery visas",
            ],
            "tasks": [
                {"type": "practice", "ref": "week1-lab", "label": "Week 1 Lab: 8 transactions → journal → T-accounts → trial balance"},
                {"type": "flashcards", "deck": "mixed-week1", "label": "Mixed review flashcards (all Week 1 decks)"},
                {"type": "quiz", "ref": "quiz-week1", "label": "Week 1 Comprehensive Quiz"},
                {"type": "visa", "ref": "review", "label": "Review Mastery Visas — retake any weak areas"},
            ],
            "checkpoint": "Score ≥80% on Week 1 Comprehensive Quiz before moving on.",
            "visaUnlock": "week1-foundation",
        },
        {
            "id": 8,
            "day": 8,
            "week": 2,
            "title": "Financial Statements Map",
            "theme": "Reporting",
            "durationMinutes": 75,
            "goals": [
                "Name the three primary statements and what each shows",
                "Trace how Net Income flows into Equity",
                "Link accounts to Income Statement vs Balance Sheet",
            ],
            "tasks": [
                {"type": "read", "ref": "module-7", "label": "Read Module 7: Reading the Three Statements"},
                {"type": "flashcards", "deck": "statements", "label": "Flashcards: statement structure & links"},
                {"type": "practice", "ref": "statement-map", "label": "Map 20 accounts to the correct statement"},
                {"type": "quiz", "ref": "quiz-statements", "label": "Take Quiz: Financial Statements"},
            ],
            "checkpoint": "Sketch how Income Statement → Statement of Equity → Balance Sheet connect.",
            "visaUnlock": "financial-statements",
        },
        {
            "id": 9,
            "day": 9,
            "week": 2,
            "title": "Adjusting Entries",
            "theme": "Period-End",
            "durationMinutes": 90,
            "goals": [
                "Prepare accruals and deferrals",
                "Record depreciation and supplies used",
                "Explain why adjusting entries never involve Cash",
            ],
            "tasks": [
                {"type": "read", "ref": "module-8", "label": "Read Module 8: Adjusting Entries"},
                {"type": "practice", "ref": "adjusting", "label": "Write 12 adjusting entries"},
                {"type": "flashcards", "deck": "adjusting", "label": "Flashcards: prepaid, accrued, depreciation"},
                {"type": "quiz", "ref": "quiz-adjusting", "label": "Take Quiz: Adjusting Entries"},
            ],
            "checkpoint": "Given prepaid insurance, accrued wages, and equipment, write all three adjusting entries.",
            "visaUnlock": "adjusting-entries",
        },
        {
            "id": 10,
            "day": 10,
            "week": 2,
            "title": "Closing Entries & Temporary Accounts",
            "theme": "Period-End",
            "durationMinutes": 75,
            "goals": [
                "Distinguish permanent vs temporary accounts",
                "Close revenues, expenses, and drawings to Income Summary / Capital",
                "Produce a post-closing trial balance mentally",
            ],
            "tasks": [
                {"type": "read", "ref": "module-9", "label": "Read Module 9: Closing the Books"},
                {"type": "practice", "ref": "closing", "label": "Perform a full closing sequence"},
                {"type": "flashcards", "deck": "closing", "label": "Flashcards: temporary vs permanent"},
                {"type": "quiz", "ref": "quiz-closing", "label": "Take Quiz: Closing Entries"},
            ],
            "checkpoint": "List which account types reset to zero at year-end and which carry forward.",
            "visaUnlock": None,
        },
        {
            "id": 11,
            "day": 11,
            "week": 2,
            "title": "Finance Basics — Money, Time & Statements",
            "theme": "Finance Bridge",
            "durationMinutes": 75,
            "goals": [
                "Connect accounting numbers to business decisions",
                "Compute basic ratios: current, quick, debt-to-equity, profit margin, ROE",
                "Explain liquidity, solvency, and profitability in plain language",
            ],
            "tasks": [
                {"type": "read", "ref": "module-10", "label": "Read Module 10: Finance Basics for Accountants"},
                {"type": "flashcards", "deck": "finance-ratios", "label": "Flashcards: ratios & interpretations"},
                {"type": "practice", "ref": "ratio-lab", "label": "Compute ratios from a sample balance sheet & IS"},
                {"type": "quiz", "ref": "quiz-finance", "label": "Take Quiz: Finance Basics"},
            ],
            "checkpoint": "Given simple statements, compute current ratio and profit margin and interpret both.",
            "visaUnlock": "finance-literacy",
        },
        {
            "id": 12,
            "day": 12,
            "week": 2,
            "title": "Cash Flow Sense",
            "theme": "Finance Bridge",
            "durationMinutes": 60,
            "goals": [
                "Classify cash flows as operating, investing, financing",
                "Explain why profit ≠ cash",
                "Spot common cash traps (growth, receivables, inventory)",
            ],
            "tasks": [
                {"type": "read", "ref": "module-11", "label": "Read Module 11: Cash Flow Basics"},
                {"type": "flashcards", "deck": "cash-flow", "label": "Flashcards: O/I/F classification"},
                {"type": "practice", "ref": "cf-classify", "label": "Classify 20 cash activities"},
                {"type": "quiz", "ref": "quiz-cashflow", "label": "Take Quiz: Cash Flow"},
            ],
            "checkpoint": "Explain three reasons a profitable company can run out of cash.",
            "visaUnlock": None,
        },
        {
            "id": 13,
            "day": 13,
            "week": 2,
            "title": "Speed Drills & Weak Spots",
            "theme": "Mastery",
            "durationMinutes": 90,
            "goals": [
                "Hit automatic recall on debit/credit rules",
                "Close gaps from earlier quiz scores",
                "Complete mixed transaction speed set",
            ],
            "tasks": [
                {"type": "trainer", "ref": "dc-trainer", "label": "Debit/Credit Trainer — timed 40 rounds"},
                {"type": "flashcards", "deck": "weak-spots", "label": "Focus flashcards on missed items"},
                {"type": "practice", "ref": "speed-set", "label": "Speed set: 15 journal entries in 30 minutes"},
                {"type": "quiz", "ref": "quiz-mixed", "label": "Mixed Mastery Quiz"},
            ],
            "checkpoint": "Average ≥85% across debit/credit trainer and Mixed Mastery Quiz.",
            "visaUnlock": "speed-accuracy",
        },
        {
            "id": 14,
            "day": 14,
            "week": 2,
            "title": "Capstone Confidence Day",
            "theme": "Mastery",
            "durationMinutes": 120,
            "goals": [
                "Complete the full Capstone simulation",
                "Collect remaining Mastery Visas",
                "Write your personal 'ready checklist' for ongoing practice",
            ],
            "tasks": [
                {"type": "practice", "ref": "capstone", "label": "Capstone: 15 transactions + adjustments + statements sketch"},
                {"type": "quiz", "ref": "quiz-capstone", "label": "Capstone Exam (comprehensive)"},
                {"type": "visa", "ref": "passport", "label": "Stamp your Mastery Passport"},
                {"type": "read", "ref": "module-12", "label": "Read Module 12: Keep Sharp — Ongoing Practice Plan"},
            ],
            "checkpoint": "Pass Capstone ≥80% and hold all core Mastery Visas.",
            "visaUnlock": "capstone-ready",
        },
    ]


def modules():
    return [
        {
            "id": 1,
            "slug": "module-1",
            "title": "The Language of Business",
            "subtitle": "Accounting equation & why it never breaks",
            "level": "foundation",
            "readMinutes": 12,
            "sections": [
                {
                    "heading": "What accounting actually does",
                    "body": "Accounting is a measurement and communication system. It turns messy economic events — sales, purchases, loans, payroll — into a structured story about resources and claims. Finance then uses those numbers to decide: invest, lend, price, cut, expand. If you lost touch with the basics, start here: every advanced topic still rests on one equation.",
                },
                {
                    "heading": "The accounting equation",
                    "body": "Assets = Liabilities + Equity. Assets are resources the business controls (cash, inventory, equipment). Liabilities are outsider claims (loans, accounts payable). Equity is the owner/investor residual claim. If assets rise without a matching liability, equity rose (profit or owner investment). If assets fall without reducing a liability, equity fell (loss or owner withdrawal).",
                },
                {
                    "heading": "Expanded form",
                    "body": "Equity is not a single mystery pile. For a sole proprietor: Equity = Capital + Revenues − Expenses − Drawings. Corporations use Common Stock + Retained Earnings (and Retained Earnings grow with Net Income and shrink with Dividends). Revenues increase equity; expenses and drawings/dividends decrease equity. That is how the income statement plugs into the balance sheet.",
                },
                {
                    "heading": "Why the equation always balances",
                    "body": "Every transaction has at least two effects. Buy equipment with cash: one asset up, another asset down. Borrow cash: asset up, liability up. Earn a cash sale: asset up, equity up (via revenue). Pay wages: asset down, equity down (via expense). Double-entry is simply the discipline of recording both effects so the equation never breaks.",
                },
                {
                    "heading": "Memory anchor",
                    "body": "Picture a balance scale. Left pan = Assets. Right pan = Liabilities + Equity. Debits and credits (Day 3) are the formal left/right recording rules that keep the scale level after every entry.",
                },
            ],
            "keyTakeaways": [
                "Assets = Liabilities + Equity — always",
                "Equity absorbs profit/loss and owner activity",
                "Every transaction has dual effects",
            ],
            "selfCheck": [
                "Define asset, liability, and equity in one sentence each",
                "Show how a cash sale affects the equation",
                "Show how paying a supplier on account affects the equation",
            ],
        },
        {
            "id": 2,
            "slug": "module-2",
            "title": "The Five Account Types",
            "subtitle": "Master classification until it is automatic",
            "level": "foundation",
            "readMinutes": 15,
            "sections": [
                {
                    "heading": "Why classification comes before debits",
                    "body": "People struggle with debits and credits because they skip account typing. The debit/credit rule depends entirely on what kind of account you are touching. Master the five types first; the rules then feel mechanical instead of mystical.",
                },
                {
                    "heading": "Assets",
                    "body": "Economic resources expected to provide future benefit. Current assets convert to cash within a year (or operating cycle): Cash, Accounts Receivable, Inventory, Prepaid Expenses, Short-term Investments. Noncurrent assets last longer: Equipment, Buildings, Land, Vehicles, Long-term Investments, Intangibles (patents, goodwill). Contra-assets like Accumulated Depreciation reduce the book value of related assets.",
                },
                {
                    "heading": "Liabilities",
                    "body": "Present obligations to transfer assets or provide services. Current: Accounts Payable, Short-term Notes Payable, Accrued Expenses (wages, interest, taxes payable), Unearned/Deferred Revenue, Current portion of long-term debt. Long-term: Bonds Payable, Mortgage Payable, Long-term Notes. Unearned Revenue surprises many people — cash received before earning is a liability, not revenue yet.",
                },
                {
                    "heading": "Equity",
                    "body": "Owner residual interest. Sole prop/partnership: Capital, Drawings (contra-equity). Corporation: Common Stock, Additional Paid-in Capital, Retained Earnings, Dividends (or a Dividends account that closes to RE), Treasury Stock (contra-equity). Equity rises with investments and net income; falls with distributions and losses.",
                },
                {
                    "heading": "Revenue (Income)",
                    "body": "Inflows from delivering goods/services in the ordinary course of business: Sales Revenue, Service Revenue, Interest Revenue, Rent Revenue. Revenue increases equity. Sales Returns & Allowances and Sales Discounts are contra-revenue accounts.",
                },
                {
                    "heading": "Expenses",
                    "body": "Costs of earning revenue: Cost of Goods Sold, Salaries Expense, Rent Expense, Utilities, Insurance, Depreciation, Interest Expense, Bad Debt Expense, Supplies Expense. Expenses decrease equity. Never confuse an expense (income statement, temporary) with an asset purchase that will benefit future periods.",
                },
                {
                    "heading": "Classification drills that stick",
                    "body": "Ask three questions: (1) Is it a resource we control? → Asset. (2) Do we owe it? → Liability. (3) Is it owner claim, earnings, or distribution? → Equity family. Then: Did we earn it this period? → Revenue. Did we consume cost to earn revenue this period? → Expense. Prepaid Rent is an asset; Rent Expense is what is used up.",
                },
            ],
            "keyTakeaways": [
                "Five types: Asset, Liability, Equity, Revenue, Expense",
                "Unearned revenue is a liability; prepaid expense is an asset",
                "Revenues increase equity; expenses decrease equity",
            ],
            "selfCheck": [
                "List five examples of each account type",
                "Classify: Prepaid Insurance, Unearned Rent, Dividends, Accumulated Depreciation, COGS",
            ],
        },
        {
            "id": 3,
            "slug": "module-3",
            "title": "Debits & Credits Deep Dive",
            "subtitle": "Left, right, and normal balances — no superstition",
            "level": "core",
            "readMinutes": 18,
            "sections": [
                {
                    "heading": "Debit and credit are directions, not judgments",
                    "body": "Debit (Dr) means left side of an account. Credit (Cr) means right side. Debit does not mean 'bad' and credit does not mean 'good.' Your bank says it 'credits' your account when money enters because from the bank's view your deposit is a liability to them — they credit a liability to increase it. In your books, Cash is an asset — you debit Cash to increase it. Same economic event, different books, different sides.",
                },
                {
                    "heading": "T-accounts",
                    "body": "A T-account is a sketch of a ledger account: account title on top, debits on the left stem, credits on the right. The balance is the difference between sides. Accounts with a normal debit balance (assets, expenses, drawings) usually show a debit balance. Accounts with a normal credit balance (liabilities, equity, revenue) usually show a credit balance.",
                },
                {
                    "heading": "DEA-LER mnemonic",
                    "body": "Dividends (Drawings), Expenses, Assets → normal Debit balances (increase with debits). Liabilities, Equity (Capital/Stock/RE), Revenue → normal Credit balances (increase with credits). Say it aloud: 'DEA on the debit side; LER on the credit side.' This one mnemonic unlocks almost every basic entry.",
                },
                {
                    "heading": "Increase and decrease rules",
                    "body": "Assets: Debit ↑ Credit ↓. Liabilities: Credit ↑ Debit ↓. Equity: Credit ↑ Debit ↓. Revenue: Credit ↑ Debit ↓. Expenses: Debit ↑ Credit ↓. Drawings/Dividends: Debit ↑ Credit ↓. To decrease any account, do the opposite of its normal balance side.",
                },
                {
                    "heading": "Golden rule of every entry",
                    "body": "Total debits must equal total credits. Always. A compound entry may touch three or more accounts, but the sum of debit amounts equals the sum of credit amounts. If it does not balance, you have an error — not a philosophical exception.",
                },
                {
                    "heading": "How to analyze any transaction",
                    "body": "Step 1: What accounts are affected? Step 2: What type is each? Step 3: Did each account increase or decrease? Step 4: Apply the debit/credit rule. Step 5: Check that debits = credits. Example: Buy $2,000 supplies on account → Supplies (asset ↑ → Debit 2,000); Accounts Payable (liability ↑ → Credit 2,000).",
                },
                {
                    "heading": "Common traps",
                    "body": "Trap 1: Thinking 'debit = expense always' — only expenses (and assets/dividends) are debited to increase; liabilities are debited to decrease. Trap 2: Crediting Cash because the bank credited you — in YOUR books Cash increases with a debit. Trap 3: Mixing up Unearned Revenue (credit to increase liability) with Revenue (credit to increase revenue when earned).",
                },
            ],
            "keyTakeaways": [
                "Debit = left; Credit = right",
                "DEA-LER: Dividends/Expenses/Assets debit-normal; Liabilities/Equity/Revenue credit-normal",
                "Every journal entry: Σ debits = Σ credits",
            ],
            "selfCheck": [
                "State the increase side for each of the five account types",
                "Record: receive $5,000 cash for services to be performed later",
                "Record: perform those services",
            ],
        },
        {
            "id": 4,
            "slug": "module-4",
            "title": "Journals, Ledgers & T-Accounts",
            "subtitle": "From narrative to permanent record",
            "level": "core",
            "readMinutes": 14,
            "sections": [
                {
                    "heading": "Source documents → Journal → Ledger",
                    "body": "Source documents (invoices, receipts, bank notices) evidence events. The general journal is the chronological book of original entry. Posting copies each line into the general ledger (the collection of all accounts). Trial balance lists ledger balances to prove debit totals equal credit totals.",
                },
                {
                    "heading": "Journal entry format",
                    "body": "Date. Debit account(s) aligned left with amounts in the debit column. Credit account(s) indented with amounts in the credit column. Brief narration/description. Example: Debit Cash 10,000; Credit Owner Capital 10,000 — 'Owner investment of cash.'",
                },
                {
                    "heading": "Core patterns to memorize",
                    "body": "Owner invests cash: Dr Cash, Cr Capital. Borrow from bank: Dr Cash, Cr Notes Payable. Buy asset for cash: Dr Asset, Cr Cash. Buy asset on account: Dr Asset, Cr Accounts Payable. Pay supplier: Dr Accounts Payable, Cr Cash. Cash sale: Dr Cash, Cr Revenue. Sale on account: Dr Accounts Receivable, Cr Revenue. Customer pays: Dr Cash, Cr Accounts Receivable. Pay expense: Dr Expense, Cr Cash. Accrue expense: Dr Expense, Cr Payable.",
                },
                {
                    "heading": "Posting and balancing",
                    "body": "After journalizing, post to T-accounts / ledger accounts. Foot (add) each side and compute the balance. Asset-like accounts should not normally show credit balances (except contra accounts). If Cash has a credit balance, investigate — possible error or overdraft treatment.",
                },
            ],
            "keyTakeaways": [
                "Journal = chronological; Ledger = by account",
                "Debit lines first, credit lines indented",
                "Memorize the dozen core entry patterns",
            ],
            "selfCheck": [
                "Journalize purchase of equipment $8,000: $3,000 cash and $5,000 note",
                "Post that entry to three T-accounts",
            ],
        },
        {
            "id": 5,
            "slug": "module-5",
            "title": "The Accounting Cycle",
            "subtitle": "The repeating rhythm of a reporting period",
            "level": "core",
            "readMinutes": 12,
            "sections": [
                {
                    "heading": "Steps in order",
                    "body": "1) Analyze transactions from source documents. 2) Journalize. 3) Post to ledger. 4) Unadjusted trial balance. 5) Adjusting entries. 6) Adjusted trial balance. 7) Prepare financial statements. 8) Closing entries. 9) Post-closing trial balance. (Optional: reversing entries next period.) Learn this spine; every 'advanced' topic hangs on one of these steps.",
                },
                {
                    "heading": "Why trial balances exist",
                    "body": "A trial balance checks arithmetic equality of debits and credits. It does NOT prove you used the correct accounts — only that the books are in balance. You can debit the wrong asset and still balance. Analysis skill still matters.",
                },
                {
                    "heading": "Where beginners get lost",
                    "body": "Skipping adjustments (accruals/deferrals) produces incomplete statements. Closing too early mixes periods. Treating temporary accounts like permanent ones leaves revenue/expense balances hanging into next year — a classic error.",
                },
            ],
            "keyTakeaways": [
                "Cycle: journalize → post → trial balance → adjust → statements → close",
                "Trial balance ≠ proof of correct classification",
                "Adjustments and closings are not optional in accrual accounting",
            ],
            "selfCheck": [
                "List the cycle steps from memory",
                "State what the post-closing trial balance should contain",
            ],
        },
        {
            "id": 6,
            "slug": "module-6",
            "title": "Accrual Thinking",
            "subtitle": "When to recognize revenue and expense",
            "level": "core",
            "readMinutes": 14,
            "sections": [
                {
                    "heading": "Cash vs accrual",
                    "body": "Cash basis recognizes revenue when cash is received and expenses when cash is paid. Accrual basis recognizes revenue when earned and expenses when incurred — regardless of cash timing. GAAP/IFRS financial statements for most businesses use accrual. Cash basis can mislead: collect a huge customer prepayment and look profitable when you have only deferred a liability.",
                },
                {
                    "heading": "Revenue recognition idea",
                    "body": "Recognize revenue when you satisfy a performance obligation — deliver the good or perform the service. If cash comes first: Debit Cash, Credit Unearned Revenue; later Debit Unearned Revenue, Credit Revenue. If service first: Debit Accounts Receivable, Credit Revenue; later Debit Cash, Credit AR.",
                },
                {
                    "heading": "Matching principle",
                    "body": "Record expenses in the same period as the revenues they help generate. Cost of goods sold matches with sales. Depreciation spreads equipment cost across periods of use. Accrued wages match labor cost to the period worked even if payday is next month.",
                },
                {
                    "heading": "Four timing buckets",
                    "body": "1) Accrued revenue: earned, not yet billed/received. 2) Accrued expense: incurred, not yet paid. 3) Deferred revenue: cash in, not yet earned. 4) Deferred expense (prepaid): cash out, not yet consumed. Adjusting entries exist mainly to fix these timing gaps at period-end.",
                },
            ],
            "keyTakeaways": [
                "Accrual = earned/incurred, not cash moving",
                "Unearned = liability; Prepaid = asset",
                "Match expenses to the revenues they support",
            ],
            "selfCheck": [
                "Company receives $12,000 Dec 1 for 3 months of service — entries on Dec 1 and Dec 31",
                "Employees earned $4,000 unpaid at month-end — adjusting entry",
            ],
        },
        {
            "id": 7,
            "slug": "module-7",
            "title": "Reading the Three Statements",
            "subtitle": "Income statement, equity, balance sheet — and the links",
            "level": "reporting",
            "readMinutes": 14,
            "sections": [
                {
                    "heading": "Income Statement",
                    "body": "Performance over a period. Revenues − Expenses = Net Income (or Loss). Multi-step formats highlight Gross Profit (Sales − COGS), Operating Income, then other items and Net Income. Temporary accounts live here.",
                },
                {
                    "heading": "Statement of Owner's Equity / Retained Earnings",
                    "body": "Bridge statement. Beginning equity + investments + net income − drawings/dividends = ending equity. This is the pipe that connects period performance into the balance sheet's equity section.",
                },
                {
                    "heading": "Balance Sheet",
                    "body": "Position at a point in time. Assets listed (often current then noncurrent); liabilities (current then long-term); equity. Assets must equal Liabilities + Equity. Permanent accounts live here.",
                },
                {
                    "heading": "Articulation (the links)",
                    "body": "Net Income flows to equity. Ending cash on the balance sheet should reconcile to the cash flow statement's ending cash. Understanding articulation is the difference between memorizing formats and actually reading a business.",
                },
            ],
            "keyTakeaways": [
                "IS = period performance; BS = point-in-time position",
                "Net income updates equity",
                "Know which accounts are temporary vs permanent",
            ],
            "selfCheck": [
                "Place Cash, Sales, AP, Depreciation Expense, Common Stock on the correct statement",
                "Explain articulation in two sentences",
            ],
        },
        {
            "id": 8,
            "slug": "module-8",
            "title": "Adjusting Entries",
            "subtitle": "Making accrual accounting true at period-end",
            "level": "reporting",
            "readMinutes": 15,
            "sections": [
                {
                    "heading": "Purpose",
                    "body": "Adjusting entries update accounts before statements so revenues and expenses reflect the correct period. They almost never involve Cash — cash was recorded when it moved; adjustments allocate earning and consuming.",
                },
                {
                    "heading": "Prepaid expenses",
                    "body": "Originally: Dr Prepaid Insurance, Cr Cash. Adjusting: Dr Insurance Expense, Cr Prepaid Insurance for the portion used. Same pattern for prepaid rent and supplies (or Dr Supplies Expense, Cr Supplies).",
                },
                {
                    "heading": "Unearned revenue",
                    "body": "Originally: Dr Cash, Cr Unearned Revenue. Adjusting: Dr Unearned Revenue, Cr Revenue for the portion earned.",
                },
                {
                    "heading": "Accrued expenses & revenues",
                    "body": "Accrued wages: Dr Wages Expense, Cr Wages Payable. Accrued interest: Dr Interest Expense, Cr Interest Payable. Accrued service revenue: Dr Accounts Receivable (or Accrued Receivable), Cr Revenue.",
                },
                {
                    "heading": "Depreciation",
                    "body": "Dr Depreciation Expense, Cr Accumulated Depreciation (contra-asset). You do not credit the equipment account directly under this common method. Book value = Cost − Accumulated Depreciation.",
                },
            ],
            "keyTakeaways": [
                "Adjustments allocate; they usually skip Cash",
                "Four families: prepaid, unearned, accrued exp, accrued rev (+ depreciation)",
                "Always think: what was earned/used this period?",
            ],
            "selfCheck": [
                "Adjust $6,000 prepaid rent for 1 of 6 months used",
                "Record depreciation $500 and accrued interest $200",
            ],
        },
        {
            "id": 9,
            "slug": "module-9",
            "title": "Closing the Books",
            "subtitle": "Reset temporary accounts for the new period",
            "level": "reporting",
            "readMinutes": 12,
            "sections": [
                {
                    "heading": "Temporary vs permanent",
                    "body": "Temporary (nominal): Revenues, Expenses, Drawings/Dividends, Income Summary — closed to zero each period. Permanent (real): Assets, Liabilities, Equity capital accounts — balances carry forward.",
                },
                {
                    "heading": "Classic closing sequence",
                    "body": "1) Close revenue accounts to Income Summary (Dr Revenues, Cr Income Summary). 2) Close expense accounts to Income Summary (Dr Income Summary, Cr Expenses). 3) Close Income Summary to Capital/Retained Earnings (net income: Dr Income Summary, Cr Capital/RE; loss reverses). 4) Close Drawings/Dividends to Capital/RE (Dr Capital/RE, Cr Drawings/Dividends).",
                },
                {
                    "heading": "Post-closing trial balance",
                    "body": "Only permanent accounts remain. If a revenue or expense still has a balance, closing is incomplete.",
                },
            ],
            "keyTakeaways": [
                "Close temporary accounts; keep permanent ones",
                "Income Summary is a clearing account for closing",
                "Post-closing TB = balance sheet accounts only",
            ],
            "selfCheck": [
                "Write the four closing entries given Revenue 50k, Expenses 35k, Drawings 5k",
            ],
        },
        {
            "id": 10,
            "slug": "module-10",
            "title": "Finance Basics for Accountants",
            "subtitle": "Ratios and decisions from the numbers you record",
            "level": "finance",
            "readMinutes": 14,
            "sections": [
                {
                    "heading": "Accounting records; finance decides",
                    "body": "Accounting produces reliable measures. Finance asks: Can we pay bills? Are we too leveraged? Are we profitable enough? What return do owners earn? Basic ratios translate statements into decision language.",
                },
                {
                    "heading": "Liquidity",
                    "body": "Current ratio = Current Assets / Current Liabilities. Quick (acid-test) ratio = (Cash + Marketable Securities + AR) / Current Liabilities. Higher generally means more short-term cushion — but too high may mean idle cash.",
                },
                {
                    "heading": "Solvency",
                    "body": "Debt-to-equity = Total Liabilities / Equity. Debt ratio = Total Liabilities / Total Assets. These speak to long-term risk and creditor vs owner financing.",
                },
                {
                    "heading": "Profitability",
                    "body": "Gross margin = Gross Profit / Sales. Profit margin = Net Income / Sales. ROA = Net Income / Average Total Assets. ROE = Net Income / Average Equity. Trend and peer context matter more than a single magic number.",
                },
                {
                    "heading": "Time value taste",
                    "body": "A dollar today beats a dollar in five years because it can earn returns (and faces inflation/risk). PV and FV concepts sit behind bonds, leases, and capital budgeting — you only need the intuition now: timing of cash changes value.",
                },
            ],
            "keyTakeaways": [
                "Liquidity = short-term pay ability; solvency = long-term structure",
                "Margins and ROE/ROA measure performance",
                "Ratios need context: industry, trend, strategy",
            ],
            "selfCheck": [
                "Compute current ratio and debt-to-equity from a tiny balance sheet",
                "Interpret a profit margin falling while sales rise",
            ],
        },
        {
            "id": 11,
            "slug": "module-11",
            "title": "Cash Flow Basics",
            "subtitle": "Why profit is not cash — and how to classify flows",
            "level": "finance",
            "readMinutes": 12,
            "sections": [
                {
                    "heading": "Three sections",
                    "body": "Operating: core business cash (customers, suppliers, employees, interest/tax depending on presentation). Investing: long-lived assets and investments (buy/sell equipment, securities). Financing: debt and equity (borrow, repay, issue stock, dividends).",
                },
                {
                    "heading": "Profit ≠ cash",
                    "body": "Credit sales boost revenue before cash arrives. Buying inventory uses cash before COGS hits. Depreciation reduces income without using cash this period. Capex is cash out but capitalized, not fully expensed. Growth often consumes cash even when profitable.",
                },
                {
                    "heading": "Quick classification practice",
                    "body": "Collect from customers → Operating in. Pay suppliers → Operating out. Buy machine → Investing out. Sell old truck → Investing in. Bank loan → Financing in. Repay principal → Financing out. Pay dividend → Financing out. Owner contribution → Financing in.",
                },
            ],
            "keyTakeaways": [
                "O / I / F structure the cash story",
                "Accrual profit can diverge hard from cash",
                "Watch AR, inventory, and capex as cash traps",
            ],
            "selfCheck": [
                "Classify: issue stock, purchase inventory, sell equipment, pay wages",
                "Give three reasons profitable firms run out of cash",
            ],
        },
        {
            "id": 12,
            "slug": "module-12",
            "title": "Keep Sharp — Ongoing Practice Plan",
            "subtitle": "After your 14-day reset",
            "level": "mastery",
            "readMinutes": 8,
            "sections": [
                {
                    "heading": "Maintenance rhythm",
                    "body": "3× per week: 15 minutes flashcards (especially debit/credit and account typing). 1× per week: 10 journal entries from news-style narratives (a company borrowed, bought, sold, accrued). 1× per month: read one real set of financial statements and recompute two ratios.",
                },
                {
                    "heading": "Confidence checklist",
                    "body": "You are 'back' when you can: (1) classify any common account in 3 seconds, (2) recite DEA-LER, (3) journalize the top 12 transaction patterns without notes, (4) explain accrual vs cash with an example, (5) sketch how NI flows to equity, (6) name cycle steps in order.",
                },
                {
                    "heading": "Next learning lanes",
                    "body": "When basics feel automatic: inventory methods, receivables & bad debts, long-term assets, liabilities & bonds, equity transactions, statement of cash flows (indirect method), and managerial basics (cost behavior, CVP). Always return to the equation and DEA-LER when stuck.",
                },
            ],
            "keyTakeaways": [
                "Short, frequent drills beat rare cramming",
                "Use real statements to keep skills alive",
                "Basics are the debugging toolkit for advanced topics",
            ],
            "selfCheck": [
                "Schedule your next two weeks of maintenance drills",
            ],
        },
    ]


def account_types():
    examples = {
        "asset": [
            ("Cash", "current", "Money on hand and in bank accounts"),
            ("Accounts Receivable", "current", "Amounts customers owe for credit sales"),
            ("Inventory", "current", "Goods held for sale"),
            ("Supplies", "current", "Consumable items not yet used"),
            ("Prepaid Insurance", "current", "Insurance paid in advance"),
            ("Prepaid Rent", "current", "Rent paid in advance"),
            ("Short-term Investments", "current", "Marketable securities"),
            ("Notes Receivable (ST)", "current", "Promissory notes due within a year"),
            ("Equipment", "noncurrent", "Machinery and equipment cost"),
            ("Buildings", "noncurrent", "Building cost"),
            ("Land", "noncurrent", "Land cost (not depreciated)"),
            ("Vehicles", "noncurrent", "Company vehicles"),
            ("Accumulated Depreciation", "contra-asset", "Total depreciation taken to date"),
            ("Patents", "intangible", "Legal exclusive rights"),
            ("Goodwill", "intangible", "Acquisition premium not separately identifiable"),
        ],
        "liability": [
            ("Accounts Payable", "current", "Amounts owed to suppliers"),
            ("Wages Payable", "current", "Accrued unpaid wages"),
            ("Interest Payable", "current", "Accrued unpaid interest"),
            ("Taxes Payable", "current", "Taxes owed"),
            ("Unearned Revenue", "current", "Cash received before earning"),
            ("Short-term Notes Payable", "current", "Debt due within a year"),
            ("Current Portion of LTD", "current", "Long-term debt due this year"),
            ("Bonds Payable", "long-term", "Bond principal owed"),
            ("Mortgage Payable", "long-term", "Mortgage debt"),
            ("Long-term Notes Payable", "long-term", "Notes beyond one year"),
        ],
        "equity": [
            ("Owner Capital", "sole-prop", "Owner investments ± income − drawings"),
            ("Owner Drawings", "contra-equity", "Owner withdrawals"),
            ("Common Stock", "corporation", "Par/stated value of shares issued"),
            ("Additional Paid-in Capital", "corporation", "Amount above par from share issues"),
            ("Retained Earnings", "corporation", "Cumulative undistributed earnings"),
            ("Dividends", "temporary", "Distributions declared to shareholders"),
            ("Treasury Stock", "contra-equity", "Reacquired own shares"),
        ],
        "revenue": [
            ("Service Revenue", "operating", "Earnings from services"),
            ("Sales Revenue", "operating", "Earnings from goods sold"),
            ("Interest Revenue", "other", "Earnings from lending/investing"),
            ("Rent Revenue", "other", "Earnings from renting property"),
            ("Sales Returns & Allowances", "contra-revenue", "Returns and price allowances"),
            ("Sales Discounts", "contra-revenue", "Early-payment discounts granted"),
        ],
        "expense": [
            ("Cost of Goods Sold", "operating", "Cost of inventory sold"),
            ("Salaries Expense", "operating", "Employee compensation cost"),
            ("Rent Expense", "operating", "Rent consumed this period"),
            ("Utilities Expense", "operating", "Utilities consumed"),
            ("Insurance Expense", "operating", "Insurance expired"),
            ("Supplies Expense", "operating", "Supplies used"),
            ("Depreciation Expense", "operating", "Allocated cost of long-lived assets"),
            ("Interest Expense", "other", "Cost of borrowed money"),
            ("Bad Debt Expense", "operating", "Estimated uncollectible credit sales"),
            ("Advertising Expense", "operating", "Promotion costs"),
        ],
    }
    out = []
    i = 1
    meta = {
        "asset": {
            "name": "Assets",
            "normalBalance": "debit",
            "increaseWith": "debit",
            "decreaseWith": "credit",
            "equationSide": "left",
            "statement": "Balance Sheet",
            "temporary": False,
            "definition": "Resources controlled by the entity from which future economic benefits are expected.",
        },
        "liability": {
            "name": "Liabilities",
            "normalBalance": "credit",
            "increaseWith": "credit",
            "decreaseWith": "debit",
            "equationSide": "right",
            "statement": "Balance Sheet",
            "temporary": False,
            "definition": "Present obligations arising from past events, expected to result in outflow of resources.",
        },
        "equity": {
            "name": "Equity",
            "normalBalance": "credit",
            "increaseWith": "credit",
            "decreaseWith": "debit",
            "equationSide": "right",
            "statement": "Balance Sheet",
            "temporary": False,
            "definition": "Residual interest in assets after deducting liabilities; owner/investor claim.",
        },
        "revenue": {
            "name": "Revenue",
            "normalBalance": "credit",
            "increaseWith": "credit",
            "decreaseWith": "debit",
            "equationSide": "right (via equity)",
            "statement": "Income Statement",
            "temporary": True,
            "definition": "Increases in equity from delivering goods or services in ordinary activities.",
        },
        "expense": {
            "name": "Expenses",
            "normalBalance": "debit",
            "increaseWith": "debit",
            "decreaseWith": "credit",
            "equationSide": "reduces right-side equity",
            "statement": "Income Statement",
            "temporary": True,
            "definition": "Decreases in equity from consuming resources to generate revenue.",
        },
    }
    for key, m in meta.items():
        out.append(
            {
                "id": i,
                "key": key,
                "name": m["name"],
                "definition": m["definition"],
                "normalBalance": m["normalBalance"],
                "increaseWith": m["increaseWith"],
                "decreaseWith": m["decreaseWith"],
                "equationSide": m["equationSide"],
                "statement": m["statement"],
                "temporary": m["temporary"],
                "examples": [
                    {"name": n, "subtype": s, "note": note} for n, s, note in examples[key]
                ],
            }
        )
        i += 1
    return out


def mastery_visas():
    return [
        {
            "id": "account-types",
            "title": "Account Types Visa",
            "subtitle": "Classifier",
            "color": "#1F4D3A",
            "requirement": "Pass Account Types quiz ≥80% and complete account-sort practice",
            "skills": ["Identify five account types", "Give examples", "Spot contra accounts"],
            "day": 2,
        },
        {
            "id": "debits-credits",
            "title": "Debits & Credits Visa",
            "subtitle": "Double-Entry",
            "color": "#0B3A53",
            "requirement": "Pass Debits & Credits quiz ≥80% and complete 25 trainer rounds",
            "skills": ["DEA-LER recall", "Increase/decrease rules", "Balanced entries"],
            "day": 3,
        },
        {
            "id": "journal-entries",
            "title": "Journal Entries Visa",
            "subtitle": "Recorder",
            "color": "#5C3D1E",
            "requirement": "Pass Journal quiz ≥80% and complete journal-basics set",
            "skills": ["Standard patterns", "Compound entries", "Narrations"],
            "day": 4,
        },
        {
            "id": "accrual-basis",
            "title": "Accrual Basis Visa",
            "subtitle": "Timing",
            "color": "#3E5C2E",
            "requirement": "Pass Accrual quiz ≥80% and timing-cases practice",
            "skills": ["Revenue recognition", "Matching", "Accrual vs cash"],
            "day": 6,
        },
        {
            "id": "week1-foundation",
            "title": "Week 1 Foundation Visa",
            "subtitle": "Integrator",
            "color": "#1A3A2A",
            "requirement": "Pass Week 1 Comprehensive ≥80%",
            "skills": ["Equation", "Types", "Dr/Cr", "Cycle overview"],
            "day": 7,
        },
        {
            "id": "financial-statements",
            "title": "Statements Visa",
            "subtitle": "Reporter",
            "color": "#2C4A6E",
            "requirement": "Pass Statements quiz ≥80%",
            "skills": ["IS / Equity / BS map", "Articulation", "Temp vs permanent"],
            "day": 8,
        },
        {
            "id": "adjusting-entries",
            "title": "Adjusting Entries Visa",
            "subtitle": "Period-End",
            "color": "#6B4E2E",
            "requirement": "Pass Adjusting quiz ≥80%",
            "skills": ["Prepaids", "Unearned", "Accruals", "Depreciation"],
            "day": 9,
        },
        {
            "id": "finance-literacy",
            "title": "Finance Literacy Visa",
            "subtitle": "Analyst",
            "color": "#1F3D4D",
            "requirement": "Pass Finance Basics quiz ≥80%",
            "skills": ["Liquidity", "Solvency", "Profitability ratios"],
            "day": 11,
        },
        {
            "id": "speed-accuracy",
            "title": "Speed & Accuracy Visa",
            "subtitle": "Fluent",
            "color": "#4A2F1F",
            "requirement": "Mixed Mastery ≥85% and timed trainer target",
            "skills": ["Automatic classification", "Fast journalizing"],
            "day": 13,
        },
        {
            "id": "capstone-ready",
            "title": "Capstone Ready Visa",
            "subtitle": "Confident",
            "color": "#10281C",
            "requirement": "Pass Capstone Exam ≥80% and hold core visas",
            "skills": ["End-to-end cycle", "Self-sufficient refresh habit"],
            "day": 14,
        },
    ]


def flashcards():
    cards = []
    cid = 1

    def add(deck, front, back, tags=None, hint=None):
        nonlocal cid
        cards.append(
            {
                "id": cid,
                "deck": deck,
                "front": front,
                "back": back,
                "tags": tags or [],
                "hint": hint,
            }
        )
        cid += 1

    # equation
    add("equation", "State the accounting equation.", "Assets = Liabilities + Equity", ["foundation"])
    add("equation", "What are assets?", "Resources controlled by the business expected to provide future benefit.", ["foundation"])
    add("equation", "What are liabilities?", "Outsider claims — present obligations to transfer assets or services.", ["foundation"])
    add("equation", "What is equity?", "The residual owner/investor claim: Assets − Liabilities.", ["foundation"])
    add("equation", "How does net income affect the equation?", "It increases equity (retained earnings / capital).", ["foundation"])
    add("equation", "Effect: owner invests cash.", "Assets ↑ and Equity ↑ (same amount).", ["transactions"])
    add("equation", "Effect: borrow cash from bank.", "Assets ↑ and Liabilities ↑.", ["transactions"])
    add("equation", "Effect: buy equipment for cash.", "One asset ↑, another asset ↓ (total assets unchanged).", ["transactions"])
    add("equation", "Effect: pay an account payable.", "Assets ↓ and Liabilities ↓.", ["transactions"])
    add("equation", "Effect: cash sale of services.", "Assets ↑ and Equity ↑ (via revenue).", ["transactions"])
    add("equation", "Effect: pay wages in cash.", "Assets ↓ and Equity ↓ (via expense).", ["transactions"])
    add("equation", "Expanded equity (sole prop).", "Capital + Revenues − Expenses − Drawings.", ["foundation"])
    add("equation", "Does the equation ever not balance?", "No. If it doesn't, the analysis/recording is incomplete or wrong.", ["foundation"])
    add("equation", "Where do revenues and expenses live in the equation?", "They are temporary accounts that change equity.", ["foundation"])
    add("equation", "Buy inventory on account — equation effect?", "Assets ↑ (Inventory) and Liabilities ↑ (AP).", ["transactions"])

    # account types
    for name, typ in [
        ("Cash", "Asset"),
        ("Accounts Receivable", "Asset"),
        ("Inventory", "Asset"),
        ("Prepaid Rent", "Asset"),
        ("Equipment", "Asset"),
        ("Accumulated Depreciation", "Contra-asset"),
        ("Accounts Payable", "Liability"),
        ("Wages Payable", "Liability"),
        ("Unearned Revenue", "Liability"),
        ("Bonds Payable", "Liability"),
        ("Owner Capital", "Equity"),
        ("Owner Drawings", "Contra-equity / Equity withdrawal"),
        ("Common Stock", "Equity"),
        ("Retained Earnings", "Equity"),
        ("Dividends", "Equity distribution (temporary)"),
        ("Service Revenue", "Revenue"),
        ("Sales Revenue", "Revenue"),
        ("Sales Discounts", "Contra-revenue"),
        ("Salaries Expense", "Expense"),
        ("Cost of Goods Sold", "Expense"),
        ("Depreciation Expense", "Expense"),
        ("Interest Expense", "Expense"),
        ("Supplies (unused)", "Asset"),
        ("Supplies Expense", "Expense"),
        ("Prepaid Insurance", "Asset"),
        ("Insurance Expense", "Expense"),
    ]:
        add("account-types", f"Account type: {name}?", typ, ["classify"])

    add("account-types", "Is Unearned Revenue income?", "Not yet — it is a liability until earned.", ["trap"])
    add("account-types", "Is Prepaid Insurance an expense?", "Not yet — it is an asset until used/expired.", ["trap"])
    add("account-types", "Name the five primary account types.", "Assets, Liabilities, Equity, Revenue, Expenses.", ["foundation"])
    add("account-types", "Which account types appear on the Balance Sheet?", "Assets, Liabilities, Equity (permanent).", ["statements"])
    add("account-types", "Which account types appear on the Income Statement?", "Revenues and Expenses (temporary).", ["statements"])
    add("account-types", "What is a contra account?", "An account that offsets a related account (e.g., Accumulated Depreciation, Sales Returns).", ["advanced-basic"])

    # debit credit
    add("debit-credit", "What does Debit mean?", "The left side of an account — not 'bad.'", ["foundation"])
    add("debit-credit", "What does Credit mean?", "The right side of an account — not 'good.'", ["foundation"])
    add("debit-credit", "DEA-LER stands for?", "Dividends, Expenses, Assets (debit-normal) / Liabilities, Equity, Revenue (credit-normal).", ["mnemonic"], "DEA on debit; LER on credit")
    add("debit-credit", "Normal balance of Assets?", "Debit", ["normal"])
    add("debit-credit", "Normal balance of Liabilities?", "Credit", ["normal"])
    add("debit-credit", "Normal balance of Equity?", "Credit", ["normal"])
    add("debit-credit", "Normal balance of Revenue?", "Credit", ["normal"])
    add("debit-credit", "Normal balance of Expenses?", "Debit", ["normal"])
    add("debit-credit", "Normal balance of Dividends/Drawings?", "Debit", ["normal"])
    add("debit-credit", "To increase Cash, you…", "Debit Cash.", ["rules"])
    add("debit-credit", "To decrease Cash, you…", "Credit Cash.", ["rules"])
    add("debit-credit", "To increase Accounts Payable, you…", "Credit Accounts Payable.", ["rules"])
    add("debit-credit", "To decrease Accounts Payable, you…", "Debit Accounts Payable.", ["rules"])
    add("debit-credit", "To increase Service Revenue, you…", "Credit Service Revenue.", ["rules"])
    add("debit-credit", "To increase Rent Expense, you…", "Debit Rent Expense.", ["rules"])
    add("debit-credit", "To increase Unearned Revenue, you…", "Credit Unearned Revenue (liability ↑).", ["trap"])
    add("debit-credit", "Why does a bank 'credit' your deposit?", "On the bank's books your deposit is a liability; liabilities increase with credits.", ["trap"])
    add("debit-credit", "In YOUR books, how do you record a cash deposit from a customer payment on account?", "Debit Cash, Credit Accounts Receivable.", ["rules"])
    add("debit-credit", "Non-negotiable rule of every journal entry?", "Total debits = total credits.", ["foundation"])
    add("debit-credit", "Assets increase with _____ and decrease with _____.", "Debits; Credits", ["rules"])
    add("debit-credit", "Liabilities increase with _____ and decrease with _____.", "Credits; Debits", ["rules"])

    # journal patterns
    patterns = [
        ("Owner invests cash", "Dr Cash; Cr Owner Capital"),
        ("Borrow from bank", "Dr Cash; Cr Notes Payable"),
        ("Buy supplies for cash", "Dr Supplies; Cr Cash"),
        ("Buy supplies on account", "Dr Supplies; Cr Accounts Payable"),
        ("Pay accounts payable", "Dr Accounts Payable; Cr Cash"),
        ("Provide services for cash", "Dr Cash; Cr Service Revenue"),
        ("Provide services on account", "Dr Accounts Receivable; Cr Service Revenue"),
        ("Customer pays on account", "Dr Cash; Cr Accounts Receivable"),
        ("Pay rent for current month", "Dr Rent Expense; Cr Cash"),
        ("Receive cash before earning (advance)", "Dr Cash; Cr Unearned Revenue"),
        ("Earn previously unearned revenue", "Dr Unearned Revenue; Cr Revenue"),
        ("Owner withdraws cash", "Dr Drawings; Cr Cash"),
        ("Buy equipment with cash + note", "Dr Equipment; Cr Cash; Cr Notes Payable"),
        ("Accrue unpaid wages", "Dr Wages Expense; Cr Wages Payable"),
        ("Record depreciation", "Dr Depreciation Expense; Cr Accumulated Depreciation"),
    ]
    for front, back in patterns:
        add("journal", f"Journal entry: {front}", back, ["pattern"])

    # cycle
    add("cycle", "First step of the accounting cycle?", "Analyze transactions / source documents.", ["cycle"])
    add("cycle", "After journalizing comes…", "Posting to the ledger.", ["cycle"])
    add("cycle", "What does an unadjusted trial balance prove?", "That total debit balances equal total credit balances (not that accounts are correct).", ["cycle"])
    add("cycle", "When are adjusting entries made?", "At period-end, before financial statements.", ["cycle"])
    add("cycle", "What happens in closing?", "Temporary accounts are reset to zero; net income moves to equity.", ["cycle"])
    add("cycle", "Post-closing trial balance contains…", "Only permanent (balance sheet) accounts.", ["cycle"])
    add("cycle", "List cycle spine in order.", "Journalize → Post → TB → Adjust → Adjusted TB → Statements → Close → Post-closing TB", ["cycle"])

    # accrual
    add("accrual", "Cash basis recognizes revenue when…", "Cash is received.", ["basis"])
    add("accrual", "Accrual basis recognizes revenue when…", "It is earned (performance obligation satisfied).", ["basis"])
    add("accrual", "Matching principle says…", "Record expenses in the same period as related revenues.", ["basis"])
    add("accrual", "Accrued expense means…", "Incurred but not yet paid (or fully recorded).", ["timing"])
    add("accrual", "Deferred/unearned revenue means…", "Cash collected before revenue is earned.", ["timing"])
    add("accrual", "Prepaid expense means…", "Cash paid before the expense is incurred/consumed.", ["timing"])
    add("accrual", "Do adjusting entries usually include Cash?", "No — cash was recorded when it moved.", ["trap"])

    # statements
    add("statements", "Income Statement shows…", "Revenues and expenses over a period → Net Income.", ["statements"])
    add("statements", "Balance Sheet shows…", "Assets, liabilities, equity at a point in time.", ["statements"])
    add("statements", "How does NI connect to the Balance Sheet?", "Via the equity/retained earnings bridge.", ["statements"])
    add("statements", "Is Cash on the Income Statement?", "No — Cash is a balance sheet asset (cash flows have their own statement).", ["trap"])
    add("statements", "Is Unearned Revenue a revenue line?", "No — liability on the Balance Sheet until earned.", ["trap"])
    add("statements", "Gross profit equals…", "Net Sales − Cost of Goods Sold.", ["statements"])

    # adjusting
    add("adjusting", "Adjust prepaid insurance used.", "Dr Insurance Expense; Cr Prepaid Insurance.", ["adjust"])
    add("adjusting", "Adjust supplies used.", "Dr Supplies Expense; Cr Supplies.", ["adjust"])
    add("adjusting", "Adjust unearned revenue now earned.", "Dr Unearned Revenue; Cr Revenue.", ["adjust"])
    add("adjusting", "Accrue wages owed.", "Dr Wages Expense; Cr Wages Payable.", ["adjust"])
    add("adjusting", "Record depreciation.", "Dr Depreciation Expense; Cr Accumulated Depreciation.", ["adjust"])
    add("adjusting", "Accrue interest owed.", "Dr Interest Expense; Cr Interest Payable.", ["adjust"])
    add("adjusting", "Book value of equipment equals…", "Cost − Accumulated Depreciation.", ["adjust"])

    # closing
    add("closing", "Temporary accounts include…", "Revenues, Expenses, Drawings/Dividends, Income Summary.", ["close"])
    add("closing", "Permanent accounts include…", "Assets, Liabilities, Capital / Stock / Retained Earnings.", ["close"])
    add("closing", "Close revenue to Income Summary.", "Dr Revenue; Cr Income Summary.", ["close"])
    add("closing", "Close expenses to Income Summary.", "Dr Income Summary; Cr Expenses.", ["close"])
    add("closing", "Close Income Summary with net income.", "Dr Income Summary; Cr Capital or Retained Earnings.", ["close"])
    add("closing", "Close drawings.", "Dr Capital / RE; Cr Drawings / Dividends.", ["close"])

    # finance ratios
    add("finance-ratios", "Current ratio", "Current Assets ÷ Current Liabilities — short-term liquidity.", ["ratios"])
    add("finance-ratios", "Quick ratio", "(Cash + Marketable Securities + AR) ÷ Current Liabilities.", ["ratios"])
    add("finance-ratios", "Debt-to-equity", "Total Liabilities ÷ Equity — leverage/solvency.", ["ratios"])
    add("finance-ratios", "Profit margin", "Net Income ÷ Sales — profitability per sales dollar.", ["ratios"])
    add("finance-ratios", "ROE", "Net Income ÷ Average Equity — return to owners.", ["ratios"])
    add("finance-ratios", "ROA", "Net Income ÷ Average Assets — return on resource base.", ["ratios"])
    add("finance-ratios", "Gross margin", "Gross Profit ÷ Sales.", ["ratios"])
    add("finance-ratios", "Liquidity vs solvency", "Liquidity: near-term bill paying. Solvency: long-term debt capacity/structure.", ["finance"])

    # cash flow
    add("cash-flow", "Buy equipment — cash flow section?", "Investing outflow.", ["cf"])
    add("cash-flow", "Collect from customers — section?", "Operating inflow.", ["cf"])
    add("cash-flow", "Issue shares — section?", "Financing inflow.", ["cf"])
    add("cash-flow", "Pay dividends — section?", "Financing outflow.", ["cf"])
    add("cash-flow", "Bank loan proceeds — section?", "Financing inflow.", ["cf"])
    add("cash-flow", "Repay loan principal — section?", "Financing outflow.", ["cf"])
    add("cash-flow", "Why can profit ≠ cash?", "Timing differences: AR, inventory, payables, depreciation, capex, financing.", ["cf"])
    add("cash-flow", "Pay suppliers — section?", "Operating outflow.", ["cf"])

    # mixed / weak spots duplicates for review decks
    for c in list(cards):
        if c["deck"] in ("debit-credit", "account-types", "journal") and c["id"] % 3 == 0:
            add("mixed-week1", c["front"], c["back"], ["review", c["deck"]])
        if c["deck"] in ("adjusting", "closing", "statements", "finance-ratios") and c["id"] % 4 == 0:
            add("weak-spots", c["front"], c["back"], ["review", c["deck"]])

    return cards


def quizzes():
    def q(qid, quiz_id, prompt, options, answer, explain, qtype="mcq"):
        return {
            "id": qid,
            "quizId": quiz_id,
            "prompt": prompt,
            "options": options,
            "answer": answer,
            "explain": explain,
            "type": qtype,
        }

    questions = []
    n = 1

    # quiz-equation
    eq = [
        ("The accounting equation is:", ["Assets = Liabilities + Equity", "Assets = Liabilities − Equity", "Assets + Liabilities = Equity", "Assets = Revenue − Expenses"], 0, "Assets equal the sum of creditor and owner claims."),
        ("Paying a supplier for an amount owed does what?", ["Decrease assets and decrease liabilities", "Decrease assets and decrease equity", "Increase assets and increase liabilities", "No effect"], 0, "Dr AP, Cr Cash — both sides of BS fall."),
        ("Owner invests a truck into the business:", ["Assets ↑ Equity ↑", "Assets ↑ Liabilities ↑", "Assets ↓ Equity ↓", "Only memo entry"], 0, "Asset contributed increases capital."),
        ("Net loss affects the equation by:", ["Decreasing equity", "Increasing liabilities always", "Increasing assets", "No effect on equity"], 0, "Losses reduce retained earnings/capital."),
        ("Which is NOT an asset?", ["Accounts Payable", "Cash", "Inventory", "Prepaid Rent"], 0, "AP is a liability."),
        ("Buy land with cash:", ["Composition of assets changes; totals may stay same", "Liabilities increase", "Equity increases", "Expenses increase"], 0, "Land ↑ Cash ↓."),
        ("Revenues ultimately increase:", ["Equity", "Liabilities only", "Contra-assets", "Drawings"], 0, "Via net income into capital/RE."),
        ("If assets are 80 and liabilities 50, equity is:", ["30", "130", "50", "80"], 0, "80 − 50 = 30."),
        ("Unearned revenue is classified as:", ["Liability", "Revenue", "Equity", "Asset"], 0, "Obligation to perform or refund."),
        ("Drawings/dividends:", ["Decrease equity", "Increase expenses on BS", "Increase assets", "Increase liabilities"], 0, "Distributions reduce owner claim."),
    ]
    for prompt, opts, ans, exp in eq:
        questions.append(q(n, "quiz-equation", prompt, opts, ans, exp))
        n += 1

    # account types
    at = [
        ("Prepaid Insurance is a(n):", ["Asset", "Expense", "Liability", "Equity"], 0, "Future benefit remains."),
        ("Unearned Rent is a(n):", ["Liability", "Revenue", "Asset", "Equity"], 0, "Cash before earning."),
        ("Accumulated Depreciation is a:", ["Contra-asset", "Liability", "Expense", "Equity"], 0, "Offsets asset cost."),
        ("COGS is a(n):", ["Expense", "Asset", "Liability", "Equity"], 0, "Cost matched to sales."),
        ("Retained Earnings is:", ["Equity", "Revenue", "Asset", "Liability"], 0, "Cumulative earnings kept."),
        ("Which is temporary?", ["Service Revenue", "Cash", "Accounts Payable", "Common Stock"], 0, "Closed each period."),
        ("Supplies on hand are:", ["Asset", "Expense", "Equity", "Revenue"], 0, "Unused supplies are asset."),
        ("Sales Returns & Allowances is:", ["Contra-revenue", "Expense asset", "Liability", "Equity capital"], 0, "Offsets sales."),
        ("Wages Payable is:", ["Liability", "Expense", "Asset", "Equity"], 0, "Obligation unpaid."),
        ("Which belongs on the income statement?", ["Depreciation Expense", "Accumulated Depreciation", "Prepaid Rent", "Unearned Revenue"], 0, "Expense is IS; others BS."),
        ("Dividends (declared) primarily affect:", ["Equity", "Operating expenses always", "Assets only with no equity change", "Revenue"], 0, "Distributions reduce equity."),
        ("Patents are typically:", ["Intangible assets", "Liabilities", "Equity", "Revenues"], 0, "Long-lived rights."),
    ]
    for prompt, opts, ans, exp in at:
        questions.append(q(n, "quiz-account-types", prompt, opts, ans, exp))
        n += 1

    # debits credits
    dc = [
        ("Debit means:", ["Left side", "Increase always", "Decrease always", "Bad news"], 0, "Direction, not judgment."),
        ("Normal balance of expenses:", ["Debit", "Credit", "Either", "None"], 0, "DEA-LER."),
        ("To increase Notes Payable:", ["Credit it", "Debit it", "Ignore until paid", "Debit Cash only"], 0, "Liabilities credit ↑."),
        ("Cash sale of services:", ["Dr Cash; Cr Revenue", "Dr Revenue; Cr Cash", "Dr Cash; Cr Unearned", "Dr AR; Cr Cash"], 0, "Asset ↑ Revenue ↑."),
        ("Pay rent for this month in cash:", ["Dr Rent Expense; Cr Cash", "Dr Cash; Cr Rent Expense", "Dr Prepaid Rent; Cr Revenue", "Dr Rent Expense; Cr AP"], 0, "Expense incurred now."),
        ("DEA-LER: which are debit-normal?", ["Dividends, Expenses, Assets", "Liabilities, Equity, Revenue", "Only Cash", "Only Expenses"], 0, "Classic mnemonic."),
        ("Receive advance from customer:", ["Dr Cash; Cr Unearned Revenue", "Dr Cash; Cr Revenue", "Dr Unearned; Cr Cash", "Dr Revenue; Cr Cash"], 0, "Liability until earned."),
        ("Decrease an asset with a:", ["Credit", "Debit", "Memo only", "Closing entry only"], 0, "Opposite of normal debit."),
        ("Every journal entry must:", ["Balance debits and credits", "Include Cash", "Include Revenue", "Be a single line"], 0, "Double-entry rule."),
        ("Why 'bank credit' ≠ your book credit for Cash:", ["Bank liability vs your asset", "Banks never use double-entry", "Credits always increase cash for you", "Debits are illegal at banks"], 0, "Different entity perspective."),
        ("Accrue wages:", ["Dr Wages Expense; Cr Wages Payable", "Dr Wages Payable; Cr Expense", "Dr Cash; Cr Wages Expense", "Dr Expense; Cr Cash"], 0, "Incurred unpaid."),
        ("Owner withdrawal of cash:", ["Dr Drawings; Cr Cash", "Dr Expense; Cr Capital", "Dr Capital; Cr Revenue", "Dr Cash; Cr Drawings"], 0, "Drawings debit-normal."),
    ]
    for prompt, opts, ans, exp in dc:
        questions.append(q(n, "quiz-debits-credits", prompt, opts, ans, exp))
        n += 1

    # journal
    jn = [
        ("Buy $1,500 equipment for cash:", ["Dr Equipment 1500; Cr Cash 1500", "Dr Cash 1500; Cr Equipment 1500", "Dr Expense 1500; Cr Cash 1500", "Dr Equipment 1500; Cr Revenue 1500"], 0, "Asset swap."),
        ("Provide $900 services on account:", ["Dr AR 900; Cr Service Revenue 900", "Dr Cash 900; Cr AR 900", "Dr Revenue 900; Cr AR 900", "Dr AR 900; Cr Unearned 900"], 0, "Earned on credit."),
        ("Customer pays the $900:", ["Dr Cash 900; Cr AR 900", "Dr AR 900; Cr Cash 900", "Dr Cash 900; Cr Revenue 900", "Dr Revenue 900; Cr Cash 900"], 0, "Settle receivable."),
        ("Compound: equipment $10k with $4k cash + $6k note:", ["Dr Equipment 10k; Cr Cash 4k; Cr Notes Payable 6k", "Dr Cash 4k; Dr Notes 6k; Cr Equipment 10k", "Dr Equipment 4k; Cr Cash 4k only", "Dr Expense 10k; Cr Note 10k"], 0, "Compound entry balances."),
        ("Pay $700 previously recorded AP:", ["Dr AP 700; Cr Cash 700", "Dr Expense 700; Cr Cash 700", "Dr Cash 700; Cr AP 700", "Dr AP 700; Cr Expense 700"], 0, "Settle liability."),
        ("Proper journal form places:", ["Debits first, credits indented", "Credits first always", "Only one account per entry", "Amounts only in narration"], 0, "Standard presentation."),
        ("Bank loan $5,000 cash:", ["Dr Cash; Cr Notes Payable", "Dr Notes Payable; Cr Cash", "Dr Cash; Cr Revenue", "Dr Expense; Cr Notes"], 0, "Debt financing."),
        ("Record supplies bought on account $200:", ["Dr Supplies; Cr AP", "Dr AP; Cr Supplies", "Dr Supplies Expense; Cr Cash", "Dr Expense; Cr Supplies"], 0, "Asset + liability."),
    ]
    for prompt, opts, ans, exp in jn:
        questions.append(q(n, "quiz-journal", prompt, opts, ans, exp))
        n += 1

    # cycle
    cy = [
        ("Order: after posting to ledger you prepare:", ["Unadjusted trial balance", "Closing entries first", "Only cash flow statement", "Tax return only"], 0, "Check equality before adjustments."),
        ("Financial statements are prepared from:", ["Adjusted trial balance (typically)", "Source documents only", "Post-closing TB revenues", "Unposted journals"], 0, "After adjustments."),
        ("Closing entries occur:", ["After statements (end of period)", "Before analyzing transactions", "Instead of adjustments", "Only when cash is low"], 0, "Standard cycle order."),
        ("A balanced trial balance guarantees:", ["Debits equal credits — not perfect classification", "All accounts correct", "No fraud", "Cash is accurate"], 0, "Limited assurance."),
        ("Which is a permanent account?", ["Accounts Receivable", "Rent Expense", "Service Revenue", "Dividends"], 0, "BS accounts carry forward."),
        ("Source documents are used to:", ["Analyze and journalize transactions", "Close Income Summary", "Compute ROE only", "Replace ledgers"], 0, "Evidence trail."),
    ]
    for prompt, opts, ans, exp in cy:
        questions.append(q(n, "quiz-cycle", prompt, opts, ans, exp))
        n += 1

    # accrual
    ac = [
        ("Accrual accounting records revenue when:", ["Earned", "Cash is collected always", "Invoice is printed only", "Owner decides"], 0, "Earning process."),
        ("Cash collected before earning is:", ["Unearned revenue (liability)", "Immediate equity forever", "An expense", "A contra-asset"], 0, "Deferral."),
        ("Matching principle links:", ["Expenses to related revenues/period", "Assets to liabilities only", "Debits to bank statements", "Cash to equity"], 0, "Period alignment."),
        ("Employees worked now, paid next month:", ["Accrued expense", "Prepaid expense", "Unearned revenue", "Contra-liability"], 0, "Incurred unpaid."),
        ("Company finished work, not yet billed:", ["Accrued revenue", "Unearned revenue", "Prepaid rent", "Drawing"], 0, "Earned unbilled."),
        ("Paying a 12-month insurance policy upfront creates:", ["Prepaid Insurance (asset)", "12 months of expense immediately always", "A liability", "Revenue"], 0, "Defer expense."),
        ("Main reason profit ≠ cash:", ["Timing & noncash items under accrual", "Math errors only", "Equity never changes", "Banks forbid cash"], 0, "AR, inventory, depreciation, etc."),
        ("Adjusting entries typically exclude:", ["Cash", "Expenses", "Revenues", "Payables"], 0, "Cash already timed when moved."),
    ]
    for prompt, opts, ans, exp in ac:
        questions.append(q(n, "quiz-accrual", prompt, opts, ans, exp))
        n += 1

    # week1 comprehensive — sample from mix
    for quiz_id, count in [("quiz-week1", 15)]:
        pool = [x for x in questions if x["quizId"] in ("quiz-equation", "quiz-account-types", "quiz-debits-credits", "quiz-journal", "quiz-cycle", "quiz-accrual")]
        for i, item in enumerate(pool[:count]):
            questions.append(
                q(
                    n,
                    quiz_id,
                    item["prompt"],
                    item["options"],
                    item["answer"],
                    item["explain"],
                )
            )
            n += 1

    # statements
    st = [
        ("Net Income appears first on / flows to:", ["Equity / Retained Earnings bridge", "Assets directly as Cash always", "Liabilities", "Contra-revenue"], 0, "Articulation."),
        ("Point-in-time statement:", ["Balance Sheet", "Income Statement", "Statement of Cash Flows period total only", "Trial balance revenues"], 0, "Position snapshot."),
        ("Period performance statement:", ["Income Statement", "Balance Sheet", "Chart of accounts", "Post-closing TB alone"], 0, "Revenues − expenses."),
        ("Gross profit =", ["Sales − COGS", "Sales − Operating expenses", "Assets − Liabilities", "Cash − Payables"], 0, "Merchandiser metric."),
        ("Which is an income statement account?", ["Interest Expense", "Interest Payable", "Prepaid Interest", "Notes Payable"], 0, "Expense vs liability/prepaid."),
        ("Ending equity depends on:", ["Begin equity ± investments ± NI − distributions", "Only cash", "Only liabilities", "Only assets purchased"], 0, "Equity rollforward."),
        ("Cash is reported on:", ["Balance Sheet (and SCF)", "Income Statement as revenue", "Only equity section", "Never"], 0, "Asset + cash flow statement."),
        ("Unearned Revenue sits on:", ["Balance Sheet liabilities", "Income Statement always", "Equity capital", "Contra-asset"], 0, "Until earned."),
    ]
    for prompt, opts, ans, exp in st:
        questions.append(q(n, "quiz-statements", prompt, opts, ans, exp))
        n += 1

    # adjusting
    adj = [
        ("Prepaid rent $6,000 for 6 months; one month passes. Adjust:", ["Dr Rent Expense 1000; Cr Prepaid Rent 1000", "Dr Prepaid 1000; Cr Expense 1000", "Dr Expense 6000; Cr Cash 6000", "Dr Cash 1000; Cr Rent 1000"], 0, "1/6 used."),
        ("Depreciation for the period:", ["Dr Depreciation Expense; Cr Accumulated Depreciation", "Dr Equipment; Cr Expense", "Dr Accum Dep; Cr Cash", "Dr Expense; Cr Equipment always required"], 0, "Contra-asset method."),
        ("Earn $2,000 of previously unearned:", ["Dr Unearned Revenue 2000; Cr Revenue 2000", "Dr Revenue; Cr Unearned", "Dr Cash; Cr Revenue", "Dr Unearned; Cr Cash"], 0, "Liability → revenue."),
        ("Accrued interest $150:", ["Dr Interest Expense 150; Cr Interest Payable 150", "Dr Payable; Cr Expense", "Dr Expense; Cr Cash", "Dr Interest Revenue; Cr Cash"], 0, "Accrued expense."),
        ("Supplies begin 800, buy 200, end 300. Supplies expense:", ["700", "500", "300", "1000"], 0, "800+200−300=700."),
        ("Adjusting entries usually omit:", ["Cash", "Income statement accounts", "Balance sheet accounts", "Contra accounts"], 0, "Cash timing already recorded."),
        ("Book value equals:", ["Cost − Accumulated Depreciation", "Cost + Accumulated Depreciation", "Fair value always", "Cost − Expense × years only without accum"], 0, "Carrying amount."),
        ("Accrued revenue adjusting entry typically:", ["Dr Receivable; Cr Revenue", "Dr Revenue; Cr Cash", "Dr Unearned; Cr Cash", "Dr Expense; Cr Payable"], 0, "Earned not yet recorded."),
    ]
    for prompt, opts, ans, exp in adj:
        questions.append(q(n, "quiz-adjusting", prompt, opts, ans, exp))
        n += 1

    # closing
    cl = [
        ("Which is closed?", ["Service Revenue", "Cash", "Accounts Payable", "Land"], 0, "Temporary."),
        ("Close revenues:", ["Dr Revenues; Cr Income Summary", "Dr Income Summary; Cr Revenues", "Dr Revenues; Cr Cash", "Dr Capital; Cr Revenues"], 0, "Zero revenue."),
        ("Close expenses:", ["Dr Income Summary; Cr Expenses", "Dr Expenses; Cr Income Summary", "Dr Expenses; Cr Cash", "Dr Capital; Cr Expenses directly only always"], 0, "Dump expenses into summary."),
        ("Net income closing (sole prop):", ["Dr Income Summary; Cr Capital", "Dr Capital; Cr Income Summary", "Dr Cash; Cr Capital", "Dr Revenue; Cr Drawings"], 0, "NI to capital."),
        ("After closing, expenses balance should be:", ["Zero", "Equal to revenues", "Equal to assets", "Credit balance"], 0, "Reset."),
        ("Post-closing TB excludes:", ["Dividends / expenses / revenues", "Cash", "Liabilities", "Capital"], 0, "Temps gone."),
    ]
    for prompt, opts, ans, exp in cl:
        questions.append(q(n, "quiz-closing", prompt, opts, ans, exp))
        n += 1

    # finance
    fin = [
        ("Current ratio measures:", ["Liquidity", "Market share", "Tax rate", "Depreciation method"], 0, "CA/CL."),
        ("Debt-to-equity measures:", ["Leverage / solvency structure", "Gross margin", "Cash sales only", "Inventory turns only"], 0, "TL/Equity."),
        ("Profit margin =", ["NI / Sales", "Sales / NI", "CA / CL", "NI / Assets"], 0, "Profitability."),
        ("ROE focuses on return to:", ["Owners' equity", "Only creditors", "Inventory", "Tax authorities"], 0, "NI/Equity."),
        ("Quick ratio excludes:", ["Inventory (and usually prepaids)", "Cash", "AR", "Marketable securities"], 0, "More stringent liquidity."),
        ("Rising sales with falling profit margin may mean:", ["Costs growing faster than sales", "Always fraud", "Assets = 0", "No liabilities allowed"], 0, "Efficiency/cost pressure."),
        ("Solvency primarily concerns:", ["Long-term ability to meet obligations", "Next-day petty cash only", "Only revenue recognition", "Font on statements"], 0, "Structure/risk."),
        ("A very high current ratio could mean:", ["Idle current assets / inefficient use", "Guaranteed high ROE", "Zero liabilities always", "Negative equity"], 0, "Context matters."),
    ]
    for prompt, opts, ans, exp in fin:
        questions.append(q(n, "quiz-finance", prompt, opts, ans, exp))
        n += 1

    # cashflow
    cf = [
        ("Purchase of a delivery van is:", ["Investing outflow", "Operating inflow", "Financing inflow", "Equity expense"], 0, "Long-lived asset."),
        ("Cash from customers is:", ["Operating inflow", "Investing", "Financing", "Not reported"], 0, "Core operations."),
        ("Issuing stock for cash is:", ["Financing inflow", "Operating", "Investing", "Revenue"], 0, "Equity financing."),
        ("Paying dividends is:", ["Financing outflow", "Operating expense cash always", "Investing inflow", "Never cash"], 0, "Owner distribution."),
        ("Depreciation affects cash how (directly)?", ["No direct cash effect", "Always cash out equal to expense", "Financing inflow", "Investing inflow"], 0, "Noncash expense."),
        ("Repaying bank loan principal:", ["Financing outflow", "Operating outflow always", "Investing outflow", "Expense on IS equals cash"], 0, "Financing."),
        ("Profitable but cash-tight — common cause:", ["Growth in AR/inventory or heavy capex", "Too much depreciation cash drain", "Equity too high", "No revenues"], 0, "Working capital & investing."),
        ("Sale of old equipment for cash:", ["Investing inflow", "Operating inflow always", "Financing", "Revenue section of BS"], 0, "Investing."),
    ]
    for prompt, opts, ans, exp in cf:
        questions.append(q(n, "quiz-cashflow", prompt, opts, ans, exp))
        n += 1

    # mixed + capstone: reuse varied
    mixed_src = [x for x in questions if x["quizId"] in ("quiz-debits-credits", "quiz-adjusting", "quiz-statements", "quiz-finance", "quiz-account-types")]
    for i, item in enumerate(mixed_src[:12]):
        questions.append(q(n, "quiz-mixed", item["prompt"], item["options"], item["answer"], item["explain"]))
        n += 1

    cap_src = [x for x in questions if x["quizId"] in ("quiz-equation", "quiz-debits-credits", "quiz-accrual", "quiz-adjusting", "quiz-closing", "quiz-cashflow", "quiz-finance")]
    for i, item in enumerate(cap_src[:20]):
        questions.append(q(n, "quiz-capstone", item["prompt"], item["options"], item["answer"], item["explain"]))
        n += 1

    quiz_meta = [
        {"id": "quiz-equation", "title": "Accounting Equation", "day": 1, "passScore": 80, "visa": None},
        {"id": "quiz-account-types", "title": "Account Types", "day": 2, "passScore": 80, "visa": "account-types"},
        {"id": "quiz-debits-credits", "title": "Debits & Credits", "day": 3, "passScore": 80, "visa": "debits-credits"},
        {"id": "quiz-journal", "title": "Journal Entries", "day": 4, "passScore": 80, "visa": "journal-entries"},
        {"id": "quiz-cycle", "title": "Accounting Cycle", "day": 5, "passScore": 80, "visa": None},
        {"id": "quiz-accrual", "title": "Accrual vs Cash", "day": 6, "passScore": 80, "visa": "accrual-basis"},
        {"id": "quiz-week1", "title": "Week 1 Comprehensive", "day": 7, "passScore": 80, "visa": "week1-foundation"},
        {"id": "quiz-statements", "title": "Financial Statements", "day": 8, "passScore": 80, "visa": "financial-statements"},
        {"id": "quiz-adjusting", "title": "Adjusting Entries", "day": 9, "passScore": 80, "visa": "adjusting-entries"},
        {"id": "quiz-closing", "title": "Closing Entries", "day": 10, "passScore": 80, "visa": None},
        {"id": "quiz-finance", "title": "Finance Basics", "day": 11, "passScore": 80, "visa": "finance-literacy"},
        {"id": "quiz-cashflow", "title": "Cash Flow", "day": 12, "passScore": 80, "visa": None},
        {"id": "quiz-mixed", "title": "Mixed Mastery", "day": 13, "passScore": 85, "visa": "speed-accuracy"},
        {"id": "quiz-capstone", "title": "Capstone Exam", "day": 14, "passScore": 80, "visa": "capstone-ready"},
    ]
    return quiz_meta, questions


def practice_problems():
    problems = []
    pid = 1

    def add(set_id, title, prompt, solution, difficulty="basic", kind="journal"):
        nonlocal pid
        problems.append(
            {
                "id": pid,
                "setId": set_id,
                "title": title,
                "prompt": prompt,
                "solution": solution,
                "difficulty": difficulty,
                "kind": kind,
            }
        )
        pid += 1

    # classify basics
    items = [
        ("Company car", "Asset"),
        ("Bank loan due in 2 years", "Liability"),
        ("Owner capital", "Equity"),
        ("Cash register balance", "Asset"),
        ("Invoice from supplier unpaid", "Liability"),
        ("Trademark", "Asset"),
        ("Sales for the month", "Revenue"),
        ("Electricity used this month", "Expense"),
        ("Customer deposit for future work", "Liability"),
        ("Rent paid for next quarter", "Asset"),
        ("Shares issued at par", "Equity"),
        ("Interest owed on loan", "Liability"),
        ("Goods on shelves for sale", "Asset"),
        ("Owner personal withdrawal", "Equity (Drawings)"),
        ("Advertising campaign this week", "Expense"),
    ]
    for i, (name, ans) in enumerate(items, 1):
        add("classify-basics", f"Classify {i}: {name}", f"Is '{name}' an Asset, Liability, Equity, Revenue, or Expense?", ans, kind="classify")

    # account sort extras
    more = [
        ("Allowance for Doubtful Accounts", "Contra-asset"),
        ("Sales Discounts", "Contra-revenue"),
        ("Treasury Stock", "Contra-equity"),
        ("Current portion of mortgage", "Liability (current)"),
        ("Interest Revenue", "Revenue"),
        ("Bad Debt Expense", "Expense"),
        ("Office Supplies on hand", "Asset"),
        ("Dividends Payable", "Liability"),
        ("Additional Paid-in Capital", "Equity"),
        ("Unearned Subscriptions", "Liability"),
    ]
    for i, (name, ans) in enumerate(more, 1):
        add("account-sort", f"Sort {i}: {name}", f"Classify '{name}' precisely.", ans, kind="classify")

    # still need many for account-sort — add standard list
    for i, (name, ans) in enumerate(
        [
            ("Cash", "Asset"),
            ("AR", "Asset"),
            ("AP", "Liability"),
            ("Service Revenue", "Revenue"),
            ("Rent Expense", "Expense"),
            ("Prepaid Insurance", "Asset"),
            ("Unearned Revenue", "Liability"),
            ("Common Stock", "Equity"),
            ("RE", "Equity"),
            ("Inventory", "Asset"),
            ("Wages Payable", "Liability"),
            ("Depreciation Expense", "Expense"),
            ("Accumulated Depreciation", "Contra-asset"),
            ("Land", "Asset"),
            ("Notes Payable", "Liability"),
            ("Drawings", "Contra-equity"),
            ("COGS", "Expense"),
            ("Sales", "Revenue"),
            ("Utilities Expense", "Expense"),
            ("Mortgage Payable", "Liability"),
        ],
        1,
    ):
        add("account-sort", f"Type drill {i}", f"Account: {name}", ans, kind="classify")

    journals = [
        ("Owner invests $25,000 cash", "Dr Cash 25,000; Cr Owner Capital 25,000"),
        ("Borrowed $10,000 from bank on a note", "Dr Cash 10,000; Cr Notes Payable 10,000"),
        ("Bought supplies $600 on account", "Dr Supplies 600; Cr Accounts Payable 600"),
        ("Paid $600 to settle the supplies AP", "Dr Accounts Payable 600; Cr Cash 600"),
        ("Provided services for $3,200 cash", "Dr Cash 3,200; Cr Service Revenue 3,200"),
        ("Provided services $1,800 on account", "Dr Accounts Receivable 1,800; Cr Service Revenue 1,800"),
        ("Collected $1,200 of AR", "Dr Cash 1,200; Cr Accounts Receivable 1,200"),
        ("Paid monthly rent $1,500", "Dr Rent Expense 1,500; Cr Cash 1,500"),
        ("Received $4,000 advance for future work", "Dr Cash 4,000; Cr Unearned Revenue 4,000"),
        ("Completed 1/4 of the advance work ($1,000)", "Dr Unearned Revenue 1,000; Cr Service Revenue 1,000"),
        ("Owner withdrew $800 cash", "Dr Owner Drawings 800; Cr Cash 800"),
        ("Bought equipment $9,000: $2,000 cash + $7,000 note", "Dr Equipment 9,000; Cr Cash 2,000; Cr Notes Payable 7,000"),
    ]
    for i, (p, s) in enumerate(journals, 1):
        add("journal-basics", f"JE {i}", p, s, kind="journal")

    for i, step in enumerate(
        [
            "Analyze source documents",
            "Journalize",
            "Post to ledger",
            "Unadjusted trial balance",
            "Adjusting entries",
            "Adjusted trial balance",
            "Financial statements",
            "Closing entries",
            "Post-closing trial balance",
        ],
        1,
    ):
        add("cycle-order", f"Cycle step position {i}", f"What is step {i} of the accounting cycle?", step, kind="order")

    timing = [
        ("Dec 1: receive $3,000 for 3 months of service starting Dec 1. Entry on Dec 1?", "Dr Cash 3,000; Cr Unearned Revenue 3,000"),
        ("Dec 31 adjusting for one month earned of that advance?", "Dr Unearned Revenue 1,000; Cr Service Revenue 1,000"),
        ("Employees earned $2,500 unpaid at month end.", "Dr Wages Expense 2,500; Cr Wages Payable 2,500"),
        ("Paid $1,200 for 6 months insurance on day 1.", "Dr Prepaid Insurance 1,200; Cr Cash 1,200"),
        ("Month-end: one month of that insurance expired.", "Dr Insurance Expense 200; Cr Prepaid Insurance 200"),
        ("Finished $900 of work not yet billed.", "Dr Accounts Receivable 900; Cr Service Revenue 900"),
        ("Customer paid $500 for work done last month on account.", "Dr Cash 500; Cr Accounts Receivable 500"),
        ("Utility bill $140 arrived for this month, unpaid.", "Dr Utilities Expense 140; Cr Utilities Payable (or AP) 140"),
        ("Cash basis: when is the $3,000 advance revenue?", "When cash received — entire $3,000 (cash basis). Accrual spreads as earned."),
        ("Why is cash basis misleading for the advance?", "Shows revenue before obligation is satisfied; liability ignored."),
    ]
    for i, (p, s) in enumerate(timing, 1):
        add("timing-cases", f"Timing {i}", p, s, difficulty="core", kind="analysis")

    week1 = [
        ("Narrative set A1: Owner invests 20,000 cash", "Dr Cash 20,000; Cr Capital 20,000"),
        ("A2: Buy inventory 5,000 on account", "Dr Inventory 5,000; Cr AP 5,000"),
        ("A3: Cash sales 8,000 with COGS 3,000 (periodic ignore COGS if service co — assume service: only revenue). For merchandiser perpetual:", "Dr Cash 8,000; Cr Sales 8,000 and Dr COGS 3,000; Cr Inventory 3,000"),
        ("A4: Pay wages 2,000", "Dr Wages Expense 2,000; Cr Cash 2,000"),
        ("A5: Pay AP 2,500", "Dr AP 2,500; Cr Cash 2,500"),
        ("A6: Accrue interest 100", "Dr Interest Expense 100; Cr Interest Payable 100"),
        ("A7: Unearned earned 700", "Dr Unearned Revenue 700; Cr Revenue 700"),
        ("A8: Depreciation 400", "Dr Depreciation Expense 400; Cr Accumulated Depreciation 400"),
        ("Build trial balance idea", "List each account balance; total debits must equal total credits."),
        ("If TB debit total 55,400 what must credits be?", "55,400"),
    ]
    for i, (p, s) in enumerate(week1, 1):
        add("week1-lab", f"Lab {i}", p, s, difficulty="core", kind="lab")

    for i, (acct, stmt) in enumerate(
        [
            ("Cash", "Balance Sheet"),
            ("Sales Revenue", "Income Statement"),
            ("AP", "Balance Sheet"),
            ("Rent Expense", "Income Statement"),
            ("Common Stock", "Balance Sheet"),
            ("COGS", "Income Statement"),
            ("Unearned Revenue", "Balance Sheet"),
            ("Depreciation Expense", "Income Statement"),
            ("Accumulated Depreciation", "Balance Sheet"),
            ("Dividends", "Equity statement / closes to RE (not IS revenue)"),
            ("Inventory", "Balance Sheet"),
            ("Interest Payable", "Balance Sheet"),
            ("Interest Expense", "Income Statement"),
            ("Prepaid Insurance", "Balance Sheet"),
            ("Service Revenue", "Income Statement"),
            ("Retained Earnings", "Balance Sheet"),
            ("Equipment", "Balance Sheet"),
            ("Bad Debt Expense", "Income Statement"),
            ("Allowance for Doubtful Accounts", "Balance Sheet"),
            ("Notes Payable", "Balance Sheet"),
        ],
        1,
    ):
        add("statement-map", f"Map {i}", f"Which statement primarily reports {acct}?", stmt, kind="classify")

    adjs = [
        ("Prepaid insurance 2,400 for 12 months; 3 months elapsed", "Dr Insurance Expense 600; Cr Prepaid Insurance 600"),
        ("Supplies on hand were 900; count shows 350", "Dr Supplies Expense 550; Cr Supplies 550"),
        ("Unearned 6,000; 40% now earned", "Dr Unearned Revenue 2,400; Cr Revenue 2,400"),
        ("Weekly wages 4,000; 3 of 5 days accrued at month-end", "Dr Wages Expense 2,400; Cr Wages Payable 2,400"),
        ("Annual depreciation on equipment 3,600; one month", "Dr Depreciation Expense 300; Cr Accumulated Depreciation 300"),
        ("Note payable 12,000 at 10% annual; one month interest accrued", "Dr Interest Expense 100; Cr Interest Payable 100"),
        ("Performed $1,100 unbilled consulting", "Dr AR 1,100; Cr Service Revenue 1,100"),
        ("Property tax accrued estimate 750", "Dr Tax Expense 750; Cr Taxes Payable 750"),
        ("Rent received in advance monthly recognition 900", "Dr Unearned Rent 900; Cr Rent Revenue 900"),
        ("Advertising prepaid remaining 2 months of 5 originally; monthly is 200", "Dr Advertising Expense 200; Cr Prepaid Advertising 200"),
        ("Expired portion of license fee prepaid 150", "Dr License Expense 150; Cr Prepaid License 150"),
        ("Accrue utility 180", "Dr Utilities Expense 180; Cr Utilities Payable 180"),
    ]
    for i, (p, s) in enumerate(adjs, 1):
        add("adjusting", f"Adjust {i}", p, s, difficulty="core", kind="journal")

    add(
        "closing",
        "Full close",
        "Revenue 40,000; Expenses total 28,000; Drawings 3,000. Write four closing entries.",
        "1) Dr Revenue 40,000; Cr Income Summary 40,000. 2) Dr Income Summary 28,000; Cr Expenses 28,000. 3) Dr Income Summary 12,000; Cr Capital 12,000. 4) Dr Capital 3,000; Cr Drawings 3,000.",
        difficulty="core",
        kind="journal",
    )
    add("closing", "What remains after closing?", "List account types still open.", "Permanent accounts only: assets, liabilities, capital/equity permanent accounts.", kind="analysis")
    add("closing", "Income Summary role", "Why use Income Summary?", "Clearing account to close temps and move NI/loss to capital/RE.", kind="analysis")

    add(
        "ratio-lab",
        "Compute liquidity",
        "CA 45,000; Inventory 15,000; Prepaids 2,000; CL 20,000. Current ratio and quick ratio?",
        "Current = 45,000/20,000 = 2.25. Quick = (45,000−15,000−2,000)/20,000 = 1.40.",
        difficulty="core",
        kind="compute",
    )
    add(
        "ratio-lab",
        "Leverage & margin",
        "Liabilities 70,000; Equity 30,000; Sales 200,000; NI 12,000. D/E and profit margin?",
        "D/E = 70/30 = 2.33. Margin = 12/200 = 6%.",
        difficulty="core",
        kind="compute",
    )
    add(
        "ratio-lab",
        "ROE",
        "NI 25,000; Beginning equity 100,000; Ending equity 150,000. Approximate ROE using average equity.",
        "Average equity 125,000; ROE = 25/125 = 20%.",
        difficulty="core",
        kind="compute",
    )

    for i, (act, sec) in enumerate(
        [
            ("Pay employees", "Operating out"),
            ("Buy warehouse", "Investing out"),
            ("Issue bonds", "Financing in"),
            ("Collect AR", "Operating in"),
            ("Pay dividend", "Financing out"),
            ("Sell marketable securities (investment)", "Investing in"),
            ("Purchase inventory", "Operating out"),
            ("Owner capital cash contribution", "Financing in"),
            ("Repay note principal", "Financing out"),
            ("Interest paid (often operating under US GAAP)", "Operating out (common US GAAP presentation)"),
            ("Buy long-term investment", "Investing out"),
            ("Proceeds from sale of equipment", "Investing in"),
            ("Pay suppliers", "Operating out"),
            ("Borrow from bank", "Financing in"),
            ("Tax refund from operations", "Operating in"),
            ("Loan to supplier (note receivable LT)", "Investing out"),
            ("Repurchase treasury stock", "Financing out"),
            ("Customer advance received", "Operating in"),
            ("Capital expenditure on software capitalized", "Investing out"),
            ("Short-term trading activity nuance — treat investments carefully", "Investing (generally) — know policy"),
        ],
        1,
    ):
        add("cf-classify", f"CF {i}", f"Classify: {act}", sec, kind="classify")

    for i, p in enumerate(
        [
            ("Cash sale 500", "Dr Cash 500; Cr Revenue 500"),
            ("Credit sale 700", "Dr AR 700; Cr Revenue 700"),
            ("Collect 300 AR", "Dr Cash 300; Cr AR 300"),
            ("Buy supplies 50 cash", "Dr Supplies 50; Cr Cash 50"),
            ("AP payment 120", "Dr AP 120; Cr Cash 120"),
            ("Accrue wages 200", "Dr Wages Expense 200; Cr Wages Payable 200"),
            ("Earn unearned 80", "Dr Unearned 80; Cr Revenue 80"),
            ("Depreciation 60", "Dr Dep Expense 60; Cr Accum Dep 60"),
            ("Owner invest 1,000", "Dr Cash 1,000; Cr Capital 1,000"),
            ("Borrow 2,000", "Dr Cash 2,000; Cr Notes Payable 2,000"),
            ("Pay rent 400", "Dr Rent Expense 400; Cr Cash 400"),
            ("Buy equipment 1,500 on note", "Dr Equipment 1,500; Cr Notes Payable 1,500"),
            ("Owner draw 100", "Dr Drawings 100; Cr Cash 100"),
            ("Prepaid insurance 240 cash", "Dr Prepaid Insurance 240; Cr Cash 240"),
            ("Expire insurance 20", "Dr Insurance Expense 20; Cr Prepaid Insurance 20"),
        ],
        1,
    ):
        add("speed-set", f"Speed {i}", p[0], p[1], difficulty="drill", kind="journal")

    capstone_steps = [
        ("Capstone JE1", "Owner invests 50,000 cash", "Dr Cash 50,000; Cr Capital 50,000"),
        ("Capstone JE2", "Buy equipment 12,000 cash", "Dr Equipment 12,000; Cr Cash 12,000"),
        ("Capstone JE3", "Buy supplies 1,500 on account", "Dr Supplies 1,500; Cr AP 1,500"),
        ("Capstone JE4", "Cash services 9,000", "Dr Cash 9,000; Cr Revenue 9,000"),
        ("Capstone JE5", "Credit services 4,000", "Dr AR 4,000; Cr Revenue 4,000"),
        ("Capstone JE6", "Collect AR 2,500", "Dr Cash 2,500; Cr AR 2,500"),
        ("Capstone JE7", "Pay salaries 3,000", "Dr Salaries Expense 3,000; Cr Cash 3,000"),
        ("Capstone JE8", "Pay AP 900", "Dr AP 900; Cr Cash 900"),
        ("Capstone JE9", "Receive advance 1,800", "Dr Cash 1,800; Cr Unearned Revenue 1,800"),
        ("Capstone JE10", "Pay prepaid rent 2,400 for 6 months", "Dr Prepaid Rent 2,400; Cr Cash 2,400"),
        ("Capstone JE11", "Borrow 5,000 note", "Dr Cash 5,000; Cr Notes Payable 5,000"),
        ("Capstone JE12", "Owner draw 700", "Dr Drawings 700; Cr Cash 700"),
        ("Capstone JE13", "Pay utilities 350", "Dr Utilities Expense 350; Cr Cash 350"),
        ("Capstone JE14", "Purchase advertising 200 cash", "Dr Advertising Expense 200; Cr Cash 200"),
        ("Capstone JE15", "Customer pays 600 toward new advance", "Dr Cash 600; Cr Unearned Revenue 600"),
        ("Adj1", "Rent used: 1 month of prepaid", "Dr Rent Expense 400; Cr Prepaid Rent 400"),
        ("Adj2", "Supplies on hand 600 (bought 1,500, none previously)", "Dr Supplies Expense 900; Cr Supplies 900"),
        ("Adj3", "Earn 1,000 of unearned", "Dr Unearned Revenue 1,000; Cr Revenue 1,000"),
        ("Adj4", "Depreciation 200", "Dr Depreciation Expense 200; Cr Accumulated Depreciation 200"),
        ("Adj5", "Accrue wages 500", "Dr Wages Expense 500; Cr Wages Payable 500"),
        ("Statements", "Sketch IS: revenues and expenses; then equity update; then BS assets = liabilities + equity", "Verify articulation: NI flows to capital; BS balances."),
    ]
    for title, prompt, sol in capstone_steps:
        add("capstone", title, prompt, sol, difficulty="capstone", kind="lab")

    return problems


def glossary():
    terms = [
        ("Account", "A record that tracks increases and decreases in a specific asset, liability, equity, revenue, or expense."),
        ("Accounting cycle", "The sequence of steps from analyzing transactions to post-closing trial balance each period."),
        ("Accounting equation", "Assets = Liabilities + Equity."),
        ("Accounts payable", "Amounts owed to suppliers for purchases on credit."),
        ("Accounts receivable", "Amounts owed by customers for sales on credit."),
        ("Accrual basis", "Recognize revenues when earned and expenses when incurred."),
        ("Accrued expense", "Expense incurred but not yet paid or recorded."),
        ("Accrued revenue", "Revenue earned but not yet billed or received."),
        ("Accumulated depreciation", "Contra-asset totaling depreciation taken to date."),
        ("Adjusting entry", "Period-end entry to update accruals/deferrals before statements."),
        ("Asset", "Resource controlled expected to provide future benefit."),
        ("Balance sheet", "Statement of financial position at a point in time."),
        ("Book value", "Asset cost minus related accumulated depreciation (carrying amount)."),
        ("Cash basis", "Recognize revenues and expenses when cash is received or paid."),
        ("Chart of accounts", "Organized listing of all account titles and codes."),
        ("Closing entries", "Entries that zero temporary accounts and update equity."),
        ("Compound entry", "Journal entry affecting more than two accounts."),
        ("Contra account", "Account that offsets a related account's balance."),
        ("Credit", "Right side of an account."),
        ("Current asset", "Asset expected to convert to cash within one year/operating cycle."),
        ("Current liability", "Obligation due within one year/operating cycle."),
        ("Current ratio", "Current assets divided by current liabilities."),
        ("Debit", "Left side of an account."),
        ("Deferral", "Cash exchanged before revenue is earned or expense incurred."),
        ("Depreciation", "Allocation of a tangible long-lived asset's cost over useful life."),
        ("Dividend", "Distribution of earnings to shareholders."),
        ("Double-entry", "System where each transaction is recorded with equal debits and credits."),
        ("Drawings", "Owner withdrawals from a sole proprietorship/partnership."),
        ("Equity", "Residual interest = Assets − Liabilities."),
        ("Expense", "Cost consumed to generate revenue; decreases equity."),
        ("Financial statements", "Income statement, equity/RE statement, balance sheet, cash flow statement."),
        ("General journal", "Chronological record of original entries."),
        ("General ledger", "Collection of all individual accounts."),
        ("Going concern", "Assumption the entity will continue operating into the foreseeable future."),
        ("Gross profit", "Net sales minus cost of goods sold."),
        ("Income statement", "Reports revenues and expenses for a period."),
        ("Income Summary", "Temporary clearing account used in closing."),
        ("Intangible asset", "Nonphysical asset such as patents or trademarks."),
        ("Journalizing", "Recording transactions in the journal."),
        ("Ledger", "Book/file of accounts; often the general ledger."),
        ("Liability", "Present obligation expected to cause outflow of resources."),
        ("Liquidity", "Ability to meet short-term obligations."),
        ("Matching principle", "Recognize expenses in the period with related revenues."),
        ("Materiality", "Concept that insignificant items may be treated expediently."),
        ("Net income", "Revenues minus expenses (when positive)."),
        ("Normal balance", "Side (debit or credit) where increases are recorded for an account type."),
        ("Note payable", "Written promissory obligation to pay."),
        ("Posting", "Transferring journal entry amounts into ledger accounts."),
        ("Prepaid expense", "Asset arising from paying before consuming a benefit."),
        ("Profit margin", "Net income divided by sales."),
        ("Quick ratio", "Strict liquidity ratio excluding inventory/prepaids from numerator."),
        ("Retained earnings", "Cumulative earnings less dividends for a corporation."),
        ("Revenue", "Inflows from ordinary activities that increase equity."),
        ("Revenue recognition", "Criteria/timing for recording revenue as earned."),
        ("Solvency", "Ability to meet long-term obligations."),
        ("Source document", "Evidence of a transaction (invoice, receipt, etc.)."),
        ("T-account", "Simplified ledger account shape used for analysis."),
        ("Temporary account", "Revenue, expense, drawings/dividends — closed each period."),
        ("Trial balance", "List of accounts and balances to test debit/credit equality."),
        ("Unearned revenue", "Liability for cash received before earning revenue."),
        ("Working capital", "Current assets minus current liabilities."),
        ("ROA", "Return on assets: NI / average total assets."),
        ("ROE", "Return on equity: NI / average equity."),
        ("Operating cash flow", "Cash generated/used by core operations."),
        ("Investing cash flow", "Cash for long-lived assets and investments."),
        ("Financing cash flow", "Cash from debt and equity activities."),
        ("Articulation", "The links among financial statements (e.g., NI to equity)."),
        ("Permanent account", "Balance sheet account that carries forward."),
        ("Fiscal period", "Accounting time span covered by statements."),
        ("Compound interest intuition", "Interest earns interest; timing changes money's value."),
    ]
    return [{"id": i + 1, "term": t, "definition": d} for i, (t, d) in enumerate(terms)]


def cheat_sheets():
    return [
        {
            "id": 1,
            "slug": "dea-ler",
            "title": "DEA-LER Normal Balances",
            "body": "DEBIT-normal: Dividends/Drawings, Expenses, Assets.\nCREDIT-normal: Liabilities, Equity, Revenue.\nIncrease on the normal side; decrease on the opposite side.\nEvery entry: Σ Debits = Σ Credits.",
        },
        {
            "id": 2,
            "slug": "transaction-patterns",
            "title": "12 Core Journal Patterns",
            "body": "1 Invest cash: Dr Cash Cr Capital\n2 Borrow: Dr Cash Cr Notes Payable\n3 Buy asset cash: Dr Asset Cr Cash\n4 Buy asset on account: Dr Asset Cr AP\n5 Pay AP: Dr AP Cr Cash\n6 Cash revenue: Dr Cash Cr Revenue\n7 Credit revenue: Dr AR Cr Revenue\n8 Collect AR: Dr Cash Cr AR\n9 Pay expense: Dr Expense Cr Cash\n10 Customer advance: Dr Cash Cr Unearned\n11 Earn advance: Dr Unearned Cr Revenue\n12 Accrue expense: Dr Expense Cr Payable",
        },
        {
            "id": 3,
            "slug": "adjusting-4",
            "title": "Four Adjusting Families",
            "body": "Prepaid used: Dr Expense Cr Prepaid\nUnearned earned: Dr Unearned Cr Revenue\nAccrued expense: Dr Expense Cr Payable\nAccrued revenue: Dr Receivable Cr Revenue\n(+ Depreciation: Dr Dep Exp Cr Accum Dep)\nUsually NO Cash in adjustments.",
        },
        {
            "id": 4,
            "slug": "cycle",
            "title": "Accounting Cycle Spine",
            "body": "Analyze → Journalize → Post → Unadj TB → Adjust → Adj TB → Statements → Close → Post-close TB",
        },
        {
            "id": 5,
            "slug": "statements-map",
            "title": "Statement Mapping",
            "body": "Income Statement: Revenues, Expenses → NI\nEquity/RE: Begin + NI − Drawings/Div + Investments → End\nBalance Sheet: Assets = Liabilities + Equity\nCash Flow: Operating / Investing / Financing",
        },
        {
            "id": 6,
            "slug": "ratios",
            "title": "Ratio Pocket Card",
            "body": "Current = CA/CL\nQuick = (Cash+MS+AR)/CL\nDebt-to-Equity = TL/Equity\nProfit margin = NI/Sales\nROA = NI/Avg Assets\nROE = NI/Avg Equity\nGross margin = GP/Sales",
        },
        {
            "id": 7,
            "slug": "analysis-steps",
            "title": "5-Step Transaction Analysis",
            "body": "1 Which accounts?\n2 What types?\n3 Increase or decrease?\n4 Debit or credit per rules?\n5 Do amounts balance?",
        },
        {
            "id": 8,
            "slug": "temp-perm",
            "title": "Temporary vs Permanent",
            "body": "Temporary (close): Revenues, Expenses, Drawings/Dividends, Income Summary\nPermanent (carry): Assets, Liabilities, Capital/Stock/RE",
        },
    ]


def trainer_prompts():
    """Prompts for the debit/credit trainer."""
    rows = []
    tid = 1
    scenarios = [
        ("Cash increases", "debit", "asset"),
        ("Cash decreases", "credit", "asset"),
        ("Accounts Payable increases", "credit", "liability"),
        ("Accounts Payable decreases", "debit", "liability"),
        ("Service Revenue increases", "credit", "revenue"),
        ("Rent Expense increases", "debit", "expense"),
        ("Owner Capital increases", "credit", "equity"),
        ("Owner Drawings increase", "debit", "equity"),
        ("Unearned Revenue increases", "credit", "liability"),
        ("Prepaid Insurance increases", "debit", "asset"),
        ("Equipment increases", "debit", "asset"),
        ("Notes Payable increases", "credit", "liability"),
        ("Accounts Receivable increases", "debit", "asset"),
        ("Accounts Receivable decreases", "credit", "asset"),
        ("Interest Expense increases", "debit", "expense"),
        ("Interest Payable increases", "credit", "liability"),
        ("Accumulated Depreciation increases", "credit", "contra-asset"),
        ("Depreciation Expense increases", "debit", "expense"),
        ("Common Stock increases", "credit", "equity"),
        ("Dividends increase", "debit", "equity"),
        ("Inventory increases", "debit", "asset"),
        ("COGS increases", "debit", "expense"),
        ("Sales Revenue increases", "credit", "revenue"),
        ("Wages Payable decreases (paid)", "debit", "liability"),
        ("Supplies decrease when used", "credit", "asset"),
        ("Supplies Expense increases", "debit", "expense"),
        ("Retained Earnings increase via NI close", "credit", "equity"),
        ("Bonds Payable increase", "credit", "liability"),
        ("Land increases", "debit", "asset"),
        ("Utilities Expense increases", "debit", "expense"),
        ("Short-term investments increase", "debit", "asset"),
        ("Taxes Payable increase", "credit", "liability"),
        ("Sales Returns increase", "debit", "contra-revenue"),
        ("Allowance for Doubtful Accounts increases", "credit", "contra-asset"),
        ("Bad Debt Expense increases", "debit", "expense"),
        ("Mortgage Payable decreases", "debit", "liability"),
        ("Interest Revenue increases", "credit", "revenue"),
        ("Prepaid Rent decreases as used", "credit", "asset"),
        ("Unearned Revenue decreases as earned", "debit", "liability"),
        ("Treasury Stock increases (more shares bought back)", "debit", "contra-equity"),
    ]
    for prompt, answer, account_kind in scenarios:
        rows.append(
            {
                "id": tid,
                "prompt": prompt,
                "answer": answer,
                "accountKind": account_kind,
                "explain": f"For a {account_kind} movement described, the correct side is {answer}.",
            }
        )
        tid += 1
    return rows


def journal_scenarios():
    """Scenarios for the interactive Journal Entry Builder."""
    accounts = [
        "Cash",
        "Accounts Receivable",
        "Supplies",
        "Prepaid Rent",
        "Prepaid Insurance",
        "Inventory",
        "Equipment",
        "Accumulated Depreciation",
        "Accounts Payable",
        "Notes Payable",
        "Wages Payable",
        "Interest Payable",
        "Unearned Revenue",
        "Owner Capital",
        "Owner Drawings",
        "Service Revenue",
        "Sales Revenue",
        "Rent Expense",
        "Wages Expense",
        "Utilities Expense",
        "Insurance Expense",
        "Supplies Expense",
        "Depreciation Expense",
        "Interest Expense",
    ]
    scenarios = [
        ("Owner invests $15,000 cash to start the business.", "Cash", "Owner Capital", 15000,
         "Asset up (debit Cash); owner claim up (credit Capital)."),
        ("Borrow $8,000 from the bank on a note.", "Cash", "Notes Payable", 8000,
         "Asset up; liability up."),
        ("Buy $650 of supplies on account.", "Supplies", "Accounts Payable", 650,
         "Asset up; liability up. Supplies are an asset until used."),
        ("Pay the $650 owed for supplies.", "Accounts Payable", "Cash", 650,
         "Liability down (debit AP); asset down (credit Cash)."),
        ("Perform services and collect $2,400 cash.", "Cash", "Service Revenue", 2400,
         "Asset up; revenue up (credit)."),
        ("Bill a client $1,900 for completed services.", "Accounts Receivable", "Service Revenue", 1900,
         "Earned now — recognize revenue even though cash comes later."),
        ("Client pays the $1,900 previously billed.", "Cash", "Accounts Receivable", 1900,
         "Swap one asset for another. No new revenue — already recognized."),
        ("Pay $1,200 rent for the current month.", "Rent Expense", "Cash", 1200,
         "Benefit consumed now → expense (debit)."),
        ("Pay $3,600 rent covering the next 6 months.", "Prepaid Rent", "Cash", 3600,
         "Future benefit → asset, not expense yet."),
        ("One month of that prepaid rent expires.", "Rent Expense", "Prepaid Rent", 600,
         "Adjusting entry: move used portion from asset to expense."),
        ("Receive a $2,000 advance for work to be done next month.", "Cash", "Unearned Revenue", 2000,
         "Cash before earning → liability, not revenue."),
        ("Complete half of the advance work ($1,000).", "Unearned Revenue", "Service Revenue", 1000,
         "Earn it → reduce the liability, recognize revenue."),
        ("Pay employees $1,750 in wages for work this period.", "Wages Expense", "Cash", 1750,
         "Cost of labor consumed → expense."),
        ("Accrue $900 of wages earned but unpaid at month-end.", "Wages Expense", "Wages Payable", 900,
         "Incurred but unpaid → expense plus payable. No cash yet."),
        ("Buy $5,000 of equipment, paying cash.", "Equipment", "Cash", 5000,
         "Long-lived asset, not an expense — cost allocated later via depreciation."),
        ("Record $250 monthly depreciation on equipment.", "Depreciation Expense", "Accumulated Depreciation", 250,
         "Credit the contra-asset, not Equipment directly."),
        ("Owner withdraws $500 cash for personal use.", "Owner Drawings", "Cash", 500,
         "Drawings (debit-normal) reduce equity; not a business expense."),
        ("Receive the $180 utility bill for this month; will pay later.", "Utilities Expense", "Accounts Payable", 180,
         "Expense incurred now; liability until paid."),
        ("Accrue $75 of interest owed on the bank note.", "Interest Expense", "Interest Payable", 75,
         "Interest accumulates with time — accrue even before payment."),
        ("Pay $960 for a 12-month insurance policy starting today.", "Prepaid Insurance", "Cash", 960,
         "Future coverage → asset. Expense it monthly as it expires."),
        ("One month of the insurance policy expires.", "Insurance Expense", "Prepaid Insurance", 80,
         "Adjusting entry moves 1/12 of the premium to expense."),
        ("A count shows $220 of supplies were used this period.", "Supplies Expense", "Supplies", 220,
         "Used portion becomes expense; remainder stays an asset."),
        ("Sell goods for $3,000 cash (record the sale only).", "Cash", "Sales Revenue", 3000,
         "Merchandiser sale — revenue side. (COGS entry is separate.)"),
        ("Buy $1,400 of inventory on account.", "Inventory", "Accounts Payable", 1400,
         "Goods for resale are an asset until sold."),
    ]
    return {
        "accounts": accounts,
        "scenarios": [
            {
                "id": i + 1,
                "narrative": text,
                "debit": dr,
                "credit": cr,
                "amount": amt,
                "explain": why,
            }
            for i, (text, dr, cr, amt, why) in enumerate(scenarios)
        ],
    }


def work_plan_overview():
    return {
        "id": 1,
        "product": "Ledger Reset",
        "tagline": "A 14-day finance & accounting basics reboot",
        "audience": "Professionals who once learned the basics and need confident recall in 1–2 weeks",
        "weeklyHours": "7–10 hours/week (about 60–90 minutes most days)",
        "outcomes": [
            "Automatic account-type classification",
            "Fluent debit/credit rules via DEA-LER",
            "Confident journal entries for common transactions",
            "Working mental model of the accounting cycle and statements",
            "Basic finance ratio literacy and cash-flow sense",
        ],
        "method": [
            "Daily lesson + flashcards + practice + quiz",
            "Mastery Visas as competence stamps — not participation trophies",
            "Week 1 foundations; Week 2 reporting, finance bridge, capstone",
            "Spaced drills on weak cards after each quiz",
        ],
        "rulesOfEngagement": [
            "Speak answers out loud before flipping cards",
            "Never skip classification — type first, then debit/credit",
            "Missed quiz items become same-day flashcards",
            "Pass score is 80% (85% on Mixed Mastery)",
            "If a day is missed, do flashcards only — resume lessons next day without stacking guilt",
        ],
    }


def decks():
    return [
        {"id": "equation", "title": "Accounting Equation", "day": 1},
        {"id": "account-types", "title": "Account Types", "day": 2},
        {"id": "debit-credit", "title": "Debits & Credits", "day": 3},
        {"id": "journal", "title": "Journal Patterns", "day": 4},
        {"id": "cycle", "title": "Accounting Cycle", "day": 5},
        {"id": "accrual", "title": "Accrual & Timing", "day": 6},
        {"id": "mixed-week1", "title": "Week 1 Mixed Review", "day": 7},
        {"id": "statements", "title": "Financial Statements", "day": 8},
        {"id": "adjusting", "title": "Adjusting Entries", "day": 9},
        {"id": "closing", "title": "Closing Entries", "day": 10},
        {"id": "finance-ratios", "title": "Finance Ratios", "day": 11},
        {"id": "cash-flow", "title": "Cash Flow Classes", "day": 12},
        {"id": "weak-spots", "title": "Weak Spot Drill", "day": 13},
    ]


def mnemonics():
    return [
        {
            "id": 1,
            "title": "DEA-LER",
            "body": "Debit-normal: Dividends, Expenses, Assets. Credit-normal: Liabilities, Equity, Revenue.",
        },
        {
            "id": 2,
            "title": "ALORE",
            "body": "Assets, Liabilities, Owner's Equity, Revenue, Expenses — the five families to classify first.",
        },
        {
            "id": 3,
            "title": "Left-Right Scale",
            "body": "Debit left, credit right. The accounting equation is a scale — every entry keeps it level.",
        },
        {
            "id": 4,
            "title": "Cash is shy at adjustments",
            "body": "If you are adjusting, Cash usually does not appear — you are allocating earning/consuming.",
        },
        {
            "id": 5,
            "title": "Temps take a bow",
            "body": "Temporary accounts take a curtain call at closing — they leave the stage at zero.",
        },
        {
            "id": 6,
            "title": "OIF for cash",
            "body": "Operating, Investing, Financing — three doors for every cash movement.",
        },
    ]


def main():
    quiz_meta, questions = quizzes()
    jb = journal_scenarios()
    db = {
        "meta": [
            {
                "id": 1,
                "name": "Ledger Reset",
                "version": "1.0.0",
                "description": "Comprehensive finance & accounting basics refresh: 14-day plan, lessons, flashcards, quizzes, practice sets, mastery visas, and trainers.",
                "countsNote": "Generated dataset for learning API / local app",
            }
        ],
        "workPlan": [work_plan_overview()],
        "studyPlan": study_plan(),
        "modules": modules(),
        "accountTypes": account_types(),
        "decks": decks(),
        "flashcards": flashcards(),
        "quizzes": quiz_meta,
        "questions": questions,
        "practiceProblems": practice_problems(),
        "glossary": glossary(),
        "cheatSheets": cheat_sheets(),
        "masteryVisas": mastery_visas(),
        "trainerPrompts": trainer_prompts(),
        "mnemonics": mnemonics(),
        "journalBuilder": [
            {"id": 1, "accounts": jb["accounts"], "scenarios": jb["scenarios"]}
        ],
    }

    out = ROOT / "db.json"
    out.write_text(json.dumps(db, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    counts = {k: (len(v) if isinstance(v, list) else 1) for k, v in db.items()}
    print("Wrote", out)
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
