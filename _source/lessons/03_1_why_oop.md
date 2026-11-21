**Object-Oriented Programming organises a program around *objects* — bundles of data plus the actions that work on that data — instead of around a list of procedures.** This lesson explains *why* that idea exists and introduces all its core concepts in plain words.

## The Problem: Procedural Programs Get Fragile as They Grow

Suppose we write a banking program the way we've been writing programs so far — **procedurally**: data in variables, and separate functions that act on it.

```cpp
#include <iostream>
using namespace std;

double balance = 500;                 // global data — ANY function can touch it

void deposit(double amt)  { balance += amt; }
void withdraw(double amt) { balance -= amt; }          // oops: no check for overdraft
void applyBonus()         { balance = balance * 100; } // a buggy function elsewhere

int main()
{
    deposit(250);
    withdraw(1000);                   // balance goes negative — nothing stopped it
    cout << "Balance: " << balance << endl;
    return 0;
}
```

```output
Balance: -250
```

What's wrong with this approach?

- **Data is unprotected.** Any function in the program can change `balance` — correctly or not. In a 10,000-line program, finding *who* broke the balance is a nightmare.
- **Rules are scattered.** The rule "you can't withdraw more than you have" should live in *one* place, but nothing ties it to the balance.
- **Data and behaviour are separated.** `balance` and the functions that use it are related, but the code doesn't show that relationship.
- **Hard to scale.** Need 1,000 accounts? You'd need 1,000 balances and functions that take "which account" as an extra parameter everywhere.

## The Object-Oriented Idea

Instead of asking *"What are the steps?"*, OOP asks **"What are the things (objects) in this problem, what does each one know, and what can each one do?"**

In a bank, the "thing" is an **Account**. An account *knows* its balance and *can* deposit and withdraw — and it enforces its own rules. Nobody outside can change the balance directly.

```text
          Procedural view                               Object-oriented view
  ┌──────────────┐   ┌────────────┐              ┌───────────────────────────────┐
  │ deposit()    │   │            │              │  Account object               │
  │ withdraw()   │──►│  balance   │◄── anyone    │  data:    balance (hidden)    │
  │ applyBonus() │   │  (global)  │              │  actions: deposit(), withdraw()│
  └──────────────┘   └────────────┘              │  rule:    no overdraft        │
                                                 └───────────────────────────────┘
                                                    outsiders can only send requests
```

You'll write this exact `Account` class in Lesson 3.3.

:::analogy
A **restaurant**. In a "procedural" restaurant, customers walk into the kitchen and cook their own food using the shared ingredients — chaos. In an "object-oriented" restaurant, the **kitchen** is an object: it owns the ingredients (data) and knows how to cook (behaviour). Customers just send a request ("one pizza, please") and get the result. They can't touch the ingredients directly.
:::

## Procedural vs Object-Oriented Programming

| Procedural Programming (POP) | Object-Oriented Programming (OOP) |
|---|---|
| Program divided into **functions** | Program divided into **objects** |
| Focus on **steps/algorithms** | Focus on **data** and the objects that own it |
| **Top-down** approach | **Bottom-up** approach (build objects, then combine them) |
| Data often global, moves freely | Data **hidden** inside objects (data hiding) |
| Hard to extend without changing existing code | Easy to extend (inheritance, polymorphism) |
| Less reuse | High reuse |
| No access control | `public`, `private`, `protected` |
| e.g. C, Pascal, FORTRAN | e.g. C++, Java, C#, Python |

## The Core Concepts of OOP — in Plain Words

You'll study each in detail later; here is the big picture so the words don't feel strange.

