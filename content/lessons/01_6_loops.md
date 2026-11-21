**A loop repeats a block of code while a condition stays true. Instead of writing the same line 100 times, you write it once and loop.**

## The Problem: Repetition by Hand Doesn't Scale

Print the numbers 1 to 5? Five `cout` lines. Print 1 to 10,000? Impossible by hand. Sum the marks of 60 students? Read until the user enters -1? We need **repetition**.

## The Four Parts of Every Loop

Every correct loop has:
1. **Initialization** — set up a control variable (`i = 1`).
2. **Condition** — decide whether to run again (`i <= 5`).
3. **Body** — the work to repeat.
4. **Update** — change the control variable so the loop eventually stops (`i++`).

Forget the update and the loop never ends (an **infinite loop**).

:::analogy
Climbing stairs: you start on step 1 (initialization), you keep climbing while you're not at the top (condition), each time you take a step (body) and move up one (update). Forget to move up and you'd "climb" forever on the same step.
:::

## 1. The while Loop — "check first, then do"

```cpp
#include <iostream>
using namespace std;

int main()
{
    int n = 1234, sum = 0;
    while (n > 0)          // condition checked BEFORE each iteration
    {
        sum += n % 10;     // take the last digit
        n /= 10;           // remove the last digit
    }
    cout << "Sum of digits = " << sum << endl;
    return 0;
}
```

```output
Sum of digits = 10
```

Trace it: n = 1234 → add 4 → n = 123 → add 3 → n = 12 → add 2 → n = 1 → add 1 → n = 0 → stop. Sum = 10.

## 2. The do-while Loop — "do first, then check"

The body runs **at least once**, because the condition is checked at the end. Perfect for menus ("show the menu, then ask whether to repeat").

```cpp
#include <iostream>
using namespace std;

int main()
{
    int i = 10;
    do {
        cout << "Runs once even though 10 < 5 is false" << endl;
    } while (i < 5);                       // <- note the semicolon

    //@input: 1 2 0
    int choice;
    do {
        cout << "Menu 1/2, 0 to exit: ";
        cin >> choice;
        cout << "You chose " << choice << endl;
    } while (choice != 0);
    return 0;
}
```

With input `1 2 0`:

```output
Runs once even though 10 < 5 is false
Menu 1/2, 0 to exit: You chose 1
Menu 1/2, 0 to exit: You chose 2
Menu 1/2, 0 to exit: You chose 0
```

## 3. The for Loop — "count from here to there"

All four loop parts in one line: `for (initialization; condition; update) { body }`.
Order of execution: **init (once) → check → body → update → check → body → update → … → check fails → exit.**

```cpp
#include <iostream>
using namespace std;

int main()
{
    for (int i = 1; i <= 5; i++)
        cout << i * i << " ";             // squares
    cout << endl;

    long long fact = 1;
    for (int i = 1; i <= 10; i++) fact *= i;
    cout << "10! = " << fact << endl;
    return 0;
}
```

```output
1 4 9 16 25 
10! = 3628800
```

| | Entry-controlled (`while`, `for`) | Exit-controlled (`do-while`) |
|---|---|---|
| Condition checked | **before** the body | **after** the body |
| Minimum runs | 0 | 1 |
| Typical use | counting, reading until a value | menus, input validation |

## 4. break and continue

- `break` — **leave the loop immediately**.
- `continue` — **skip the rest of this iteration**, jump to the next one.

```cpp
#include <iostream>
using namespace std;

int main()
{
    for (int i = 1; i <= 10; i++)
    {
        if (i % 2 == 0) continue;   // skip even numbers
        if (i > 7) break;           // stop completely after 7
        cout << i << " ";
    }
    cout << endl;
    return 0;
}
```

```output
1 3 5 7 
```

## 5. Nested Loops and Patterns

A loop inside a loop: for **each** turn of the outer loop, the inner loop runs **completely**. Think of a clock — the minute hand goes all the way around for every single move of the hour hand. This is how we print patterns (rows × columns).

```cpp
#include <iostream>
using namespace std;

int main()
{
    for (int row = 1; row <= 4; row++)
    {
        for (int col = 1; col <= row; col++)   // row 1 has 1 star, row 2 has 2 ...
            cout << "* ";
        cout << endl;
    }
    return 0;
}
```

```output
* 
* * 
* * * 
* * * * 
```

## 6. Designing Loops: Which Loop When?

| Situation | Loop style | Example |
|---|---|---|
| You know how many times | **counter-controlled** → `for` | print the table of 7 |
| Repeat until a special "stop" value | **sentinel-controlled** → `while` | read marks until -1 |
| Repeat until something becomes true | **flag-controlled** → `while` with a `bool` | search until found |
| Must run at least once | `do-while` | menus |

```cpp
#include <iostream>
using namespace std;

int main()
{
    //@input: 70 85 90 -1
    int m, sum = 0, count = 0;
    cin >> m;                    // read the first value BEFORE the loop
    while (m != -1)              // -1 is the sentinel (stop signal)
    {
        sum += m;
        count++;
        cin >> m;                // read the next value (the "update")
    }
    cout << "Average = " << static_cast<double>(sum) / count << endl;

    int n = 29;                  // flag-controlled: is n prime?
    bool isPrime = true;
    for (int d = 2; d * d <= n && isPrime; d++)
        if (n % d == 0) isPrime = false;
    cout << n << (isPrime ? " is prime" : " is not prime") << endl;
    return 0;
}
```

With input `70 85 90 -1`:

```output
Average = 81.6667
29 is prime
```

**Loop design checklist:** check the **first** iteration, the **last** iteration, and the case where the loop runs **zero** times. This catches "off-by-one" errors (`<` vs `<=`).

:::key
- Loop = initialization + condition + body + update.
- `while`/`for` check first (may run 0 times); `do-while` checks last (runs at least once).
- `break` exits the innermost loop; `continue` skips to the next iteration.
- Inner loop completes fully for each outer iteration.
- Choose counter-, sentinel- or flag-controlled designs based on the problem.
:::

:::mistakes
- `for (i = 0; i < 5; i++);` — the semicolon makes an **empty** loop body.
- Missing `;` after `} while (cond)`.
- Forgetting the update → infinite loop.
- `<=` vs `<` off-by-one errors.
- Thinking `break` exits **all** nested loops — only the innermost.
- Using a loop variable declared in `for (int i…)` after the loop — it no longer exists.
:::

:::exam
- *"Differentiate entry-controlled and exit-controlled loops."* → the table.
- *Output questions* with `break`/`continue`, nested loops, stray semicolons.
- *Programs:* sum of digits, reverse a number, palindrome, factorial, prime check, patterns, Fibonacci series.
:::

:::def
A **loop** is a control structure that repeatedly executes a block of statements as long as a condition is true. `while` and `for` are **entry-controlled** loops (condition tested before the body); `do-while` is an **exit-controlled** loop (condition tested after the body, so the body executes at least once).
:::

## Quick Check

:::q Q1 · How many times does `Hi` print? `int i = 5; while (i < 5) { cout << "Hi"; i++; }`
:::ans
**0 times** — the condition is false at the start, and `while` checks first.
:::
:::

:::q Q2 · What is printed? `for (int i = 1; i <= 3; i++) for (int j = 1; j <= 3; j++) { if (j == 2) break; cout << i << j << " "; }`
:::ans
`11 21 31` — `break` only leaves the inner loop.
:::
:::

:::q Q3 · Which loop is best for a menu that must appear at least once? Why?
:::ans
`do-while` — it is exit-controlled, so the body (showing the menu) runs at least once before the condition is checked.
:::
:::
