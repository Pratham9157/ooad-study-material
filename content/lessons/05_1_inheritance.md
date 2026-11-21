**Inheritance lets a new class automatically get the data and functions of an existing class, and then add or change only what's different.** It models an "is-a" relationship and saves you from rewriting code.

## The Problem: Copy-Paste Classes

A library has two kinds of staff: Librarians and Accountants. Both have a name, an ID and a salary, and both can `login()`. Written separately:

```text
class Librarian  { name, id, salary, login(), issueBook() }
class Accountant { name, id, salary, login(), prepareReport() }
```

The common parts are written **twice**. Add a field (say `phone`) or fix a bug in `login()`, and you must change **both** classes — and every future staff class. This duplication is exactly what inheritance removes.

## The Idea: Put the Common Part in a Parent Class

```text
                 ┌─────────────────────────┐
                 │ Staff  (base / parent)  │   name, id, salary, login()
                 └────────────▲────────────┘
                 ┌────────────┴────────────┐
      ┌────────────────────┐     ┌────────────────────┐
      │ Librarian (derived)│     │ Accountant (derived)│
      │ + issueBook()      │     │ + prepareReport()  │
      └────────────────────┘     └────────────────────┘
       Librarian IS-A Staff       Accountant IS-A Staff
```

- The existing class is the **base class** (parent / superclass).
- The new class is the **derived class** (child / subclass).
- The derived class **inherits** the base's members and **adds** its own.

:::analogy
Children inherit features from their parents — eye colour, surname — and then develop their own skills. A child doesn't need to "re-invent" having eyes; they get them automatically, and add what makes them unique. Similarly, every `Car` **is a** `Vehicle`: it gets wheels and an engine from "vehicle" and adds air-conditioning.
:::

**The is-a test:** inheritance is right only if "Derived **is a** Base" makes sense. "Car is a Vehicle" ✓. "Car is an Engine" ✗ (a car **has** an engine — that's composition, Lesson 8.2).

## Syntax

```text
class Derived : access-mode Base
{
    // extra members
};
```

```cpp
#include <iostream>
using namespace std;

class Vehicle                             // base class
{
protected:                                // visible to child classes, hidden from outside
    int regNo;
public:
    void setReg(int r) { regNo = r; }
    void start() { cout << "Vehicle " << regNo << " started" << endl; }
};

class Car : public Vehicle                // Car IS-A Vehicle
{
    int seats;
public:
    void setSeats(int s) { seats = s; }
    void info() { cout << "Car " << regNo << " has " << seats << " seats" << endl; }
};

int main()
{
    Car c;
    c.setReg(4521);        // inherited from Vehicle
    c.setSeats(5);         // Car's own
    c.start();             // inherited
    c.info();
    return 0;
}
```

```output
Vehicle 4521 started
Car 4521 has 5 seats
```

`Car` never defined `setReg` or `start`, yet it has them.

## The protected Access Specifier

- `private` members of the base are **inherited but not accessible** in the derived class (they exist inside the object; the child just can't touch them directly).
- `protected` members are hidden from the outside world **but accessible in derived classes**. That's why `regNo` above is `protected`.

## Access Modes: public, protected, private Inheritance

The word after the colon decides how inherited members are seen **through the derived class**:

| Base member ↓ / Mode → | `public` inheritance | `protected` inheritance | `private` inheritance |
|---|---|---|---|
| `public` | stays **public** | becomes **protected** | becomes **private** |
| `protected` | stays **protected** | stays **protected** | becomes **private** |
| `private` | **not accessible** | **not accessible** | **not accessible** |

Memory trick: the mode is a **ceiling** — members can only become *more* restricted, never more open. **Public inheritance** is used 99% of the time (it's the true "is-a"). Default: `class D : B` means **private** inheritance; `struct D : B` means public.

```cpp
#include <iostream>
using namespace std;

class A
{
private:   int x = 1;
protected: int y = 2;
public:    int z = 3;
};

class B : public A  { public: void f() { cout << y << z << endl; } };  // x not accessible
class C : private A { public: void f() { cout << y << z << endl; } };  // y, z now private in C

int main()
{
    B b; b.f();
    cout << b.z << endl;    // OK: z is still public through B
    C c; c.f();
    // cout << c.z;         // ERROR: z became private in C
    return 0;
}
```

```output
23
3
23
```

## Why Inheritance Is Useful

- **Reusability** — write common code once.
- **Extensibility** — add new kinds (e.g. `Security` staff) without touching existing classes.
- **Maintainability** — fix a bug in the base and every child benefits.
- **Models real hierarchies** naturally.
- **Enables polymorphism** (Lesson 5.4).

**Not inherited:** constructors, destructor, assignment operator, friend relationships. (The child *calls* the parent's constructor — Lesson 5.3.)

:::key
- Inheritance: derived class acquires base class members; models **is-a**; enables reuse.
- Syntax: `class Derived : public Base`.
- `protected` = hidden outside, visible to children. Private members are inherited but inaccessible.
- Access mode only restricts. Default for `class` is private inheritance.
:::

:::mistakes
- Saying "private members are not inherited" — they **are** inherited, just not accessible.
- Using inheritance for "has-a" relationships (Car : Engine).
- Forgetting that `class D : B` means private inheritance.
- Expecting `protected` members to be accessible from `main`.
:::

:::exam
- *"What is inheritance? Explain with an example. What are its advantages?"*
- *"Explain the visibility of base class members in public, protected and private derivation."* → the table.
- *"What is the protected access specifier?"*
:::

:::def
**Inheritance** is the mechanism by which a new class (derived class) acquires the properties — data members and member functions — of an existing class (base class), and may add new members or redefine inherited ones. It represents an "is-a" relationship and supports reusability.
:::

## Quick Check

:::q Q1 · In `class D : protected B`, what does a public member of B become in D?
:::ans
**protected**.
:::
:::

:::q Q2 · Should `Student` inherit from `Person`? Should `Library` inherit from `Book`? Why?
:::ans
`Student : Person` ✓ — a student **is a** person. `Library : Book` ✗ — a library **has** books (composition/aggregation), it isn't a book.
:::
:::
