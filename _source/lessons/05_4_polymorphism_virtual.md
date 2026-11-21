**Polymorphism means "one interface, many forms": the same function call does different things depending on which object receives it. In C++, run-time polymorphism is achieved with virtual functions.**

## The Problem: Treating Different Objects the Same Way

A drawing app holds many shapes — circles, squares, triangles — and wants to draw all of them in a loop. Ideally we'd store them all in **one** array of "shapes" and call `draw()` on each. C++ allows a **base-class pointer to point to a derived object** (a circle *is a* shape), so let's try:

```cpp
#include <iostream>
using namespace std;

class Shape  { public: void draw() { cout << "Drawing shape" << endl; } };
class Circle : public Shape { public: void draw() { cout << "Drawing circle" << endl; } };

int main()
{
    Circle c;
    Shape *p = &c;      // a Shape pointer pointing to a Circle (allowed: "upcasting")
    p->draw();          // we want "Drawing circle"...
    return 0;
}
```

```output
Drawing shape
```

It drew a generic shape! Without extra help, the compiler decides which `draw()` to call by looking at the **pointer's type** (`Shape*`) at **compile time**. This is **static (early) binding**. It doesn't know the pointer actually points to a Circle.

## The Solution: Virtual Functions

Mark the function **`virtual`** in the base class. Now the decision is made at **run time**, by looking at the **actual object** being pointed to. This is **dynamic (late) binding**.

```cpp
#include <iostream>
using namespace std;

class Shape
{
public:
    virtual void draw() { cout << "Drawing shape" << endl; }   // virtual!
    void info() { cout << "I am a shape" << endl; }             // not virtual
};

class Circle : public Shape
{
public:
    void draw() override { cout << "Drawing circle" << endl; } // override = "please check I really override"
    void info() { cout << "I am a circle" << endl; }
};

class Square : public Shape
{
public:
    void draw() override { cout << "Drawing square" << endl; }
};

void render(Shape &s) { s.draw(); }      // works for ANY shape (references are polymorphic too)

int main()
{
    Circle c; Square s; Shape g;
    Shape *list[3] = {&c, &s, &g};       // one array, different kinds of objects
    for (int i = 0; i < 3; i++)
        list[i]->draw();                 // each object draws ITSELF

    Shape *p = &c;
    p->info();                           // info() is NOT virtual → pointer type decides
    render(s);
    return 0;
}
```

```output
Drawing circle
Drawing square
Drawing shape
I am a shape
Drawing square
```

:::analogy
A school principal announces on the speaker: **"Everyone, do your job!"** — one message. The teacher teaches, the guard guards, the cook cooks. The principal doesn't need to know who is listening or check each person's role; **each person responds in their own way**. The announcement is the virtual function call; the staff are the derived objects.
:::

## Why This Is Powerful

The loop `list[i]->draw()` was written **once**. If tomorrow you add a `Triangle` class that overrides `draw()`, the loop works with triangles **without a single change**. Code written against the base class automatically works with future derived classes. This is the foundation of many design patterns in Chapter 14.

## How It Works: vtable and vptr

- Every class with virtual functions gets a hidden table — the **virtual table (vtable)** — listing the addresses of its versions of the virtual functions.
- Every object of such a class carries a hidden **virtual pointer (vptr)** pointing to its class's vtable.
- `p->draw()` becomes: follow `p` to the object → follow its vptr to the vtable → find `draw` → call it.

```text
 Circle object           Circle's vtable                Square object          Square's vtable
 ┌───────────┐           ┌──────────────────┐           ┌───────────┐          ┌──────────────────┐
 │ vptr ─────┼─────────► │ &Circle::draw    │           │ vptr ─────┼────────► │ &Square::draw    │
 │ ...data   │           └──────────────────┘           │ ...data   │          └──────────────────┘
 └───────────┘                                          └───────────┘
```

## Rules for Virtual Functions

1. Declared with `virtual` in the base class; must be a **non-static member** function.
2. Polymorphism works only through a **pointer or reference** to the base class. Calling through an object directly uses static binding.
3. The derived version must have the **same signature** (name, parameters, `const`-ness). Write `override` so the compiler catches mistakes.
4. Once virtual, always virtual — it stays virtual in all derived classes.
5. **Constructors cannot be virtual**; **destructors can and often should be** (Lesson 5.5).
6. If a derived class doesn't override it, the base version is used.

## Object Slicing: How to Lose Polymorphism

If you copy a derived object into a **base object** (by value), only the base part is copied — the rest is "sliced off". The copy is a plain base object.

```cpp
#include <iostream>
using namespace std;

class Animal { public: virtual void speak() const { cout << "..." << endl; } };
class Cat : public Animal { public: void speak() const override { cout << "Meow" << endl; } };

void byValue(Animal a)      { a.speak(); }   // sliced copy
void byRef(const Animal &a) { a.speak(); }   // polymorphic

int main()
{
    Cat c;
    byValue(c);
    byRef(c);
    return 0;
}
```

```output
...
Meow
```

**Moral:** for polymorphism, always use **pointers or references**, never pass by value.

## The Big Picture: Two Kinds of Polymorphism

```text
                        Polymorphism ("many forms")
                       /                            \
  Compile-time (static / early binding)        Run-time (dynamic / late binding)
  ├── Function overloading                     └── Virtual functions
  ├── Operator overloading                         (overriding + base pointer/reference)
  └── Templates
```

| Static (early) binding | Dynamic (late) binding |
|---|---|
| Decided at compile time | Decided at run time |
| Normal calls, overloading, calls through objects | Virtual functions via base pointer/reference |
| Faster | Slightly slower (vtable lookup) |
| Less flexible | Flexible, extensible |

:::key
- Without `virtual`, a base pointer calls the base version (static binding).
- With `virtual`, the actual object's version runs (dynamic binding) via vtable/vptr.
- Works only through pointers/references; pass-by-value slices the object.
- Polymorphism: compile-time (overloading) vs run-time (virtual functions).
:::

:::mistakes
- Forgetting `virtual` in the base and expecting the derived version through a base pointer.
- A slightly different signature in the derived class (e.g. missing `const`) → it's **not** an override. Use `override`.
- Expecting polymorphism from `Shape s = circle; s.draw();` — slicing + static binding.
- Saying constructors can be virtual.
:::

:::exam
- *"What is a virtual function? How is run-time polymorphism achieved? Explain with a program."* (Top question — include the "without virtual" problem, the fix, and the vtable diagram.)
- *"Differentiate compile-time and run-time polymorphism / early and late binding."*
- Output questions mixing virtual and non-virtual calls through base pointers.
:::

:::def
**Polymorphism** is the ability of the same function call or operator to behave differently depending on the type of the object it is applied to. A **virtual function** is a member function declared with the keyword `virtual` in a base class and overridden in derived classes, such that a call through a base-class pointer or reference is resolved at run time according to the actual object type (**dynamic/late binding**).
:::

## Quick Check

:::q Q1 · `Base` has `virtual void f()` and non-virtual `void g()`; `Derived` overrides both. With `Base *p = new Derived;`, which versions do `p->f()` and `p->g()` call?
:::ans
`p->f()` → **Derived::f** (virtual, dynamic binding). `p->g()` → **Base::g** (non-virtual, static binding by pointer type).
:::
:::

:::q Q2 · What is object slicing and how do you avoid it?
:::ans
When a derived object is copied into a base-class **object** (by value), the derived part is cut off and polymorphism is lost. Avoid it by using base-class **pointers or references**.
:::
:::
