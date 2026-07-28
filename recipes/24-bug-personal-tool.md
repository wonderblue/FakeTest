# Debug a Personal Tool

**Slug:** `bug-personal-tool`  
**Category:** advanced  
**Level:** advanced

## When to use
A tracker/script/page you use personally is broken.

## Variables
`{{GOAL}}`, `{{CONTEXT}}`, `{{FILES}}`, `{{INPUT_DUMP}}`, `{{SUCCESS_CRITERIA}}`

## Prompt
```
MODE: Debug (or Agent if simple)
GOAL: {{GOAL}}
CONTEXT: {{CONTEXT}}
FILES: {{FILES}}
Repro steps: {{INPUT_DUMP}}
CONSTRAINTS: Prefer evidence over guessing; don't widen scope
SUCCESS_CRITERIA: {{SUCCESS_CRITERIA}}
```

## Done when
Issue fixed or you have a clear blocker.

## Safety
Back up files before big changes.
