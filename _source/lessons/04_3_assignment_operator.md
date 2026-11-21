**The assignment operator `=` copies one *existing* object into another *existing* object. Like the copy constructor, the default version is shallow — so classes that own memory must overload it.**

## The Problem: The Copy Constructor Isn't Enough

The copy constructor handles `Text b = a;` (creating `b`). But what about this?

```cpp
Text a("Hello"), b("World");
b = a;          // b ALREADY exists and already owns memory holding "World"
```

The default `operator=` copies the pointer: now `b` points to `a`'s memory, **`b`'s old memory ("World") is leaked**, and both objects will delete the same memory at the end. Assignment has *one extra job* compared to the copy constructor: **throw away the old contents first**.

:::analogy
The copy constructor is like **moving into a new, empty flat** and furnishing it as a copy of a friend's flat. Assignment is like **redecorating a flat you already live in**: first you must clear out your old furniture, *then* bring in copies of the friend's. And if someone asks you to "redecorate your flat to look like your own flat", you should do nothing at all — otherwise you'd throw out your furniture and have nothing left to copy!
:::

## The Recipe for operator=

```text
ClassName& operator=(const ClassName &other)
{
    if (this != &other)        // 1. self-assignment check (a = a)
    {
        // 2. release the old resource
        // 3. allocate new memory and copy other's contents
    }
    return *this;              // 4. return *this so that a = b = c works
}
```

```cpp
#include <iostream>
#include <cstring>
using namespace std;

class Text
{
    char *s;
public:
    Text(const char *str = "")
    {
        s = new char[strlen(str) + 1];
        strcpy(s, str);
    }
    Text(const Text &t)                       // copy constructor: NEW object
    {
        s = new char[strlen(t.s) + 1];
        strcpy(s, t.s);
        cout << "copy ctor" << endl;
    }
    Text& operator=(const Text &t)            // assignment: EXISTING object
    {
        cout << "operator=" << endl;
        if (this != &t)                       // 1. not assigning to myself?
        {
            delete[] s;                       // 2. free the old text
            s = new char[strlen(t.s) + 1];    // 3. allocate + copy
            strcpy(s, t.s);
        }
        return *this;                         // 4. allow chaining
    }
    ~Text() { delete[] s; }
    void show() const { cout << s << endl; }
};

int main()
{
    Text a("Hello"), b("World"), c;
    Text d = a;        // copy constructor (d is being created)
    c = b;             // operator=        (c already exists)
    a = b = d;         // operator= twice, right to left: b = d, then a = b
    a.show(); b.show(); c.show(); d.show();
    return 0;
}
```

```output
copy ctor
operator=
operator=
operator=
Hello
Hello
World
Hello
```

## Copy Constructor vs Assignment Operator

| Copy constructor | Assignment operator |
|---|---|
| Creates a **new** object from an existing one | Copies into an **already existing** object |
| `X b = a;`, `X b(a);`, pass by value | `b = a;` |
| Nothing old to clean up | Must free the **old** resource first |
| No self-assignment problem | Must check `this != &other` |
| No return value (it's a constructor) | Returns `X&` (`*this`) for chaining |

**How to tell them apart in code:** if the line **declares** the object (`Text d = a;`), it's the copy constructor — even though there's an `=` sign. If the object **already existed** (`c = b;`), it's assignment.

:::note The Rule of Three
If a class needs a custom **destructor**, **copy constructor**, or **copy assignment operator**, it almost certainly needs **all three** — because all three exist to manage the same resource (like heap memory).
:::

:::key
- `operator=` copies into an existing object: check self-assignment, free old, copy new, `return *this`.
- `X b = a;` → copy constructor; `b = a;` (b exists) → assignment.
- Rule of Three: destructor, copy constructor, assignment operator go together.
:::

:::mistakes
- Forgetting the self-assignment check: `a = a;` would delete the data and then copy from deleted memory.
- Returning `void` → `a = b = c;` won't compile.
- Forgetting to free the old memory → leak.
- Thinking `Text d = a;` calls `operator=` because it has an `=` sign.
:::

:::exam
- *"Explain overloading of the assignment operator with a program. Why is a self-assignment check needed?"*
- *"Differentiate copy constructor and assignment operator."* → the table.
:::

:::def
The **overloaded assignment operator** (`ClassName& operator=(const ClassName &)`) copies the contents of one existing object into another existing object of the same class. A user-defined version is needed for classes that manage dynamic resources, to release the old resource, perform a deep copy, guard against self-assignment, and return `*this` to allow chained assignment.
:::

## Quick Check

:::q Q1 · Copy constructor or assignment? (a) `Text t = s;` (b) `t = s;` (c) `Text t(s);` (d) `show(s)` where `show(Text x)`
:::ans
(a) copy constructor, (b) assignment, (c) copy constructor, (d) copy constructor (pass by value).
:::
:::

:::q Q2 · Why does `operator=` return `*this` by reference?
:::ans
So the result can be used in a further assignment — chaining like `a = b = c;` — without making extra copies.
:::
:::
