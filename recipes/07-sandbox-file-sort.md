# Sandbox File Cleanup

**Slug:** `sandbox-file-sort`  
**Category:** automation  
**Level:** starter

## When to use
Messy Downloads / Desktop chaos.

## Variables
`{{GOAL}}`, `{{FILES}}`, `{{RISK_TOLERANCE}}`, `{{OUTPUT_PATH}}`, `{{SUCCESS_CRITERIA}}`

## Prompt
```
MODE: Plan then Agent
GOAL: {{GOAL}}
FILES: {{FILES}}
RISK_TOLERANCE: {{RISK_TOLERANCE}}
CONSTRAINTS:
- Work only inside a sandbox copy folder I specify
- Propose a plan markdown first and wait
- No permanent deletes
NAMING: YYYY-MM-DD_topic_description.ext
OUTPUT_PATH: {{OUTPUT_PATH}}
SUCCESS_CRITERIA: {{SUCCESS_CRITERIA}}
```

## Done when
Sandbox looks right; originals untouched until you manually finish.

## Safety
Never allow unsupervised delete on originals.
