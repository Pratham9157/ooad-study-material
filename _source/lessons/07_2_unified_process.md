**The Unified Process (UP) is a popular way to organise an object-oriented software project: build the system in short, repeated cycles (iterations), each producing a working, tested piece of software, instead of doing all requirements, then all design, then all coding.**

## The Problem: The Waterfall Trap

The traditional **waterfall** process works like this: gather *all* requirements → design *everything* → code *everything* → test *everything* → deliver.

What goes wrong:
- Requirements are **never** fully known at the start; they change as users see the product.
- Big mistakes are discovered only during testing, at the very end — when fixing them is most expensive.
- Users see working software only after months, and often say "that's not what we meant".

:::analogy
**Waterfall** is like building an entire house from a blueprint and showing it to the owner only at the end. **Iterative development** is like building and finishing **one room at a time**, getting the owner's feedback after each room, and adjusting the plan for the next one. Mistakes are caught when they're small.
:::

## Iterative and Incremental Development

- Development is organised into a series of short, **fixed-length** mini-projects called **iterations**.
- Each iteration includes its own **requirements, design, implementation and testing**, and ends with a **tested, integrated, executable** partial system.
- The system grows **incrementally**, iteration by iteration.
- Iterations are **timeboxed** — Larman recommends **2 to 6 weeks**. If work doesn't fit, the scope is reduced; the deadline doesn't move.

| Waterfall | Iterative & incremental (UP) |
|---|---|
| All requirements, then all design, then all code | A little of everything in every iteration |
| Working software only at the end | Working software after every iteration |
| Risks discovered late | High risks tackled early |
| Assumes requirements are stable | Embraces change, uses feedback |

## Understanding the Unified Process

**UP** is an iterative, incremental process for building object-oriented systems. (The **Rational Unified Process, RUP**, is a detailed commercial version.) It is described as:
- **Iterative and incremental**,
- **Use-case driven** (use cases guide planning, design and testing),
- **Architecture-centric** (a solid core architecture is built early),
- **Risk-driven** (the riskiest things are done first).

### The four phases

```text
 ┌───────────┬────────────────────┬────────────────────────────────────┬──────────────┐
 │ Inception │    Elaboration     │            Construction            │  Transition  │  ──► time
 │  (it 1)   │   (it 2)  (it 3)   │  (it 4) (it 5) (it 6) (it 7) ...   │   (it N)     │
 └───────────┴────────────────────┴────────────────────────────────────┴──────────────┘
  each phase = one or more iterations; each iteration ends with a tested executable increment
```

