# Messy List → CSV Tracker

**Slug:** `notes-to-csv`  
**Category:** automation  
**Level:** starter

## When to use
Trips, inventories, gift lists, home tasks.

## Variables
`{{GOAL}}`, `{{INPUT_DUMP}}`, `{{CONSTRAINTS}}`, `{{OUTPUT_PATH}}`

## Prompt
```
MODE: Agent
GOAL: {{GOAL}}
INPUT_DUMP:
{{INPUT_DUMP}}
FORMAT: CSV with columns you propose (ask me to confirm columns first)
CONSTRAINTS: {{CONSTRAINTS}}
OUTPUT_PATH: {{OUTPUT_PATH}}
SUCCESS_CRITERIA: Opens cleanly in Sheets/Excel
```

## Done when
CSV imports cleanly with headers you understand.

## Safety
No sensitive IDs in trackers you might share.
