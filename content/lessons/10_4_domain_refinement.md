**In later iterations, the domain model is refined: similar concepts are organised into hierarchies (generalization), relationship data gets its own class (association classes), and whole–part relationships are marked (composition).**

## Part 1 — Conceptual Class Hierarchies (Generalization)

### The problem

The library accepts fines by **cash**, **card** and **UPI**. If we model three unrelated classes, we repeat their common data (amount, date) and their common association (each *pays for* a Fine) three times — and lose the idea that they're all "payments".

### The idea

**Generalization** = identifying what concepts have **in common** and putting it in a **superclass**, with **subclasses** for the specific kinds.

```text
                        ┌──────────────┐
                        │  *Payment*   │      italic = abstract (every payment is one of the kinds below)
                        │  amount      │
                        │  date        │
                        └──────▲───────┘
            ┌──────────────────┼──────────────────┐
     ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
     │ CashPayment  │   │ CardPayment  │   │ UPIPayment   │
     │ tendered     │   │ cardNumber   │   │ upiId        │
     └──────────────┘   └──────────────┘   └──────────────┘
```

:::analogy
Biology's classification: *Animal → Mammal → Dog*. Everything true of all mammals (warm-blooded, has hair) is stated once at "Mammal"; each species adds its own specifics.
:::

### Two rules to check a subclass

1. **The 100% Rule** — **100% of the superclass's definition must apply to the subclass**: every attribute and association of `Payment` must make sense for `CardPayment`. (Every card payment has an amount and pays for a fine ✓.)
2. **The Is-a Rule** — every member of the subclass set must be a member of the superclass set: "A CardPayment **is a** Payment" ✓. "A Member is a Library" ✗.

A subclass passing both is a **conforming subclass**.

### When to create a subclass

Create a subclass when it:
1. has **extra attributes** of interest (`CardPayment.cardNumber`),
2. has **extra associations** of interest (`CardPayment` *paid-with* `CreditCard`),
3. is **handled differently** (card payments need authorization),
4. **behaves differently** in a way that matters (`StudentMember` vs `FacultyMember` with different loan limits).

**Don't** create subclasses just because you *can* classify (e.g. `RedBook` / `BlueBook` — no different attributes, links or handling).

### When to create a superclass

When several classes are variations of a similar concept, satisfy the 100% and Is-a rules, and share **common attributes or associations** that can be moved up.

### Abstract conceptual classes

If **every** instance of the superclass must belong to one of the subclasses, the superclass is **abstract** — written in *italics*. Every payment is cash, card or UPI → *Payment* is abstract.

### Don't model states as subclasses

An issued copy and an available copy are the *same* copy at different times. Objects can't change their class, so `IssuedCopy` / `AvailableCopy` subclasses are wrong. Use a `status` attribute, or a **state machine diagram** (Lesson 12.1).

## Part 2 — Association Classes

### The problem

Where do `issueDate` and `dueDate` belong? Not in `Member` (a member has many loans) and not in `BookCopy` (a copy is borrowed many times). They belong to **the borrowing relationship itself**.

### The idea

An **association class** is an association that is also a class, with its own attributes. It's drawn as a class box connected by a **dashed line** to the association line.

```text
   ┌──────────┐ *                          * ┌──────────────┐
   │  Member  │──────────────┬───────────────│  BookCopy    │
   └──────────┘              ┆               └──────────────┘
                     ┌───────────────┐
                     │     Loan      │    association class: its attributes describe
                     │ issueDate     │    the relationship, not either end
                     │ dueDate       │
                     └───────────────┘
```

Clues: an attribute that describes the relationship; a many-to-many association that needs extra data. Other examples: `Employment` (salary) between Person and Company; `Enrollment` (grade) between Student and Course; Larman's `ServiceContract` (merchantID) between Store and AuthorizationService.

## Part 3 — Aggregation and Composition in the Domain Model

Mark strong whole–part relationships with **composition** (◆): Sale ◆ SalesLineItem, Book ◆ Chapter, Hospital ◆ Department. Larman suggests composition when:
- the part's **lifetime is bound** to the whole's (create–delete dependency),
- there's an obvious **physical or logical assembly**,
- **properties of the whole propagate** to the parts (move the house → rooms move),
- **operations on the whole propagate** to the parts (delete the order → delete its lines).

And for shared aggregation: "if in doubt, leave it out". (Full comparison: [Lesson 8.2](08_2_aggregation_composition.html).)

## Part 4 — Other Refinements (Brief)

- **Qualified association** — a qualifier picks one object out of many: `Catalog [isbn] ── 1 Book` (given an ISBN, exactly one Book).
- **Reflexive association** — a class associated with itself: Member *refers* Member.
- **Derived elements** — `/total`, shown only when useful.
- **Packages** — split a big domain model into packages (Core, Loans, Payments) — Lesson 12.3.

:::key
- Generalization groups similar concepts; check with the **100% rule** and the **Is-a rule**.
- Subclass when there are extra attributes, extra associations, different handling or behaviour.
- Abstract superclass (italic) when every instance belongs to a subclass. Don't model states as subclasses.
- Association class: attributes that belong to the relationship itself (Loan between Member and BookCopy).
- Composition for strong whole–part with lifetime dependency.
:::

:::mistakes
- Subclasses that fail the 100% rule (e.g. a subclass that can't have one of the parent's associations).
- Using subclasses for states (`OverdueLoan`).
- Putting relationship data (dueDate) into one of the two classes instead of an association class.
- Pointless subclasses with nothing different.
:::

:::exam
- *"Explain domain model refinement. What are the 100% and Is-a rules?"*
- *"When should conceptual subclasses/superclasses be defined?"*
- *"What is an association class? Give an example."*
:::

:::def
**Generalization** is the activity of identifying commonality among concepts and defining superclass (general concept) and subclass (specialized concept) relationships. The **100% rule** states that 100% of the superclass's definition (attributes and associations) must be applicable to the subclass; the **Is-a rule** states that all members of the subclass set must be members of the superclass set. An **association class** models an association that has its own attributes.
:::

## Quick Check

:::q Q1 · Does `LargePayment` (amount > ₹10,000) make a good subclass of Payment?
:::ans
Usually **no** — unless large payments have extra attributes/associations or are handled differently (e.g. need manager approval). Otherwise it's just a value condition.
:::
:::

:::q Q2 · Students enrol in courses and receive a grade per course. Where does `grade` go?
:::ans
In an **association class** `Enrollment` on the Student ∗—∗ Course association — the grade belongs to the (student, course) pair.
:::
:::
