**Object-Oriented Analysis (OOA) is figuring out *what* the problem is in terms of real-world objects. Object-Oriented Design (OOD) is deciding *how* software objects will work together to solve it.** Welcome to Part II — from writing classes to *designing* systems.

## The Problem: Coding Before Thinking

In Part I you learned to *write* classes. But given a real project — "build a library system" — which classes should exist? Should `Member` calculate fines or should `Loan`? Who creates a `Loan` object? Teams that jump straight into code usually end up with:
- classes that don't match how users think about the problem,
- one giant class doing everything,
- designs that collapse the moment a requirement changes.

OOAD gives a **disciplined way of thinking before (and while) coding**.

:::analogy
**Building a house.** Analysis: the architect interviews the family — how many rooms, a study, a garden? (*What do we need?*) Design: the architect draws blueprints — walls, pipes, wiring (*How will we build it?*). Programming: the builders construct it. Skipping straight to construction produces a house nobody wants to live in.
:::

## Understanding Analysis and Design

| | Analysis | Design |
|---|---|---|
| Question | **What** is the problem? What are the requirements? | **How** will software solve it? |
| Slogan (Larman) | "**Do the right thing**" | "**Do the thing right**" |
| OO focus | Find and describe the **objects (concepts) in the problem domain** | Define **software objects** and how they **collaborate** |
| Library example | "There are Members, Books, Copies, Loans, Fines. A member borrows a copy." | "A `Loan` object knows its due date and calculates its own fine; a `Member` keeps a list of `Loan`s." |
| Typical artifacts | use cases, domain model, system sequence diagrams | interaction diagrams, design class diagrams |

Then **Object-Oriented Programming (OOP)** implements the design: `class Loan { … int fine() const; };`

## A Tiny Complete Example (Larman's Dice Game)

*Requirement:* a player rolls two dice; if the total is 7 they win.

```text
1. Define use cases           "Play a Dice Game: the player rolls the dice. If the total is 7, they win;
   (requirements)              otherwise they lose."

2. Define the domain model     Player ──rolls──► Die (2)        concepts from the REAL world
   (analysis)                  Player ──plays──► DiceGame

3. Assign responsibilities &   :DiceGame ──play()──► die1:Die ──roll()──
   draw interaction diagrams              ──►        die1:Die ──getFaceValue()──   who does what, in which order
   (design)

4. Define design class         DiceGame { die1, die2 : Die ; play() }      software classes with methods
   diagrams (design)           Die      { faceValue : int ; roll(), getFaceValue() }
```

Notice the flow: **requirements → real-world concepts → object collaboration → software classes**. Part II teaches each of these steps, one chapter at a time, using our Library system.

## Why Object-Oriented Analysis & Design?

- The software's structure **mirrors the real world**, so it's easier to understand and discuss with users. (Larman calls this a **low representational gap**: a real "Loan" ↔ a software `Loan`.)
- Responsibilities are spread over many small objects → easier to change and reuse.
- The same concepts and diagrams (UML) are shared by analysts, designers and programmers.

:::key
- OOA = find **what**: real-world concepts and requirements. OOD = decide **how**: software objects and their collaboration. OOP = implement.
- Analysis: "do the right thing"; design: "do the thing right".
- Flow: use cases → domain model → interaction diagrams → design class diagrams → code.
:::

:::mistakes
- Saying the analysis model contains software classes with methods — analysis shows **conceptual** classes only.
- Thinking analysis, design and programming happen once, in strict order — in iterative development (next lesson) they happen in **every** iteration.
:::

:::exam
- *"Define OOA and OOD. Differentiate them with an example."* → the table + library example.
- *"Explain the steps of OOAD using a simple example."* → the dice game.
:::

:::def
**Object-Oriented Analysis (OOA)** is the process of investigating a problem and its requirements by identifying and describing the objects or concepts in the problem domain. **Object-Oriented Design (OOD)** is the process of defining software objects — their responsibilities and how they collaborate — to fulfil the requirements. Analysis emphasises *what* the system must do; design emphasises *how* it will do it.
:::

## Quick Check

:::q Q1 · Classify as analysis or design: (a) "A hospital has doctors and patients; patients book appointments." (b) "The `AppointmentScheduler` class calls `doctor.isFree(slot)` before creating an `Appointment`."
:::ans
(a) **Analysis** — describes real-world concepts. (b) **Design** — describes software objects and their collaboration.
:::
:::

:::q Q2 · What does "low representational gap" mean?
:::ans
The software design closely mirrors the real-world domain (e.g. a real loan ↔ a `Loan` class), making the software easier to understand and change.
:::
:::
