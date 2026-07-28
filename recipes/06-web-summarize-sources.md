# Summarize Links Fairly

**Slug:** `web-summarize-sources`  
**Category:** web  
**Level:** starter

## When to use
You have articles/URLs and need a fair digest.

## Variables
`{{TOOLS}}`, `{{CONTEXT}}`, `{{GOAL}}`, `{{UNKNOWN_POLICY}}`

## Prompt
```
MODE: Ask
GOAL: Summarize the following sources without merging them into one mushy opinion
TOOLS: {{TOOLS}}
CONTEXT: {{CONTEXT}}
For each source: 3 bullet summary + possible bias/limitations
Then: overlap vs disagreements
Then: what it means for {{GOAL}}
UNKNOWN_POLICY: {{UNKNOWN_POLICY}}
```

## Done when
You see agreements and disagreements clearly.

## Safety
Don't skip reading the key primary source for high-stakes topics.
