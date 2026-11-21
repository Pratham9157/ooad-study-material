:::tip How Part II is examined
Part II questions are mostly **define/differentiate**, **draw a diagram for a given scenario**, **identify the relationship**, and **write a use case**. For diagram questions: (1) list the elements first (actors/classes), (2) draw neatly with correct arrowheads, (3) label multiplicities and stereotypes, (4) add 2–3 lines explaining your choices. Model answers below are drawn in text form; draw them properly on paper.
:::

## Section A · Definitions & Short Answers

:::q A1 · Define OOA and OOD. Give an example of each for an ATM system.
:::ans
**OOA** – investigating the problem/requirements by finding and describing the **objects/concepts in the problem domain** ("do the right thing"). ATM example: concepts *Customer, Account, ATM, Card, Transaction, Bank*.
**OOD** – defining **software objects** and how they **collaborate** to fulfil requirements ("do the thing right"). ATM example: a software class `Account` with `withdraw(amount)` that checks the balance, and a `TransactionController` that receives the `withdraw` system operation and delegates to `Account`.
:::
:::

:::q A2 · List and explain the four phases of the Unified Process.
:::ans
1. **Inception** – approximate vision, business case, scope, vague cost/time estimates; decide whether to proceed. (Not a requirements phase.)
2. **Elaboration** – refined vision, iterative implementation of the **core architecture**, resolution of **high risks**, identification of most requirements and scope, realistic estimates. (Not a design phase.)
3. **Construction** – iterative implementation of the remaining lower-risk, easier elements; preparation for deployment.
4. **Transition** – beta tests, deployment, training.
Each phase consists of one or more **timeboxed iterations**, each producing an executable, tested increment.
:::
:::

:::q A3 · What is the difference between a UP phase and a UP discipline?
:::ans
A **phase** is a **time period** in the project (inception, elaboration, construction, transition) ending in a milestone. A **discipline** is a **set of activities and artifacts in one subject area** (requirements, design, implementation, test, …) that is performed **across all phases** with varying intensity. E.g. design work happens in elaboration *and* construction.
:::
:::

:::q A4 · What is UML? Is it a methodology? Explain the three ways of applying UML.
:::ans
UML is a **visual language for specifying, constructing and documenting the artifacts of systems** (OMG standard). It is **not** a methodology/process — it's a notation; a process like UP tells you what to do. Three ways: **UML as sketch** (informal, partial diagrams to explore ideas), **UML as blueprint** (detailed diagrams for forward/reverse engineering), **UML as programming language** (complete executable specification generating code, MDA).
:::
:::

