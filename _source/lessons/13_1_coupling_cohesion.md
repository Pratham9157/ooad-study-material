**Coupling measures how much a class depends on other classes. Cohesion measures how focused a class's own responsibilities are. Good design aims for *low coupling* and *high cohesion*.** These two ideas are the yardstick for every design decision in this chapter.

## The Problem: The Class That Does Everything

```cpp
#include <iostream>
#include <string>
using namespace std;

class LibraryManager                         // a "god class"
{
public:
    int fine(int lateDays) { return lateDays * 5; }                   // business rule
    string toHtml(const string &s) { return "<p>" + s + "</p>"; }     // formatting
    void email(const string &to) { cout << "emailing " << to << endl; } // messaging
    // ... plus database code, logging, report printing ...
};

int main()
{
    LibraryManager m;
    cout << m.toHtml("Fine: Rs " + to_string(m.fine(3))) << endl;
    m.email("asha@example.com");
    return 0;
}
```

```output
<p>Fine: Rs 15</p>
emailing asha@example.com
```

It works, but what's wrong?
- **Low cohesion:** fines, HTML and email have nothing to do with each other. The class is hard to understand and grows forever.
- **High coupling:** everything in the system depends on `LibraryManager`; any change to it (say, the email library) can break unrelated features like fines.
- **Hard to reuse or test:** you can't reuse the fine rule without dragging email and HTML along.

## Understanding Coupling

**Coupling** = how strongly one class is **connected to, knows about, or relies on** other classes.
- **High (tight) coupling:** a change in one class forces changes in many others.
- **Low (loose) coupling:** classes can change independently.

**Ways class X can be coupled to class Y (C++):** X has an attribute of type Y (or pointer/reference); X calls Y's methods; X's method has a parameter, local or return value of type Y; X inherits from Y (strongest); X implements interface Y.

:::analogy
**Coupling** is like how your phone charger connects to your phone. A universal USB-C port (low coupling) lets you use any charger. A phone that only works with one special charger soldered on (high coupling) means if the charger breaks, the phone is useless.
:::

## Understanding Cohesion

**Cohesion** = how **strongly related and focused** the responsibilities of a single class are.
- **High cohesion:** the class does one kind of job well (e.g. `FinePolicy` only computes fines).
- **Low cohesion:** the class does many unrelated jobs (the god class above).

:::analogy
**Cohesion** is like a well-run kitchen where the chef only cooks, the cashier only bills and the cleaner only cleans. Each role is focused (high cohesion). A restaurant where one person cooks, bills, cleans, delivers and does accounts is low cohesion — slow, error-prone, impossible to replace.
:::

## The Fix: Split by Responsibility

```cpp
#include <iostream>
#include <string>
using namespace std;

class FinePolicy    { public: int fine(int lateDays) const { return lateDays * 5; } };
class HtmlFormatter { public: string paragraph(const string &s) const { return "<p>" + s + "</p>"; } };
class Mailer        { public: void send(const string &to) const { cout << "emailing " << to << endl; } };

int main()
{
    FinePolicy p; HtmlFormatter f; Mailer m;
    cout << f.paragraph("Fine: Rs " + to_string(p.fine(3))) << endl;
    m.send("asha@example.com");
    return 0;
}
```

```output
<p>Fine: Rs 15</p>
emailing asha@example.com
```

Same output, but now each class is **focused** (high cohesion) and the fine rule doesn't depend on email or HTML (low coupling). You can change the email system without touching fines, and reuse `FinePolicy` anywhere.

## Degrees of Cohesion (Larman)

1. **Very low** — one class responsible for many things in **very different areas** (database *and* networking).
2. **Low** — one class solely responsible for a **complex** task in one area (a database class with hundreds of methods).
3. **Moderate** — light, sole responsibilities in a few related areas.
4. **High** — **moderate** responsibilities in **one** area, collaborating with other classes for the rest.

Rule of thumb: a highly cohesive class has a **small number of methods**, with **closely related** functionality, and **doesn't do too much work** itself.

## Coupling vs Cohesion

| Coupling | Cohesion |
|---|---|
| Between **different** classes | Within **one** class |
| Measures **dependency** | Measures **focus** |
| Aim **LOW** | Aim **HIGH** |
| High → changes ripple through the system | Low → hard to understand, maintain, reuse |

They usually go together: splitting a low-cohesion class into focused ones tends to reduce coupling too.

## A Few More Everyday Design Principles

- **DRY — Don't Repeat Yourself:** every piece of knowledge (a rule, a formula) should live in **one** place. Duplicate code means duplicate bugs.
- **KISS — Keep It Simple:** prefer the simplest design that works.
- **YAGNI — You Aren't Gonna Need It:** don't build features "just in case".
- **Separation of concerns:** keep UI, business logic and data access in separate classes/layers (the layers in Lesson 12.3).

:::key
- Coupling = dependence between classes → keep **low**. Cohesion = focus within a class → keep **high**.
- God classes have low cohesion and high coupling: split them by responsibility.
- High coupling to **stable** things (like `std::string`) is fine; avoid coupling to unstable things.
- DRY, KISS, YAGNI and separation of concerns support the same goal.
:::

:::mistakes
- Saying "high coupling, low cohesion is good" — it's the opposite.
- Confusing the two: coupling is *between* classes; cohesion is *inside* one class.
- Thinking zero coupling is the goal — objects must collaborate; the aim is *low*, not none.
:::

:::exam
- *"Define coupling and cohesion. Why should coupling be low and cohesion high?"*
- *"Explain the Low Coupling and High Cohesion GRASP patterns"* (Lesson 13.3 — this lesson gives the theory).
:::

:::def
**Coupling** is a measure of how strongly one element is connected to, has knowledge of, or relies on other elements. **Cohesion** is a measure of how strongly related and focused the responsibilities of an element are. Good object-oriented design aims for **low coupling** and **high cohesion**.
:::

## Quick Check

:::q Q1 · A `Student` class stores marks, prints PDF report cards and sends SMS to parents. What's the problem and the fix?
:::ans
**Low cohesion** (unrelated jobs) and unnecessary coupling to PDF/SMS libraries. Split into `Student` (data + marks logic), `ReportCardPrinter`, and `SmsNotifier`.
:::
:::

:::q Q2 · Is a class that uses `std::vector` heavily "highly coupled" in a bad way?
:::ans
No — coupling to **stable**, standard elements is rarely a problem. The concern is coupling to unstable, frequently changing classes.
:::
:::
