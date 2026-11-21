**`cout` sends data to the screen and `cin` reads data from the keyboard. The arrows `<<` and `>>` show the direction the data flows.**

## The Problem: A Program That Can't Talk Is Useless

A program that always works on fixed numbers isn't very useful. We need to **ask the user** for input (marks, name, choice) and **show** them results. C++ does this with **streams**.

## Understanding Streams

A **stream** is a flow of characters, like water through a pipe:
- `cout` (*console output*) is a pipe that flows **to the screen**.
- `cin` (*console input*) is a pipe that flows **from the keyboard**.
- `<<` is the **insertion operator** — it *inserts* data into the output stream.
- `>>` is the **extraction operator** — it *extracts* data from the input stream into a variable.

:::analogy
Picture two conveyor belts. On the **output belt** you *put* items with `<<` and they travel to the screen. From the **input belt** you *take* items off with `>>` and place them into your variables. The arrows always point the way the items travel: `cout << x` (x goes **to** cout), `cin >> x` (data goes **into** x).
:::

## Output with cout

You can chain many items in one statement:

```cpp
#include <iostream>
using namespace std;

int main()
{
    int marks = 85;
    cout << "Marks: " << marks << endl;      // text, then a variable, then newline
    cout << "Line one\n";                     // \n also starts a new line
    cout << "Tab\tseparated" << endl;
    cout << "She said \"Hi\"" << endl;        // \" prints a double quote
    return 0;
}
```

```output
Marks: 85
Line one
Tab	separated
She said "Hi"
```

**Escape sequences** are special characters written with a backslash:

| Sequence | Meaning |
|---|---|
| `\n` | new line |
| `\t` | tab |
| `\"` | double quote |
| `\'` | single quote |
| `\\` | backslash itself |
| `\0` | null character (marks the end of a C-string) |

**`endl` vs `'\n'`:** both move to the next line; `endl` also **flushes** the output buffer (forces the text out immediately). `'\n'` is slightly faster.

## Input with cin

```cpp
#include <iostream>
using namespace std;

int main()
{
    //@input: 21 85.5
    int age;
    double marks;
    cout << "Enter age and marks: ";
    cin >> age >> marks;                 // reads two values, separated by space/Enter
    cout << "\nAge " << age << ", marks " << marks << endl;
    return 0;
}
```

If the user types `21 85.5`:

```output
Enter age and marks: 
Age 21, marks 85.5
```

## How cin >> Actually Reads (Important!)

1. It **skips** any spaces, tabs or newlines at the start.
2. It reads characters that fit the variable's type.
3. It **stops** at the next space/tab/newline (or a character that doesn't fit).

So if you read a name with `cin >> name` and the user types `Riya Sharma`, you only get `Riya`. (To read a whole line, use `getline` — Lesson 6.2.)

:::key
- `cout << value` prints; `cin >> variable` reads.
- Chain multiple items: `cout << a << " " << b;` and `cin >> a >> b;`
- `cin >>` skips leading whitespace and stops at the next whitespace.
- `\n` = new line, `\t` = tab, `endl` = new line + flush.
:::

:::mistakes
- `cin << x` or `cout >> x` — arrows the wrong way.
- Expecting `cin >> name` to read a name with spaces.
- Forgetting that output doesn't end with a newline automatically.
- Trying to read into a literal: `cin >> 5;` is an error.
:::

:::exam
- *"Explain `cin` and `cout` with the insertion and extraction operators."* → stream idea + the two operators + small program.
- *"Differentiate `endl` and `\n`."* → both give a new line; `endl` also flushes the buffer.
:::

## Quick Check

:::q Q1 · What does this print? `cout << "A\tB\nC";`
:::ans
```text
A	B
C
```
`\t` inserts a tab between A and B; `\n` moves C to the next line.
:::
:::

:::q Q2 · The user types `  42   7`. What do `a` and `b` contain after `cin >> a >> b;` (both `int`)?
:::ans
`a = 42`, `b = 7` — `cin >>` skips the extra spaces.
:::
:::
