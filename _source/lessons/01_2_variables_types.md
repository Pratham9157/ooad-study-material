**A variable is a named box in memory that holds a value. The data type decides what kind of value the box can hold and how big the box is.**

## The Problem: Programs Need to Remember Things

To calculate a student's percentage you need to remember their marks, the total, and the result. The computer's memory is a huge row of numbered cells — but remembering "cell number 1,048,232 holds the marks" is impossible for humans. Variables let us give memory locations **meaningful names**.

## Understanding Variables

```cpp
int marks = 85;
```

This one line does three things:
1. **Reserves memory** big enough for a whole number (`int`).
2. **Names** that memory `marks`.
3. **Stores** the value `85` in it.

Every variable has four properties: a **name** (`marks`), a **type** (`int`), a **value** (`85`) and an **address** (where it lives in memory).

:::analogy
Think of labelled storage boxes in a cupboard. The **label** is the variable's name, the **shape/size of the box** is its data type (a shoe box can't hold a guitar), and **what's inside** is its value. You can replace what's inside any time, but the box's shape stays the same.
:::

## Declaring, Initializing and Assigning

| Term | Example | What happens |
|---|---|---|
| **Declaration** | `int age;` | The box is created. Its contents are unknown (garbage)! |
| **Initialization** | `int age = 20;` | The box is created *and* filled immediately. |
| **Assignment** | `age = 21;` | An existing box gets a new value (the old one is lost). |

```cpp
#include <iostream>
using namespace std;

int main()
{
    int age = 20;          // declaration + initialization
    int marks;             // declaration only
    marks = 85;            // assignment
    int a = 5, b = 10;     // several at once

    a = b;                 // COPY b's value into a  -> a is 10
    b = 3;                 // only b changes; a stays 10
    marks = marks + 5;     // right side uses the OLD value: 85 + 5

    cout << age << " " << marks << " " << a << " " << b << endl;
    return 0;
}
```

```output
20 90 10 3
```

Notice `marks = marks + 5`. In maths this is nonsense, but in C++ `=` means **"compute the right side, then store it in the left side"**. It is an *instruction*, not an equation.

## Data Types: Choosing the Right Box

| Type | Stores | Typical size | Example |
|---|---|---|---|
| `int` | whole numbers | 4 bytes | `42`, `-7` |
| `float` | decimals (≈7 digits precision) | 4 bytes | `3.14f` |
| `double` | decimals (≈15 digits precision) — **the default for decimals** | 8 bytes | `3.14159` |
| `char` | a single character | 1 byte (always) | `'A'` |
| `bool` | true / false | 1 byte | `true` |
| `void` | "nothing" (used for functions returning nothing) | — | — |

Modifiers adjust the size/range: `short`, `long`, `long long`, `unsigned` (no negatives, bigger positive range).

:::note Sizes are "typical"
Only `char` is guaranteed to be 1 byte. Other sizes depend on the compiler/machine. Old 16-bit Turbo C++ used 2-byte `int`; modern compilers use 4 bytes. Use `sizeof(type)` to check.
:::

### Characters are secretly numbers

A `char` is stored as a number — its **ASCII code**. `'A'` is 65, `'a'` is 97, `'0'` is 48. That's why you can do arithmetic on characters:

```cpp
#include <iostream>
using namespace std;

int main()
{
    char grade = 'A';
    bool passed = true;
    double cgpa = 8.75;
    cout << grade << " " << passed << " " << cgpa << endl;  // bool prints as 1
    cout << (int)grade << endl;          // the ASCII code of 'A'
    char next = grade + 1;               // 65 + 1 = 66 = 'B'
    cout << next << endl;
    cout << "int is " << sizeof(int) << " bytes, double is " << sizeof(double) << " bytes" << endl;
    return 0;
}
```

```output
A 1 8.75
65
B
int is 4 bytes, double is 8 bytes
```

Handy ASCII facts: `'A'`–`'Z'` = 65–90, `'a'`–`'z'` = 97–122 (lowercase = uppercase + 32), `'0'`–`'9'` = 48–57.

## Constants: Values That Must Never Change

Some values should never change — like π or the maximum number of books a member may borrow. Make them **constants** so that nobody (including you) changes them by accident.

```cpp
#include <iostream>
using namespace std;

#define PI 3.14159            // old C style: text replacement, no type

int main()
{
    const int MAX_BOOKS = 5;  // C++ style: typed constant
    // MAX_BOOKS = 6;         // ERROR: cannot assign to a const
    cout << MAX_BOOKS << " " << PI << endl;
    return 0;
}
```

```output
5 3.14159
```

| `const` | `#define` |
|---|---|
| Understood by the compiler, has a type | Plain text substitution by the preprocessor |
| Type-checked, follows scope rules | No type checking, no scope |
| **Preferred in C++** | C style |

:::key
- A variable = name + type + value + address.
- `=` means "store the right side into the left side".
- Choose the type by the kind of data: `int`, `double`, `char`, `bool`.
- `char` values are ASCII numbers; `bool` prints as 1/0.
- Use `const` for values that must not change.
:::

:::mistakes
- Using a variable before giving it a value: `int x; cout << x;` prints garbage.
- `char c = "A";` — double quotes make a *string*. A char uses single quotes: `'A'`.
- Expecting `cout << true;` to print `true` — it prints `1`.
- Thinking `a = b;` links the two variables forever — it only copies the current value.
- Declaring `const int MAX;` without a value → error (a const must be initialized).
- Putting a semicolon in `#define PI 3.14;` → every `PI` becomes `3.14;`.
:::

:::exam
- *"What is a data type? Explain the built-in data types of C++."* → definition + the table + sizes "typically".
- *"Differentiate `const` and `#define`."* → the table above.
- Output questions with `char` arithmetic, e.g. `char c = 'a' - 32; cout << c;` → `A`.
:::

:::def
A **variable** is a named memory location whose value can change during program execution. A **data type** specifies the kind of data a variable can store, the memory it occupies, and the operations allowed on it.
:::

## Quick Check

:::q Q1 · What is printed? `int x = 7; int y = x; x = 10; cout << y;`
:::ans
`7` — `y = x` copied the value 7 at that moment; changing `x` later doesn't affect `y`.
:::
:::

:::q Q2 · What is printed? `char c = 'C'; cout << (int)c << " " << (char)(c + 2);`
:::ans
`67 E` — 'C' is 67; 67 + 2 = 69 = 'E'.
:::
:::

:::q Q3 · Why is `const` preferred over `#define` in C++?
:::ans
`const` has a **type** (so the compiler checks it), follows **scope** rules, and shows up in the debugger; `#define` is blind text replacement with none of these safety checks.
:::
:::
