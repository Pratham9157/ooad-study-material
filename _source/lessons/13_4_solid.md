**SOLID is a set of five design principles for writing classes that are easy to change and extend. It isn't in your syllabus by name, but it overlaps heavily with GRASP and explains *why* design patterns work — useful for long answers and viva.**

## Why Learn SOLID?

GRASP tells you *who* should do what. SOLID gives five short rules that keep designs flexible as requirements change. Each one connects to something you've already learned.

| Letter | Principle | One-line meaning | Connected to |
|---|---|---|---|
| **S** | Single Responsibility | a class should have **one reason to change** | High Cohesion |
| **O** | Open/Closed | open for **extension**, closed for **modification** | Polymorphism, Protected Variations, Strategy |
| **L** | Liskov Substitution | a child must be usable **anywhere** its parent is expected | 100% & Is-a rules |
| **I** | Interface Segregation | many small, specific interfaces beat one fat interface | High Cohesion |
| **D** | Dependency Inversion | depend on **abstractions** (interfaces), not concrete classes | Low Coupling, Adapter, Bridge |

## S — Single Responsibility Principle

A class should have **only one reason to change**. The "LibraryManager" god class from Lesson 13.1 changes if the fine rules change, if the HTML layout changes, *and* if the email provider changes — three reasons. Split it.

:::analogy
A Swiss-army knife is handy, but if the scissors break, the whole tool goes for repair. Separate tools each have one job and one reason to be replaced.
:::

## O — Open/Closed Principle

You should be able to **add** new behaviour **without editing** existing, tested code. Instead of a growing `switch` on fine types, use a `FineStrategy` interface; a new rule is a new class (Strategy pattern, Lesson 14.6).

```cpp
#include <iostream>
using namespace std;

class FineRule                                  // abstraction: closed for modification
{
public:
    virtual int fine(int lateDays) const = 0;
    virtual ~FineRule() { }
};
class StandardRule : public FineRule { public: int fine(int d) const override { return d * 5; } };
class StudentRule  : public FineRule { public: int fine(int d) const override { return d * 2; } };
// tomorrow: class SeniorRule : public FineRule {...}  — added WITHOUT touching the code below

int charge(const FineRule &rule, int days) { return rule.fine(days); }   // never needs editing

int main()
{
    StandardRule s; StudentRule st;
    cout << charge(s, 4) << " " << charge(st, 4) << endl;
    return 0;
}
```

```output
20 8
```

## L — Liskov Substitution Principle

If `Child` inherits from `Parent`, then code written for `Parent` must still work correctly when given a `Child`. A child must **not break the parent's promises**.
Classic violation: `Square` inheriting from `Rectangle` — code that sets width and height independently gets surprised when a square changes both. If a subclass can't honour the parent's behaviour, inheritance is the wrong tool. (Compare the domain model's **100% rule**.)

## I — Interface Segregation Principle

Don't force classes to implement methods they don't need. Instead of one big `LibraryMachine` interface with `scan()`, `print()` and `acceptCash()`, define `Scanner`, `Printer`, `CashAcceptor` — a self-issue kiosk implements only what it supports.

## D — Dependency Inversion Principle

High-level code (business rules) should depend on **abstractions**, not on concrete low-level classes. `FineCollector` should depend on a `PaymentGateway` interface, not directly on `QuickPayAPI`; then the provider can change (Adapter pattern, Lesson 14.4). This is how you achieve **low coupling** in practice.

:::key
- SRP: one reason to change (≈ High Cohesion).
- OCP: extend by adding classes, not by editing old ones (≈ Polymorphism/Protected Variations).
- LSP: subclasses must be fully substitutable for their parents (≈ 100% rule).
- ISP: small, specific interfaces.
- DIP: depend on interfaces, not concrete classes (≈ Low Coupling).
:::

:::mistakes
- Treating SOLID as GRASP replacements in a GRASP question — answer GRASP questions with GRASP terms; mention SOLID only as extra support.
- Thinking OCP means "never change code" — it means *new behaviour* should arrive as *new code*, not edits to stable code.
:::

:::exam
- Not a syllabus heading, but excellent support for *"what makes a good design?"* or *"explain the benefits of the Strategy/Adapter pattern"* answers. A viva favourite.
:::

:::def
**SOLID** is an acronym for five object-oriented design principles: Single Responsibility (a class should have one reason to change), Open/Closed (open for extension, closed for modification), Liskov Substitution (subtypes must be substitutable for their base types), Interface Segregation (clients should not depend on methods they do not use) and Dependency Inversion (depend on abstractions, not concretions).
:::

## Quick Check

:::q Q1 · Adding a new payment type requires editing a 200-line `switch` in `PaymentProcessor`. Which principle is violated, and what's the fix?
:::ans
**Open/Closed** (and SRP). Fix: a `Payment` interface with one class per payment type (polymorphism/Strategy); new types are added as new classes.
:::
:::
