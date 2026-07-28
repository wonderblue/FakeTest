# Ledger Reset

A **14-day finance & accounting basics reboot** for anyone who has lost touch with the fundamentals and wants confident recall again.

Built as rich learning data in `db.json` (compatible with [my-json-server](https://my-json-server.typicode.com/)) plus a local interactive study app.

## What’s inside

| Artifact | Count (approx.) | Purpose |
|---|---:|---|
| 14-day study / work plan | 14 days | Daily goals, tasks, checkpoints |
| Deep-dive modules | 12 | Equation → statements → finance bridge |
| Flashcards | 160+ | Decks for types, Dr/Cr, journals, ratios… |
| Quizzes | 14 (140+ questions) | Pass to stamp Mastery Visas |
| Practice problems | 180 | Classify, journalize, adjust, capstone |
| Mastery Visas | 10 | Competence “passport” stamps |
| Debit/Credit trainer | 40 prompts | Speed drills for left/right rules |
| Glossary + cheat sheets | 70 + 8 | Quick reference |

Focus areas: **account types**, **debits & credits (DEA-LER)**, journal patterns, accrual timing, the accounting cycle, statements, adjusting/closing, and basic finance ratios / cash-flow sense.

## Try the study app

Serve the repo root over HTTP (browsers block local `fetch` of `db.json` from `file://`):

```bash
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080).

Progress (quiz scores, visas, flashcard marks, completed days) saves in your browser via `localStorage`.

## Use the data API

Fork and point my-json-server at this repo, or run any JSON server against `db.json`.

Example endpoints:

- `/studyPlan`
- `/modules`
- `/flashcards`
- `/quizzes` + `/questions`
- `/practiceProblems`
- `/masteryVisas`
- `/accountTypes`
- `/cheatSheets`
- `/glossary`
- `/trainerPrompts`

Demo-style host pattern:

`https://my-json-server.typicode.com/<user>/<repo>/studyPlan`

## Regenerate data

```bash
python3 scripts/build_db.py
```

## Suggested path

1. Follow **Plan** day by day (Week 1 foundations, Week 2 reporting + finance + capstone).
2. Read the day’s **Lesson**, drill **Flashcards**, run the **Dr/Cr Trainer**, then take the **Quiz**.
3. Stamp **Visas** as you pass — they are competence gates, not participation badges.
4. Keep **Reference** cheat sheets open while writing journal entries on paper.

## License

See `LICENSE`.
