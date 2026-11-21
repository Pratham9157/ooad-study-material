**A class is a blueprint that describes what data an object holds and what it can do. An object is a real "thing" built from that blueprint.** This is the heart of the whole course.

## The Problem: Data Without Rules

With a structure, any code can do this:

```cpp
struct Account { int number; double balance; };
Account a = {1001, 500};
a.balance = -99999;      // nothing prevents nonsense
```

The data and the rules that should protect it (e.g. "balance can't go negative") are disconnected. We want the account to **own its data and its own operations**, so that the *only* way to change the balance is through operations that check the rules.

## Understanding Classes and Objects

A **class** bundles two things:
- **Data members** (attributes) — what each object *knows*: `accNo`, `balance`.
- **Member functions** (methods) — what each object *can do*: `deposit()`, `withdraw()`.

An **object** is an **instance** of a class — a variable of that class type with its own copy of the data.

```text
     CLASS (blueprint)                       OBJECTS (instances)
 ┌────────────────────────┐          ┌──────────────────┐  ┌──────────────────┐
 │ BankAccount            │  creates │ a1               │  │ a2               │
 │  data:  accNo, balance │ ───────► │ accNo   = 1001   │  │ accNo   = 1002   │
 │  funcs: deposit(),     │          │ balance = 750    │  │ balance = 3000   │
 │         withdraw() ... │          └──────────────────┘  └──────────────────┘
 └────────────────────────┘          each object has its OWN data; functions are shared
```

:::analogy
A **cookie cutter and cookies**. The cutter (class) defines the shape; it isn't a cookie itself and you can't eat it. Each cookie (object) has the same shape but its own toppings (data values). One cutter, many cookies.
:::

## Writing Your First Class

```cpp
#include <iostream>
using namespace std;

class BankAccount
{
private:                          // hidden from the outside world
    int accNo;
    double balance;

public:                           // the "buttons" anyone may press
    void open(int no, double initial)
    {
        accNo = no;
        balance = (initial >= 0) ? initial : 0;
    }
    void deposit(double amt)
    {
        if (amt > 0) balance += amt;
    }
    bool withdraw(double amt)
    {
        if (amt > 0 && amt <= balance) { balance -= amt; return true; }
        return false;             // the rule lives in ONE place
    }
    double getBalance() { return balance; }
};                                // <- semicolon!

int main()
{
    BankAccount a;                // create an object
    a.open(1001, 500);            // call methods with the dot operator
    a.deposit(250);
    cout << a.getBalance() << endl;
    cout << (a.withdraw(1000) ? "ok" : "insufficient funds") << endl;
    // a.balance = -99999;        // ERROR: balance is private
    return 0;
}
```

```output
750
insufficient funds
```

Compare with the procedural version in Lesson 3.1: the overdraft that produced `-250` is now impossible.

## Methods: The Things an Object Can Do

The functions inside a class are its **methods**. Common kinds:
- **Accessor (getter)** — returns information without changing anything: `getBalance()`.
- **Mutator (setter)** — changes data in a controlled way: `deposit()`, `withdraw()`.
- **Helper** — an internal function, usually `private`, used by other methods.

Calling a method is **message passing**: `a.deposit(250)` = "object `a`, please deposit 250".

## Defining Methods Inside vs Outside the Class

For short methods, define them inside the class. For longer ones, declare inside and define outside with the **scope resolution operator `::`**, which says "this function belongs to that class".

```cpp
#include <iostream>
using namespace std;

class Rectangle
{
    int length, breadth;                         // private by default in a class
public:
    void set(int l, int b) { length = l; breadth = b; }   // defined inside
    int area();                                            // only declared
    void show();
};

int Rectangle::area()                            // defined outside with ::
{
    return length * breadth;                     // can use private members
}

void Rectangle::show()
{
    cout << length << " x " << breadth << " = " << area() << endl;  // a method calling a method
}

int main()
{
    Rectangle r1, r2;                            // two objects, separate data
    r1.set(4, 5);
    r2.set(2, 3);
    r1.show();
    r2.show();
    return 0;
}
```

```output
4 x 5 = 20
2 x 3 = 6
```

| Defined inside the class | Defined outside the class |
|---|---|
| Automatically **inline** | Not inline (unless you write `inline`) |
| Best for short methods | Best for longer methods; keeps the class tidy |
| No `::` needed | Needs `ReturnType ClassName::name(params)` |

## How Objects Live in Memory

- Each object gets **its own copy of the data members** (r1 has its own length; r2 has its own).
- **Methods are shared** — only one copy of `area()`'s code exists for all objects. (How does `area()` know whose `length` to use? Through a hidden pointer called `this` — Lesson 4.1.)
- So `sizeof(object)` counts only data, never functions.
- An object of an **empty class** still takes **1 byte**, so that every object has a unique address.

```cpp
#include <iostream>
using namespace std;

class Empty { };
class TwoInts { int a, b; public: void f() { } void g() { } };

int main()
{
    cout << sizeof(Empty) << " " << sizeof(TwoInts) << endl;   // functions add nothing
    return 0;
}
```

```output
1 8
```

:::key
- Class = blueprint with data members + member functions; object = an instance.
- A class takes no memory for data until objects are created; each object has its own data, methods are shared.
- Use `.` to call methods: `obj.method()`; define outside with `ClassName::`.
- Getters read, setters change data under the class's own rules.
:::

:::mistakes
- Forgetting the `;` after the class.
- Accessing private members from `main` (`r1.length = 5;`) → error.
- Defining a method outside without `ClassName::` → it becomes an unrelated global function.
- Calling a method on the class name (`Rectangle.area()`) instead of an object (`r1.area()`).
- Saying an empty class's object has size 0 — it's 1.
:::

:::exam
- *"Define class and object. Explain with an example program."*
- *"How are member functions defined inside and outside a class?"*
- *"Explain how memory is allocated for objects."*
:::

:::def
A **class** is a user-defined data type that binds together data members and member functions that operate on them, and acts as a blueprint for creating objects. An **object** is an instance of a class: a run-time entity that has its own state (values of data members), behaviour (member functions) and identity.
:::

## Quick Check

:::q Q1 · If a class has 3 int data members and 10 member functions, how many bytes does each object take (with 4-byte ints, ignoring padding)?
:::ans
**12 bytes** — only data members occupy space in each object; functions are shared code.
:::
:::

:::q Q2 · What does `::` mean in `int Rectangle::area()`?
:::ans
It's the scope resolution operator — it says `area` is a member function **of class `Rectangle`**, so it can access Rectangle's members.
:::
:::

:::q Q3 · What is message passing?
:::ans
Objects interacting by calling each other's methods, e.g. `acc.withdraw(500)` sends the message "withdraw 500" to the object `acc`.
:::
:::
