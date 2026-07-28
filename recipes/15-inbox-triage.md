# Inbox Folder Triage

**Slug:** `inbox-triage`  
**Category:** automation  
**Level:** starter

## When to use
When Inbox/ is a junk drawer.

## Variables
`{{RISK_TOLERANCE}}`

## Prompt
```
MODE: Plan then Agent
GOAL: Triage @Inbox into Projects/Reference/Archive suggestions
CONSTRAINTS: Propose moves in a plan file first; wait for approval; no deletes
FORMAT: Table of file → suggested destination → why
RISK_TOLERANCE: {{RISK_TOLERANCE}}
```

## Done when
Inbox has a clear plan; you approved moves.

## Safety
Approve before any bulk moves.
