**Decision statements let a program choose different paths depending on conditions — just like you decide "if it's raining, take an umbrella; otherwise don't".**

## The Problem: One Path Doesn't Fit All

So far our programs ran every line from top to bottom. But real programs must react: a student with 92 marks gets grade A, one with 45 fails; an ATM gives cash only if the balance is enough. We need **selection** (branching).

Every program is built from three basic structures — **sequence** (one after another), **selection** (choose a path) and **repetition** (loops, next lesson). Together they are called the **flow of control**.

## Boolean Expressions: The Questions We Ask

A **Boolean expression** has the answer true or false: `marks >= 40`, `balance > amount && pin == 1234`.

In C++, **any non-zero value counts as true, and only 0 is false**. So `if (5)` and even `if (-3)` are true.

Two useful laws (De Morgan) for rewriting conditions:
- `!(A && B)` is the same as `!A || !B`
- `!(A || B)` is the same as `!A && !B`

## 1. The if Statement

```text
if (condition)              if (condition)                 if (c1)       ... else if (c2) ... else ...
    statement;                  statement1;                (first true condition wins, the rest are skipped)
                            else
                                statement2;
```

```cpp
#include <iostream>
using namespace std;

int main()
{
    int marks = 72;
    if (marks >= 90)
        cout << "Grade A" << endl;
    else if (marks >= 75)
        cout << "Grade B" << endl;
    else if (marks >= 60)
        cout << "Grade C" << endl;      // 72 >= 60 is the first true test
    else
        cout << "Fail" << endl;

    int n = -4;
    if (n >= 0) {                       // a NESTED if: an if inside another if
        if (n % 2 == 0) cout << "positive even" << endl;
        else            cout << "positive odd" << endl;
    } else {
        cout << "negative" << endl;
    }
    return 0;
}
```

```output
Grade C
negative
```

**Use braces `{ }`** whenever a branch has more than one statement. Without braces, only the **first** statement belongs to the `if`.

### The "dangling else" trap

When there are two `if`s and one `else`, the `else` belongs to the **nearest** unmatched `if` — no matter how you indent it.

```cpp
#include <iostream>
using namespace std;

int main()
{
    int a = 5, b = 2;
    if (a > 10)
        if (b > 1)
            cout << "X" << endl;
    else                        // looks like it belongs to if (a > 10)... but it doesn't!
        cout << "Y" << endl;
    cout << "done" << endl;     // a > 10 is false, so the whole inner part is skipped
    return 0;
}
```

```output
done
```

## 2. The switch Statement — A Multiway Branch

When you compare **one value** against many fixed options (a menu!), `switch` is cleaner than a long if-else ladder.

:::analogy
A vending machine: press 1 → tea, 2 → coffee, 3 → juice, anything else → "invalid". The machine jumps straight to the matching button's action.
:::

```cpp
#include <iostream>
using namespace std;

int main()
{
    int choice = 2;
    switch (choice)
    {
        case 1:  cout << "Tea" << endl;    break;
        case 2:  cout << "Coffee" << endl; break;
        case 3:  cout << "Juice" << endl;  break;
        default: cout << "Invalid" << endl;
    }

    char grade = 'B';            // what happens WITHOUT break? "fall-through"
    switch (grade)
    {
        case 'A': cout << "Excellent ";
        case 'B': cout << "Good ";       // starts here...
        case 'C': cout << "Pass ";       // ...and keeps going
        default:  cout << "End";
    }
    cout << endl;
    return 0;
}
```

```output
Coffee
Good Pass End
```

**How switch works:** jump to the matching `case`, run statements **until a `break`** (or the end). Without `break`, execution *falls through* into the next cases — sometimes useful (`case 'a': case 'e': case 'i': …` for vowels), usually a bug.

**Rules of switch:**
1. The value must be an **integer-like type**: `int`, `char`, `bool`, `enum`. **Not** `float`, `double` or `string`.
2. `case` labels must be **constants** and **unique** (`case marks >= 90:` is illegal).
3. `default` is optional and runs when no case matches.

| if-else ladder | switch |
|---|---|
| Any condition: ranges, `&&`, decimals | Only "equals one of these constants" |
| Tests conditions one by one | Jumps directly to the matching case |
| Best for ranges (`marks >= 90`) | Best for menus and fixed choices |

:::key
- Only 0 is false; any non-zero value is true.
- if / else if / else: the **first** true branch runs, the rest are skipped.
- `else` pairs with the nearest unmatched `if`.
- switch works on integral types; remember `break`, or execution falls through.
:::

:::mistakes
- `if (x = 5)` instead of `if (x == 5)` — the assignment makes the condition always true.
- `if (marks > 40);` — the stray semicolon ends the if; the next line always runs.
- Missing braces around multiple statements in a branch.
- Forgetting `break` in a switch.
- Using `switch` on a `string` or `double`.
- Writing `if (ch == 'a' || 'e')` — always true because `'e'` is non-zero. Write `ch == 'a' || ch == 'e'`.
:::

:::exam
- *Output questions* with fall-through, dangling else and `if (a = 0)`.
- *"Differentiate if-else and switch."* → the table.
- *Programs:* grade calculator, largest of three numbers, menu-driven calculator.
:::

:::def
**Flow of control** is the order in which the statements of a program are executed. **Selection statements** (`if`, `if-else`, `switch`) choose which statements to execute based on a condition; `switch` is a **multiway branch** that selects one of many cases based on the value of an integral expression.
:::

## Quick Check

:::q Q1 · What is printed? `int a = 0; if (a = 0) cout << "zero"; else cout << "nonzero";`
:::ans
`nonzero` — `a = 0` assigns 0 and the condition's value is 0 (false).
:::
:::

:::q Q2 · What is printed when `n = 3`? `switch(n){ case 1: cout<<"1"; case 3: cout<<"3"; case 5: cout<<"5"; break; default: cout<<"D"; }`
:::ans
`35` — starts at case 3, falls through to case 5, then `break`.
:::
:::

:::q Q3 · Why can't `switch` be used to check `marks >= 90`?
:::ans
Case labels must be **constant values** to compare for equality; `switch` cannot test ranges or arbitrary conditions. Use an if-else ladder.
:::
:::
