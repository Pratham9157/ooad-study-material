**The Strategy pattern (behavioural) puts each version of an algorithm in its own class behind a common interface, so the algorithm can be chosen and swapped at run time.**

What varies: **the algorithm** (how a fine is calculated). What stays the same: **the code that uses it** (the Loan).

## 1. The Problem: Fine Rules Keep Changing

The library charges fines differently: standard members ₹5/day; students get 2 grace days then ₹2/day; senior citizens pay nothing. A first attempt:

```cpp
#include <iostream>
#include <string>
using namespace std;

class Loan
{
    int lateDays;
    string memberType;
public:
    Loan(int late, const string &type) : lateDays(late), memberType(type) { }
    int fine() const
    {
        if (memberType == "standard") return lateDays * 5;
        else if (memberType == "student") return lateDays > 2 ? (lateDays - 2) * 2 : 0;
        else if (memberType == "senior") return 0;
        return 0;        // and next month: "festival week waiver", "faculty rate"...
    }
};

int main()
{
    cout << Loan(5, "standard").fine() << " " << Loan(5, "student").fine() << endl;
    return 0;
}
```

```output
25 6
```

### What's wrong with this?

- **Violates Open/Closed:** every new rule means editing `Loan::fine()`.
- **Bloated conditional logic** that keeps growing.
- **Hard to test** each rule in isolation.
- **Low cohesion:** `Loan` now knows every pricing policy in the library.
- **String-based dispatch:** a typo like `"Student"` silently gives 0.

## 2. Understanding Strategy

> **GoF intent:** "Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it." (Also known as **Policy**.)

:::analogy
**Getting to the airport.** You can drive, take a cab, take the metro, or take the airport shuttle. The goal is the same; the *strategy* differs. You choose one based on time, budget or traffic — and you can switch at the last minute. The "trip" (context) doesn't change; only the travel strategy does.
:::

### Participants

```text
 ┌──────────────────────────┐   strategy   ┌────────────────────────────┐
 │ Loan  (Context)          │◇────────────►│ FineStrategy  (Strategy)   │
 │ - lateDays               │              │ + fine(days) = 0           │
 │ + setStrategy(s)         │              └─────────────△──────────────┘
 │ + report()  → delegates  │            ┌───────────────┼────────────────┐
 └──────────────────────────┘   ┌──────────────┐ ┌─────────────┐ ┌───────────────────┐
                                │ StandardFine │ │ StudentFine │ │ SeniorCitizenFine │
                                └──────────────┘ └─────────────┘ └───────────────────┘
                                                  (Concrete Strategies)
```

- **Strategy** — common interface for all algorithms (`FineStrategy`).
- **Concrete Strategies** — each algorithm in its own class.
- **Context** — holds a reference to a strategy and **delegates** the work to it (`Loan`). The context doesn't know or care which strategy it has.

## 3. How It Works

1. The client creates a Loan with a strategy (e.g. `StandardFine`).
2. When the fine is needed, the Loan calls `strategy->fine(lateDays)`.
3. Virtual dispatch runs the chosen algorithm.
4. The client can call `setStrategy(...)` at any time to switch.

## 4. Implementing It Step by Step

```cpp
#include <iostream>
#include <string>
using namespace std;

// STEP 1: the Strategy interface
class FineStrategy
{
public:
    virtual int fine(int lateDays) const = 0;
    virtual string name() const = 0;
    virtual ~FineStrategy() { }
};

// STEP 2: one class per algorithm
class StandardFine : public FineStrategy
{
public:
    int fine(int d) const override { return d * 5; }
    string name() const override { return "standard"; }
};
class StudentFine : public FineStrategy
{
public:
    int fine(int d) const override { return d > 2 ? (d - 2) * 2 : 0; }   // 2 grace days, Rs 2/day
    string name() const override { return "student"; }
};
class SeniorCitizenFine : public FineStrategy
{
public:
    int fine(int) const override { return 0; }                           // waived
    string name() const override { return "senior"; }
};

// STEP 3: the Context delegates to its current strategy
class Loan
{
    int lateDays;
    const FineStrategy *strategy;
public:
    Loan(int late, const FineStrategy *s) : lateDays(late), strategy(s) { }
    void setStrategy(const FineStrategy *s) { strategy = s; }            // swap at run time
    void report() const
    {
        cout << strategy->name() << " fine for " << lateDays << " days: Rs "
             << strategy->fine(lateDays) << endl;
    }
};

// STEP 4: client code
int main()
{
    StandardFine standard; StudentFine student; SeniorCitizenFine senior;
    Loan loan(5, &standard);
    loan.report();
    loan.setStrategy(&student);   loan.report();
    loan.setStrategy(&senior);    loan.report();
    return 0;
}
```

```output
standard fine for 5 days: Rs 25
student fine for 5 days: Rs 6
senior fine for 5 days: Rs 0
```

Notice each strategy class has a **single responsibility**, and `Loan` contains **no if/else** about member types.

## 5. What We Gained

- **Open/Closed:** a new rule (e.g. `FestivalWaiver`) is a new class; `Loan` is untouched.
- **Single responsibility:** each algorithm lives in its own class.
- **Testability:** test each strategy on its own.
- **Run-time flexibility:** switch algorithms while running.
- **No string-based dispatch.**
- **Composition over inheritance:** Loan *has* a strategy instead of having `StudentLoan`, `SeniorLoan` subclasses.
- *Cost:* more small classes; the client must pick the right strategy (often a **factory** does it).

## When to Use It

- You have **several variants of an algorithm** (pricing, discounts, fines, sorting, routing, compression).
- You see a growing `if/else` or `switch` that selects behaviour.
- The behaviour should be **changeable at run time**.

**Larman's example:** pricing strategies for a `Sale` — `PercentDiscountPricingStrategy`, `AbsoluteDiscountOverThresholdPricingStrategy`.

**Strategy vs State:** same structure, different intent — Strategy: the *client* chooses an algorithm; State: behaviour changes *automatically* as the object's internal state changes.

:::key
- Strategy = family of interchangeable algorithms behind one interface; the context delegates.
- Participants: Strategy, Concrete Strategies, Context.
- Replaces conditionals; open/closed; switchable at run time.
:::

:::mistakes
- Keeping a `switch` inside the context "to choose the strategy" — that defeats the pattern.
- Confusing Strategy (behavioural, algorithms) with Bridge (structural, abstraction vs implementation).
:::

:::exam
- *"Explain the Strategy pattern with its structure and a C++ example."* → intent, problem with if/else, analogy, class diagram, code + output, what we gained.
:::

:::def
**Strategy** (behavioural): "Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it." Participants: Strategy (interface), ConcreteStrategy, and Context (holds and delegates to a strategy).
:::

## Quick Check

:::q Q1 · A shopping cart supports "no discount", "10% off" and "buy 2 get 1". Which pattern, and what are the participants?
:::ans
**Strategy.** Strategy: `DiscountStrategy`; Concrete strategies: `NoDiscount`, `PercentOff`, `BuyTwoGetOne`; Context: `Cart`.
:::
:::
