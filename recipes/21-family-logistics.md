# Family Logistics Board

**Slug:** `family-logistics`  
**Category:** life-ops  
**Level:** starter

## When to use
Multiple people, multiple calendars, chaos.

## Variables
`{{GOAL}}`, `{{PEOPLE}}`, `{{DATES}}`, `{{INPUT_DUMP}}`, `{{OUTPUT_PATH}}`

## Prompt
```
MODE: Agent
GOAL: {{GOAL}}
PEOPLE: {{PEOPLE}}
DATES: {{DATES}}
INPUT_DUMP:
{{INPUT_DUMP}}
FORMAT: Shared checklist by person + critical path + conflicts
CONSTRAINTS: Mark HUMAN GATES; don't invent commitments
OUTPUT_PATH: {{OUTPUT_PATH}}
```

## Done when
Everyone knows their next action.

## Safety
Confirm with humans before treating TBD as real.
