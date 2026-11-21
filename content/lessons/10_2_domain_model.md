**A domain model is a picture of the important *real-world* concepts in the problem area and how they relate — the vocabulary of the problem, drawn as a simple class diagram with no software details.**

## The Problem: Developers Don't Speak "Library"

A team of programmers starts building the library system. One calls a book a "Title", another an "Item", a third "Resource". Is a "book" the idea of *Clean Code*, or the physical copy on shelf 3? Does a fine belong to a member or to a loan? Without a shared understanding of the **domain** (the problem area), the design becomes confused.

The **domain model** fixes this before design starts: a shared, visual **dictionary** of the domain.

:::analogy
Before writing a travel guide to a city, you draw a **map of the city**: its landmarks and the roads between them. You don't draw the guidebook's chapters yet. The domain model is that map of the *problem* — later, the design (the guidebook) is organised around it.
:::

## Understanding the Domain Model

- It is a **visual representation of conceptual classes or real-situation objects** in a domain (Larman).
- It's built in the **Elaboration** phase, as part of the **Business Modeling** discipline.
- It shows three things: **conceptual classes**, **associations** between them, and **attributes**.
- It **does not** show software classes (no `LoanDatabase`, `IssueController`, `Window`), and **no operations/methods**.

**Why bother?** It gives everyone a common vocabulary, and it inspires the names of software classes later — so the code mirrors the real world (a **low representational gap**).

A **conceptual class** has three aspects:
- **Symbol** — its name ("Loan").
- **Intension** — its definition ("a record that a member borrowed a copy until a due date").
- **Extension** — the set of all real examples (every actual loan).

## How to Find Conceptual Classes — Three Strategies

### Strategy 1: Reuse existing models

Many domains (inventory, finance, healthcare) already have published models and "analysis patterns". Start from those if available.

### Strategy 2: Use a category list

Go through a checklist of typical categories and ask "what's this in my domain?"

| Category | Library | Shop (Larman's POS) |
|---|---|---|
| Business transactions | Loan, FinePayment, Reservation | Sale, Payment |
| Transaction line items | — | SalesLineItem |
| Product/service in a transaction | BookCopy | Item |
| Where is it recorded? | Catalog, LoanRegister | Register |
| Roles of people/organisations | Member, Librarian | Cashier, Customer |
| Places | Library, Branch | Store |
| Physical objects | BookCopy, Shelf | Item |
| Descriptions of things | Book | ProductDescription |
| Catalogs | Catalog | ProductCatalog |
| Other systems | PaymentGateway | CreditAuthorizationService |
| Records of finance/contracts | Fine, MembershipRecord | Receipt |

### Strategy 3: Find noun phrases (linguistic analysis)

Underline the nouns in the use case text:

> "**Member** arrives at the **desk** with **book copies**. **Librarian** starts a new **issue session**, enters the **member ID**. **System** validates the member, records a **loan** for the **copy** with a **due date**, and prints the **slip**."

Candidates: Member, Desk, BookCopy, Librarian, IssueSession, MemberID, System, Loan, DueDate, Slip. Then **filter**:
- *MemberID*, *DueDate* → simple values → **attributes**, not classes.
- *System* → the software itself → not a domain concept.
- *Desk*, *Slip* → irrelevant to our requirements → drop.

Noun-phrase analysis is a **starting point**, not a mechanical rule — words can be ambiguous or have synonyms.

## Three Guidelines

1. **Mapmaker principle:** use the words of the domain ("Member", not "UserEntity"); leave out irrelevant things; don't add things that aren't there.
2. **Attribute or class?** *"If we don't think of X as a number or text in the real world, X is probably a conceptual class, not an attribute."* A flight's destination is an **Airport** (a class), not a string.
3. It's better to have too many fine-grained concepts than too few — you can merge later.

## Description Classes

### The problem

Store the title, author and ISBN inside every physical **BookCopy**:
1. If the library owns 10 copies of *Clean Code*, the same title/author/ISBN is **repeated 10 times**.
2. If all copies are lost, **the information about the book disappears** — the library can't even say "we had this book; want to reserve a new copy?"

### The solution

Create a **description class** — a class that **describes** other things. `Book` holds title/author/ISBN once; each `BookCopy` (the physical item) links to its `Book`.

```text
     Without a description class                      With a description class
 ┌─────────────────────────┐            ┌──────────────────┐ 1   Describes ▶   * ┌──────────────┐
 │ BookCopy                │            │ Book             │──────────────────────│ BookCopy     │
 │ copyId                  │            │ isbn             │                      │ copyId       │
 │ title    (repeated)     │            │ title            │                      │ status       │
 │ author   (repeated)     │            │ author           │                      └──────────────┘
 │ isbn     (repeated)     │            └──────────────────┘
 └─────────────────────────┘             description class                         physical item
```

:::analogy
A **restaurant menu item** "Paneer Tikka — ₹250, spicy" is a description; each plate actually served is an item. The menu entry exists even when no plate is on any table. Larman's example: `ProductDescription` (price, description) describes many `Item`s in a store.
:::

**Add a description class when:**
- information about an item is needed **even if no instance currently exists**,
- deleting the instances would **lose** information that must be kept,
- it **reduces repeated** information.

Other examples: `FlightDescription` (route, schedule) vs `Flight` (a specific date's flight); `RoomType` vs `Room`; `Medicine` vs a prescription line.

:::key
- Domain model = conceptual classes + associations + attributes; no software classes, no operations.
- Find concepts by: reusing models, category lists, noun phrases (then filter).
- Mapmaker principle; "not number/text → class".
- Description classes (Book ↔ BookCopy, ProductDescription ↔ Item) avoid repetition and information loss.
:::

:::mistakes
- Including software things (database, UI, controller) or methods.
- Making complex concepts into string attributes.
- Mixing up Book (description) with BookCopy (physical item).
- Treating noun-phrase analysis as mechanical — always filter.
:::

:::exam
- *"What is a domain model? How are conceptual classes identified?"* → definition + three strategies + noun-phrase example.
- *"What is a description class? When is it needed?"* → problem + Book/BookCopy or ProductDescription/Item + three conditions.
:::

:::def
A **domain model** is a visual representation of conceptual classes or real-situation objects in a domain, showing conceptual classes, associations and attributes (but no software objects or operations). A **conceptual class** is an idea, thing or object in the domain. A **description class** contains information that describes something else (e.g. ProductDescription describes Items), used to avoid redundancy and loss of information.
:::

## Quick Check

:::q Q1 · From "A patient books an appointment with a doctor for a date and time slot", which nouns become classes and which become attributes?
:::ans
Classes: **Patient, Appointment, Doctor**. Attributes: **date, time slot** (of Appointment).
:::
:::

:::q Q2 · An airline stores flight number, route and schedule in each individual dated flight. What problem arises, and what's the fix?
:::ans
Repeated information and loss of the route information when no flights exist on some dates. Fix: a **description class** `FlightDescription` (number, route, schedule) describing many `Flight` instances.
:::
:::
