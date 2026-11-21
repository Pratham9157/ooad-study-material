**GRASP is a set of nine principles (by Craig Larman) that help you decide *which class should do what*. The two most fundamental are Information Expert ("give the job to the class that has the information") and Creator ("let the class that contains or records objects create them").**

## The Problem: Where Should This Code Go?

You're designing the library. Three questions come up immediately:
- Who should calculate a member's **total fine**?
- Who should create a new **Loan** object?
- Who should receive the librarian's "issue this copy" request?

Put the code in the wrong class and you get god classes, tangled dependencies and duplicated logic (Lesson 13.1). **GRASP** gives proven answers.

## Responsibilities: Doing and Knowing

A **responsibility** is an obligation of a class — something it must **do** or **know**:

| Doing | Knowing |
|---|---|
| doing something itself (create an object, calculate) | knowing its own private data |
| starting actions in other objects | knowing related objects |
| controlling/coordinating other objects | knowing things it can derive or calculate |
| *a Member creates a Loan; a Loan calculates its fine* | *a Loan knows its due date; a Member knows its loans* |

You assign responsibilities while drawing **interaction diagrams**: every message arrow you draw gives a responsibility to the receiving class. This approach is called **Responsibility-Driven Design (RDD)**.

A **pattern** is a **named problem/solution pair** that can be applied in new situations, with advice on how to apply it and its trade-offs. **GRASP** = **General Responsibility Assignment Software Patterns**. The nine: **Information Expert, Creator, Controller, Low Coupling, High Cohesion**, Polymorphism, Pure Fabrication, Indirection, Protected Variations. Your syllabus focuses on the first five.

## Pattern 1: Information Expert

| | |
|---|---|
| **Problem** | What is a general principle for assigning responsibilities to objects? |
| **Solution** | Assign the responsibility to the **information expert** — the class that **has the information** needed to fulfil it. |

:::analogy
In an office, if you need to know the leave balance of an employee, you ask **HR**, because HR keeps those records — not the canteen. Give each question to whoever **already has the information**.
:::

**Library example — "Who calculates a member's total fine?"**
- To know the *total*, you need all of the member's loans → **Member** knows its loans → `Member::totalFine()`.
- To know each loan's fine, you need its due and return dates → **Loan** knows them → `Loan::fine()`.

**Larman's POS example:** `Sale::getTotal()` (Sale knows its line items) → `SalesLineItem::getSubtotal()` (knows quantity) → `ProductDescription::getPrice()` (knows price). Responsibility is spread to wherever the data lives.

```text
  :FineHandler          m : Member                  :Loan[i]
       │ t := totalFine()   │                            │
       │───────────────────►│   loop [for each loan]     │
       │                    │── f := fine() ────────────►│    each object computes what
       │                    │◄ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│    it has the information for
       │◄ ─ ─ ─ ─ ─ t ─ ─ ─ ─│                            │
```

**Contraindication:** don't follow Expert blindly if it hurts coupling/cohesion — e.g. should a `Loan` save *itself* to the database because it has the data? No — that would mix database code into a domain class (low cohesion, coupling to DB libraries). Use a separate persistence class.

**Benefits:** information stays **encapsulated**; behaviour is **distributed** across lightweight, focused classes.

## Pattern 2: Creator

| | |
|---|---|
| **Problem** | Who should be responsible for **creating a new instance** of class A? |
| **Solution** | Assign class **B** the responsibility to create A if **one or more** of these is true (the more, the better): **(1)** B **contains or compositely aggregates** A; **(2)** B **records** A; **(3)** B **closely uses** A; **(4)** B **has the initializing data** for A. Prefer the class that contains/aggregates A. |

:::analogy
A **notebook factory binds its own pages** — the notebook contains the pages, so it makes sense for it to create them. You wouldn't ask the pen shop to make the notebook's pages.
:::

**Library example — "Who creates a Loan?"** A `Member` **records** its loans (keeps a list) and **has the initializing data** (itself + the copy) → **Member creates Loan**.
**POS example:** `Sale` **contains** `SalesLineItem`s → **Sale creates SalesLineItem**. `Book` ◆ `Chapter` → Book creates Chapter.

**Contraindication:** if creation is **complex** (choosing among several classes, recycling objects for performance), delegate to a **Factory** (Lesson 14.2).

**Benefit:** **low coupling** — B is already connected to A, so creating it adds no new dependency.

## Expert + Creator in Code

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Loan
{
    string title;
    int dueDay, returnDay;
public:
    Loan(const string &t, int due, int ret) : title(t), dueDay(due), returnDay(ret) { }
    int fine() const                           // EXPERT: Loan knows its own dates
    {
        int late = returnDay - dueDay;
        return late > 0 ? late * 5 : 0;        // Rs 5 per late day
    }
};

class Member
{
    string name;
    vector<Loan> loans;                        // Member records its Loans
public:
    Member(const string &n) : name(n) { }
    void addLoan(const string &title, int due, int ret)
    {
        loans.push_back(Loan(title, due, ret)); // CREATOR: Member creates Loan
    }
    int totalFine() const                      // EXPERT: Member knows all its loans
    {
        int total = 0;
        for (const Loan &l : loans) total += l.fine();   // delegate the per-loan part
        return total;
    }
};

int main()
{
    Member m("Asha");
    m.addLoan("Clean Code", 10, 14);           // 4 days late
    m.addLoan("Refactoring", 12, 11);          // on time
    m.addLoan("UML Distilled", 5, 8);          // 3 days late
    cout << "Total fine: Rs " << m.totalFine() << endl;
    return 0;
}
```

```output
Total fine: Rs 35
```

:::key
- Responsibilities = doing + knowing; assigned while drawing interaction diagrams.
- **Expert:** give the job to the class with the information (Loan.fine, Member.totalFine, Sale.getTotal).
- **Creator:** B creates A if B contains/aggregates, records, closely uses, or has the data for A (Member creates Loan, Sale creates SalesLineItem).
- Both lead to low coupling and high cohesion; watch the contraindications.
:::

:::mistakes
- Putting `calculateFine()` in the UI or a controller that has to pull data out of loans — the **Loan** is the expert.
- Letting an unrelated class (e.g. the controller) create objects it doesn't contain, adding coupling.
- Applying Expert to persistence (domain objects saving themselves in SQL).
:::

:::exam
- *"What is GRASP? Explain Information Expert and Creator with examples."* — state Problem/Solution exactly, give the Sale/SalesLineItem or Member/Loan example, draw a small sequence diagram.
:::

:::def
**GRASP** (General Responsibility Assignment Software Patterns) is a set of principles for assigning responsibilities to classes. **Information Expert:** assign a responsibility to the class that has the information necessary to fulfil it. **Creator:** assign class B the responsibility to create instances of class A if B contains or compositely aggregates A, records A, closely uses A, or has the initializing data for A.
:::

## Quick Check

:::q Q1 · In a shopping cart, who should calculate the cart total? Who should create a CartItem?
:::ans
**Cart** calculates the total (Expert — it knows its items, each item computes its subtotal). **Cart** creates CartItem (Creator — it contains them).
:::
:::

:::q Q2 · State the four conditions of the Creator pattern.
:::ans
B contains/compositely aggregates A; B records A; B closely uses A; B has the initializing data for A.
:::
:::