:::q A5 · Define actor, scenario and use case. Name the three kinds of actors.
:::ans
**Actor** – something with behaviour (person in a role, computer system, organization) that interacts with the system. **Scenario** – a specific sequence of actions and interactions between actors and the system (one use case instance). **Use case** – a collection of related success and failure scenarios describing an actor using the system to achieve a goal. Actors: **primary** (goals fulfilled by the system, e.g. Cashier), **supporting** (provides a service to the system, e.g. payment authorization service), **offstage** (has an interest but doesn't interact, e.g. tax agency).
:::
:::

:::q A6 · Differentiate «include» and «extend» relationships.
:::ans
| «include» | «extend» |
|---|---|
| Base use case **always** executes the included behaviour | Extending use case **conditionally** adds behaviour |
| Used to factor out **common** behaviour from several use cases | Used to add optional behaviour **without modifying** the base |
| Arrow from **base → included** | Arrow from **extending → base** |
| Base is incomplete without it | Base is complete without it; base doesn't know about the extension |
| e.g. Issue Book «include» Validate Member | e.g. Pay Fine «extend» Return Book (if overdue) |
:::
:::

:::q A7 · What is a domain model? What does it contain and what does it NOT contain?
:::ans
A **visual representation of conceptual classes or real-situation objects in a domain** (visual dictionary). **Contains:** conceptual classes, associations (with multiplicities), attributes. **Does NOT contain:** software classes/artifacts (windows, databases, controllers), operations/methods, responsibilities, foreign-key attributes.
:::
:::

:::q A8 · What is a description class? When should one be used? Give an example.
:::ans
A class that contains information **describing something else** — e.g. `ProductDescription` (price, description, itemID) describes many `Item`s; `Book` (ISBN, title, author) describes many `BookCopy` objects. Use it when: information about an item/service is needed **independent of the existence of instances**; deleting instances would **lose information**; it **reduces redundancy**.
:::
:::

:::q A9 · State the 100% rule and the Is-a rule.
:::ans
**100% rule:** 100% of the conceptual superclass's definition (all attributes and associations) must be applicable to the subclass. **Is-a rule:** all members of the subclass set must be members of the superclass set ("Subclass *is a* Superclass"). A subclass satisfying both is a **conforming subclass**.
:::
:::

:::q A10 · Differentiate aggregation and composition with examples and notation.
:::ans
**Aggregation** – weak whole–part; parts can exist independently and be shared; hollow diamond at the whole; e.g. Team ◇— Player. **Composition** – strong whole–part; part belongs to exactly one whole, its lifetime is bound to the whole, and the whole creates/deletes its parts; filled diamond at the whole; e.g. Book ◆— Chapter, Sale ◆— SalesLineItem. (Larman suggests avoiding aggregation because of its vague semantics.)
:::
:::

:::q A11 · What is FURPS+?
:::ans
A requirements classification: **F**unctional (features), **U**sability (human factors, help), **R**eliability (failure frequency, recoverability), **P**erformance (response time, throughput), **S**upportability (maintainability, configurability) and **+** (implementation, interface, operations, packaging, legal constraints). Functional requirements go in use cases; the rest in the Supplementary Specification.
:::
:::

:::q A12 · Explain the EBP test and the Boss test for use cases.
:::ans
**EBP (Elementary Business Process) test:** a good user-goal use case is a task performed by **one person in one place at one time**, in response to a business event, that **adds measurable business value** and leaves data in a **consistent state** (e.g. *Process Sale* ✓, *Log In* ✗). **Boss test:** if your boss asks what you did all day and you answer with the use case name (e.g. "logged in"), would the boss be happy? If not, it's too low-level.
:::
:::

## Section B · MCQs

:::q B1 · In which UP phase is the core architecture implemented and high risks resolved?
(a) Inception (b) Elaboration (c) Construction (d) Transition
:::ans
**(b) Elaboration**.
:::
:::

:::q B2 · Which of these is NOT a UML structure diagram?
(a) Class (b) Component (c) Deployment (d) State machine
:::ans
**(d) State machine** — it's a behaviour diagram.
:::
:::

:::q B3 · A hollow triangle on a dashed line indicates:
(a) generalization (b) realization (c) dependency (d) aggregation
:::ans
**(b) realization** (a class implementing an interface). Solid line + hollow triangle = generalization.
:::
:::

:::q B4 · In a use case diagram, the «extend» arrow points from:
(a) base to extension (b) extension to base (c) actor to use case (d) included to base
:::ans
**(b) extension to base**.
:::
:::

:::q B5 · Which artifact belongs to the UP Business Modeling discipline?
(a) Use-case model (b) Domain model (c) Design model (d) Test model
:::ans
**(b) Domain model**.
:::
:::

:::q B6 · The multiplicity `0..1` means:
(a) exactly one (b) zero or more (c) zero or one (d) one or more
:::ans
**(c) zero or one**.
:::
:::

:::q B7 · Which should NOT appear in a domain model?
(a) Conceptual classes (b) Associations (c) Attributes (d) Operations
:::ans
**(d) Operations**.
:::
:::

:::q B8 · The recommended iteration length in UP (Larman) is:
(a) 1–2 days (b) 2–6 weeks (c) 6–12 months (d) no fixed length
:::ans
**(b) 2–6 weeks**, timeboxed.
:::
:::

:::q B9 · Which statement about use cases is TRUE?
(a) Use cases are primarily diagrams (b) Use cases are text documents (c) Use cases describe internal design (d) Use cases capture non-functional requirements best
:::ans
**(b)** — use cases are written text; the diagram is secondary.
:::
:::

:::q B10 · The person who maintains the vocabulary of the domain model without adding things not in the domain follows the:
(a) Is-a rule (b) 100% rule (c) Mapmaker principle (d) Boss test
:::ans
**(c) Mapmaker principle**.
:::
:::

## Section C · Identify the Relationship

:::q C1 · For each pair, name the most appropriate UML relationship and draw its notation: (i) Car – Engine, (ii) Student – Course, (iii) Dog – Animal, (iv) Order – OrderLine, (v) ReportPrinter uses a Formatter only inside one method, (vi) ArrayList implements List, (vii) Department – Professor, (viii) Person – Person (as a parent).
:::ans
| Pair | Relationship | Notation |
|---|---|---|
| Car – Engine | **Composition** (engine is a part; in most models its life is bound to the car) — aggregation is also accepted if the engine can be moved to another car | Car ◆── Engine |
| Student – Course | **Association** (many-to-many), e.g. *Enrolls-in* `* ── *`; an association class `Enrollment` (grade) if needed | Student ─── Course |
| Dog – Animal | **Generalization** | Dog ──▷ Animal |
| Order – OrderLine | **Composition** | Order ◆── 1..* OrderLine |
| ReportPrinter – Formatter | **Dependency** | ReportPrinter - - -> Formatter |
| ArrayList – List | **Realization** | ArrayList - - -▷ «interface» List |
| Department – Professor | **Aggregation / association** (professors exist independently, can move) | Department ◇── Professor |
| Person – Person (parent) | **Reflexive association** with roles `parent 0..2` / `child *` | Person ─┐ (loop back to itself) |
:::
:::

:::q C2 · Read the multiplicities: `Customer 1 ──── places ──── 0..* Order` and `Order * ──── contains ──── 1..* Product`.
:::ans
- One customer places **zero or more** orders; each order is placed by **exactly one** customer.
- One order contains **one or more** products; a product can appear in **zero or more** (`*`) orders.
:::
:::

:::q C3 · Draw the class diagram corresponding to this C++ code and name each relationship.
```cpp
#include <vector>
#include <string>
using namespace std;
class Engine { };
class Driver { public: string name; };
class Logger { public: void log(string) { } };
class Vehicle { public: virtual ~Vehicle() { } };
class Car : public Vehicle
{
    Engine engine;               // (1)
    vector<Driver*> drivers;     // (2)
public:
    void start(Logger &l) { l.log("start"); }   // (3)
};
int main() { Car c; return 0; }
```
:::ans
```uml
                        ┌──────────┐
                        │ Vehicle  │
                        └────△─────┘
                             │   generalization (Car is-a Vehicle)
 ┌────────┐ 1          ┌─────┴───────────────┐                 ┌────────┐
 │ Engine │───────────◆│ Car                 │- - - - - - - - >│ Logger │
 └────────┘ composition│─────────────────────│   dependency    └────────┘
                       │ + start(l : Logger) │
                       └──────────◇──────────┘
                                  │ aggregation
                                * │
                             ┌────────┐
                             │ Driver │
                             └────────┘
```
(1) `Engine engine;` → **composition** Car ◆── 1 Engine (member object, same lifetime).
(2) `vector<Driver*> drivers;` → **aggregation / association** Car ◇── * Driver (pointers to objects Car doesn't own).
(3) `Logger &l` only as a parameter → **dependency** Car - - -> Logger.
`class Car : public Vehicle` → **generalization** Car ──▷ Vehicle.
(Diamonds are at the **Car** end — the whole.)
:::
:::

## Section D · Use-Case Questions

:::q D1 · Draw a use case diagram for an ATM system with actors Customer, Bank (system) and Technician. Use at least one «include» and one «extend».
:::ans
```uml
                  ┌──────────────────────── ATM System ─────────────────────────┐
     O            │                                                              │
    /|\ ──────────┼──── ( Withdraw Cash ) - - «include» - -> ( Authenticate )   │
    / \ ──────────┼──── ( Deposit Cash )  - - «include» - ->      ▲              │      ┌──────────┐
  Customer ───────┼──── ( Check Balance ) - - «include» - - - - - ┘              ├──────│ «actor»  │
                  │            ▲                                                 │      │  Bank    │
                  │            ┆ «extend» [customer wants a receipt]             │      │  System  │
                  │     ( Print Receipt )                                        │      └──────────┘
     O            │                                                              │
    /|\ ──────────┼──── ( Refill Cash )                                          │
    / \ ──────────┼──── ( Perform Maintenance )                                  │
  Technician      └──────────────────────────────────────────────────────────────┘
```
- Customer (primary) — Withdraw Cash, Deposit Cash, Check Balance.
- All three **«include»** *Authenticate* (verify card + PIN) — common mandatory behaviour.
- *Print Receipt* **«extend»s** *Check Balance* (or Withdraw) — optional, at extension point "after transaction".
- Bank System — supporting actor associated with transaction use cases.
- Technician — Refill Cash, Perform Maintenance.
:::
:::

:::q D2 · Write a fully dressed use case for "Withdraw Cash" (ATM).
:::ans
```text
Use Case: Withdraw Cash
Scope: ATM System          Level: User goal          Primary Actor: Customer
Stakeholders and Interests:
  Customer: wants correct cash quickly; does not want money debited without receiving cash.
  Bank: wants accurate debit, wants withdrawals limited to balance and daily limit; wants fraud prevented.
Preconditions: ATM is operational and connected to the Bank System.
Success Guarantee: Cash dispensed; account debited by the same amount; transaction logged; card returned.
Main Success Scenario:
  1. Customer inserts card.
  2. System reads the card and asks for PIN.
  3. Customer enters PIN.
  4. System verifies card and PIN with the Bank System (include Authenticate).
  5. Customer chooses Withdraw and enters an amount.
  6. System requests authorization from the Bank System for the amount.
  7. Bank System approves; System debits the account and logs the transaction.
  8. System dispenses cash and returns the card.
  9. Customer takes the cash and card.
Extensions:
  4a. Invalid PIN: System asks again; after 3 failures the card is retained.
  6a. Insufficient balance or daily limit exceeded: System informs Customer; returns to step 5.
  6b. Bank System unreachable: System informs Customer, returns card, ends use case.
  8a. ATM has insufficient cash: System reverses the debit, informs Customer.
  9a. Customer does not take cash within 30 s: System retracts cash and reverses the debit.
Special Requirements: Response within 5 seconds; screen readable in sunlight.
Technology & Data Variations: Card read by magnetic stripe or chip; amount via keypad.
Frequency: Very high.
```
:::
:::

:::q D3 · Identify which of the following are good user-goal level use cases: (a) Log In, (b) Book Ticket, (c) Enter Seat Number, (d) Cancel Booking, (e) Run Airline, (f) Validate Credit Card.
:::ans
Good (pass EBP/Boss tests): **(b) Book Ticket, (d) Cancel Booking**. (a) Log In – too small; usually a sub-function/precondition. (c) Enter Seat Number – a single step. (e) Run Airline – far too big (a business process). (f) Validate Credit Card – a sub-function, a candidate for «include».
:::
:::

## Section E · Domain Model Questions

:::q E1 · Problem statement: "A hospital has many departments. Each department has many doctors; a doctor works in one department. Patients book appointments with doctors for a date and time slot. An appointment may result in one prescription that lists several medicines with dosage." — Identify conceptual classes using noun-phrase analysis and draw the domain model.
:::ans
**Noun phrases:** hospital, department, doctor, patient, appointment, date, time slot, prescription, medicine, dosage.
**Filtering:** date, time slot → attributes of Appointment; dosage → attribute of a **PrescriptionLine** (dosage belongs to the medicine *in that prescription*, not to the medicine in general — similar to SalesLineItem.quantity). **Medicine** is a description-like class (name, manufacturer).

```uml
 ┌──────────┐ 1   Has  ▶  1..* ┌────────────┐ 1   Employs ▶  1..* ┌──────────┐
 │ Hospital │◆─────────────────│ Department │─────────────────────│  Doctor  │
 │──────────│                  │────────────│                     │──────────│
 │ name     │                  │ name       │                     │ name     │
 └──────────┘                  └────────────┘                     │ specialty│
                                                                  └────┬─────┘
                                                                     1 │ Attends ▼
 ┌──────────┐ 1   Books  ▶   * ┌──────────────┐ *                      │
 │ Patient  │──────────────────│ Appointment  │────────────────────────┘
 │──────────│                  │──────────────│
 │ name     │                  │ date         │
 │ phone    │                  │ timeSlot     │
 └──────────┘                  └──────┬───────┘
                                    1 │ Results-in ▼
                                 0..1 │
                               ┌──────────────┐ 1   Contains ▶  1..* ┌──────────────────┐  *   Is-for ▶  1 ┌──────────┐
                               │ Prescription │◆─────────────────────│ PrescriptionLine │───────────────────│ Medicine │
                               │──────────────│                      │──────────────────│                   │──────────│
                               │ dateIssued   │                      │ dosage           │                   │ name     │
                               └──────────────┘                      │ durationDays     │                   └──────────┘
                                                                     └──────────────────┘
```
Notes: Hospital ◆ Department (departments don't exist outside the hospital); Prescription ◆ PrescriptionLine; Medicine acts as a **description class**; no operations.
:::
:::

:::q E2 · A student modelled a library like this. Find at least four mistakes.
```text
┌──────────────────────────┐          ┌────────────────────────┐
│ Loan                     │          │ BookCopy               │
│──────────────────────────│          │────────────────────────│
│ memberId : int           │          │ title, author, isbn    │
│ copyId : int             │          │ status                 │
│ dueDate                  │          │────────────────────────│
│──────────────────────────│          │ + issue()              │
│ + calculateFine()        │          └────────────────────────┘
└──────────────────────────┘
   (no lines between the classes)            ┌──────────────┐
                                             │ LoanDatabase │
                                             └──────────────┘
```
:::ans
1. **Operations** (`calculateFine()`, `issue()`) don't belong in a domain model.
2. **Foreign-key attributes** `memberId`, `copyId` — relate classes with **associations** (Loan *Is-for* BookCopy, Member *Initiates* Loan) instead.
3. **Missing associations and multiplicities** (no lines).
4. `LoanDatabase` is a **software artifact**, not a domain concept.
5. `title, author, isbn` in BookCopy → should be in a **description class** `Book` (redundancy, information loss).
6. `Member` concept is missing entirely.
:::
:::

:::q E3 · For a "Payment" hierarchy with CashPayment, CardPayment and ChequePayment: (a) when is it justified to create these subclasses? (b) Should Payment be abstract? (c) Would "LargePayment" (amount > 10,000) be a good subclass?
:::ans
(a) Justified because each subclass has **additional attributes** (cardNumber, chequeNumber, amountTendered), **additional associations** (CardPayment–CreditCard, ChequePayment–Bank), and is **handled differently** (card needs authorization, cheque needs clearance). They satisfy the **100%** and **Is-a** rules.
(b) Yes — if every payment must be one of these kinds, Payment is an **abstract conceptual class** (italic name).
(c) Usually **no** — unless large payments have different attributes/associations or are processed differently (e.g. need manager approval). Otherwise it's just an attribute value condition, not a meaningful subclass.
:::
:::

## Section F · Long Answer

:::q F1 · Explain the Unified Process in detail: characteristics, phases, disciplines, artifacts and best practices. Contrast with waterfall.
:::ans
Structure: (1) definition & characteristics — iterative, incremental, use-case driven, architecture-centric, risk-driven, timeboxed iterations of 2–6 weeks; (2) phase diagram + four phases with goals ([Lesson 7.2](07_2_unified_process.html)); (3) disciplines table + effort chart ([Lesson 7.2](07_2_unified_process.html)); (4) key artifacts per discipline: Domain Model, Use-Case Model, Vision, Supplementary Specification, Glossary, Design Model, SAD, Data Model, Implementation Model, Test Model, SW Development Plan; (5) best practices list ([Lesson 7.2](07_2_unified_process.html)); (6) waterfall vs iterative table ([Lesson 7.2](07_2_unified_process.html)); (7) the warning: inception ≠ requirements, elaboration ≠ design.
:::
:::

:::q F2 · What is a domain model? Explain how conceptual classes, associations and attributes are identified, with an example.
:::ans
Definition and purpose (lower representational gap, visual dictionary). Three strategies to find conceptual classes (reuse models, category list with table, noun phrase analysis with an example text and filtering). Mapmaker principle and attribute-vs-class guideline. Description classes. Associations: need-to-remember, naming format, multiplicity, common associations list. Attributes: simple types, data type classes, no foreign keys, derived attributes. Finish with a drawn domain model (e.g. the library model in [Lesson 10.3](10_3_associations_attributes.html)).
:::
:::

:::q F3 · Explain use case modelling: actors, scenarios, formats, the fully dressed template and how use cases are related (include, extend, generalization), with a diagram.
:::ans
Definitions; actor types table; formats (brief, casual, fully dressed); fully dressed template sections with a short example (Issue Book or Withdraw Cash); guidelines (essential/black-box style, actor-goal perspective); how to find use cases + EBP/Boss/Size tests; diagram notation; include/extend/generalization comparison table + diagram with correct arrow directions; when to use use cases.
:::
:::
