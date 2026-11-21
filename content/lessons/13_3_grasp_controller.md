**The Controller pattern decides which object first receives a request coming from the user interface. Low Coupling and High Cohesion are the yardsticks used to choose between design alternatives.** This lesson also summarises the other four GRASP patterns.

## Pattern 3: Controller

### The problem

The librarian clicks "Issue" on the screen. The UI code (a window or web page) receives the click. Where should the **business logic** go? If the window itself checks loan limits, creates loans and updates copies:
- the logic is **trapped in the UI** — you can't reuse it from a mobile app, a kiosk or a test,
- the window class becomes a bloated mix of screen code and business rules (low cohesion).

### The solution

| | |
|---|---|
| **Problem** | What first object **beyond the UI layer** receives and coordinates ("controls") a **system operation**? |
| **Solution** | Assign the responsibility to a class representing **one** of: **(1) Facade controller** — the overall **system**, a **root object**, a **device** the software runs in, or a major **subsystem** (e.g. `Library`, `Register`, `ATM`). **(2) Use case / session controller** — a class representing the **use case scenario**, named `<UseCaseName>Handler`, `…Coordinator` or `…Session` (e.g. `IssueBookHandler`, `ProcessSaleHandler`). Use the same controller for all system events of one use case. |

**Key rule:** UI objects should **not** handle system events — they just **forward** them. And the controller itself does little work: it **delegates** to domain objects.

:::analogy
A **hotel reception desk**. Guests (the UI) don't walk into the kitchen or the laundry; they tell reception. Reception doesn't cook or wash either — it **coordinates**, forwarding each request to the right department. If one receptionist tried to also cook and clean, they'd be a "bloated controller".
:::

### In code

```cpp
#include <iostream>
#include <string>
using namespace std;

class Member                                  // domain object
{
    string name;
    int loans = 0;
public:
    Member(const string &n) : name(n) { }
    bool canBorrow() const { return loans < 2; }
    void addLoan() { loans++; }
    string getName() const { return name; }
};

class IssueBookHandler                        // USE CASE CONTROLLER for "Issue Book"
{
    Member *current = nullptr;
public:
    void startIssue(Member *m) { current = m; }          // system operation 1
    string enterCopy(const string &title)                // system operation 2
    {
        if (current == nullptr) return "error: start a session first";   // checks legal order
        if (!current->canBorrow()) return "error: loan limit reached";   // delegates the rule
        current->addLoan();                                              // delegates the work
        return title + " issued to " + current->getName();
    }
    void endIssue() { current = nullptr; }                // system operation 3
};

class ConsoleUI                               // UI: no business logic, only forwards
{
    IssueBookHandler &controller;
public:
    ConsoleUI(IssueBookHandler &c) : controller(c) { }
    void onScan(const string &title) { cout << controller.enterCopy(title) << endl; }
};

int main()
{
    Member asha("Asha");
    IssueBookHandler handler;
    ConsoleUI ui(handler);
    ui.onScan("Clean Code");          // before startIssue → wrong order
    handler.startIssue(&asha);
    ui.onScan("Clean Code");
    ui.onScan("Refactoring");
    ui.onScan("UML Distilled");       // limit is 2
    handler.endIssue();
    return 0;
}
```

```output
error: start a session first
Clean Code issued to Asha
Refactoring issued to Asha
error: loan limit reached
```

**Benefits:** the same domain logic can be driven by any UI (console, web, mobile, tests) — **pluggable interfaces**; and the controller can check that system operations happen in a **legal order**.

**Bloated controller (a warning sign):** one controller receives *all* system events of *all* use cases, or does the work itself instead of delegating, and has lots of attributes. **Cure:** use **use case controllers** (one per use case) and make them **delegate**.

| Facade controller | Use case controller |
|---|---|
| One class for the whole system/subsystem (`Library`, `Register`) | One class per use case (`IssueBookHandler`) |
| Fine when there are few system events | Better when there are many events — avoids bloat |

## Pattern 4: Low Coupling

| | |
|---|---|
| **Problem** | How to support **low dependency, low change impact and increased reuse**? |
| **Solution** | Assign responsibilities so that **coupling remains low**. Use this principle to **evaluate alternatives**. |

