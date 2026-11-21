**A constructor is a special member function that runs automatically the moment an object is created, to give it a valid starting state.**

## The Problem: Objects Born With Garbage

```cpp
#include <iostream>
using namespace std;

class Box
{
    int length, width;
public:
    void set(int l, int w) { length = l; width = w; }
    int area() { return length * width; }
};

int main()
{
    Box b;
    b.set(3, 4);          // what if someone forgets this line?
    cout << b.area() << endl;
    return 0;
}
```

```output
12
```

It works — but only because we remembered to call `set()`. Forget it and `area()` uses garbage values. In a big program, *someone* will forget. We want initialization to be **automatic and impossible to skip**.

## Understanding Constructors

A **constructor** has the **same name as the class** and **no return type**. C++ calls it automatically whenever an object is created.

:::analogy
When you switch on a brand-new phone, it **automatically** sets a default language, time and wallpaper before you can use it. You don't call "setup" — it happens as the phone comes into existence. That automatic setup is the constructor.
:::

**Characteristics of a constructor** (memorise these — a very common question):
1. Same name as the class.
2. No return type — not even `void`.
3. Called **automatically** when an object is created.
4. Usually `public`.
5. Can take parameters, can have **default arguments**, and can be **overloaded**.
6. Cannot be `virtual`, `static` or `const`.
7. Not inherited (a child class calls its parent's constructor instead).
8. If you write **no** constructor, the compiler provides a default one (which leaves built-in members uninitialized).

## Types of Constructors

| Type | Parameters | Example |
|---|---|---|
| **Default constructor** | none | `Box()` |
| **Parameterized constructor** | one or more | `Box(int l, int w)` |
| **Copy constructor** | a reference to another object of the same class | `Box(const Box &b)` — Lesson 4.2 |

## Constructor Overloading

**Constructor overloading** means having **several constructors** with different parameter lists, so objects can be created in different ways. The compiler chooses one based on the arguments (just like function overloading, Lesson 2.5).

```cpp
#include <iostream>
using namespace std;

class Box
{
    int length, width;
public:
    Box()                       // default constructor
    {
        length = width = 1;
        cout << "Default ctor" << endl;
    }
    Box(int side)               // parameterized: a square box
    {
        length = width = side;
        cout << "One-arg ctor" << endl;
    }
    Box(int l, int w)           // parameterized: two arguments
    {
        length = l; width = w;
        cout << "Two-arg ctor" << endl;
    }
    int area() { return length * width; }
};

int main()
{
    Box b1;              // calls Box()          — note: NOT  Box b1();
    Box b2(5);           // calls Box(int)
    Box b3(3, 4);        // calls Box(int, int)
    Box b4 = Box(2, 6);  // explicit call
    cout << b1.area() << " " << b2.area() << " " << b3.area() << " " << b4.area() << endl;
    return 0;
}
```

```output
Default ctor
One-arg ctor
Two-arg ctor
Two-arg ctor
1 25 12 12
```

## A Constructor With Default Arguments

One constructor with defaults can replace several overloads:

```cpp
#include <iostream>
using namespace std;

class Time
{
    int h, m;
public:
    Time(int hh = 0, int mm = 0) { h = hh; m = mm; }   // works as 0-, 1- and 2-arg
    void show() { cout << h << ":" << m << endl; }
};

int main()
{
    Time t1, t2(9), t3(10, 30);
    t1.show(); t2.show(); t3.show();
    return 0;
}
```

```output
0:0
9:0
10:30
```

Careful: if a class has both `Time()` and `Time(int hh = 0, int mm = 0)`, then `Time t;` is **ambiguous** (both fit) → error.

## The Member Initializer List

Instead of assigning inside the body, you can **initialize** members before the body runs:

```text
ClassName(params) : member1(value1), member2(value2) { body }
```

It's **required** for:
1. `const` data members (they can't be assigned, only initialized),
2. reference data members,
3. members whose class has no default constructor,
4. passing arguments to a base-class constructor (Chapter 5).

```cpp
#include <iostream>
using namespace std;

class Student
{
    const int roll;                 // must be set at creation and never changed
    double cgpa;
public:
    Student(int r, double c) : roll(r), cgpa(c) { }   // initializer list
    void show() { cout << roll << " " << cgpa << endl; }
};

int main()
{
    Student s(7, 9.2);
    s.show();
    return 0;
}
```

```output
7 9.2
```

## The Disappearing Default Constructor

If you write **any** constructor yourself, the compiler **stops** providing the default one:

```cpp
#include <iostream>
using namespace std;
//@expect: compile-error

class Box
{
    int l;
public:
    Box(int x) { l = x; }    // only a parameterized constructor
};

int main()
{
    Box b1(5);   // OK
    Box b2;      // ERROR: no default constructor Box() exists anymore
    return 0;
}
```

Fix: also write `Box() { l = 0; }`, or give the parameter a default: `Box(int x = 0)`.

## Creating Objects Dynamically

`new` creates an object on the heap **and calls its constructor**:

```cpp
#include <iostream>
using namespace std;

class Point
{
    int x, y;
public:
    Point(int a = 0, int b = 0) : x(a), y(b) { }
    void show() { cout << "(" << x << "," << y << ")" << endl; }
};

int main()
{
    Point *p = new Point(3, 4);   // constructor runs with 3, 4
    p->show();
    delete p;
    return 0;
}
```

```output
(3,4)
```

:::key
- Constructor = same name as class, no return type, runs automatically at object creation.
- Types: default, parameterized, copy. Overloading = several constructors with different parameters.
- Default arguments can merge several constructors into one (watch for ambiguity).
- Initializer list is required for `const`/reference members (and base classes).
- Writing any constructor removes the compiler's default constructor.
:::

:::mistakes
- Giving a constructor a return type (`void Box()`) → error.
- **`Box b();`** does NOT create an object — it declares a *function* named `b` returning `Box` (the "most vexing parse"). Write `Box b;`.
- Defining only `Box(int)` and then writing `Box b;` or `new Box[5]`.
- Assigning a `const` member inside the constructor body.
- Trying to call a constructor on an existing object (`b1.Box(5)`).
:::

:::exam
- *"What is a constructor? List its characteristics."*
- *"Explain the types of constructors with a program."*
- *"What is constructor overloading? Illustrate."* (Unit 1 — very likely!)
- *"Find the error"* — `Box b;` without a default constructor, `Box b();`.
:::

:::def
A **constructor** is a special member function, with the same name as its class and no return type, that is invoked automatically when an object is created in order to initialize it. **Constructor overloading** is defining more than one constructor in a class with different parameter lists, so that objects can be initialized in different ways.
:::

## Quick Check

:::q Q1 · Which constructor runs for each? `class A { public: A(); A(int); A(int,int); };` → `A x; A y(5); A z(1,2); A w = A(3);`
:::ans
`x` → `A()`, `y` → `A(int)`, `z` → `A(int,int)`, `w` → `A(int)`.
:::
:::

:::q Q2 · Why does `class T { const int k; public: T(int v) { k = v; } };` fail? Fix it.
:::ans
A `const` member can't be assigned; it must be initialized: `T(int v) : k(v) { }`.
:::
:::

:::q Q3 · Can a constructor be overloaded? Can it be virtual?
:::ans
It **can** be overloaded; it **cannot** be virtual.
:::
:::
