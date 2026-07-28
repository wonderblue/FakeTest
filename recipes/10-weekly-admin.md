# Weekly Admin Sweep

**Slug:** `weekly-admin`  
**Category:** life-ops  
**Level:** starter

## When to use
Sunday/Monday life admin.

## Variables
`{{FILES}}`, `{{DATES}}`, `{{OUTPUT_PATH}}`, `{{SUCCESS_CRITERIA}}`

## Prompt
```
MODE: Agent
GOAL: Build this week's admin plan from my dumps and project folders
FILES: {{FILES}}
DATES: {{DATES}}
FORMAT: Top 7 tasks with time estimates + deferred list + waiting-on list
CONSTRAINTS: Be ruthless; max 7 active tasks
OUTPUT_PATH: {{OUTPUT_PATH}}
SUCCESS_CRITERIA: {{SUCCESS_CRITERIA}}
```

## Done when
You know the only seven things that matter this week.

## Safety
Don't let AI guilt you into a 40-item list.
