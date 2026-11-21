**An abstract class is a class that represents a general idea and can't be turned into objects directly. It declares "every child *must* provide this function" using a pure virtual function.**

## The Problem: A Base Class That Shouldn't Exist on Its Own

In the last lesson, `Shape::draw()` printed "Drawing shape". But what *is* a generic shape? You can't draw one, or compute its area. Two problems:
1. Someone could create a meaningless `Shape s;` object.
2. A new child class (say `Triangle`) might **forget** to write its own `area()`, silently inheriting a fake one.

We need a way to say: **"Shape is only a concept. Every real shape MUST define `area()`."**

## The Idea: Pure Virtual Functions

```cpp
virtual double area() const = 0;   // "= 0" means: no body here — children must provide it
```

- A virtual function with `= 0` is a **pure virtual function**.
- A class with **at least one** pure virtual function is an **abstract class**.
- You **cannot create objects** of an abstract class — but you **can** have pointers and references to it.
- A derived class must override **all** pure virtual functions to become **concrete** (creatable). If it misses one, it's abstract too.

:::analogy
"**Vehicle**" in a driving-school rulebook says: *every vehicle must be able to start and stop.* But nobody can buy "a vehicle" — you buy a car, a bike or a truck, each of which actually **implements** starting and stopping in its own way. The rulebook is the abstract class; car, bike and truck are concrete classes.
:::

## Building It Step by Step

**Step 1 — the abstract base defines the contract.** **Step 2 — concrete classes fulfil it.** **Step 3 — client code uses only the base type.**

```cpp
#include <iostream>
using namespace std;

class Shape                                   // STEP 1: abstract class
{
public:
    virtual double area() const = 0;          // pure virtual: every shape MUST implement
    virtual void name() const { cout << "Shape"; }   // ordinary virtual, has a default
    void describe() const                     // normal function using the virtual ones
    {
        name();
        cout << " with area " << area() << endl;
    }
    virtual ~Shape() { }                      // virtual destructor (see below)
};

class Rectangle : public Shape                // STEP 2: concrete classes
{
    double l, b;
public:
    Rectangle(double x, double y) : l(x), b(y) { }
    double area() const override { return l * b; }
    void name() const override { cout << "Rectangle"; }
};

class Circle : public Shape
{
    double r;
public:
    Circle(double x) : r(x) { }
    double area() const override { return 3.14 * r * r; }
    // name() not overridden → uses Shape's default
};

int main()                                    // STEP 3: client uses only Shape*
{
    // Shape s;                               // ERROR: cannot create an abstract object
    Shape *shapes[2] = {new Rectangle(2, 5), new Circle(1)};
    for (int i = 0; i < 2; i++) shapes[i]->describe();
    for (int i = 0; i < 2; i++) delete shapes[i];
    return 0;
}
```

```output
Rectangle with area 10
Shape with area 3.14
```

`describe()` was written **once** in the base and works for every present and future shape.

## Interfaces

An **interface** is an abstract class with **only pure virtual functions** (and a virtual destructor) — no data, no implementations. It's a pure *contract*: "anything that implements me can do these things". C++ has no `interface` keyword; this is how you express one. Design patterns (Chapter 14) and UML "realization" (Lesson 8.3) rely on interfaces.

```text
class Printable                      // an interface
{
public:
    virtual void print() const = 0;
    virtual ~Printable() { }
};
```

| Abstract class | Concrete class |
|---|---|
| Has at least one pure virtual function | All functions implemented |
| Cannot be instantiated | Can be instantiated |
| Used as a base / contract | Used to create objects |
| Can have data, constructors, normal functions | — |

## Virtual Destructors: Cleaning Up Properly

**The problem:** you `delete` a derived object **through a base pointer**. If the base destructor is **not** virtual, only the base destructor is guaranteed to be considered — formally it's undefined behaviour, and in practice the **derived destructor usually never runs**, leaking whatever the derived object owned.

**The fix:** make the base destructor `virtual`. Then deleting through a base pointer runs the derived destructor first, then the base destructor.

```cpp
#include <iostream>
using namespace std;

class Base
{
public:
    Base() { cout << "Base ctor" << endl; }
    virtual ~Base() { cout << "Base dtor" << endl; }   // virtual!
};

class Derived : public Base
{
    int *buffer;
public:
    Derived() { buffer = new int[100]; cout << "Derived ctor" << endl; }
    ~Derived() { delete[] buffer; cout << "Derived dtor (buffer freed)" << endl; }
};

int main()
{
    Base *p = new Derived;
    delete p;      // virtual dtor → Derived dtor, then Base dtor
    return 0;
}
```

```output
Base ctor
Derived ctor
Derived dtor (buffer freed)
Base dtor
```

Without `virtual`, a typical compiler prints only `Base dtor` here, and the buffer leaks.

**Rule:** any class with virtual functions (i.e. meant to be used through base pointers) should have a **virtual destructor**.

:::key
- Pure virtual: `virtual f() = 0;` → the class becomes abstract (no objects, but pointers/references OK).
- Derived classes must override all pure virtual functions to be concrete.
- Interface = only pure virtual functions; a contract.
- Base classes used polymorphically need virtual destructors.
:::

:::mistakes
- Trying to create an object of an abstract class.
- Overriding only some pure virtual functions → the child is still abstract.
- Writing `= NULL` or `= 1` instead of `= 0`.
- Saying abstract classes can't have data members or constructors — they can.
- Forgetting the virtual destructor in a polymorphic base class.
:::

:::exam
- *"What is a pure virtual function? What is an abstract class? Explain with an example."*
- *"Why do we need virtual destructors?"*
- *"Find the error"*: instantiating an abstract class, or a child that forgot a pure virtual function.
:::

:::def
A **pure virtual function** is a virtual function that has no definition in the base class and is declared by assigning 0 (`virtual void f() = 0;`). A class containing at least one pure virtual function is an **abstract class**: it cannot be instantiated and serves as a base class whose derived classes must override all pure virtual functions. A **virtual destructor** ensures that, when a derived object is deleted through a base-class pointer, the derived destructor is called before the base destructor.
:::

## Quick Check

:::q Q1 · `class Animal { virtual void sound() = 0; virtual void move() = 0; };` and `class Fish : public Animal { void move() {…} };` — can you write `Fish f;`?
:::ans
**No** — `Fish` didn't override `sound()`, so it's still abstract.
:::
:::

:::q Q2 · Can you declare `Shape *p;` if `Shape` is abstract?
:::ans
**Yes** — pointers and references to abstract classes are allowed (that's how polymorphism uses them); only creating objects is forbidden.
:::
:::
