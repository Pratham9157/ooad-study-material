**UML (Unified Modeling Language) is a standard *visual language* — a set of diagram types — for describing software systems. It is a notation, not a process.**

## The Problem: Everyone Draws Differently

Without a standard, one designer draws classes as circles, another as boxes; one uses an arrow to mean "inherits", another to mean "calls". Diagrams become confusing and can't be shared across teams or tools. UML gives everyone **one agreed set of symbols**.

:::analogy
UML is to software what **architectural drawing symbols** are to buildings. Any architect anywhere understands what a door symbol or a staircase symbol means. Likewise, any developer understands a UML class box or an inheritance arrow.
:::

## Understanding UML

- **UML is a visual language** for **specifying, constructing and documenting** the artifacts of software systems.
- It is a **standard** maintained by the **OMG** (Object Management Group), adopted in **1997**, created by **Booch, Rumbaugh and Jacobson** ("the three amigos"). Current version: UML 2.x.
- **It is NOT a methodology or process.** UML tells you *how to draw*; a process like UP tells you *what to do and when*.

## Three Ways People Use UML

| Mode | What it means |
|---|---|
| **UML as sketch** | quick, informal, partial diagrams on a whiteboard to explore ideas (the most common use) |
| **UML as blueprint** | detailed diagrams used to generate code (forward engineering) or to understand existing code (reverse engineering) |
| **UML as programming language** | the model is complete enough to generate the whole executable system (rare) |

## Three Perspectives

The same class-box notation can describe different things:
1. **Conceptual perspective** — things in the real world (the *domain model*: a real "Loan").
2. **Specification (software) perspective** — software abstractions and interfaces.
3. **Implementation perspective** — actual classes in a specific language (C++ `class Loan`).

## The 14 UML 2 Diagrams

```text
                                       UML 2 diagrams
                 ┌─────────────────────────┴──────────────────────────┐
     STRUCTURE (static) — what exists               BEHAVIOUR (dynamic) — what happens
     ├── Class diagram          ★                   ├── Use case diagram           ★
     ├── Object diagram                             ├── Activity diagram           ★
     ├── Package diagram        ★                   ├── State machine diagram      ★
     ├── Component diagram      ★                   └── Interaction diagrams
     ├── Deployment diagram     ★                       ├── Sequence diagram       ★
     ├── Composite structure diagram                    ├── Communication diagram  ★
     └── Profile diagram                                ├── Interaction overview diagram
                                                        └── Timing diagram
                                        ★ = in your syllabus
```

| Diagram | Answers the question | Lesson |
|---|---|---|
| Use case | What does the system do for whom? | 9.2 |
| Class | Which classes, attributes, operations, relationships? | 10.1 |
| Object | What do the objects look like at one moment? | 10.1 |
| Sequence | In what order do objects send messages? | 11.2 |
| Communication | Which objects are linked, and what messages flow? | 11.3 |
| State machine | How does one object react to events over its life? | 12.1 |
| Activity | What is the flow of a process, including parallel steps? | 12.2 |
| Package | How is the system grouped into packages/layers? | 12.3 |
| Component | What are the replaceable software parts and interfaces? | 12.3 |
| Deployment | What runs on which hardware? | 12.3 |

:::key
- UML = standard visual modelling **language** (OMG, 1997; Booch, Rumbaugh, Jacobson). Not a process.
- Used as sketch, blueprint or programming language; from conceptual, specification or implementation perspective.
- UML 2 has 14 diagrams: 7 structure + 7 behaviour (4 of which are interaction diagrams).
:::

:::mistakes
- Calling UML a methodology or process.
- Saying UML has 9 diagrams — that was UML 1.x; UML 2 has 14.
- Classifying sequence diagrams as structural — they're behavioural (interaction) diagrams.
:::

:::exam
- *"What is UML? Classify the UML diagrams."* → definition + the tree.
- *"Explain the ways of applying UML."*
:::

:::def
The **Unified Modeling Language (UML)** is a standard visual language for specifying, constructing and documenting the artifacts of software systems. UML 2 defines **structure diagrams** (class, object, package, component, deployment, composite structure, profile) and **behaviour diagrams** (use case, activity, state machine, and the interaction diagrams: sequence, communication, interaction overview, timing).
:::

## Quick Check

:::q Q1 · Is UML a process? What is the relationship between UML and UP?
:::ans
No — UML is a **notation** (language). UP is a **process** that uses UML diagrams as artifacts.
:::
:::

:::q Q2 · Name three structure diagrams and three behaviour diagrams.
:::ans
Structure: class, package, deployment (also object, component…). Behaviour: use case, sequence, state machine (also activity, communication…).
:::
:::
