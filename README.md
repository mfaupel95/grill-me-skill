# grill-me

A Claude Code / Cowork skill that interviews you relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree.

Use it when you want to stress-test a plan, poke holes in a design, or just say "grill me".

## Install

Drop the `SKILL.md` (or the whole folder) into your skills directory:

```
~/.claude/skills/grill-me/SKILL.md
```

Then trigger it by saying "grill me" or asking Claude to stress-test a plan.

## Question channels

Use the AskUserQuestion popup when the host provides it and a user can reply.
Otherwise, interactive chat uses one plain-text question at a time with numbered
options and a custom-answer option. Without a user reply channel, the interview
stops and reports unresolved decisions and the next question for a human; it does
not manufacture answers or claim that the design is resolved.

## Local checks

Run `python -B -m unittest discover -s tests -v` from the repository root.
These are static prompt-contract checks, not model-behavior evaluations. They
only read this README and SKILL.md; no runtime packages or network are required.
