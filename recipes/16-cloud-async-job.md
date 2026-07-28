# Cloud Agent Async Brief

**Slug:** `cloud-async-job`  
**Category:** cloud  
**Level:** intermediate

## When to use
Jobs to kick off from phone or while away.

## Variables
`{{FILES}}`, `{{GOAL}}`, `{{CONTEXT}}`, `{{CONSTRAINTS}}`, `{{OUTPUT_PATH}}`, `{{SUCCESS_CRITERIA}}`

## Prompt
```
Run as Cloud Agent on repo {{FILES}}
GOAL: {{GOAL}}
CONTEXT: {{CONTEXT}}
CONSTRAINTS: {{CONSTRAINTS}}
OUTPUT_PATH: {{OUTPUT_PATH}}
SUCCESS_CRITERIA: {{SUCCESS_CRITERIA}}
When done: summarize changes + how to review
Do not require interactive questions; if blocked, write BLOCKERS.md
```

## Done when
You can review a branch/PR without re-explaining context.

## Safety
Connect source control; no secrets in the brief.
