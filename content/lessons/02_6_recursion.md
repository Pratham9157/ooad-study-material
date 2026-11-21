**Recursion is when a function solves a problem by calling *itself* on a smaller version of the same problem — until the problem is so small that the answer is obvious.**

## The Problem: Some Problems Are Defined in Terms of Themselves

Look at factorial:
- 5! = 5 × 4!
- 4! = 4 × 3!
- … and 1! = 1.

The definition of factorial *uses factorial*. Many problems have this shape — sum of digits, power, Fibonacci, searching a sorted list, folders inside folders. Recursion lets the code mirror the definition directly.

:::analogy
**Russian nesting dolls.** To find the smallest doll: open the doll in front of you. If there's another doll inside, do the *same thing* with that doll (recursive case). If it's solid, you've found it (base case). Each step is the same action on a smaller doll.
:::

## The Two Rules of Every Recursive Function

1. **Base case** — a simple input whose answer is known directly. It **stops** the recursion.
2. **Recursive case** — the function calls itself with a **smaller** input that moves **towards** the base case.

Forget the base case (or never move towards it) and the function calls itself forever until memory runs out → **stack overflow**.

```cpp
#include <iostream>
using namespace std;

long long fact(int n)
{
    if (n <= 1) return 1;          // base case
    return n * fact(n - 1);        // recursive case: smaller problem
}

int main()
{
    cout << fact(5) << endl;
    return 0;
}
```

```output
120
```

## How It Works: Tracing fact(4)

Each call waits for the call it made. The calls pile up (going down), then the answers come back (going up):

```text
fact(4) = 4 * fact(3)                       going DOWN (calls pile up)
              fact(3) = 3 * fact(2)
                            fact(2) = 2 * fact(1)
                                          fact(1) = 1        ← base case reached
                            fact(2) = 2 * 1 = 2              coming back UP
              fact(3) = 3 * 2 = 6
fact(4) = 4 * 6 = 24
```

Every waiting call sits on the **call stack** with its own copy of `n`. That's why recursion uses more memory than a loop.

## More Classic Examples

```cpp
#include <iostream>
using namespace std;

int fib(int n)                    // 0 1 1 2 3 5 8 13 ...
{
    if (n <= 1) return n;         // two base cases: fib(0)=0, fib(1)=1
    return fib(n - 1) + fib(n - 2);
}

int sumDigits(int n)
{
    if (n == 0) return 0;
    return n % 10 + sumDigits(n / 10);   // last digit + sum of the rest
}

int power(int b, int e)
{
    if (e == 0) return 1;
    return b * power(b, e - 1);
}

int main()
{
    cout << fib(7) << " " << sumDigits(4321) << " " << power(2, 5) << endl;
    return 0;
}
```

```output
13 10 32
```

## Where You Print Matters (Favourite Output Question!)

Code **before** the recursive call runs on the way **down**; code **after** it runs on the way **back up** — in **reverse** order.

```cpp
#include <iostream>
using namespace std;

void down(int n)
{
    if (n == 0) return;
    cout << n << " ";     // print first, then recurse
    down(n - 1);
}

void up(int n)
{
    if (n == 0) return;
    up(n - 1);            // recurse first...
    cout << n << " ";     // ...print while returning
}

int main()
{
    down(4); cout << endl;
    up(4);   cout << endl;
    return 0;
}
```

```output
4 3 2 1 
1 2 3 4 
```

## Recursion vs Iteration

| Recursion | Iteration (loops) |
|---|---|
| Function calls itself | Uses `for` / `while` |
| Stops at the base case | Stops when the loop condition fails |
| Uses the call stack → more memory, slower | Usually faster, less memory |
| Missing base case → stack overflow | Wrong condition → infinite loop |
| Elegant for naturally recursive problems (trees, Tower of Hanoi, divide & conquer) | Better for simple repetition |

Any recursion can be rewritten as a loop and vice versa.

:::key
- Recursion = base case + recursive case moving towards it.
- Calls stack up going down; results are combined coming back up.
- Statements after the recursive call run in reverse order.
- Recursion is elegant but uses more memory than loops.
:::

:::mistakes
- No base case, or a recursive call that doesn't shrink the problem (`fact(n)` calling `fact(n)`) → stack overflow.
- `return fact(n - 1);` instead of `return n * fact(n - 1);`.
- Getting the print order wrong in "predict the output" questions.
- A base case that can be skipped: `f(n)` with `if (n == 0)` but calls `f(n - 2)` from an odd `n` never reaches 0.
:::

:::exam
- *"What is recursion? Write a recursive function for factorial / Fibonacci / GCD / sum of digits."*
- *"Compare recursion and iteration."*
- *Trace/predict output* of recursive functions.
:::

:::def
**Recursion** is a technique in which a function calls itself, directly or indirectly, to solve a problem by reducing it to smaller instances of the same problem. A recursive function must have a **base case**, which ends the recursion, and a **recursive case**, which moves towards the base case.
:::

## Quick Check

:::q Q1 · What does `int f(int n){ if(n==0) return 0; return n + f(n-2); }` return for `f(6)`? What happens with `f(5)`?
:::ans
`f(6)` = 6 + 4 + 2 + 0 = **12**. `f(5)` → 5, 3, 1, -1, -3 … never reaches 0 → **infinite recursion / stack overflow**.
:::
:::

:::q Q2 · Write a recursive GCD using Euclid's rule gcd(a, b) = gcd(b, a % b), gcd(a, 0) = a.
:::ans
```cpp
#include <iostream>
using namespace std;

int gcd(int a, int b)
{
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main()
{
    cout << gcd(48, 18) << endl;
    return 0;
}
```
```output
6
```
:::
:::
