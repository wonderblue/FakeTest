# Trip Planner Checklist

**Slug:** `trip-planner`  
**Category:** life-ops  
**Level:** starter

## When to use
Weekends away, family trips, work+personal travel.

## Variables
`{{GOAL}}`, `{{PEOPLE}}`, `{{LOCATION}}`, `{{DATES}}`, `{{BUDGET}}`, `{{PRIORITY}}`, `{{CONSTRAINTS}}`, `{{REVIEW_GATE}}`, `{{OUTPUT_PATH}}`

## Prompt
```
MODE: Plan then Agent
GOAL: {{GOAL}}
PEOPLE: {{PEOPLE}}
LOCATION: {{LOCATION}}
DATES: {{DATES}}
BUDGET: {{BUDGET}}
PRIORITY: {{PRIORITY}}
CONSTRAINTS: {{CONSTRAINTS}}
FORMAT: Day-by-day outline + packing list + booking checklist with HUMAN GATES marked
REVIEW_GATE: {{REVIEW_GATE}}
OUTPUT_PATH: {{OUTPUT_PATH}}
```

## Done when
You have a checklist you can execute — bookings still on you.

## Safety
AI must not auto-book or invent visa rules.
