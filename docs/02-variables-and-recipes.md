# Variables & Recipes

Spoon-feeding kit: fill blanks → paste into Cursor → review → save winners to `Wins/`.

---

## Variables dictionary

| Token | Meaning | Example |
|---|---|---|
| `{{GOAL}}` | What success looks like | Draft a polite invoice follow-up |
| `{{CONTEXT}}` | Background | Met Tuesday; payment promised Friday |
| `{{AUDIENCE}}` | Who reads it | Busy vendor AP clerk |
| `{{TONE}}` | Voice | Warm, direct, no guilt, no emojis |
| `{{LENGTH}}` | Size | Under 120 words |
| `{{FORMAT}}` | Shape | Markdown checklist with owners |
| `{{FILES}}` | `@` paths | `@Inbox/notes.md` |
| `{{CONSTRAINTS}}` | Hard do-nots | No deletes; no invented dates |
| `{{EXAMPLES}}` | Samples to imitate | Match `@Reference/voice-samples.md` |
| `{{DEADLINE}}` | Time pressure | Need draft in 10 minutes |
| `{{SUCCESS_CRITERIA}}` | Done-when | I can paste into Gmail after one edit |
| `{{PRIORITY}}` | Tradeoff preference | Clarity over cleverness |
| `{{TOOLS}}` | Allowed integrations | Web search OK; don’t post to Slack |
| `{{BUDGET}}` | Money ceiling | Under $1,800 excl. booked flights |
| `{{PEOPLE}}` | Who’s involved | Carson + Sam + two kids |
| `{{LOCATION}}` | Place limits | Walkable downtown |
| `{{DATES}}` | Time window | Oct 10 evening → Oct 14 noon |
| `{{RISK_TOLERANCE}}` | Carefulness | Sandbox moves only |
| `{{UNKNOWN_POLICY}}` | When unsure | List unknowns; never fabricate sources |
| `{{REVIEW_GATE}}` | Needs Carson’s eyes | Payment promises / legal claims |
| `{{INPUT_DUMP}}` | Messy paste zone | Raw bullets |
| `{{OUTPUT_PATH}}` | Where to save | `Projects/.../draft.md` |
| `{{LANGUAGE}}` | Output language | US English |
| `{{DOMAIN}}` | Topic area | Travel / admin / research |
| `{{MODEL_HINT}}` | Optional care note | Prefer careful reasoning for money topics |

**Use-often core:** `GOAL`, `CONTEXT`, `CONSTRAINTS`, `SUCCESS_CRITERIA`, `FORMAT`.

---

## How to run any Recipe

1. Pick the **mode** named in the Recipe (Ask / Plan / Agent / Debug).  
2. Copy the prompt from the app **Recipes** tab or `recipes/*.md`.  
3. Replace every `{{...}}` with real text (delete unused optional lines).  
4. Attach files with `@` where `{{FILES}}` / `{{EXAMPLES}}` need them.  
5. Let Cursor work → **read the summary/diff** → Accept or Reject.  
6. Save the filled prompt + output into `Wins/` if it worked.

---

## Recipe catalog (24)

Categories match the study app filters.

### Learning & planning

1. **Explain This Like I'm Not Technical** (`ask-explain`) — confusing letters, PDFs, errors  
2. **Plan a Personal System** (`plan-personal-system`) — fuzzy multi-step systems  
3. **Teach-Back Check** (`teach-back`) — quiz yourself after learning  
4. **Draft User Rules From Complaints** (`rule-drafter`) — turn recurring corrections into short rules  

### Writing & docs

5. **Draft an Email in My Voice** (`draft-email`)  
6. **Meeting Notes → Action List** (`meeting-to-actions`)  
7. **Decision One-Pager** (`decision-one-pager`)  
8. **Rewrite Keeping My Voice** (`voice-preserve-rewrite`)  
9. **Repurpose One Note Many Ways** (`content-repurpose`)  
10. **Build a Reusable Template** (`template-builder`)  

### Web & research

11. **Decision Research Brief** (`research-brief`)  
12. **Summarize Links Fairly** (`web-summarize-sources`)  
13. **Compare Vendors / Services** (`compare-vendors`)  

### Files & automation

14. **Sandbox File Cleanup** (`sandbox-file-sort`)  
15. **Messy List → CSV Tracker** (`notes-to-csv`)  
16. **Inbox Folder Triage** (`inbox-triage`)  
17. **Turn How I Do It Into a Mini SOP** (`sop-from-chaos`)  

### Life ops

18. **Trip Planner Checklist** (`trip-planner`)  
19. **Weekly Admin Sweep** (`weekly-admin`)  
20. **Family Logistics Board** (`family-logistics`)  
21. **Weekly Review Ritual** (`weekly-review`)  

### Cloud / browser / advanced

22. **Cloud Agent Async Brief** (`cloud-async-job`)  
23. **Screenshot Help** (`screenshot-help`)  
24. **Debug a Personal Tool** (`bug-personal-tool`)  

Full prompt text lives in `db.json` → `recipes` and in printable files under `/recipes`.

---

## Starter User Rules (paste into Customize → Rules)

```text
- I am non-technical: explain jargon in plain English (short parentheses OK).
- Ask before deleting files or moving originals; prefer sandbox copies.
- Do not invent facts, dates, prices, or citations; label unknowns.
- Default tone: warm, direct, no hype, no emoji unless I ask.
- Prefer Markdown files in Templates/ and Projects/.
- When producing deliverables, restate DONE-WHEN and list human gates.
- Keep answers structured: short summary first, then steps.
```

Official rules docs: https://cursor.com/docs/rules  
Rules vs Skills: https://cursor.com/learn/customizing-agents
