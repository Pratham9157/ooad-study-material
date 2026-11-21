**A communication diagram (called a *collaboration diagram* in UML 1) shows the same object interaction as a sequence diagram, but laid out as a network: objects connected by links, with numbered messages along the links.**

## The Problem: Sequence Diagrams Grow Sideways

Sequence diagrams are great for time order, but every new object adds a new column. With 8 objects the diagram becomes very wide, and on a whiteboard you constantly run out of space. Sometimes you also care more about **who is linked to whom** than about exact timing.

:::analogy
A sequence diagram is a **timeline** of a phone-call chain. A communication diagram is the **phone network map** — people drawn wherever there's space, lines showing who can call whom, and each call labelled "1st", "1.1", "1.2"… to show the order.
:::

## The Notation

- **Objects** as boxes (`:IssueBookHandler`, `m : Member`) — no lifelines.
- **Links** — plain lines between objects that communicate (a link is an instance of an association).
- **Messages** — small arrows next to a link, with a **sequence number**: `1: enterCopy(copyId)`.
- **Nested (decimal) numbering** — calls made *while handling* message 1 are `1.1`, `1.2`; calls inside `1.2` are `1.2.1` …
- **Condition** — `[available] 1.3: addLoan(c)`.
- **Iteration** — `1*: [i = 1..n] next()` (the `*` means repeated).
- **Creation** — `create(…)` message, optionally «create» on the new object.

## The enterCopy Interaction as a Communication Diagram

```text
                       enterCopy(copyId)
         :Librarian/UI ─────────────────► ┌──────────────────────┐
                                   1 ──►  │  :IssueBookHandler   │
                                          └──────────────────────┘
                  1.1: c := findCopy(copyId) │        │    │ 1.3: [available] addLoan(c)
                               ▼             │        │    ▼
                      ┌──────────────┐       │        │  ┌──────────────┐
                      │   :Catalog   │───────┘        │  │  m : Member  │
                      └──────────────┘                │  └──────────────┘
                                                      │         │ 1.3.1: create(c, due)
                    1.2: available := isAvailable()   │         ▼
                                  ▼                   │  ┌──────────────┐
                           ┌──────────────┐           │  │    :Loan     │
                           │ c : BookCopy │───────────┘  └──────────────┘
                           └──────────────┘ ◄───────────────────┘
                                           1.3.2: markIssued()
```

Order of execution: **1 → 1.1 → 1.2 → 1.3 → 1.3.1 → 1.3.2** — exactly the same as the sequence diagram in Lesson 11.2.

## Sequence vs Communication Diagrams

| Sequence diagram | Communication diagram |
|---|---|
| Columns (lifelines); time flows down | Network/graph layout; objects placed anywhere |
| **Time order** is obvious | Order only via sequence numbers (harder to follow) |
| Rich notation: frames (alt/loop), activation bars | Simpler notation; no frames |
| New objects add width | Space-efficient; easy to add objects |
| Best for complex logic and documentation | Best for showing **links/structure** and quick sketches |

Both are **interaction diagrams** and are **semantically equivalent** — tools can convert one into the other.

## When to Use Communication Diagrams

- When you want to emphasise **which objects are linked** (the structure supporting the interaction) — e.g. to check every message travels along an existing link.
- For **quick whiteboard sketching** — they use space well.
- When the interaction is **simple** and exact time order isn't the main point.

Prefer **sequence diagrams** when ordering, loops and conditions matter, or for readers new to UML.

:::key
- Communication (collaboration) diagram = objects + links + numbered messages.
- Decimal numbering (1, 1.1, 1.2, 1.2.1) shows nesting; `*` iteration; `[ ]` condition.
- Equivalent to sequence diagrams; better for structure & sketching, worse for time order.
:::

:::mistakes
- Flat numbering (1, 2, 3, 4) — loses which call happens inside which.
- Sending a message between objects with no link drawn.
- Calling it a structural diagram — it's an interaction (behaviour) diagram.
:::

:::exam
- *"Explain the collaboration/communication diagram with an example."*
- *"Differentiate sequence and communication diagrams."* → the table.
- *"When should communication diagrams be used?"*
:::

:::def
A **communication diagram** (UML 1: **collaboration diagram**) is an interaction diagram that shows objects, the links between them and the messages sent along those links, with sequence numbers (often in nested decimal form) indicating the order of messages. It emphasises the structural organisation of the objects that interact.
:::

## Quick Check

:::q Q1 · Message `2.1.3` — what does it mean?
:::ans
The third message sent while handling message `2.1` (which itself was sent while handling message 2).
:::
:::

:::q Q2 · Which diagram would you choose to explain a 12-step interaction with two loops and a condition to a new team member?
:::ans
A **sequence diagram** — clearer time order and frames for loops/conditions.
:::
:::
