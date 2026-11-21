**A friend function is an outside (non-member) function that a class trusts enough to let it see its private data. A friend class is a whole class given that same trust.**

## The Problem: Sometimes Two Classes Need to Cooperate

Encapsulation keeps data private — good. But consider:
- A function that compares the private balance of an `Account` object with the private limit of a `Loan` object. Whose member should it be? It needs **both** classes' private data.
- `operator<<` for printing must take `cout` as its left operand, so it can't be a member (Lesson 4.4) — but it needs the private data to print.

We need a **controlled exception** to data hiding.

:::analogy
Your house is locked to outsiders (private). You give a **spare key to a trusted friend**. The friend isn't a family member (not a member function), but can enter. Important: *you* decide who gets a key — someone can't declare themselves your friend. And your friend's friends don't automatically get keys.
:::

## Understanding Friend Functions

Declare the function **inside** the class with the keyword `friend`; define it **outside** like a normal function (no `ClassName::`, no `friend` keyword).

**Properties of a friend function:**
1. It is **not a member** of the class.
2. It is called like a normal function — `sumBoth(p, q)` — **not** with an object and dot.
3. It has **no `this` pointer**; it reaches members through object parameters (`x.a`).
4. It can be declared in the `public` or `private` part — no difference.
5. Friendship is **granted by the class**, not taken.
6. Friendship is **not inherited**, **not transitive** (friend of a friend is not a friend) and **not mutual**.

## Example: One Function, Friend of Two Classes

```cpp
#include <iostream>
using namespace std;

class Beta;                         // forward declaration: "Beta exists, defined later"

class Alpha
{
    int a;
public:
    Alpha(int x) : a(x) { }
    friend int sumBoth(const Alpha &, const Beta &);   // Alpha trusts sumBoth
};

class Beta
{
    int b;
public:
    Beta(int y) : b(y) { }
    friend int sumBoth(const Alpha &, const Beta &);   // Beta trusts it too
};

int sumBoth(const Alpha &x, const Beta &y)   // a normal function: no Alpha:: in front
{
    return x.a + y.b;                         // reads private data of BOTH classes
}

int main()
{
    Alpha p(10);
    Beta q(25);
    cout << sumBoth(p, q) << endl;            // called like any ordinary function
    return 0;
}
```

```output
35
```

**Why the forward declaration?** `Alpha` mentions `Beta` before `Beta` is defined; `class Beta;` tells the compiler the name exists.

## Friend Operators: Making `50 + obj` Work

```cpp
#include <iostream>
using namespace std;

class Money
{
    int rupees;
public:
    Money(int r = 0) : rupees(r) { }
    friend Money operator+(const Money &a, const Money &b);
    void show() const { cout << "Rs " << rupees << endl; }
};

Money operator+(const Money &a, const Money &b)
{
    return Money(a.rupees + b.rupees);
}

int main()
{
    Money m(100);
    (m + 50).show();     // operator+(m, Money(50))
    (50 + m).show();     // operator+(Money(50), m) — works because it's not a member
    return 0;
}
```

```output
Rs 150
Rs 150
```

## Friend Classes

If class `Mechanic` is declared a **friend class** of `Engine`, then **every** member function of `Mechanic` can access `Engine`'s private members.

```cpp
#include <iostream>
using namespace std;

class Engine
{
    int horsepower;
    friend class Mechanic;            // the whole Mechanic class is trusted
public:
    Engine(int hp) : horsepower(hp) { }
};

class Mechanic
{
public:
    void tune(Engine &e) { e.horsepower += 20; }
    void report(const Engine &e) { cout << "HP: " << e.horsepower << endl; }
};

int main()
{
    Engine e(100);
    Mechanic m;
    m.report(e);
    m.tune(e);
    m.report(e);
    return 0;
}
```

```output
HP: 100
HP: 120
```

## Member Function vs Friend Function

| Member function | Friend function |
|---|---|
| Belongs to the class | Not a member; outside the class's scope |
| Called through an object: `obj.f()` | Called like a normal function: `f(obj)` |
| Has a `this` pointer | No `this` pointer |
| Access specifier matters | Can be declared anywhere in the class |
| Inherited by derived classes | Not inherited |

:::warn Use friends sparingly
Friends **weaken encapsulation**. Use them only when there's a real need: operators like `<<`/`>>`, symmetric operators like `50 + obj`, or functions that genuinely need two classes' internals.
:::

:::key
- A friend is a trusted non-member with access to private/protected members.
- Declared inside with `friend`, defined outside like a normal function, called without an object, no `this`.
- Friendship is granted, not inherited, not transitive, not mutual.
- A friend class makes all its member functions friends.
:::

:::mistakes
- Defining the friend as `int Alpha::sumBoth(…)` — it's not a member.
- Calling it as `p.sumBoth(p, q)`.
- Using `this` inside a friend function.
- Forgetting the forward declaration when two classes refer to each other.
- Assuming friendship is inherited or mutual.
:::

:::exam
- *"What is a friend function? State its characteristics. Write a program using a friend function common to two classes."* (Very common!)
- *"What is a friend class?"*
- *"Differentiate member and friend functions."*
:::

:::def
A **friend function** is a non-member function that is granted access to the private and protected members of a class by being declared inside the class with the keyword `friend`. A **friend class** is a class all of whose member functions are granted such access. Friendship is neither inherited, transitive nor mutual.
:::

## Quick Check

:::q Q1 · If class A declares class B as its friend, can A's functions access B's private members?
:::ans
No — friendship is **not mutual**. Only B can access A's private members.
:::
:::

:::q Q2 · Why is `operator<<` usually a friend?
:::ans
Its left operand is `ostream` (`cout`), not the object, so it can't be a member of our class; yet it needs our private data to print — hence a friend.
:::
:::
