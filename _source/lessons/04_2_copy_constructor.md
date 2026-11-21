**A copy constructor creates a new object as a copy of an existing one. The default copy is "shallow" — and for objects that own heap memory, that's a disaster unless you write a "deep" copy yourself.**

## The Problem: Two Objects Sharing One Notebook

Look at a class that owns heap memory (like the `Name` class from Lesson 3.8). When you write `Marks b = a;`, C++ copies every data member of `a` into `b`. For a pointer member, that copies **the address**, not the data it points to:

```text
 Shallow copy (what C++ does by default)
   a.data ─┐
           ├──►  [ 90 | 0 | 0 ]        ONE array, two owners!
   b.data ─┘

   - change b's marks → a's marks change too (surprise!)
   - when both objects die, both destructors delete[] the SAME array → crash (double delete)
```

:::analogy
Two roommates who "copied" a notebook by just writing down **where** the notebook is kept. Now they both scribble in the same notebook, and when one moves out and throws it away, the other one's notes vanish too. A **deep copy** means actually photocopying every page into a **new** notebook.
:::

## Understanding the Copy Constructor

```cpp
ClassName(const ClassName &other);
```

It runs when a **new** object is created from an existing one:
1. **Initialization**: `Box b = a;`, `Box b(a);`
2. **Passing an object by value** to a function.
3. **Returning an object by value** (often optimised away by the compiler — "copy elision" — so you may not see it).

It does **not** run for `b = a;` when `b` already exists — that's the **assignment operator** (next lesson).

### Why must the parameter be a reference?

If it were `Box(Box other)` (by value), then passing `other` would need a copy… which calls the copy constructor… which needs a copy… forever. So C++ requires a reference. `const` is added because copying shouldn't change the source.

## Seeing When It's Called

```cpp
#include <iostream>
using namespace std;

class Box
{
    int len;
public:
    Box(int l) : len(l)            { cout << "Param ctor " << len << endl; }
    Box(const Box &b) : len(b.len) { cout << "Copy ctor " << len << endl; }
};

void byValue(Box b)      { cout << "inside byValue" << endl; }
void byRef(const Box &b) { cout << "inside byRef" << endl; }

int main()
{
    Box a(10);
    Box b = a;       // copy ctor
    Box c(a);        // copy ctor
    byValue(a);      // copy ctor (the parameter is a new copy)
    byRef(a);        // NO copy
    b = c;           // NOT the copy ctor — that's assignment
    return 0;
}
```

```output
Param ctor 10
Copy ctor 10
Copy ctor 10
Copy ctor 10
inside byValue
inside byRef
```

## Writing a Deep Copy Constructor

The fix for the shared-notebook problem: allocate **new** memory and copy the **contents**.

```cpp
#include <iostream>
using namespace std;

class Marks
{
    int *data;
    int n;
public:
    Marks(int size) : n(size)
    {
        data = new int[n];
        for (int i = 0; i < n; i++) data[i] = 0;
    }
    Marks(const Marks &other) : n(other.n)      // DEEP copy constructor
    {
        data = new int[n];                       // step 1: new memory of our own
        for (int i = 0; i < n; i++)              // step 2: copy the values
            data[i] = other.data[i];
    }
    ~Marks() { delete[] data; }
    void set(int i, int v) { data[i] = v; }
    int get(int i) const { return data[i]; }
};

int main()
{
    Marks a(3);
    a.set(0, 90);
    Marks b = a;              // deep copy: b gets its OWN array
    b.set(0, 50);             // only b changes
    cout << a.get(0) << " " << b.get(0) << endl;
    return 0;                 // two destructors free two DIFFERENT arrays: safe
}
```

```output
90 50
```

With the default (shallow) copy constructor, this would print `50 50` and then crash with a double delete.

| Shallow copy | Deep copy |
|---|---|
| Copies member values as they are (pointer → same address) | Allocates new memory and copies the pointed-to data |
| Done by the compiler-generated copy constructor | Needs a user-defined copy constructor |
| Objects share heap memory → side effects + double delete | Each object owns independent memory |
| Fine for classes without pointers/resources | Needed for classes that own heap memory |

:::key
- Copy constructor `X(const X&)` builds a new object from an existing one.
- Called on initialization from an object and on pass-by-value (and return-by-value, unless elided).
- Parameter must be a reference (by value → infinite recursion).
- Default = shallow copy; classes with pointer members need a deep copy.
:::

:::mistakes
- Writing the parameter by value: `Box(Box b)` → compile error.
- Thinking `b = a;` (both existing) calls the copy constructor.
- Forgetting that passing by value calls the copy constructor (count them in output questions!).
- Relying on the default copy for classes with `new`-ed memory.
:::

:::exam
- *"What is a copy constructor? When is it invoked? Why is its argument a reference?"*
- *"Differentiate shallow copy and deep copy with a program."*
- *"How many times is the copy constructor called?"* output questions.
:::

:::def
A **copy constructor** is a constructor that initializes a new object using an existing object of the same class; its parameter is a reference to the class type, typically `ClassName(const ClassName &obj)`. A **shallow copy** copies member values directly (so pointer members share the same memory); a **deep copy** allocates separate memory and copies the data it points to.
:::

## Quick Check

:::q Q1 · How many copy-constructor calls? `A a1; A a2 = a1; A a3(a2); f(a1); g(a1); a3 = a1;` where `f(A x)` and `g(A &x)`.
:::ans
**3** — `a2 = a1` (initialization), `a3(a2)`, and `f(a1)` (pass by value). `g` takes a reference; `a3 = a1` is assignment.
:::
:::

:::q Q2 · When does a class need a user-defined copy constructor?
:::ans
When it owns a resource through a pointer (heap memory, file handle…), so the default shallow copy would make two objects share and double-free it.
:::
:::
