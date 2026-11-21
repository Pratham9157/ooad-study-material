**Scope answers the question "where in the program can this name be seen?" and lifetime answers "how long does this variable exist?"**

## The Problem: Name Clashes and Accidental Changes

Two functions both want a variable called `count` or `i`. Should they interfere with each other? And what if some function anywhere in a 5,000-line program can change the total marks — how would you ever find the bug? C++ solves this with **scope rules**.

## Local Variables

A **local variable** is declared inside a function or a block `{ }`. It:
- is **visible only inside that block**,
- is **created** when the block starts and **destroyed** when it ends,
- starts with a **garbage** value unless you initialize it.

Because each function's locals are private, two functions can both have an `i` without any conflict.

## Global Variables

A **global variable** is declared outside all functions. It is visible to every function after its declaration and exists for the whole program run. Convenient — but dangerous: any function can change it, so bugs are hard to trace. Use them sparingly.

## Shadowing and the Scope Resolution Operator `::`

If a local variable has the same name as a global, the local one **hides (shadows)** the global inside its block. To reach the global anyway, write `::name`.

```cpp
#include <iostream>
using namespace std;

int x = 100;                  // global

void show()
{
    int y = 5;                // local to show()
    cout << "show: x=" << x << " y=" << y << endl;    // sees the global x
}

int main()
{
    int x = 10;               // local x hides the global x
    cout << "local x = " << x << ", global x = " << ::x << endl;
    {
        int x = 1;            // an inner block can hide it again
        cout << "inner x = " << x << endl;
    }
    cout << "back in main x = " << x << endl;
    show();
    return 0;
}
```

```output
local x = 10, global x = 100
inner x = 1
back in main x = 10
show: x=100 y=5
```

:::analogy
Names inside a family. At home, "Dad" means *your* dad (local). At a family reunion, there are many dads — each family's "Dad" refers to their own. And "The Prime Minister" means the same person to everyone in the country (global). If someone at home is nicknamed "Prime Minister", that nickname hides the real one at home — unless you clearly say "*the country's* Prime Minister" (`::`).
:::

## Static Local Variables: A Local That Remembers

A **`static` local variable** is still visible only inside its function, but it is created **once** and **keeps its value between calls**.

```cpp
#include <iostream>
using namespace std;

void counter()
{
    int a = 0;            // re-created on every call
    static int s = 0;     // created and initialized only ONCE
    a++; s++;
    cout << "a=" << a << " s=" << s << endl;
}

int main()
{
    counter(); counter(); counter();
    return 0;
}
```

```output
a=1 s=1
a=1 s=2
a=1 s=3
```

## Summary Table: Storage Classes

| Kind | Where declared | Visible in (scope) | Lives for (lifetime) | Default value |
|---|---|---|---|---|
| Local (automatic) | inside a block | that block | that block | garbage |
| Static local | inside a block with `static` | that block | whole program | 0 |
| Global | outside all functions | whole file (after declaration) | whole program | 0 |

:::key
- Local = visible and alive only inside its block. Global = visible everywhere, alive always.
- A local name hides a global one; `::name` reaches the global.
- `static` locals keep their value between calls.
- Prefer locals; globals make bugs hard to trace.
:::

:::mistakes
- Using a variable outside its block (e.g. a `for` loop's `i` after the loop).
- Expecting a normal local to keep its value between calls — only `static` locals do.
- Thinking `::x` means "the variable in the enclosing block" — it always means the **global**.
:::

:::exam
- Output questions mixing global, local, inner-block and `::` variables.
- *"Differentiate local and global variables."* / *"What is a static variable?"*
:::

:::def
The **scope** of an identifier is the region of the program in which it is visible. A **local variable** is declared within a block and is accessible only inside it; a **global variable** is declared outside all functions and is accessible throughout the program. A **static local variable** has local scope but exists for the entire program and retains its value between function calls.
:::

## Quick Check

:::q Q1 · What is printed? `int c(){ static int n = 10; return n++; }` called three times as `cout << c() << c() << c();` on separate statements.
:::ans
`10`, `11`, `12` — the static `n` keeps its value; `n++` returns the old value.
:::
:::

:::q Q2 · Inside a function that has a local `int total`, how do you print the global `total`?
:::ans
`cout << ::total;`
:::
:::
