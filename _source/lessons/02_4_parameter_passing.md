**Parameter passing decides whether a function works on a *copy* of your data or on the *original*.** C++ offers three ways: by value, by reference and by address (pointer).

## The Problem: The swap() That Doesn't Swap

Here's a function every beginner writes:

```cpp
#include <iostream>
using namespace std;

void swap1(int a, int b)
{
    int t = a; a = b; b = t;
    cout << "inside: a=" << a << " b=" << b << endl;
}

int main()
{
    int x = 1, y = 2;
    swap1(x, y);
    cout << "outside: x=" << x << " y=" << y << endl;
    return 0;
}
```

```output
inside: a=2 b=1
outside: x=1 y=2
```

Inside the function, the values *are* swapped… but `x` and `y` in `main` are untouched! Why? Because `a` and `b` were **copies**.

## The Three Ways

:::analogy
- **Call by value** = giving a friend a **photocopy** of your notes. They can scribble all over it; your original notes are unchanged.
- **Call by reference** = handing over **your actual notebook**. Whatever they write, you'll see.
- **Call by address (pointer)** = giving them **your home address**; they go to your house and edit the notebook there.
:::

```cpp
#include <iostream>
using namespace std;

void byValue(int a, int b)       { int t = a; a = b; b = t; }      // works on copies
void byReference(int &a, int &b) { int t = a; a = b; b = t; }      // a, b ARE x, y
void byPointer(int *a, int *b)   { int t = *a; *a = *b; *b = t; }  // a, b hold addresses

int main()
{
    int x = 1, y = 2;
    byValue(x, y);
    cout << "after byValue:     " << x << " " << y << endl;
    byReference(x, y);
    cout << "after byReference: " << x << " " << y << endl;
    byPointer(&x, &y);                       // must pass ADDRESSES
    cout << "after byPointer:   " << x << " " << y << endl;
    return 0;
}
```

```output
after byValue:     1 2
after byReference: 2 1
after byPointer:   1 2
```

(The last line swapped them back, so it shows 1 2 again.)

## How Each One Works in Memory

```text
Call by value:            main: x=1  y=2        swap: a=1  b=2   (separate copies)
Call by reference:        main: x=1  y=2  ◄──── swap: a,b are just new NAMES for x,y
Call by address:          main: x=1  y=2  ◄──── swap: a=&x  b=&y (they hold addresses)
```

| | By value | By reference | By address |
|---|---|---|---|
| Parameter | `int a` | `int &a` | `int *a` |
| Call | `f(x)` | `f(x)` | `f(&x)` |
| Copy made? | yes, of the value | no | only of the address |
| Can change caller's variable? | **no** | **yes** | **yes** (via `*a`) |
| Can pass a literal like `f(5)`? | yes | no (unless `const &`) | no |

## const Reference: Fast *and* Safe

For big data (like objects later), copying is slow, but passing by reference lets the function change it. The best of both: **`const` reference** — no copy, and the compiler forbids changes:

```cpp
void print(const string &s);   // fast (no copy) + safe (can't modify s)
```

You'll use this constantly in Chapters 3–6.

## Returning Several Results

A function can only `return` one value. Reference parameters let it "return" more:

```cpp
#include <iostream>
using namespace std;

void minMax(const int a[], int n, int &mn, int &mx)
{
    mn = mx = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] < mn) mn = a[i];
        if (a[i] > mx) mx = a[i];
    }
}

int main()
{
    int data[5] = {4, 9, 1, 7, 3}, lo, hi;
    minMax(data, 5, lo, hi);
    cout << "min=" << lo << " max=" << hi << endl;
    return 0;
}
```

```output
min=1 max=9
```

## Arrays Are Always Passed "by Address"

When you pass an array, C++ passes only the **address of its first element**. So a function can change the caller's array, and it can't know the array's size by itself — that's why we pass `n` separately.

```cpp
#include <iostream>
using namespace std;

void doubleAll(int a[], int n)
{
    for (int i = 0; i < n; i++) a[i] *= 2;   // changes the ORIGINAL array
}

int main()
{
    int v[3] = {1, 2, 3};
    doubleAll(v, 3);
    cout << v[0] << " " << v[1] << " " << v[2] << endl;
    return 0;
}
```

```output
2 4 6
```

## Returning by Reference

A function can also *return* a reference, so the call can appear on the left of `=`. (This idea comes back for operator overloading in Chapter 4.) **Never** return a reference to a local variable — it is destroyed when the function ends.

```cpp
#include <iostream>
using namespace std;

int& element(int a[], int i) { return a[i]; }

int main()
{
    int arr[3] = {1, 2, 3};
    element(arr, 1) = 50;     // assigns to arr[1]
    cout << arr[1] << endl;
    return 0;
}
```

```output
50
```

:::key
- **By value**: function gets a copy → caller unchanged.
- **By reference** (`&`): function works on the original → caller changes.
- **By address** (`*`): pass `&x`, use `*a` inside → caller changes.
- `const &` = no copy and no modification (best for big objects).
- Arrays are always passed as addresses.
:::

:::mistakes
- Expecting a by-value `swap` to swap the caller's variables.
- Calling a reference-parameter function with a literal: `byReference(1, 2)` → error.
- Calling a pointer-parameter function without `&`: `byPointer(x, y)` → error.
- Using `sizeof(a)/sizeof(a[0])` inside a function to find an array's length — wrong (gives the pointer size).
- Returning a reference to a local variable.
:::

:::exam
- *"Explain the parameter passing techniques in C++ with a program."* → the swap program with all three + the table. (A favourite 5–8 mark question.)
- Output questions: `void f(int a, int &b) { a *= 10; b *= 10; }`.
:::

:::def
**Call by value** passes a copy of the argument, so changes inside the function do not affect the caller. **Call by reference** passes an alias of the argument, so changes affect the caller's variable. **Call by address** passes the address of the argument through a pointer, allowing the function to modify the caller's variable by dereferencing.
:::

## Quick Check

:::q Q1 · What is printed? `void f(int a, int &b){ a = a*10; b = b*10; }` with `int x=2, y=3; f(x, y); cout << x << " " << y;`
:::ans
`2 30` — `a` was a copy; `b` was a reference to `y`.
:::
:::

:::q Q2 · Why is `void show(const Student &s)` preferred over `void show(Student s)`?
:::ans
It avoids copying the whole object (faster, less memory) while `const` guarantees `show` cannot modify it.
:::
:::
