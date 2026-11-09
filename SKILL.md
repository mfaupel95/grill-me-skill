---
name: grill-me
description: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
---

Interview the user relentlessly about every aspect of their plan until you reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.

## How to ask questions

When AskUserQuestion is available and a user can reply, use its multiple-choice popup so the user can quickly select an answer or type a custom one.

If AskUserQuestion is unavailable but the user can reply in chat, ask one plain-text question with numbered options and allow a custom answer. Do not pretend to call a missing tool or bypass a tool restriction.

If no user reply channel is available (for example, an unattended run), stop the interview and report the unresolved decisions, why they matter, and the next question for a human. Do not invent answers or claim shared understanding without the user's input.

Ask **one question at a time**. Wait for the user's answer before moving to the next question. This keeps the conversation focused and prevents overwhelm.

For each question, provide 2–4 concrete multiple-choice options representing the most likely answers or directions. Think about what the user would realistically choose — generic options like "Yes" / "No" aren't helpful unless the question is genuinely binary. Offer the "Other" field in the popup or a custom answer in chat.

## Flow

1. After receiving an answer, briefly acknowledge the decision (1–2 sentences max), then ask the next unresolved question using the question method above. If no unresolved decisions remain, summarize instead.
2. If a question can be answered by exploring the codebase or files, explore them yourself instead of asking the user.
3. Continue until all branches of the design tree are resolved, or pause with an explicit list of unresolved decisions if user input is unavailable.
4. When finished, provide a concise summary of all decisions made.
