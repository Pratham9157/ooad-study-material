**Patterns are most useful together. This final lesson shows how to choose and combine GoF patterns in one system, and how to turn finished design diagrams into C++ code.** It brings the whole course together.

## Part 1 — Applying GoF Patterns

### How to choose a pattern

1. **Find the point of change** — what is likely to vary? (A payment provider? A fine rule? Who needs notifications?) — GRASP *Protected Variations*.
2. **Match the problem to a pattern's intent** (learn the one-line intents!).
3. **Apply it** with interfaces + polymorphism.
4. **Check** the result with GRASP: lower coupling? higher cohesion?

| Design problem in the library | Pattern | How |
|---|---|---|
| Several payment providers with different APIs | **Adapter** | `QuickPayAdapter`, `BankUpiAdapter` implement `PaymentGateway` |
| Who creates the right adapter / strategy (based on config)? | **(Simple) Factory** — a Pure Fabrication | `ServicesFactory` |
| Exactly one factory, reachable from anywhere | **Singleton** | `ServicesFactory::getInstance()` |
| Different fine policies | **Strategy** | a `Loan` delegates to a `FineStrategy` |
| Waiting members / displays must hear about returns | **Observer** | `BookTitle` notifies observers |
| Notice types × delivery channels | **Bridge** | `Notice` holds a `Channel` |
| Reminders created by subclass-specific services | **Factory Method** | `ReminderService::createReminder()` |

This is the same reasoning Larman uses for his POS case study: **Adapter** for external tax/accounting services, a **Factory** to create the adapters, **Singleton** to access the factory, **Strategy** for pricing (with **Composite** to combine several pricing rules), **Facade** for a rules engine, and **Observer** to refresh the UI when the sale changes.

### Four patterns cooperating

```cpp
#include <iostream>
#include <string>
using namespace std;

// ---------- Strategy ----------
class FineStrategy
{
public:
    virtual int fine(int lateDays) const = 0;
    virtual ~FineStrategy() { }
};
class StandardFine : public FineStrategy { public: int fine(int d) const override { return d * 5; } };
class StudentFine  : public FineStrategy { public: int fine(int d) const override { return d * 2; } };

// ---------- Adapter ----------
class PaymentGateway
{
public:
    virtual bool pay(int rupees) = 0;
    virtual ~PaymentGateway() { }
};
class QuickPayAPI { public: int makeTxn(long paise) { cout << "QuickPay " << paise << " paise" << endl; return 200; } };
class QuickPayAdapter : public PaymentGateway
{
    QuickPayAPI api;
public:
    bool pay(int rupees) override { return api.makeTxn(rupees * 100L) == 200; }
};

// ---------- Simple Factory + Singleton ----------
class ServicesFactory
{
    StandardFine standard;
    StudentFine student;
    QuickPayAdapter gateway;
    ServicesFactory() { }
public:
    static ServicesFactory& getInstance() { static ServicesFactory f; return f; }
    const FineStrategy& fineStrategyFor(const string &memberType) const
    {
        if (memberType == "student") return student;       // selection logic lives in ONE place
        return standard;
    }
    PaymentGateway& paymentGateway() { return gateway; }
};

// ---------- Controller (GRASP) ----------
class ReturnBookHandler
{
public:
    void returnCopy(const string &memberType, int lateDays)
    {
        ServicesFactory &f = ServicesFactory::getInstance();
        int amount = f.fineStrategyFor(memberType).fine(lateDays);
        cout << memberType << " owes Rs " << amount << endl;
        if (amount > 0 && f.paymentGateway().pay(amount)) cout << "paid" << endl;
    }
};

int main()
{
    ReturnBookHandler h;
    h.returnCopy("student", 4);
    h.returnCopy("regular", 0);
    return 0;
}
```

```output
student owes Rs 8
QuickPay 800 paise
paid
regular owes Rs 0
```

The controller knows **nothing** about QuickPay or the individual fine rules — change the provider or add a rule, and `ReturnBookHandler` stays the same.

## Part 2 — Mapping Designs to Code

### The problem

You've finished the **design class diagrams (DCDs)** and **sequence diagrams**. How do you turn them into code systematically, rather than "just start typing"?

:::analogy
The design is the **architect's blueprint**; coding is **construction**. Each symbol in the blueprint (a wall, a door) maps to a specific construction task. Likewise each UML element maps to a specific C++ construct.
:::

### The mapping rules (Larman)

**From the DCD → class definitions**
- Each design class → a C++ `class` with the same name.
- Attributes → data members (with their types and visibility).
- Operation signatures → member function declarations.
- `create(...)` messages → constructors.
- A **navigable association** A → B → a **reference attribute** in A (pointer/reference to B); the **role name** becomes the **attribute name**.
- Generalization → inheritance; realization → inheriting from a pure-abstract class.

**From interaction diagrams → method bodies**
- The **sequence of messages** inside an activation = the **sequence of statements** in that method.
- Message `m()` sent to `b` from inside `A::x()` → `b->m();` inside `A::x()`.
- `create` → `new`; `loop` frame → `for`/`while`; `alt`/`opt` → `if`.

