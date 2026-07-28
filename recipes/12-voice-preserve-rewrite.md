# Rewrite Keeping My Voice

**Slug:** `voice-preserve-rewrite`  
**Category:** writing  
**Level:** starter

## When to use
You have a draft that sounds like a robot.

## Variables
`{{EXAMPLES}}`, `{{INPUT_DUMP}}`, `{{TONE}}`, `{{OUTPUT_PATH}}`

## Prompt
```
MODE: Agent
GOAL: Rewrite for clarity while sounding like me
EXAMPLES: {{EXAMPLES}}
INPUT_DUMP:
{{INPUT_DUMP}}
TONE: {{TONE}}
CONSTRAINTS: Keep my meaning; flag any factual changes
OUTPUT_PATH: {{OUTPUT_PATH}}
```

## Done when
It sounds like Carson, not a brochure.

## Safety
Check that meaning didn't shift on commitments.