| Phase | Goal (Larman's wording) | Library example |
|---|---|---|
| **Inception** | Approximate **vision**, **business case**, **scope**, rough estimates. *Should we build it?* | "An online library system for 5,000 members; worth building." |
| **Elaboration** | Refined vision, **iterative implementation of the core architecture**, **resolution of high risks**, identification of **most requirements**, realistic estimates | Build and test issue/return with the real database; domain model; most use cases written |
| **Construction** | Iterative implementation of the **remaining, lower-risk** parts; prepare for deployment | Reports, reservations, fines, admin screens |
| **Transition** | **Beta testing, deployment**, training | Pilot in one branch, then all branches |

:::warn The most common exam mistake about UP
**Inception is NOT "the requirements phase", and elaboration is NOT "the design phase".** Every phase contains requirements, design, coding and testing work — just in different amounts. Treating phases as waterfall steps is exactly what Larman warns against ("superimposing waterfall on UP").
:::

### Disciplines (the kinds of work)

A **discipline** is a set of related activities — e.g. Requirements or Design. Disciplines run **across all phases** with changing effort.

| Discipline | About | Key artifacts |
|---|---|---|
| **Business Modeling** | understanding the domain | **Domain Model** |
| **Requirements** | what the system must do | **Use-Case Model**, Vision, **Supplementary Specification**, **Glossary** |
| **Design** | the software solution | **Design Model** (interaction & class diagrams), Software Architecture Document |
| **Implementation** | coding & building | source code, executables |
| **Test** | checking quality | test cases |
| **Deployment** | delivering the system | deployment plan |
| *Supporting:* configuration & change management, project management, environment | | |

```text
                   Inception  Elaboration   Construction     Transition
 Business Modeling   ▃▃        ▆▆▆▃          ▁
 Requirements        ▆▆        ▇▇▇▆▃         ▃▂▁               ▁
 Design              ▂         ▆▇▇▆          ▅▅▄▃              ▁
 Implementation      ▁         ▄▆▆▅          ▇▇▇▇▇▆            ▂
 Test                ▁         ▃▄▄▄          ▆▆▆▆▆▆            ▄
 Deployment                    ▁             ▂▂▃               ▇▇
            (bar height ≈ effort; every discipline appears in many phases)
```

**Phase vs discipline:** a phase is a **period of time**; a discipline is a **type of work** done throughout.

### UP best practices

1. Tackle **high-risk, high-value** issues in early iterations.
2. **Continuously engage users** for feedback.
3. Build a **cohesive core architecture** early.
4. **Test early, often and realistically**.
5. Apply **use cases**.
6. Do some **visual modelling (UML)**.
7. Carefully **manage requirements** and **change requests**.

## Types of Requirements: FURPS+

UP classifies requirements with **FURPS+**:

| | Category | Library example |
|---|---|---|
| **F** | Functional — features | issue/return books, calculate fines |
| **U** | Usability — ease of use, help | a new member can borrow within 2 minutes |
| **R** | Reliability — failures, recovery | available 99.5% of opening hours |
| **P** | Performance — speed, capacity | search results in under 2 seconds |
| **S** | Supportability — maintainability, configurability | fine rate changeable without code changes |
| **+** | implementation, interface, operations, packaging, legal constraints | must run on existing servers |

Functional requirements go into **use cases**; the others (non-functional) into the **Supplementary Specification**.

## Background: Where UP Came From (Bahrami)

Before UML/UP, three methods were popular: **Booch** (strong in design), **Rumbaugh's OMT** (object, dynamic and functional models; strong in analysis), and **Jacobson's OOSE/Objectory** (use-case driven). These three authors joined Rational, merged their notations into **UML** and their processes into the **Unified Process**. Bahrami's **Unified Approach** similarly combines the best of the three.

:::key
- UP = iterative, incremental, use-case driven, architecture-centric, risk-driven; timeboxed iterations of 2–6 weeks.
- Phases: Inception (vision, scope) → Elaboration (core architecture, high risks, most requirements) → Construction (the rest) → Transition (beta, deployment).
- Disciplines (requirements, design, implementation, test, …) run across all phases.
- FURPS+: functional → use cases; non-functional → supplementary specification.
:::

:::mistakes
- Treating UP phases like waterfall steps (inception = requirements, elaboration = design).
- Confusing **phases** (time) with **disciplines** (kinds of work).
- Saying working software appears only in construction — every iteration produces an executable.
:::

:::exam
- *"Explain the Unified Process with its phases."* (Very common.) Draw the phase diagram, explain each phase, list disciplines and best practices, contrast with waterfall.
- *"Differentiate iterative and waterfall development."*
- *"What is FURPS+?"*
:::

:::def
The **Unified Process (UP)** is an iterative and incremental, use-case-driven, architecture-centric software development process in which the project is organised into timeboxed iterations grouped into four phases — **inception, elaboration, construction and transition** — each iteration producing a tested, executable increment of the system.
:::

## Quick Check

:::q Q1 · In which phase are the core architecture built and the high risks resolved?
:::ans
**Elaboration.**
:::
:::

:::q Q2 · An iteration can't finish all planned features by its end date. What does timeboxing say to do?
:::ans
Keep the end date and **reduce the scope** of that iteration (move features to a later iteration).
:::
:::

:::q Q3 · Is "search results in under 2 seconds" functional or non-functional? Where is it documented?
:::ans
Non-functional (**Performance**); documented in the **Supplementary Specification**.
:::
:::
