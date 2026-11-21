**A computer only does exactly what you tell it, in exactly the order you tell it.** A program is that list of instructions. In this lesson you'll write your first C++ program and understand every single line of it.

## The Problem: Computers Don't Understand English

You can't tell a computer "show a greeting". It only understands machine instructions (0s and 1s). Writing those by hand is impossible for humans. So we write in a **programming language** like C++, which is readable for us, and a tool called a **compiler** translates it into machine code.

## Your First Program

```cpp
#include <iostream>
using namespace std;

int main()
{
    cout << "Hello, OOAD!" << endl;
    return 0;
}
```

```output
Hello, OOAD!
```

Six lines. Let's understand them one by one.

## Line-by-Line Explanation

**1. `#include <iostream>`** — "Bring in the tools for input and output."
C++ itself has no built-in command to print. Printing lives in a *library* (ready-made code). `iostream` = **i**nput/**o**utput **stream**. Lines starting with `#` are handled by the **preprocessor** *before* compilation — it literally pastes the library's declarations into your file.

**2. `using namespace std;`** — "I'll use the standard names without a prefix."
Everything from the standard library lives in a group (a **namespace**) called `std`. Without this line you would have to write `std::cout`. With it, just `cout`.

**3. `int main()`** — "The program starts here."
Every C++ program must have exactly **one** `main` function. When you run the program, the operating system calls `main`. The `int` means `main` gives back a whole number to the operating system when it finishes.

**4. `{ … }`** — the **body** of `main`. Everything between the braces is what `main` does. A pair of braces is called a **block**.

**5. `cout << "Hello, OOAD!" << endl;`** — "Send this text to the screen, then a new line."
`cout` (pronounced *see-out*) is the screen. `<<` means "send into". Text in double quotes is a **string**. `endl` ends the line. The **semicolon** `;` ends the statement — like a full stop ends a sentence.

**6. `return 0;`** — "Finished successfully." Returning 0 from `main` tells the OS that everything went fine.

:::analogy
A C++ program is like a recipe card. The top lines list what you borrow from the kitchen cupboard (`#include`), and then there is exactly one place marked **"START HERE"** (`main`). The cook reads the steps from top to bottom, one at a time, and each step ends with a full stop (`;`).
:::

## Comments: Notes for Humans

The compiler ignores comments; they're for people reading your code.

```cpp
#include <iostream>
using namespace std;

// This is a single-line comment
/* This is a
   multi-line comment */
int main()
{
    cout << "Comments are ignored" << endl;   // a comment can also follow code
    return 0;
}
```

```output
Comments are ignored
```

## From Code to Running Program

When you click "Run", several steps happen:

```text
 hello.cpp ──► Preprocessor ──► Compiler ──► Object code ──► Linker ──► hello.exe ──► Loader runs it
 (your code)   (handles #include)  (checks &     (.o / .obj)    (adds library            (in memory)
                                   translates)                   code like cout)
```

- **Compiler errors** (syntax errors) are caught at compile time — e.g. a missing semicolon.
- **Run-time errors** happen while running — e.g. dividing by zero.
- **Logical errors** — the program runs but gives a wrong answer (the hardest to find!).

## Tokens: The "Words" of C++

Just as a sentence is made of words and punctuation, a C++ program is made of **tokens** — the smallest units the compiler understands:

| Token type | What it is | Examples |
|---|---|---|
| **Keywords** | Reserved words with a fixed meaning | `int`, `return`, `class`, `if`, `while` |
| **Identifiers** | Names *you* choose | `marks`, `totalFine`, `Student` |
| **Literals** | Fixed values written directly | `25`, `3.14`, `'A'`, `"Hello"`, `true` |
| **Operators** | Symbols that do something | `+`, `-`, `=`, `==`, `<<`, `&&` |
| **Punctuators** | Separators | `;`, `,`, `{ }`, `( )`, `#` |

### Rules for naming identifiers

1. Use letters, digits and underscore `_` only.
2. **Cannot start with a digit** (`2marks` ❌, `marks2` ✅).
3. No spaces or symbols like `-`, `@`, `$` (`total-marks` ❌).
4. Cannot be a keyword (`float` ❌ — but `Float` ✅ because…)
5. C++ is **case-sensitive**: `total`, `Total` and `TOTAL` are three different names.

:::key
- Execution always starts at `int main()`.
- `#include <iostream>` gives you `cout`/`cin`; `using namespace std;` lets you skip `std::`.
- Every statement ends with `;`. Blocks are wrapped in `{ }`.
- Source code → preprocessor → compiler → linker → executable.
- Five token types: keywords, identifiers, literals, operators, punctuators.
:::

:::mistakes
- Writing `void main()` (an old Turbo C++ habit). Standard C++ requires `int main()`.
- Writing `#include <iostream.h>` — the `.h` version is outdated and doesn't exist in modern compilers.
- Putting a semicolon after `#include <iostream>;` — directives don't end with `;`.
- Forgetting the semicolon after a statement → compile error.
- Writing `Cout` or `Main` — C++ is case-sensitive.
- Saying `main` or `cout` is a keyword — they are identifiers (special names), not keywords.
:::

:::exam
- *"Explain the structure of a C++ program with an example."* → Write the Hello program and explain each line (header, namespace, `main`, body, statement, return).
- *"What are tokens? Explain the rules for identifiers."* → The table above + the five rules.
- MCQ: "Which is a valid identifier: `_rate2`, `2rate`, `rate-2`, `int`?" → `_rate2`.
:::

## Quick Check

:::q Q1 · Why does every C++ program need a `main()` function?
:::ans
`main()` is the **entry point** — the operating system starts running the program by calling `main`. A program without `main` cannot be linked into an executable.
:::
:::

:::q Q2 · Which of these identifiers are valid? `my_name`, `1st`, `Class`, `class`, `total$`
:::ans
Valid: `my_name`, `Class` (capital C is different from the keyword). Invalid: `1st` (starts with a digit), `class` (keyword), `total$` (`$` not allowed in standard C++).
:::
:::

:::q Q3 · What is the difference between a compile-time error and a logical error?
:::ans
A **compile-time error** breaks the language rules (e.g. missing `;`) and the program won't compile. A **logical error** compiles and runs but produces the wrong result (e.g. using `+` where you meant `*`).
:::
:::
