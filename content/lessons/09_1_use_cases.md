**A use case is a written story of how someone uses the system to achieve a goal — including what happens when things go right and when they go wrong.** Use cases are how we capture *what the system must do*.

## The Problem: "Make a Library System" Is Not a Requirement

A client says "we need a library system". What exactly must it do? If developers guess, they'll build the wrong thing. A simple features list ("system shall issue books") helps, but it misses the **context**: *who* issues? *what happens* if the member has unpaid fines? *what if* the book is reserved by someone else?

Use cases capture requirements as **stories from the user's point of view**, including the failures — exactly where the missing requirements usually hide.

:::analogy
A use case is like a **film script** for one goal. It names the characters (actors), describes the normal storyline step by step (main success scenario), and also scripts the "what if" scenes — what if the card is declined, what if the book is missing (extensions).
:::

## Key Terms

- **Actor** — something with behaviour that interacts with the system: a **person in a role** (Member, Librarian), another **computer system** (Payment Gateway), or an **organisation**.
- **Scenario** — one specific path through the story, e.g. "Asha borrows *Clean Code* successfully" or "Ravi tries to borrow but has unpaid fines". A scenario is also called a **use case instance**.
- **Use case** — a **collection of related success and failure scenarios** describing an actor using the system to achieve a goal. Named **verb + noun**: *Issue Book*, *Pay Fine*, *Process Sale*.

### Three kinds of actors

| Actor | Meaning | Library example |
|---|---|---|
| **Primary actor** | uses the system to achieve their own goal | Librarian, Member |
| **Supporting actor** | provides a service *to* the system | Payment Gateway, Email service |
| **Offstage actor** | has an interest in the outcome but doesn't interact directly | Auditor, university finance office |

## Three Formats: Brief, Casual, Fully Dressed

You don't write every use case in full detail on day one. UP uses three levels of detail:

**Brief** — one paragraph, usually the success path.
> *Issue Book:* A member brings books to the desk. The librarian identifies the member and scans each copy. The system checks the member's eligibility, records a loan with a due date for each copy, and prints a slip.

**Casual** — a few informal paragraphs covering the main and some alternative scenarios.
> *Return Book:* The librarian scans a returned copy; the system closes the loan and marks the copy available. *If the copy is overdue*, the system calculates a fine and records it. *If another member reserved it*, the system notifies them.

**Fully dressed** — every step and variation, with supporting sections. Written for the most important use cases.

## The Fully Dressed Template (with Example)

```text
Use Case UC1: Issue Book
Scope:            Library Management System
Level:            User goal
Primary Actor:    Librarian
Stakeholders and Interests:
  - Librarian: wants fast, accurate issuing.
  - Member: wants to borrow quickly and know the due date.
  - Library management: wants correct records and loan limits enforced.
Preconditions:    The librarian is logged in.
Success Guarantee (Postconditions):
  Loans are saved; copies are marked "issued"; the member's loan count is updated; a slip is printed.
Main Success Scenario:
  1. Member arrives at the desk with copies to borrow.
  2. Librarian starts a new issue session.
  3. Librarian enters the member ID.
  4. System validates the member and shows their details and current loans.
  5. Librarian enters a copy ID.
  6. System records a loan for the copy with a due date and shows the title and due date.
     Librarian repeats steps 5-6 until all copies are entered.
  7. Librarian ends the session.
  8. System saves the loans and prints the slip.
Extensions (alternate flows):
  *a. At any time the system fails: librarian restarts; system restores the session.
  4a. Member ID invalid or membership expired: system shows an error; session ends.
  4b. Member has unpaid fines above the limit: system shows the fine (see UC4 Pay Fine).
  6a. Copy ID not found: system shows an error; librarian re-enters it.
  6b. Member has reached the loan limit: system refuses the copy.
  6c. Copy is reserved for another member: system refuses the copy.
Special Requirements:   each scan handled within 2 seconds.
Technology & Data Variations: copy ID by barcode scanner or keyboard.
Frequency of Occurrence:      almost continuous during opening hours.
Open Issues:                   should members self-issue at a kiosk?
```