**1. Object** — a "thing" in the program with **state** (its data), **behaviour** (what it can do) and **identity** (it's distinct from other objects, even identical-looking ones).
*Your phone: state = 70% battery; behaviour = call(), charge(); identity = its own IMEI number.*

**2. Class** — the **blueprint** from which objects are made. It describes what data and behaviour every object of that kind has. A class is a **user-defined data type**.
*The phone model's design spec is the class; each phone in a shop is an object.*

**3. Abstraction** — showing only the **essential** features and hiding unnecessary details.
*You drive a car using a steering wheel and pedals, without knowing how the fuel injection works.*

**4. Encapsulation** — **wrapping** data and the functions that operate on it into one unit (the class).
*A medicine capsule wraps different powders in one shell.*

**5. Data hiding** — preventing direct outside access to an object's data; it can be reached only through the object's functions. (Achieved by encapsulation + `private`.)
*Your bank balance can be changed only through the bank's counters/app, never by reaching into the vault.*

**6. Inheritance** — a new class **acquires** the properties of an existing class and adds its own ("is-a" relationship). It enables **reuse**.
*A Car **is a** Vehicle: it inherits wheels and an engine, and adds air-conditioning.*

**7. Polymorphism** — "many forms": the **same message** produces **different behaviour** depending on the object.
*"Draw!" makes a circle draw a circle and a square draw a square.*

**8. Dynamic binding** — deciding *which* function body to run **at run time** (based on the actual object), not at compile time. (Chapter 5.)

**9. Message passing** — objects communicate by **calling each other's methods**: `account.withdraw(500)` means "send the message *withdraw 500* to the account object".

:::analogy
Put them all together with a **TV remote** (a real-world object): it has state (battery level, current channel) and behaviour (change channel). Its circuit board is hidden (data hiding) inside the plastic case (encapsulation); you only see buttons (abstraction). A "smart remote" adds voice control to a basic remote (inheritance). The "power" button turns off a TV, an AC or a fan differently (polymorphism). Pressing a button sends a signal (message passing).
:::

## Benefits and Applications of OOP

**Benefits:** reusability (classes and inheritance), data security (data hiding), easier maintenance and modification, real-world modelling, scalability for large projects, team development, less duplicated code.

**Applications:** GUI and windowing systems, games, simulations, real-time systems, CAD/CAM, object-oriented databases, AI and expert systems, web and mobile apps.

:::note Is C++ a "pure" OOP language?
No. C++ is a **hybrid/multi-paradigm** language: it supports OOP, but you can also write procedural code (functions outside classes, `main` itself is not in a class). Languages like Smalltalk are "pure" OOP.
:::

:::key
- Procedural = organise by **steps**; OOP = organise by **things (objects)** that own data + behaviour.
- OOP protects data (data hiding), keeps rules in one place, and scales better.
- Concepts: object, class, abstraction, encapsulation, data hiding, inheritance, polymorphism, dynamic binding, message passing.
:::

:::mistakes
- Saying "a class is an object". A class is the **blueprint**; an object is an **instance** made from it.
- Treating abstraction and encapsulation as the same thing (see Lesson 3.5 for the difference).
- Forgetting **identity** when listing an object's characteristics (state, behaviour, identity).
- Calling C++ a pure object-oriented language.
:::

:::exam
- *"Explain the basic concepts of OOP with examples."* (Very common, 8–10 marks.) Write each concept: one-line definition + real-world example + one-line C++ hint.
- *"Differentiate procedural and object-oriented programming."* → the table.
- *"What are the benefits/applications of OOP?"*
:::

:::def
**Object-Oriented Programming (OOP)** is a programming paradigm in which a program is organised as a collection of objects, each an instance of a class, that combine data (state) and functions (behaviour) and interact by sending messages to one another. Its main features are abstraction, encapsulation, inheritance and polymorphism.
:::

## Quick Check

:::q Q1 · Give the state, behaviour and identity of a "Student" object.
:::ans
State: roll number, name, marks. Behaviour: attendClass(), takeExam(), showResult(). Identity: each student is a distinct object even if two have the same name/marks (e.g. their own roll number / memory location).
:::
:::

:::q Q2 · Which OOP concept is shown? (a) A `SavingsAccount` reuses everything in `Account`. (b) `balance` can be changed only through `deposit()`. (c) `shape.draw()` draws different shapes.
:::ans
(a) **Inheritance**, (b) **Encapsulation / data hiding**, (c) **Polymorphism**.
:::
:::

:::q Q3 · Name two problems of procedural programming that OOP solves.
:::ans
Any two: unprotected (global) data that any function can corrupt; rules scattered across functions; data and behaviour not bundled; difficulty extending/reusing code in large programs.
:::
:::
