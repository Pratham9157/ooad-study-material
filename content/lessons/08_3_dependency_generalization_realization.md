**Dependency means "uses for a moment". Generalization means "is a kind of" (inheritance). Realization means "promises to do what an interface says".** With these three, you'll know all six UML class relationships.

## 1. Dependency — "uses temporarily"

### The problem

A `ReportPrinter` needs a `Formatter` only while printing — it receives one as a parameter, uses it, and forgets it. It doesn't *keep* a formatter, so it's not an association. But it still **depends** on it: if `Formatter`'s interface changes, `ReportPrinter` may break. We want to show that weaker link.

:::analogy
You **use a taxi** to get to college. You depend on it for that trip, but you don't own it or keep it — tomorrow you might use a different one. That's a dependency. Owning your own bike would be an association.
:::

**Dependency** = one class **uses** another temporarily: as a **parameter**, a **local variable**, a **return type**, or by calling its **static** method. A change in the supplier may affect the client.
**UML:** a **dashed arrow** pointing from the user (client) to the used class (supplier).

```text
   ┌──────────────┐                    ┌────────┐
   │ FineCalculator│- - - - - - - - - ->│  Date  │    FineCalculator uses Date only as a parameter
   └──────────────┘                    └────────┘
```

## 2. Generalization — "is a kind of"

**Generalization** is the UML name for **inheritance** (Chapter 5): a general class (parent) and a more specific class (child). The child **is a** parent.
**UML:** a **solid line with a hollow triangle** pointing **to the parent**.

```text
   ┌──────────┐            ┌──────────┐
   │Librarian │───────────▷│  Staff   │       Librarian IS-A Staff
   └──────────┘            └──────────┘
```

## 3. Realization — "implements"

**Realization** is the relationship between an **interface** (a contract: only pure virtual functions, Lesson 5.5) and a class that **implements** it.
**UML:** a **dashed line with a hollow triangle** pointing **to the interface**, which is marked `«interface»`.

```text
   ┌─────────────┐            ┌──────────────┐
   │ CardPayment │- - - - - -▷│ «interface»  │      CardPayment implements Payable
   └─────────────┘            │   Payable    │
                              └──────────────┘
```

:::analogy
An interface is like a **job description**: "must be able to pay(amount)". CardPayment and UPIPayment are **employees who fulfil** that job description in their own way. That's realization. Generalization, by contrast, is family inheritance: a child really *is* a kind of the parent and inherits its traits.
:::

## All Three in C++

```cpp
#include <iostream>
using namespace std;

class Date                                    // used for DEPENDENCY
{
public:
    int day;
    Date(int d) : day(d) { }
};

class FineCalculator
{
public:
    int fine(int dueDay, const Date &today) const   // Date only as a parameter → dependency
    {
        return today.day > dueDay ? (today.day - dueDay) * 5 : 0;
    }
};

class Staff                                   // GENERALIZATION parent
{
public:
    virtual void role() const { cout << "Staff" << endl; }
    virtual ~Staff() { }
};
class Librarian : public Staff                // Librarian ──▷ Staff
{
public:
    void role() const override { cout << "Librarian" << endl; }
};

class Payable                                 // an INTERFACE (only pure virtual functions)
{
public:
    virtual void pay(int amount) = 0;
    virtual ~Payable() { }
};
class CardPayment : public Payable            // REALIZATION: CardPayment - - -▷ Payable
{
public:
    void pay(int amount) override { cout << "Paid Rs " << amount << " by card" << endl; }
};

int main()
{
    FineCalculator calc;
    cout << "Fine: " << calc.fine(10, Date(14)) << endl;

    Librarian l;
    Staff &s = l;
    s.role();

    CardPayment card;
    Payable &p = card;
    p.pay(20);
    return 0;
}
```

```output
Fine: 20
Librarian
Paid Rs 20 by card
```

## The Complete Cheat Sheet: All Six Relationships

<<SVG:relationships>>

| Relationship | Meaning | Line | End symbol | C++ |
|---|---|---|---|---|
| **Dependency** | uses temporarily | dashed | open arrow → supplier | parameter, local, return type |
| **Association** | knows / connected | solid | none (or open arrow for navigability) | pointer/reference member |
| **Aggregation** | has (weak whole–part) | solid | hollow diamond ◇ at whole | pointer to external part |
| **Composition** | made of (strong whole–part) | solid | filled diamond ◆ at whole | member object |
| **Generalization** | is a | solid | hollow triangle ▷ at parent | `class Child : public Parent` |
| **Realization** | implements | dashed | hollow triangle ▷ at interface | inherit from a pure-abstract class |

**From weakest to strongest coupling:** dependency < association < aggregation < composition < generalization.

:::key
- Dependency: dashed arrow; temporary use (parameter/local/return).
- Generalization: solid line + hollow triangle to the parent (inheritance, is-a).
- Realization: dashed line + hollow triangle to the interface (implements).
- Learn the six symbols — they appear in almost every Part II exam question.
:::

:::mistakes
- Generalization (solid) vs realization (dashed) — mixing up the line style.
- Pointing the triangle at the child — it always points **to the parent/interface**.
- Drawing an association when a class only uses another as a parameter — that's a dependency.
:::

:::exam
- *"Explain the relationships between classes in UML with notation and examples."* → the cheat sheet table + drawings.
- *"Identify the relationship"* in code: member object → composition; pointer member → association/aggregation; parameter → dependency; `: public` → generalization; implementing a pure-abstract class → realization.
:::

:::def
A **dependency** is a using relationship in which a change to one class (the supplier) may affect another (the client) that uses it temporarily; shown as a dashed arrow. **Generalization** is a taxonomic "is-a" relationship between a general class and a more specific class (inheritance); shown as a solid line with a hollow triangle pointing to the general class. **Realization** is the relationship between an interface and a class that implements it; shown as a dashed line with a hollow triangle pointing to the interface.
:::

## Quick Check

:::q Q1 · Which relationship does each line of code show? (a) `class Car { Engine e; };` (b) `void Printer::print(const Report &r)` (c) `class Dog : public Animal` (d) `class Car { Driver *driver; };`
:::ans
(a) **Composition**, (b) **Dependency**, (c) **Generalization**, (d) **Association/aggregation**.
:::
:::

:::q Q2 · Describe the UML symbol for realization.
:::ans
A **dashed line** with a **hollow triangle** pointing to the interface (marked «interface»).
:::
:::