**What each important section means:**
- **Stakeholders and interests** — everyone who cares about the outcome, and what they want. The system must satisfy *all* of them (e.g. management wants limits enforced — so step 6b exists).
- **Preconditions** — what must already be true before starting.
- **Success guarantee** — what must be true when the use case succeeds.
- **Main success scenario** — the "happy path": a numbered list of actor actions and system responses, with **no branches**.
- **Extensions** — every other path, numbered by the step where it branches (`4a`, `6b`); `*a` = can happen at any step.

## Guidelines for Good Use Cases

1. **Essential, UI-free style:** "Librarian enters member ID" ✓ — not "Librarian clicks the blue button and types in box 3" ✗. Describe **intent**, not screens.
2. **Black-box:** say *what* the system does, not *how* internally. ✓ "System records the loan." ✗ "System runs an SQL INSERT into LOANS."
3. **Terse:** short, clear sentences.
4. **Actor-goal perspective:** each use case delivers something of value to an actor.

## Finding Use Cases (and Checking They're Useful)

**Steps:** (1) choose the system boundary, (2) identify primary actors, (3) list each actor's goals, (4) one use case per goal.

**Is it a good, user-goal level use case?**
- **Boss test:** "What did you do all day?" — "I issued books" ✓. "I logged in" ✗ — the boss wouldn't be impressed.
- **EBP test** (Elementary Business Process): a task done **by one person, in one place, at one time**, in response to a business event, that **adds measurable value** and leaves data **consistent**. *Issue Book* ✓; *Enter Member ID* ✗ (too small); *Run the Library* ✗ (too big).
- **Size test:** a real use case has several steps, not just one.

## When to Use Use Cases

**Use them** for capturing **functional requirements** in almost every project. In UP they drive everything: iterations are planned around use cases, designs "realize" them (sequence diagrams), and test cases come from their scenarios.

**Don't rely on them** for non-functional requirements (performance, usability…) → Supplementary Specification; for systems with little user interaction (e.g. a compiler); or for internal design details.

:::key
- Use case = related success/failure scenarios of an actor achieving a goal; named verb + noun.
- Actors: primary, supporting, offstage.
- Formats: brief, casual, fully dressed. Know the fully dressed sections.
- Write essential (UI-free), black-box, terse use cases from the actor's goal perspective.
- Boss, EBP and size tests check the right level.
:::

:::mistakes
- Treating the use case **diagram** as the use case — use cases are primarily **text**.
- Writing UI details ("click OK").
- Making use cases for tiny steps (*Enter Password*, *Click Save*).
- Putting branches (if/else) in the main success scenario — they belong in extensions.
:::

:::exam
- *"Define actor, scenario and use case. Explain the types of actors."*
- *"Write a fully dressed use case for Withdraw Cash / Issue Book / Book Ticket."* (Very common — practise the template.)
- *"Explain the formats of use cases."*
:::

:::def
A **use case** is a collection of related success and failure scenarios that describe an actor using a system to achieve a goal. An **actor** is anything with behaviour (a person in a role, an external system or an organisation) that interacts with the system. A **scenario** (use case instance) is a specific sequence of actions and interactions between actors and the system.
:::

## Quick Check

:::q Q1 · Which pass the EBP test? (a) Log In (b) Book a Movie Ticket (c) Select Seat (d) Cancel Booking
:::ans
**(b)** and **(d)**. (a) and (c) are sub-steps, too small to be user goals.
:::
:::

:::q Q2 · In an ATM, is the Bank's central computer a primary, supporting or offstage actor for "Withdraw Cash"?
:::ans
**Supporting** — it provides a service (authorization) to the ATM system.
:::
:::

:::q Q3 · What's the difference between the main success scenario and extensions?
:::ans
The main success scenario is the typical, unconditional "happy path"; extensions describe all alternative paths (errors and variations), each branching from a numbered step.
:::
:::
