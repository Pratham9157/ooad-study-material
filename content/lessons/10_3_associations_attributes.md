**Once you have the conceptual classes, you connect them with associations (the relationships worth remembering) and give them attributes (the data worth remembering). Together they complete the domain model.**

## Associations in the Domain Model

### The problem

Almost any two concepts *interact* somehow. If we drew a line for every interaction, a 15-class model would have dozens of crossing lines — unreadable. We need a rule for **which** connections deserve a line.

### The rule: "need to remember"

Show an association when **knowledge of the relationship must be preserved for some duration** — a "need-to-remember" association. We must *remember* which member borrowed which copy (a Loan), so Member–Loan–BookCopy are associated. A librarian merely *talking* to a member doesn't need remembering → no line.

:::analogy
Your phone's **contacts list** stores only the relationships you want to remember — not every person you once passed on the street. A domain model's associations are the "saved contacts" of the domain.
:::

### Guidelines

- Name associations **ClassName – VerbPhrase – ClassName** so they read like a sentence: *Member–Initiates–Loan*, *Catalog–Contains–Book*. Avoid vague names like "Has" when something more meaningful exists.
- Put **multiplicity** on both ends.
- Two classes can have **several** associations (Flight *flies-to* Airport, Flight *flies-from* Airport).
- Domain associations are **conceptual** — not database foreign keys or C++ pointers.
- Don't overdo it: focus on need-to-remember links.

Common association patterns (Larman): A is a transaction related to B (Payment–Sale); A is a line item of B; A is a part of B (Chapter–Book); A is contained in B (Book–Catalog); A is a description for B (Book–BookCopy); A is recorded in B (Loan–Register); A is a member of B (Member–Library); A uses/manages/owns B.

## Attributes in the Domain Model

### The rule

Include an attribute when the requirements suggest a need to **remember a piece of information** — e.g. a Loan's `dueDate`, a Member's `name`.

### Guidelines

1. Attributes should be **simple data types**: number, text, date, time, Boolean — or common **data-type classes** like Address, Money, PhoneNumber, ISBN.
2. **Connect classes with associations, not with attributes.**
   ✗ `Loan { memberId }` (a "foreign key" attribute)  ✓ draw a `Member — Loan` association.
3. Create a **data-type class** when a value has parts (Address, Name), its own rules (validating an ISBN), extra attributes (a promotional price with start/end dates), or a unit (Money with currency).
4. **Derived attributes** (calculable from others) are prefixed with `/`, e.g. `/numOfLoans`.
5. In a domain model, types are optional and there are **no operations**.

## The Complete Library Domain Model

<<SVG:domainmodel>>

Read it as sentences:
- A **Library** *employs* one or more Librarians, *has* many Members and *owns* one Catalog.
- The **Catalog** *contains* many **Book**s (description class), each *describing* many **BookCopy**s.
- A **Member** *initiates* many **Loan**s; each Loan *is for* exactly one BookCopy.
- A Loan *may generate* zero or one **Fine**.

Notice what's absent: no `IssueController`, no `Database`, no methods like `calculateFine()`. Those come in design.

:::key
- Associations = need-to-remember relationships; name them verb-style; add multiplicities.
- Attributes = simple data to remember; relate classes by associations, never foreign-key attributes.
- Derived attributes use `/`; data-type classes for structured values.
- The finished domain model has classes, associations, multiplicities and attributes only.
:::

:::mistakes
- Adding a line for every interaction (clutter).
- `memberId` inside `Loan` instead of an association.
- Missing multiplicities.
- Adding operations or software classes.
- Showing the same relationship twice (as an attribute **and** a line).
:::

:::exam
- *"Draw the domain model for <problem statement>."* — the most common Part II diagram question. Steps: list nouns → filter into classes/attributes → add associations with names and multiplicities → add attributes → check: no operations.
- *"How are associations and attributes identified in a domain model?"*
:::

:::def
In a domain model, an **association** is a meaningful relationship between conceptual classes whose knowledge needs to be preserved for some duration; an **attribute** is a logical data value of a conceptual class that needs to be remembered. Attributes should be simple data types; conceptual classes should be related through associations, not through attributes.
:::

## Quick Check

:::q Q1 · A student models `Order { customerId, productIds }`. What's wrong?
:::ans
These are foreign-key-style attributes. Replace them with **associations**: `Customer 1 — places — * Order`, and `Order — contains — Product` (often via an `OrderLine` with quantity).
:::
:::

:::q Q2 · Should "a cashier greets a customer" be an association in a shop's domain model?
:::ans
Usually **no** — it's a momentary interaction that doesn't need to be remembered.
:::
:::
