**A function is a named mini-program that does one job. You write it once and "call" it whenever you need that job done.**

## The Problem: One Giant main() Becomes a Mess

Imagine a result-processing program written entirely inside `main()`: reading marks, computing totals, deciding grades, printing a report — 300 lines in one block. Now:
- The "compute grade" logic is needed in three places → you copy-paste it three times.
- A bug in the grade logic must be fixed in all three copies.
- Nobody can read the program from top to bottom and understand it.

The fix is to break the program into **subprograms** — in C++, **functions** — each doing one clear job.

## Top-Down Design: Break Big Problems into Small Ones

**Top-down design** (also called **stepwise refinement** or **divide and conquer**) means: start from the big task, split it into sub-tasks, split those again, until each piece is small enough to be one function.

```text
Prepare Result Report
├── Read student data
│     ├── read name
│     └── read marks of 3 subjects
├── Compute result
│     ├── compute total
│     ├── compute percentage
│     └── decide grade
└── Print report
```

Each leaf becomes a function. `main()` then reads like a table of contents: `readData(); computeResult(); printReport();`

:::analogy
Organising a college fest. The organiser doesn't do everything personally. They split the work: *Food team*, *Decoration team*, *Stage team*. The food team splits further: *snacks*, *drinks*. Each small team does one job well, and the organiser just coordinates. `main()` is the organiser; functions are the teams.
:::

**Benefits of functions:** modularity (manageable pieces), **reusability** (write once, call many times), easier testing and debugging, readability, team work, and **abstraction** (callers don't need to know how a function works inside).

## Predefined (Library) Functions

C++ already comes with many ready-made functions. You just `#include` the right header:

| Header | Function | What it does | Example → result |
|---|---|---|---|
| `<cmath>` | `sqrt(x)` | square root | `sqrt(16)` → `4` |
| `<cmath>` | `pow(x, y)` | x to the power y | `pow(2, 10)` → `1024` |
| `<cmath>` | `ceil(x)`, `floor(x)` | round up / down | `ceil(4.2)` → `5`, `floor(4.8)` → `4` |
| `<cstdlib>` | `abs(n)` | absolute value | `abs(-7)` → `7` |
| `<cctype>` | `toupper(c)`, `tolower(c)` | change case (**returns `int`!**) | `char(toupper('a'))` → `A` |
| `<cctype>` | `isdigit(c)`, `isalpha(c)` | test a character | `isdigit('7')` → true |
| `<cstring>` | `strlen(s)` | length of a C-string | `strlen("Pune")` → `4` |

```cpp
#include <iostream>
#include <cmath>
#include <cctype>
using namespace std;

int main()
{
    cout << sqrt(16) << " " << pow(2, 10) << " " << ceil(4.2) << " " << floor(4.8) << endl;
    cout << toupper('a') << " " << char(toupper('a')) << endl;   // 65 vs A !
    return 0;
}
```

```output
4 1024 5 4
65 A
```

## Writing Your Own Functions

A user-defined function has three parts:

```cpp
#include <iostream>
using namespace std;

int add(int a, int b);            // 1. DECLARATION (prototype): name, return type, parameter types

int main()
{
    int s = add(3, 4);            // 3. CALL: 3 and 4 are the ARGUMENTS (actual parameters)
    cout << "Sum = " << s << endl;
    cout << add(add(1, 2), 10) << endl;   // a call can be used inside another call
    return 0;
}

int add(int a, int b)             // 2. DEFINITION: a and b are the PARAMETERS (formal parameters)
{
    return a + b;                 // send the result back to the caller
}
```

```output
Sum = 7
13
```

**What happens during a call, step by step:**
1. `main` reaches `add(3, 4)` and pauses.
2. The values 3 and 4 are copied into the parameters `a` and `b`.
3. The body of `add` runs; `return a + b;` sends 7 back.
4. `main` resumes, using 7 in place of the call.

- **Return type** — the type of the value sent back (`int`, `double`, …). Use `void` if nothing is returned.
- **Prototype** — needed when the function is defined *after* it is used, so the compiler knows it exists.

## Procedural Abstraction: Functions as Black Boxes

**Procedural abstraction** means using a function knowing only **what** it does, not **how** it does it. The details are hidden inside the function body.

```cpp
#include <iostream>
using namespace std;

// Precondition : n >= 0
// Postcondition: returns n! (n factorial)
long long factorial(int n)
{
    long long f = 1;
    for (int i = 2; i <= n; i++) f *= i;
    return f;
}

int main()
{
    cout << "5! = " << factorial(5) << endl;   // main doesn't care HOW it's computed
    return 0;
}
```

```output
5! = 120
```

The comment states the function's **contract**:
- **Precondition** — what must be true *before* calling (n ≥ 0).
- **Postcondition** — what will be true *after* the call (returns n!).

If you later rewrite `factorial` using recursion, `main` doesn't change at all. That's the power of abstraction — and it's the seed of OOP's *data* abstraction (Chapter 3).

:::analogy
A TV remote. You know pressing "Vol +" makes it louder — that's the **what**. You have no idea about the circuits inside — the **how**. If the manufacturer redesigns the circuit, you still press the same button.
:::

## Functions Calling Functions

Functions can call other functions, which can call others. Each call gets its own little workspace (a **stack frame**) holding its parameters and local variables. When a function finishes, its frame is removed and control returns to the caller — last called, first finished, like a stack of plates.

```cpp
#include <iostream>
using namespace std;

int square(int x) { return x * x; }

int sumOfSquares(int a, int b)
{
    return square(a) + square(b);    // this function calls another function
}

int main()
{
    cout << sumOfSquares(3, 4) << endl;   // main -> sumOfSquares -> square
    return 0;
}
```

```output
25
```

:::key
- Top-down design splits a big problem into functions; `main` becomes a short coordinator.
- A function has a **declaration** (prototype), a **definition** (body) and **calls**.
- Parameters (in the definition) receive the arguments (in the call).
- Procedural abstraction = know *what*, hide *how*; document with pre/postconditions.
:::

:::mistakes
- Calling a function before it's declared → "not declared in this scope". Add a prototype.
- Putting a `;` after the definition's header: `int add(int a, int b); { … }`.
- Writing `int add(int a, b)` — each parameter needs its own type.
- A non-void function that can end without `return` → garbage result.
- `return a, b;` does **not** return two values (it returns `b`).
- `cout << toupper('a')` prints `65` because `toupper` returns `int`.
:::

:::exam
- *"What is top-down design? What are its advantages?"*
- *"Explain function prototype, definition and call with an example."*
- *"What is procedural abstraction?"*
- *"Differentiate formal and actual parameters."*
:::

:::def
A **function** is a self-contained, named block of code that performs a specific task and can be called from other parts of the program. **Top-down design** is the technique of decomposing a problem into smaller sub-problems repeatedly until each can be solved by a simple function. **Procedural abstraction** is treating a function as a black box whose purpose is known (through its name, prototype and pre/postconditions) while its implementation is hidden.
:::

## Quick Check

:::q Q1 · In `int area(int l, int b)` and the call `area(4, 5)`, which are formal and which are actual parameters?
:::ans
`l` and `b` are **formal** parameters; `4` and `5` are **actual** parameters (arguments).
:::
:::

:::q Q2 · Why do we write a function prototype?
:::ans
So the compiler knows the function's name, return type and parameter types **before** the call appears — necessary when the function is defined after it's used (e.g. below `main`).
:::
:::

:::q Q3 · Give two advantages of dividing a program into functions.
:::ans
Any two: reusability (no duplicated code), easier debugging/testing of small pieces, readability, team work, abstraction (callers needn't know details).
:::
:::
