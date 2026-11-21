**A pointer is a variable that stores the *address* of another variable. A reference is simply *another name* for an existing variable.**

These two ideas are not named in your syllabus, but they are needed to understand **call by reference**, **the `this` pointer**, **copy constructors**, **dynamic memory** and **virtual functions**. So let's make them simple.

## The Problem: Sometimes You Need to Point at the Original

When you hand a value to a function, C++ normally gives it a **copy**. That's safe, but:
- What if the function *should* change your original variable (e.g. `swap(a, b)`)?
- What if the data is huge (a 10,000-element record) and copying wastes time?
- What if you want to create data while the program runs (Lesson 2.7)?

You need a way to refer to **the original** instead of a copy. Pointers and references do exactly that.

## Every Variable Lives at an Address

Memory is a long row of numbered cells. When you write `int x = 10;`, C++ picks a cell — say address `1000` — and stores 10 there.

```text
   address:   1000          2000
            ┌──────┐      ┌──────┐
       x →  │  10  │  p → │ 1000 │      p is a pointer: it holds x's ADDRESS
            └──────┘      └──────┘
```

- `&x` → "address of x" (1000).
- `int *p = &x;` → p is a pointer to an int; it stores 1000.
- `*p` → "go to the address in p and look inside" (10). This is called **dereferencing**.

:::analogy
A variable is a **house**; its address is the **house number**. A pointer is a **slip of paper with the house number written on it**. Dereferencing (`*p`) means *going to that house and looking inside*. If you repaint the house through the slip's directions, the house itself changes — not the slip.
:::

```cpp
#include <iostream>
using namespace std;

int main()
{
    int x = 10;
    int *p = &x;              // p holds x's address
    cout << "x = " << x << ", *p = " << *p << endl;
    *p = 25;                  // change x THROUGH the pointer
    cout << "x is now " << x << endl;

    int arr[3] = {5, 6, 7};
    int *q = arr;             // an array name gives the address of its first element
    cout << *q << " " << *(q + 1) << " " << q[2] << endl;   // q+1 moves ONE ELEMENT ahead

    int *np = nullptr;        // a pointer that points to nothing
    if (np == nullptr) cout << "np points nowhere" << endl;
    return 0;
}
```

```output
x = 10, *p = 10
x is now 25
5 6 7
np points nowhere
```

**The two meanings of `*`:** in a *declaration* (`int *p`) it means "p is a pointer"; in an *expression* (`*p = 25`) it means "the thing p points to".

## References: A Second Name

A **reference** is an **alias** — another name for an existing variable. Declared with `&` after the type.

```cpp
#include <iostream>
using namespace std;

int main()
{
    int x = 10;
    int &r = x;       // r is another name for x (no new memory, no copy)
    r = 20;           // changes x!
    cout << x << " " << r << endl;

    int y = 99;
    r = y;            // does NOT make r refer to y; it copies 99 INTO x
    cout << x << " " << y << endl;
    return 0;
}
```

```output
20 20
99 99
```

:::analogy
A reference is a **nickname**. If your friend "Robert" is also called "Bob", then giving Bob a gift *is* giving Robert a gift — it's the same person. And once someone is "Bob", the nickname can't be moved to another person.
:::

## Pointer vs Reference

| Pointer | Reference |
|---|---|
| Stores an address; is a separate variable | Just another name; no separate identity |
| Can be declared without a value | **Must** be initialized when declared |
| Can be changed to point elsewhere | **Cannot** be re-bound to another variable |
| Can be `nullptr` (point to nothing) | Cannot be null |
| Use `*p` to reach the value | Use `r` directly |
| Pointer arithmetic (`p + 1`) allowed | No arithmetic |

:::key
- `&x` gives x's address; `*p` gives the value at the address stored in p.
- A reference (`int &r = x;`) is an alias: changing `r` changes `x`.
- References must be initialized and can't be re-bound; pointers can be null and re-pointed.
:::

:::mistakes
- In `int *p, q;` only `p` is a pointer; `q` is a plain `int`.
- Dereferencing an uninitialized or null pointer → crash (undefined behaviour).
- `int &r;` with no initializer → compile error.
- Thinking `r = y;` re-binds the reference — it copies y's value into the original.
:::

:::exam
- *"Differentiate between pointer and reference."* → the table.
- Output questions with `*p` modifications and references.
:::

:::def
A **pointer** is a variable that holds the memory address of another variable; `&` gives an address and `*` dereferences a pointer. A **reference** is an alias (alternative name) for an existing variable; it must be initialized at declaration and cannot be made to refer to another variable.
:::

## Quick Check

:::q Q1 · What is printed? `int a = 5; int *p = &a; *p = *p * 2; cout << a;`
:::ans
`10` — `*p` is `a`, so `a` is doubled.
:::
:::

:::q Q2 · What is printed? `int a = 1, b = 2; int &r = a; r = b; r++; cout << a << b;`
:::ans
`32` — `r = b` copies 2 into `a`; `r++` makes `a` 3; `b` stays 2.
:::
:::
