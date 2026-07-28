# Turn How I Do It Into a Mini SOP

**Slug:** `sop-from-chaos`  
**Category:** automation  
**Level:** starter

## When to use
When only you know how a household/admin process works.

## Variables
`{{INPUT_DUMP}}`, `{{OUTPUT_PATH}}`

## Prompt
```
MODE: Ask then Agent
GOAL: Document my process so future-me (or Agent) can repeat it
INPUT_DUMP:
{{INPUT_DUMP}}
FORMAT: Purpose / Trigger / Steps / Tools / Failure modes / Done-when
OUTPUT_PATH: Reference/sops/{{OUTPUT_PATH}}
```

## Done when
Someone else could follow the SOP cold.

## Safety
Omit secrets; point to where secrets live.
