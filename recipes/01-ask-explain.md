# Explain This Like I'm Not Technical

**Slug:** `ask-explain`  
**Category:** learning  
**Level:** starter

## When to use
Anything confusing: a letter, PDF, settings screen, error message.

## Variables
`{{GOAL}}`, `{{CONTEXT}}`, `{{FILES}}`, `{{UNKNOWN_POLICY}}`, `{{SUCCESS_CRITERIA}}`

## Prompt
```
MODE: Ask
GOAL: {{GOAL}}
CONTEXT: {{CONTEXT}}
FILES: {{FILES}}
AUDIENCE: Carson — non-technical
CONSTRAINTS:
- No jargon without a plain-English translation in parentheses
- Do not invent facts
- UNKNOWN_POLICY: {{UNKNOWN_POLICY}}
FORMAT: Short summary → What it means for me → What I should do next (max 3 steps)
SUCCESS_CRITERIA: {{SUCCESS_CRITERIA}}
```

## Done when
You understand the thing well enough to act or decide to ignore it.

## Safety
Remove account numbers from screenshots when possible.
