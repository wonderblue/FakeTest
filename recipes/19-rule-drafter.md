# Draft User Rules From Complaints

**Slug:** `rule-drafter`  
**Category:** rules  
**Level:** starter

## When to use
You keep correcting Cursor the same way.

## Variables
`{{INPUT_DUMP}}`

## Prompt
```
MODE: Ask then help me save rules
GOAL: Turn my recurring corrections into short User Rules
INPUT_DUMP:
{{INPUT_DUMP}}
CONSTRAINTS: Max 10 bullet rules; crisp; no essays
FORMAT: Paste-ready User Rules markdown
```

## Done when
Rules are short and installed.

## Safety
Don't encode rare one-offs as global rules.
