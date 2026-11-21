**An activity diagram shows the flow of a process — the steps (actions), decisions, and things that happen in parallel — and, optionally, who does each step.** Think of it as a supercharged flowchart.

## The Problem: Processes Involve Many People and Parallel Work

How does the library handle a book return? The member brings it, the librarian scans it, the system checks for a fine, the member may pay, and then — **at the same time** — the receipt is handed over and the copy is marked available. A use case describes this in text; a flowchart can't show the parallel steps or who does what. An **activity diagram** can.

:::analogy
Making breakfast: *boil water* and *toast bread* happen **in parallel** (fork); you can only *serve* once **both** are done (join). If there's no milk, you take a different path (decision). With swimlanes, you could even show that **you** boil water while **your sibling** toasts the bread.
:::

## The Notation

| Element | Symbol | Meaning |
|---|---|---|
| Initial node | filled circle ● | where the flow starts |
| Action | rounded rectangle | one step of work |
| Control flow | arrow | what comes next |
| Decision | diamond, outgoing flows with **guards** `[overdue]` / `[else]` | choose one path |
| Merge | diamond with several inputs, one output | paths come back together |
| **Fork** | thick bar, one in, many out | start **parallel** flows |
| **Join** | thick bar, many in, one out | wait until **all** parallel flows finish |
| Activity final | bull's-eye ◉ | the **whole** activity ends |
| Flow final | circle with an X ⊗ | only **that** flow ends |
| Partition (swimlane) | vertical/horizontal lanes | **who** performs each action |
| Object node | rectangle, e.g. `[Receipt]` | data/object passed between actions |
| Signals | send-signal / accept-event shapes | asynchronous events |

## Example: The Return Book Process

<<SVG:activity>>

Walk through it: the **Member** brings the copy → the **Librarian** scans it → the **System** finds the open loan → **decision**: if `[overdue]`, calculate the fine and the member pays; `[else]` skip → **merge** → **fork**: *hand over receipt* and *mark copy available* happen in parallel → **join** waits for both → end.

## Activity Diagram vs Flowchart vs State Machine

| Activity diagram | Flowchart | State machine diagram |
|---|---|---|
| UML behaviour diagram | Older, informal | UML behaviour diagram |
| Shows **parallel** flows (fork/join) and **who** does what (swimlanes) | Sequential only; no swimlanes (classically) | Shows the **states of one object** |
| Nodes are **actions**; flow moves when an action completes | Nodes are steps | Nodes are **states**; moves on **events** |
| Business processes, workflows, use case flows, algorithms | Simple algorithms | Reactive objects, life-cycles |

## When to Use Activity Diagrams

- **Business process / workflow modelling** — understanding how an organisation works (e.g. how a library processes new books), especially early in UP (Business Modeling).
- **Visualising a complex use case** — its main and alternative flows.
- **Processes with parallel steps** — fork/join make concurrency explicit.
- **Complex algorithms** — as an enhanced flowchart.
- **Data flow** — with object nodes (they can replace data-flow diagrams).

Not for: how objects call each other (→ sequence diagram), or one object's life-cycle (→ state machine).

:::key
- Activity diagram = flow of actions with decisions, merges, **forks/joins** (parallelism) and **swimlanes** (responsibility).
- Activity final ◉ ends everything; flow final ⊗ ends one branch.
- Best for business processes, workflows, complex use cases, algorithms.
:::

:::mistakes
- Using a decision diamond where you need parallel flows (use a **fork** bar).
- Forking without a matching **join**.
- Missing or overlapping guards on decision branches (add `[else]`).
- Confusing activity final (everything ends) with flow final (one branch ends).
:::

:::exam
- *"Explain activity diagram notation. Draw an activity diagram for <process> with swimlanes."* (Online order, ATM withdrawal, admission process…)
- *"Differentiate activity and state machine diagrams."*
- *"When should activity diagrams be used?"*
:::

:::def
An **activity diagram** is a UML behaviour diagram that shows the flow of control (and data) from activity to activity, including sequential and parallel flows (fork/join), decisions and merges, and — using partitions (swimlanes) — which participant performs each action. It is used for modelling business processes, workflows and complex operations.
:::

## Quick Check

:::q Q1 · What's the difference between a fork and a decision?
:::ans
A **fork** starts several flows that run **in parallel** (all are taken); a **decision** chooses **one** outgoing flow based on guards.
:::
:::

:::q Q2 · What do swimlanes show?
:::ans
**Who** (which actor, department or system) is responsible for each action.
:::
:::
