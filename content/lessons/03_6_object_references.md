**An object reference is a way to *refer to* an existing object — through a reference or a pointer — instead of making a copy of it.** In C++ you must choose explicitly between working with a copy and working with the original.

## The Problem: "I Changed It… Why Didn't It Change?"

```cpp
#include <iostream>
using namespace std;

class Counter
{
    int value = 0;
public:
    void increment() { value++; }
    int get() { return value; }
};

void addOne(Counter c) { c.increment(); }     // looks right…

int main()
{
    Counter a;
    addOne(a);
    addOne(a);
    cout << a.get() << endl;                  // …but prints 0!
    return 0;
}
```

```output
0
```

`addOne` received a **copy** of `a`. It incremented the copy, then the copy was thrown away. To work on the real `a`, the function needs a **reference** (or pointer) to it.

## Key Idea: In C++, an Object Variable *Is* the Object

:::note C++ vs Java (why the syllabus mentions "object reference")
In **Java**, a variable of class type is always a *reference* to an object: `Student s2 = s1;` makes both names point to the **same** object.
In **C++**, a variable of class type **is the object itself**. `Student s2 = s1;` creates a **second, independent copy**. To refer to the *same* object you must explicitly use a **reference** (`Student &r = s1;`) or a **pointer** (`Student *p = &s1;`).
:::

:::analogy
A **copy** is a photocopy of a document; a **reference** is a nickname for the original document ("the contract" and "that blue file" are the same paper); a **pointer** is a note saying "the document is in drawer 3". Editing the photocopy doesn't change the original; editing via the nickname or by going to drawer 3 does.
:::

## Three Ways to Get at an Object

```cpp
#include <iostream>
using namespace std;

class Counter
{
    int value;
public:
    void set(int v) { value = v; }
    void increment() { value++; }
    int get() { return value; }
};

int main()
{
    Counter a;
    a.set(10);

    Counter b = a;        // 1. a COPY: independent object
    b.increment();
    cout << "a=" << a.get() << " b=" << b.get() << endl;

    Counter &r = a;       // 2. a REFERENCE: another name for a
    r.increment();
    cout << "a=" << a.get() << endl;

    Counter *p = &a;      // 3. a POINTER: holds a's address; use ->
    p->increment();       // same as (*p).increment()
    cout << "a=" << a.get() << endl;
    return 0;
}
```

```output
a=10 b=11
a=11
a=12
```

## Passing and Returning Objects

```cpp
#include <iostream>
using namespace std;

class Counter
{
    int value = 0;
public:
    void increment() { value++; }
    int get() const { return value; }
};

void byValue(Counter c)        { c.increment(); }   // works on a copy
void byRef(Counter &c)         { c.increment(); }   // works on the original
void byPtr(Counter *c)         { c->increment(); }  // works on the original
void show(const Counter &c)    { cout << "value = " << c.get() << endl; }  // read-only, no copy

Counter makeCounter()          // returning an object (by value)
{
    Counter c;
    c.increment();
    return c;
}

int main()
{
    Counter a;
    byValue(a); show(a);
    byRef(a);   show(a);
    byPtr(&a);  show(a);
    Counter m = makeCounter();
    show(m);

    Counter list[3];           // an ARRAY of objects
    list[2].increment();
    cout << list[0].get() << list[1].get() << list[2].get() << endl;
    return 0;
}
```

```output
value = 0
value = 1
value = 2
value = 1
001
```

**Which to choose?**

| Situation | Parameter style |
|---|---|
| Function only reads the object | `const Counter &c` (no copy, no changes) |
| Function must modify the caller's object | `Counter &c` (or `Counter *c`) |
| Function needs its own private copy | `Counter c` (by value) |
| "No object" must be a valid option | `Counter *c` (can be `nullptr`) |

:::key
- In C++, `B b = a;` **copies** the object; it does not create a second name for it.
- Use a reference (`&`) or pointer (`*`, with `->`) to refer to an existing object.
- Pass objects as `const &` to read, `&` to modify; by value only when you want a copy.
- Arrays of objects work like arrays of anything else.
:::

:::mistakes
- Java thinking: expecting `b = a;` to make both names refer to the same object.
- Using `.` with a pointer to an object (`p.increment()`) — use `p->increment()`.
- Passing by value to a function that's supposed to modify the object.
- Returning a reference or pointer to a **local** object (it dies when the function ends).
:::

:::exam
- *"Explain object reference / passing objects to functions with an example."*
- *"How are pointers to objects used? Explain the arrow operator."*
- Output questions on copy vs reference vs pointer.
:::

:::def
An **object reference** is an alias for an existing object (declared as `ClassName &ref = obj;`); operations through the reference act on the original object. Objects can also be referred to through **pointers to objects**, whose members are accessed with the arrow operator (`->`). Passing an object by reference avoids copying and allows the function to modify the original.
:::

## Quick Check

:::q Q1 · What is printed? `Counter a; Counter &r = a; Counter c = a; r.increment(); c.increment(); c.increment(); cout << a.get() << c.get();` (value starts at 0)
:::ans
`12` — `r` is `a` (a becomes 1); `c` is a separate copy (c becomes 2).
:::
:::

:::q Q2 · Write the call to `increment()` through `Counter *p = &a;` in two ways.
:::ans
`p->increment();` and `(*p).increment();`
:::
:::
