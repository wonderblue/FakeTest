# Cursor Daily Driver

A **21-day, spoon-fed mastery path** so a non-technical person can make **Cursor their daily driver** for personal work, web activity, and automation — without becoming a programmer.

Built as rich learning data in `db.json` (compatible with [my-json-server](https://my-json-server.typicode.com/)) plus a local interactive study app.

## What’s inside

| Artifact | Count (approx.) | Purpose |
|---|---:|---|
| 21-day study / work plan | 21 days | Daily goals, tasks, checkpoints |
| Deep-dive modules | 21 | Install → modes → Recipes → MCP/Cloud → Personal OS |
| Prompt Variables | 25 | Fill-in-the-blank slots like `{{GOAL}}` |
| Copy-paste Recipes | 24 | Email, research, files, trips, cloud briefs… |
| Learning resources | 25 | Official docs, videos, listen-mode links |
| Flashcards | 210+ | Decks by week/theme |
| Quizzes | 21 (210 questions) | Pass to stamp Mastery Visas |
| Practice problems | 45 | Right-sized drills |
| Mastery Visas | 19 | Competence passport stamps |
| Mode Gym | 30+ prompts | Ask / Plan / Agent / Debug reflexes |
| Glossary + cheat sheets | 50+ / 8 | Quick reference |

## Try the study app

Serve the repo root over HTTP (browsers block local `fetch` of `db.json` from `file://`):

```bash
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080).

Progress (quiz scores, visas, flashcard marks, completed days) saves in your browser via `localStorage`.

## Read the full plan

Start here if you want the narrative playbook (not only the app):

1. [docs/00-start-here-cursor.md](docs/00-start-here-cursor.md) — who this is for & how to use it  
2. [docs/01-comprehensive-plan.md](docs/01-comprehensive-plan.md) — the full 21-day plan + OS blueprint  
3. [docs/02-variables-and-recipes.md](docs/02-variables-and-recipes.md) — Variables + Recipe catalog  
4. [docs/03-resources-videos-audio.md](docs/03-resources-videos-audio.md) — docs / video / audio exploration pack  
5. [recipes/](recipes/) — printable Markdown Recipe files  

## Use the data API

Fork and point my-json-server at this repo, or run any JSON server against `db.json`.

Useful endpoints:

- `/workPlan` `/studyPlan` `/modules`
- `/variables` `/recipes` `/resources`
- `/flashcards` `/quizzes` `/questions`
- `/practiceProblems` `/masteryVisas`
- `/cheatSheets` `/glossary` `/trainerPrompts` `/dailyDriverOS`

## Regenerate data

```bash
python3 scripts/build_db.py
```

## Suggested path

1. Follow **Plan** day by day (Week 1 foundations, Week 2 Recipes, Week 3 systems + capstone).  
2. Read the day’s **Lesson**, drill **Flashcards**, copy a **Recipe** into Cursor, then take the **Quiz**.  
3. Stamp **Visas** as you pass — competence gates, not participation badges.  
4. Keep **Variables** + **Reference** open while briefing Cursor.  
5. Graduate with `HOW_I_USE_CURSOR.md` in your Personal Ops folder.

## License

See `LICENSE`.
