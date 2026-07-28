# Build a Reusable Template

**Slug:** `template-builder`  
**Category:** automation  
**Level:** starter

## When to use
Meeting notes, weekly review, packing lists.

## Variables
`{{GOAL}}`, `{{FORMAT}}`, `{{OUTPUT_PATH}}`

## Prompt
```
MODE: Agent
GOAL: {{GOAL}}
FORMAT: {{FORMAT}}
CONSTRAINTS: Include Variable placeholders like {{GOAL}} where useful
OUTPUT_PATH: Templates/{{OUTPUT_PATH}}
SUCCESS_CRITERIA: I can duplicate this weekly without thinking
```

## Done when
Template is saved and you used it once successfully.

## Safety
Keep secrets out of templates.