**One-to-many associations → collections**
- `Member 1 ──► * Loan` → `vector<Loan*> loans;` in `Member` (or `vector<Loan>` for composition).

**Errors** — design error handling (exceptions or error codes) along with the methods.

**Order of implementation** — from **least-coupled** to **most-coupled** classes: classes that depend on nothing (e.g. `BookCopy`) first, then those that use them (`Loan`, then `Member`), and the controller last. Each can be compiled and **tested** as soon as it's written. Larman recommends **test-first (test-driven) development**.

### Worked example: DCD + interaction diagram → C++

```text
 Design Class Diagram (part)
 ┌──────────────────────────┐ 1     loans  * ┌──────────────────────┐ *     copy  1 ┌──────────────────────┐
 │ Member                   │───────────────►│ Loan                 │──────────────►│ BookCopy             │
 │ - name : string          │                │ - dueDay : int       │               │ - copyId : string    │
 │ + addLoan(c : BookCopy*, │                │ + Loan(c, due)       │               │ - available : bool   │
 │      today : int) : int  │                │ + getDueDay() : int  │               │ + markIssued()       │
 │ + loanCount() : int      │                └──────────────────────┘               │ + isAvailable():bool │
 └──────────────────────────┘                                                       └──────────────────────┘
 Interaction for addLoan(c, today):
   m : Member ──1: create(c, today+14)──► :Loan ──1.1: markIssued()──► c : BookCopy
```

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class BookCopy                           // least coupled: depends on nothing → written first
{
    string copyId;                       // - copyId : string
    bool available = true;               // - available : bool
public:
    BookCopy(const string &id) : copyId(id) { }
    void markIssued() { available = false; }          // + markIssued()
    bool isAvailable() const { return available; }    // + isAvailable() : bool
};

class Loan                               // depends on BookCopy
{
    BookCopy *copy;                      // role name "copy" → attribute name
    int dueDay;
public:
    Loan(BookCopy *c, int due) : copy(c), dueDay(due)  // from the create(c, today+14) message
    {
        copy->markIssued();                            // message 1.1: markIssued()
    }
    int getDueDay() const { return dueDay; }
};

class Member                             // depends on Loan
{
    string name;
    vector<Loan*> loans;                 // one-to-many "loans" → collection attribute
public:
    Member(const string &n) : name(n) { }
    int addLoan(BookCopy *c, int today)
    {
        Loan *l = new Loan(c, today + 14);             // message 1: create(c, today+14)
        loans.push_back(l);
        return l->getDueDay();
    }
    int loanCount() const { return (int)loans.size(); }
    ~Member() { for (Loan *l : loans) delete l; }      // Member owns its Loans
};

int main()                               // a small "test-first" style check
{
    BookCopy c1("C-1"), c2("C-2");
    Member m("Asha");
    int due = m.addLoan(&c1, 10);
    cout << "due day " << due << ", loans " << m.loanCount()
         << ", c1 available " << c1.isAvailable() << ", c2 available " << c2.isAvailable() << endl;
    return 0;
}
```

```output
due day 24, loans 1, c1 available 0, c2 available 1
```

## The Whole Course in One Picture

```text
 Use cases (9) ─► Domain model (10) ─► SSD & system operations (11.1) ─► Sequence diagrams (11.2)
                                                                             │  assign responsibilities
                                                                             ▼  with GRASP (13)
                                    C++ code (Part I) ◄─ mapping (14.8) ◄─ Design class diagrams (10.1)
                                                                             + GoF patterns (14)
```

:::key
- Choose patterns by spotting what varies and matching the problem to a pattern's intent; patterns often combine (Adapter + Factory + Singleton + Strategy).
- DCD → class definitions (attributes, method signatures, reference attributes from navigable associations, role names).
- Interaction diagrams → method bodies (message order = statement order).
- One-to-many → collections. Implement least-coupled classes first; test as you go.
:::

:::mistakes
- Forcing patterns where nothing varies.
- Using a single pointer for a "many" association (needs a collection).
- Adding pointers in both directions when the DCD shows one-way navigability.
- Coding the controller first — it can't compile until its collaborators exist.
:::

:::exam
- *"Explain how GoF patterns are applied in a case study (e.g. POS/library)."* → the table + reasoning.
- *"Explain mapping designs to code with an example."* → the rules + DCD/interaction → C++ example.
:::

:::def
**Mapping designs to code** is the process of translating the design model into source code: design class diagrams provide class definitions (attributes, method signatures and reference attributes derived from navigable associations), interaction diagrams provide the sequence of statements in method bodies, one-to-many associations become collections, and classes are implemented from least-coupled to most-coupled.
:::

## Quick Check

:::q Q1 · A DCD shows `Order 1 ──► * OrderLine` with role name `lines`. What member does `Order` get?
:::ans
A collection attribute named after the role: e.g. `vector<OrderLine*> lines;` (or `vector<OrderLine> lines;` since it's typically composition).
:::
:::

:::q Q2 · Which class would you implement first among `Controller`, `Customer`, `Address` (Customer has an Address; Controller uses Customer)?
:::ans
**Address** (least coupled), then **Customer**, then **Controller**.
:::
:::
