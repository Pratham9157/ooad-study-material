**Operators are the verbs of a program — they add, compare, combine and update values. An expression is any combination of values and operators that produces a single result.**

## The Problem: Raw Data Isn't Enough

Having marks stored in variables is only half the job. We need to *compute* totals, *compare* with the pass mark, and *combine* conditions ("passed AND attendance ≥ 75%"). Operators do all of this. Most are familiar from maths — but a few behave in surprising ways, and those surprises are exactly what exam questions love.

## 1. Arithmetic Operators: `+ - * / %`

They work as in maths, with **two surprises**:

**Surprise 1 — integer division throws away the fraction.**
When *both* sides are integers, `/` gives an integer: `7 / 2` is `3`, not `3.5`. If at least one side is a decimal, you get a decimal: `7 / 2.0` is `3.5`.

**Surprise 2 — `%` gives the remainder, and only works on integers.**
`7 % 3` is `1`. Very useful: `n % 2 == 0` checks for even numbers; `n % 10` gives the last digit. The sign of the result follows the **left** number: `-7 % 3` is `-1`.

## 2. Relational Operators: `< <= > >= == !=`

They compare two values and give `true` (printed as `1`) or `false` (`0`). Note `==` (two equals) means "is equal to"; a single `=` means "store into".

## 3. Logical Operators: `&&` (AND), `||` (OR), `!` (NOT)

They combine conditions:
- `A && B` is true only when **both** are true.
- `A || B` is true when **at least one** is true.
- `!A` flips true ↔ false.

**Short-circuit evaluation:** C++ stops as soon as it knows the answer. In `A && B`, if `A` is false, `B` is never evaluated. In `A || B`, if `A` is true, `B` is skipped. This is useful: `if (x != 0 && 10 / x > 2)` can never divide by zero.

:::analogy
Short-circuiting is like checking a lift: "Is the door open **and** is the lift here?" If the door is closed, you don't bother checking where the lift is.
:::

## 4. Assignment & Compound Assignment: `= += -= *= /= %=`

`x += 5` is a shortcut for `x = x + 5`. Similarly `x *= 2` means `x = x * 2`.

## 5. Increment and Decrement: `++ --`

`x++` and `++x` both add 1 to `x`. The difference appears **only when used inside a bigger expression**:

| Form | Name | Rule |
|---|---|---|
| `++x` | pre-increment | **first** increase x, **then** use the new value |
| `x++` | post-increment | **first** use the old value, **then** increase x |

```cpp
#include <iostream>
using namespace std;

int main()
{
    int a = 7, b = 2;
    cout << a / b << " " << a % b << " " << a / 2.0 << endl;   // 3 1 3.5

    int x = 5;
    int y = x++;     // y gets 5 (old value), then x becomes 6
    int z = ++x;     // x becomes 7 first, then z gets 7
    cout << x << " " << y << " " << z << endl;                 // 7 5 7

    int p = 0, q = 0;
    if (p != 0 && ++q > 0) { }   // p != 0 is false, so ++q is SKIPPED
    cout << "q = " << q << endl;

    x += 3;                      // x = 10
    cout << "x = " << x << ", a > b is " << (a > b) << endl;
    return 0;
}
```

```output
3 1 3.5
7 5 7
q = 0
x = 10, a > b is 1
```

## 6. The Conditional (Ternary) Operator: `condition ? valueIfTrue : valueIfFalse`

A compact if-else that produces a value: `int bigger = (a > b) ? a : b;`

## 7. Precedence: Who Goes First?

Just like BODMAS in maths, C++ has an order. You don't need the whole table — remember this ladder (high → low):

```text
  ( )  [ ]          brackets first
  ++ --  !  unary -  (prefix, unary operators)       right-to-left
  *  /  %
  +  -
  <  <=  >  >=
  ==  !=
  &&
  ||
  ?:                                                   right-to-left
  =  +=  -= ...                                        right-to-left
```

Operators on the same level go **left to right**, except unary, ternary and assignment, which go **right to left** (`a = b = c = 9` sets `c` first).

```cpp
#include <iostream>
using namespace std;

int main()
{
    cout << 2 + 3 * 4 << " " << (2 + 3) * 4 << " " << 10 - 4 - 3 << " " << 20 / 4 * 2 << endl;
    int a, b, c;
    a = b = c = 9;                       // right to left
    bool r = 5 > 3 && 2 > 4;             // (true) && (false)
    cout << a << " " << r << endl;
    return 0;
}
```

```output
14 20 3 10
9 0
```

## 8. Type Conversion

When an expression mixes types, C++ converts values:

- **Implicit conversion (promotion):** the "smaller" type is automatically converted to the "bigger" one — `char → int → float → double`. So `5 + 2.5` is `7.5`.
- **When storing**, the value is converted to the variable's type: `int n = 9.99;` stores **9** (the fraction is chopped off, not rounded).
- **Explicit conversion (casting):** you ask for it — `static_cast<double>(x)` (C++ style) or `(double)x` (C style).

The classic trap — calculating an average:

```cpp
#include <iostream>
using namespace std;

int main()
{
    int total = 7, count = 2;
    double wrong = total / count;                        // int/int = 3, THEN stored as 3.0
    double right = static_cast<double>(total) / count;   // 7.0 / 2 = 3.5
    int n = 9.99;                                        // truncated to 9
    cout << wrong << " " << right << " " << n << endl;
    return 0;
}
```

```output
3 3.5 9
```

:::warn Undefined behaviour
Never write expressions like `i = i++ + ++i;` that change the same variable twice in one expression. The result is **undefined** — different compilers give different answers. If such a question appears, the correct answer is "undefined behaviour".
:::

:::key
- `int / int` drops the fraction; `%` is the remainder (integers only).
- `x++` uses then increments; `++x` increments then uses.
- `&&` and `||` short-circuit.
- Precedence: unary → `* / %` → `+ -` → relational → equality → `&&` → `||` → `?:` → assignment.
- Storing a decimal in an `int` truncates. Cast before dividing to keep the fraction.
:::

:::mistakes
- `double avg = sum / n;` with integer `sum`, `n` — the fraction is lost before conversion.
- Using `%` with `float` or `double` → compile error.
- Writing `if (a < b < c)` — it compares `(a < b)` (0 or 1) with `c`. Use `a < b && b < c`.
- Confusing `=` with `==`.
- Expecting `int n = 9.99` to round to 10.
:::

:::exam
- MCQs on `17 / 5`, `17 % 5`, `-7 % 3`, precedence like `2 + 3 * 4`.
- *Predict the output* with `x++` / `++x`.
- *"Explain implicit and explicit type conversion with examples."*
:::

:::def
An **expression** is a combination of operands and operators that evaluates to a single value. **Type conversion** is changing a value from one data type to another — **implicit** (automatic, by the compiler) or **explicit** (by a cast written by the programmer).
:::

## Quick Check

:::q Q1 · Evaluate: `17 % 5 + 17 / 5`
:::ans
`2 + 3 = 5`
:::
:::

:::q Q2 · What is printed? `int x = 3; int y = x++ + 10; cout << x << " " << y;`
:::ans
`4 13` — `x++` uses 3 (so y = 13), then x becomes 4.
:::
:::

:::q Q3 · What does `cout << 7 / 2 * 2.0;` print?
:::ans
`6` — left to right: `7 / 2` = 3 (integer division), then `3 * 2.0` = 6.0, printed as `6`.
:::
:::