**Larman's classic example:** "create a Payment and associate it with the Sale".
- **Design 1:** `Register` creates the `Payment`, then passes it to `Sale` → Register is coupled to Payment **and** Sale is coupled to Payment.
- **Design 2:** `Register` calls `sale.makePayment(cash)` and **Sale creates the Payment** → Register doesn't need to know about Payment at all.
- Design 2 has **fewer couplings** → preferred.

Library equivalent: the `IssueBookHandler` calls `member.addLoan(copy)` and the **Member** creates the Loan — the handler never needs to know the `Loan` class.

**Contraindication:** coupling to **stable** elements (the standard library) is fine; don't chase low coupling at the cost of everything else.

## Pattern 5: High Cohesion

| | |
|---|---|
| **Problem** | How to keep objects **focused, understandable and manageable** (and, as a side effect, support Low Coupling)? |
| **Solution** | Assign responsibilities so that **cohesion remains high**. Use this to evaluate alternatives. |

In Design 1 above, the `Register` also takes on payment creation — one more unrelated job. As more system operations are added, Register would bloat → low cohesion. Design 2 keeps Register focused. Low coupling and high cohesion usually point to the **same** design. (Theory and cohesion levels: [Lesson 13.1](13_1_coupling_cohesion.html).)

## The Other Four GRASP Patterns (Brief)

| Pattern | Problem | Solution | Example |
|---|---|---|---|
| **Polymorphism** | How to handle behaviour that varies by type? | Use polymorphic operations (virtual functions) instead of `if/switch` on type | `Payment::authorize()` overridden by Card/UPI |
| **Pure Fabrication** | Expert would hurt cohesion/coupling — who then? | Invent an artificial, highly cohesive class that's not a domain concept | `LoanRepository` saves loans (instead of Loan saving itself) |
| **Indirection** | How to avoid direct coupling between two things? | Put an intermediate object between them | an Adapter between the domain and a payment API |
| **Protected Variations** | How to stop changes in one part from rippling? | Wrap points of likely change behind a stable interface | `PaymentGateway` interface so providers can change |

Protected Variations is the deep idea behind most design patterns (Chapter 14).

:::key
- **Controller:** first non-UI object to receive a system operation — facade (system/root/device/subsystem) or use case controller (`XxxHandler`); it delegates. Avoid bloated controllers.
- **Low Coupling:** prefer designs with fewer dependencies (Sale creates Payment, not Register).
- **High Cohesion:** keep each class focused.
- Others: Polymorphism, Pure Fabrication, Indirection, Protected Variations.
:::

:::mistakes
- Making a UI window the controller and putting business rules in it.
- One giant controller for everything that also does the work.
- Confusing GRASP Controller with MVC's controller — related idea, but GRASP Controller is specifically the first **domain-layer** object receiving a system operation.
- Thinking Low Coupling and High Cohesion are separate "objects" you create — they're **evaluation principles**.
:::

:::exam
- *"Explain the Controller pattern. Differentiate facade and use case controllers. What is a bloated controller?"*
- *"Explain Low Coupling and High Cohesion with an example."* → Register/Sale/Payment.
- *"List all nine GRASP patterns."*
:::

:::def
**Controller:** assign the responsibility of receiving or handling a system event to a non-UI class that represents the overall system, a root object, a device or a subsystem (facade controller), or a use case scenario (use case/session controller). **Low Coupling:** assign responsibilities so that unnecessary coupling remains low. **High Cohesion:** assign responsibilities so that cohesion remains high.
:::

## Quick Check

:::q Q1 · Which is the better controller for "Process Sale" in a large POS system: `SaleWindow`, `ProcessSaleHandler`, or `Database`?
:::ans
**`ProcessSaleHandler`** — a use case controller. The window is UI, and Database is a technical service.
:::
:::

:::q Q2 · Why does "Sale creates Payment" give lower coupling than "Register creates Payment"?
:::ans
Sale must know Payment anyway (it's associated with it). If Register created it, Register would also need to know Payment — an extra, avoidable dependency.
:::
:::
