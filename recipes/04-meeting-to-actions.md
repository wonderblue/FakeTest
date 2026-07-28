# Meeting Notes → Action List

**Slug:** `meeting-to-actions`  
**Category:** writing  
**Level:** starter

## When to use
After calls, school meetings, contractor visits.

## Variables
`{{INPUT_DUMP}}`, `{{OUTPUT_PATH}}`, `{{SUCCESS_CRITERIA}}`

## Prompt
```
MODE: Agent
GOAL: Turn raw notes into owners, actions, and open questions
INPUT_DUMP:
{{INPUT_DUMP}}
FORMAT: Markdown with sections Decisions / Actions (owner + due date) / Open questions
CONSTRAINTS:
- Do not invent owners or dates — mark as TBD
- Keep my wording for commitments
OUTPUT_PATH: {{OUTPUT_PATH}}
SUCCESS_CRITERIA: {{SUCCESS_CRITERIA}}
```

## Done when
Every action has an owner or TBD, and nothing important from notes is missing.

## Safety
Confirm money/legal commitments yourself.
