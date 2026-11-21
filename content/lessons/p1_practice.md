:::tip How to use this practice set
1. Attempt every question on paper **before** opening the answer.
2. For output questions, **trace line by line** with a small table of variable values — that is exactly what examiners expect.
3. Mark the ones you got wrong and re-read the matching lesson in Chapters 1–2.
Use the **Show all answers** button (top right) only for final revision.
:::

## Section A · Definitions & Short Answers (2–3 marks)

:::q A1 · Define a token. List the types of tokens in C++.
:::ans
A **token** is the smallest individual unit of a program that is meaningful to the compiler. C++ tokens: **keywords** (`int`, `class`), **identifiers** (`total`, `main`), **literals/constants** (`10`, `'a'`, `"hi"`), **operators** (`+`, `<<`, `&&`), and **punctuators/separators** (`;`, `{}`, `()`, `,`).
:::
:::

:::q A2 · What is the difference between a declaration and a definition of a function?
:::ans
- **Declaration (prototype)** tells the compiler the function's **name, return type and parameter types**, e.g. `int add(int, int);`. No body; ends with `;`. Can appear many times.
- **Definition** provides the **body** — the actual code, e.g. `int add(int a, int b) { return a + b; }`. Exactly one definition per function in a program (One Definition Rule).
:::
:::

:::q A3 · Differentiate between entry-controlled and exit-controlled loops with examples.
:::ans
| Entry-controlled | Exit-controlled |
|---|---|
| Condition tested **before** the body | Condition tested **after** the body |
| Body may execute **zero** times | Body executes **at least once** |
| `while`, `for` | `do-while` |
| `while (i < 5) {…}` | `do {…} while (i < 5);` |
:::
:::

:::q A4 · What is procedural abstraction? Why are preconditions and postconditions written?
:::ans
**Procedural abstraction** means treating a function as a **black box**: users know **what** the function does (through its name, prototype and comment), not **how** it does it. The implementation can be changed without affecting callers.
**Precondition** states what must be true before the call (valid inputs); **postcondition** states what will be true after the call (the result/effect). They document the contract between the function and its caller.
:::
:::

:::q A5 · Define function overloading. Can two functions be overloaded on return type only?
:::ans
**Function overloading** is defining multiple functions with the **same name** but **different parameter lists** (number, type, or order of parameters) in the same scope; the compiler selects the right one at compile time (static polymorphism).
**No** — functions differing **only** in return type cannot be overloaded, because the call `f();` gives the compiler no way to choose. It is a compile error.
:::
:::

:::q A6 · State the difference between call by value and call by reference.
:::ans
| Call by value | Call by reference |
|---|---|
| A **copy** of the argument is passed | An **alias** of the argument is passed |
| Changes inside the function do **not** affect the caller | Changes **do** affect the caller's variable |
| Formal parameter: `int a` | Formal parameter: `int &a` |
| Literals/expressions allowed as arguments | Argument must be a variable (lvalue), unless the parameter is `const &` |
| Extra memory/time for copying large objects | No copying → efficient for large objects |
:::
:::

:::q A7 · What is recursion? What are the two essential parts of a recursive function?
:::ans
**Recursion** is a technique where a function calls itself (directly or indirectly) to solve a problem by reducing it to smaller instances of the same problem.
Essential parts: (1) **Base case** – solved directly without recursion; stops recursion. (2) **Recursive case** – calls itself with a smaller/simpler argument that progresses towards the base case. Without a base case → infinite recursion → stack overflow.
:::
:::

:::q A8 · What is the difference between a local variable and a static local variable?
:::ans
Both have **block scope** (visible only inside the function). A normal local variable is **created on every call and destroyed on return** (value lost, initial value garbage). A `static` local variable is **initialized only once**, lives for the **entire program**, and **retains its value between calls** (default initial value 0).
:::
:::

:::q A9 · Differentiate between a pointer and a reference (any four points).
:::ans
1. A reference must be initialized when declared; a pointer need not be.
2. A reference cannot be re-seated to another variable; a pointer can be changed to point elsewhere.
3. A reference cannot be null; a pointer can be `nullptr`.
4. A reference is used directly (`r = 5`); a pointer needs dereferencing (`*p = 5`).
5. Pointer arithmetic is possible; there is no reference arithmetic.
:::
:::

:::q A10 · What are default arguments? State the rules.
:::ans
**Default arguments** are values specified in a function declaration that are used automatically when the caller omits the corresponding arguments, e.g. `void f(int a, int b = 10);`.
Rules: (1) defaults must be assigned **from right to left** – only trailing parameters can have defaults; (2) specify them **only once** (usually in the prototype); (3) arguments can be omitted only from the right in a call; (4) they can create ambiguity with overloaded functions.
:::
:::

## Section B · Multiple Choice Questions (1 mark each)

:::q B1 · Which of the following is a valid identifier?
(a) `2ndValue`  (b) `total-sum`  (c) `_rate2`  (d) `double`
:::ans
**(c) `_rate2`**. (a) starts with a digit, (b) contains `-`, (d) is a keyword.
:::
:::

:::q B2 · What is the value of `17 % 5 + 17 / 5`?
(a) 5  (b) 2  (c) 3  (d) 5.4
:::ans
**(a) 5**. `17 % 5` = 2, `17 / 5` = 3 (integer division), 2 + 3 = 5.
:::
:::

:::q B3 · Which loop executes its body at least once?
(a) `for`  (b) `while`  (c) `do-while`  (d) none
:::ans
**(c) `do-while`** — it is exit-controlled.
:::
:::

:::q B4 · A `switch` statement cannot work with which type?
(a) `int`  (b) `char`  (c) `double`  (d) `enum`
:::ans
**(c) `double`**. The switch expression must be of integral or enumeration type.
:::
:::

:::q B5 · Which operator has the highest precedence?
(a) `*`  (b) `&&`  (c) `=`  (d) `!`
:::ans
**(d) `!`** — unary operators have higher precedence than multiplicative, logical and assignment operators.
:::
:::

:::q B6 · `int a = 10; int &r = a; r++;` What is `a`?
(a) 10  (b) 11  (c) error  (d) garbage
:::ans
**(b) 11**. `r` is an alias of `a`.
:::
:::

:::q B7 · What does `cout << 7 / 2 * 2.0;` print?
(a) 7  (b) 6  (c) 7.0  (d) 3.5
:::ans
**(b) 6**. Left to right: `7 / 2` = 3 (integer division), then `3 * 2.0` = 6.0, printed as `6`.
:::
:::

:::q B8 · Which statement about inline functions is TRUE?
(a) The compiler must always inline them (b) They are a request that the compiler may ignore (c) They cannot return values (d) They cannot have parameters
:::ans
**(b)** — `inline` is only a request (hint) to the compiler.
:::
:::

:::q B9 · Default arguments must be specified:
(a) from left to right (b) from right to left (c) in any order (d) only for the first parameter
:::ans
**(b) from right to left** (trailing parameters).
:::
:::

:::q B10 · What is the output of `cout << (5 > 3 > 1);` ?
(a) 1  (b) 0  (c) error  (d) true
:::ans
**(b) 0**. `5 > 3` → 1; then `1 > 1` → 0 (false).
:::
:::

:::q B11 · Which of these correctly frees an array allocated as `int *p = new int[10];`?
(a) `delete p;` (b) `delete[] p;` (c) `free(p);` (d) `delete p[];`
:::ans
**(b) `delete[] p;`** — memory from `new[]` must be released with `delete[]`.
:::
:::

:::q B12 · The keyword used to retain a local variable's value between function calls is:
(a) `const` (b) `auto` (c) `static` (d) `extern`
:::ans
**(c) `static`**.
:::
:::

## Section C · Predict the Output (2–4 marks)

:::q C1 · Predict the output.
```cpp
#include <iostream>
using namespace std;
int main()
{
    int x = 5, y;
    y = x++ * 2;
    cout << x << " " << y << endl;
    y = ++x * 2;
    cout << x << " " << y << endl;
    return 0;
}
```
:::ans
```output
6 10
7 14
```
`x++ * 2` uses old `x` (5) → y = 10, then x = 6. `++x * 2` → x = 7 first → y = 14.
:::
:::

:::q C2 · Predict the output.
```cpp
#include <iostream>
using namespace std;
int main()
{
    int i;
    for (i = 0; i < 5; i++);
    cout << "i = " << i << endl;
    return 0;
}
```
:::ans
```output
i = 5
```
The `;` after the `for(...)` makes an empty body. The loop just increments `i` to 5; the `cout` runs once after the loop.
:::
:::

:::q C3 · Predict the output.
```cpp
#include <iostream>
using namespace std;
int main()
{
    int n = 3;
    switch (n)
    {
        case 1: cout << "One ";
        case 3: cout << "Three ";
        case 5: cout << "Five ";
                break;
        default: cout << "Other";
    }
    cout << endl;
    return 0;
}
```
:::ans
```output
Three Five 
```
Matches `case 3`, falls through to `case 5` (no break), then `break` stops before `default`.
:::
:::

:::q C4 · Predict the output.
```cpp
#include <iostream>
using namespace std;
int main()
{
    int a = 0;
    if (a = 0)
        cout << "zero" << endl;
    else
        cout << "non-zero" << endl;
    if (a = 7)
        cout << "seven, a=" << a << endl;
    return 0;
}
```
:::ans
```output
non-zero
seven, a=7
```
`a = 0` is an **assignment** whose value is 0 → false → `else`. `a = 7` evaluates to 7 → true, and `a` becomes 7.
:::
:::

:::q C5 · Predict the output.
```cpp
#include <iostream>
using namespace std;
int main()
{
    int i = 1;
    while (i <= 10)
    {
        if (i % 3 == 0) { i++; continue; }
        if (i == 8) break;
        cout << i << " ";
        i++;
    }
    cout << endl;
    return 0;
}
```
:::ans
```output
1 2 4 5 7 
```
Multiples of 3 (3, 6) are skipped; at i = 8 the loop breaks.
:::
:::

:::q C6 · Predict the output.
```cpp
#include <iostream>
using namespace std;
void change(int a, int &b)
{
    a = a * 10;
    b = b * 10;
}
int main()
{
    int x = 2, y = 3;
    change(x, y);
    cout << x << " " << y << endl;
    return 0;
}
```
:::ans
```output
2 30
```
`a` is a copy (call by value) → `x` unchanged; `b` is a reference → `y` becomes 30.
:::
:::

:::q C7 · Predict the output.
```cpp
#include <iostream>
using namespace std;
int f(int n)
{
    if (n == 0) return 0;
    return n + f(n - 2);
}
int main()
{
    cout << f(8) << endl;
    return 0;
}
```
:::ans
```output
20
```
f(8) = 8 + f(6) = 8 + 6 + f(4) = 8 + 6 + 4 + f(2) = 8 + 6 + 4 + 2 + f(0) = 20.
(Note: `f(7)` would never reach 0 → infinite recursion → stack overflow. A good follow-up viva question!)
:::
:::

:::q C8 · Predict the output.
```cpp
#include <iostream>
using namespace std;
void fun(int n)
{
    if (n > 0)
    {
        cout << n << " ";
        fun(n - 1);
        cout << n << " ";
    }
}
int main()
{
    fun(3);
    cout << endl;
    return 0;
}
```
:::ans
```output
3 2 1 1 2 3 
```
Prints on the way **down** (3 2 1), then again while **unwinding** (1 2 3).
:::
:::

:::q C9 · Predict the output.
```cpp
#include <iostream>
using namespace std;
int counter()
{
    static int c = 10;
    return c++;
}
int main()
{
    cout << counter() << " ";
    cout << counter() << " ";
    cout << counter() << endl;
    return 0;
}
```
:::ans
```output
10 11 12
```
`c` is static: initialized once, retains its value. `c++` returns the old value.
:::
:::

:::q C10 · Predict the output.
```cpp
#include <iostream>
using namespace std;
int x = 50;
int main()
{
    int x = 5;
    {
        int x = 1;
        cout << x << " " << ::x << endl;
    }
    cout << x << " " << ::x << endl;
    return 0;
}
```
:::ans
```output
1 50
5 50
```
`::x` always refers to the **global** `x`, never to an enclosing local.
:::
:::

:::q C11 · Predict the output.
```cpp
#include <iostream>
using namespace std;
int main()
{
    int a[5] = {2, 4, 6};
    int *p = a;
    cout << *p + 1 << " " << *(p + 1) << " " << a[3] << endl;
    p++;
    *p = 100;
    cout << a[0] << " " << a[1] << endl;
    return 0;
}
```
:::ans
```output
3 4 0
2 100
```
`*p + 1` = 2 + 1 = 3 (dereference first). `*(p+1)` = a[1] = 4. Uninitialized remaining elements in a partially initialized array are 0. After `p++`, p points to a[1].
:::
:::

:::q C12 · Predict the output.
```cpp
#include <iostream>
using namespace std;
int main()
{
    double d = 7 / 2;
    int i = 7.9;
    char c = 'A' + 2;
    cout << d << " " << i << " " << c << " " << c + 1 << endl;
    return 0;
}
```
:::ans
```output
3 7 C 68
```
`7/2` is integer division → 3 → stored as 3.0 (prints `3`). `7.9` truncated → 7. `'A'+2` = 67 = `'C'`. `c + 1` is an **int** expression (67 + 1) → prints `68`, not `D`.
:::
:::

:::q C13 · Predict the output.
```cpp
#include <iostream>
using namespace std;
int main()
{
    for (int i = 1; i <= 3; i++)
    {
        for (int j = 1; j <= 3; j++)
        {
            if (j == 2) break;
            cout << i << j << " ";
        }
    }
    cout << endl;
    return 0;
}
```
:::ans
```output
11 21 31 
```
`break` only exits the **inner** loop; the outer loop continues.
:::
:::

:::q C14 · Predict the output.
```cpp
#include <iostream>
using namespace std;
int main()
{
    int a = 4, b = 0;
    if (b != 0 && a / b > 1)
        cout << "big" << endl;
    else
        cout << "safe" << endl;
    bool r = (a || ++b);
    cout << r << " " << b << endl;
    return 0;
}
```
:::ans
```output
safe
1 0
```
Short-circuiting: `b != 0` is false, so `a / b` is never evaluated (no division by zero). In `a || ++b`, `a` is non-zero (true), so `++b` never runs; `b` stays 0.
:::
:::

## Section D · Find the Error(s)

:::q D1 · Find and correct the errors.
```cpp
#include <iostream>
using namespace std;
void main()
{
    int 2x = 5;
    float f = 3.5;
    cout >> f % 2;
}
```
:::ans
1. `void main()` → should be `int main()` (and `return 0;`).
2. `2x` is an invalid identifier (starts with a digit) → e.g. `x2`.
3. `cout >> …` → must be `cout << …`.
4. `%` cannot be applied to `float` → use `fmod(f, 2)` from `<cmath>`, or use integers.
:::
:::

:::q D2 · Why does this not compile? Fix it.
```cpp
#include <iostream>
using namespace std;
//@expect: compile-error
int sum(int a = 5, int b);
int main() { cout << sum(3); return 0; }
int sum(int a, int b) { return a + b; }
```
:::ans
Default arguments must be given **right-to-left**. `b` (the last parameter) has no default while `a` does → error. Fix: `int sum(int a, int b = 5);` Then `sum(3)` returns 8.
:::
:::

:::q D3 · Identify the error.
```cpp
#include <iostream>
using namespace std;
//@expect: compile-error
int area(int s) { return s * s; }
double area(int s) { return 3.14 * s * s; }
int main() { cout << area(2); return 0; }
```
:::ans
The two functions differ **only in return type** — not a valid overload. Error: *ambiguating new declaration of 'double area(int)'*. Fix: change the parameter list, e.g. `double area(double r)`.
:::
:::

:::q D4 · Identify the logical error.
```cpp
#include <iostream>
using namespace std;
//@norun
int main()
{
    int i = 1, sum = 0;
    while (i <= 10)
        sum += i;
        i++;
    cout << sum;
    return 0;
}
```
:::ans
Without braces, the `while` controls only `sum += i;`. `i++` is **outside** the loop → `i` never changes → **infinite loop**. Fix: put both statements inside `{ }`.
:::
:::

:::q D5 · Spot the problem.
```cpp
int& getValue()
{
    int x = 10;
    return x;
}
```
:::ans
It returns a **reference to a local variable**. `x` is destroyed when the function returns, so the caller receives a **dangling reference** → undefined behaviour. Return by value (`int getValue()`) instead.
:::
:::

## Section E · Write the Program

:::q E1 · Write a program that reads a number and prints whether it is a palindrome (e.g., 121, 1331).
:::ans
```cpp
#include <iostream>
using namespace std;

int main()
{
    //@input: 1331
    int n, original, reversed = 0;
    cin >> n;
    original = n;
    while (n > 0)
    {
        reversed = reversed * 10 + n % 10;   // append last digit
        n /= 10;                             // drop last digit
    }
    if (original == reversed)
        cout << original << " is a palindrome" << endl;
    else
        cout << original << " is not a palindrome" << endl;
    return 0;
}
```
Input `1331`:
```output
1331 is a palindrome
```
:::
:::

:::q E2 · Write overloaded functions `volume()` for a cube (side), a cylinder (radius, height) and a cuboid (l, b, h).
:::ans
```cpp
#include <iostream>
using namespace std;

int volume(int s)                 { return s * s * s; }             // cube
double volume(double r, int h)    { return 3.14 * r * r * h; }      // cylinder
int volume(int l, int b, int h)   { return l * b * h; }             // cuboid

int main()
{
    cout << "Cube: " << volume(3) << endl;
    cout << "Cylinder: " << volume(2.0, 5) << endl;
    cout << "Cuboid: " << volume(2, 3, 4) << endl;
    return 0;
}
```
```output
Cube: 27
Cylinder: 62.8
Cuboid: 24
```
They are told apart by the **number and type** of parameters.
:::
:::

:::q E3 · Write a recursive function to compute the GCD of two numbers (Euclid's algorithm).
:::ans
```cpp
#include <iostream>
using namespace std;

// gcd(a, 0) = a ; gcd(a, b) = gcd(b, a % b)
int gcd(int a, int b)
{
    if (b == 0) return a;        // base case
    return gcd(b, a % b);        // recursive case
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
Trace: gcd(48,18) → gcd(18,12) → gcd(12,6) → gcd(6,0) → 6.
:::
:::

:::q E4 · Write a program to print Floyd's triangle for n = 4 (rows: 1 · 2 3 · 4 5 6 · 7 8 9 10, one row per line).
:::ans
```cpp
#include <iostream>
using namespace std;

int main()
{
    int n = 4, k = 1;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
            cout << k++ << " ";
        cout << endl;
    }
    return 0;
}
```
```output
1 
2 3 
4 5 6 
7 8 9 10 
```
:::
:::

:::q E5 · Write a menu-driven calculator using `switch` and `do-while` (operations + − × ÷, exit on 0). Handle division by zero.
:::ans
```cpp
#include <iostream>
using namespace std;

int main()
{
    //@input: 1 8 2
    //@input: 4 8 0
    //@input: 0
    int ch;
    double a, b;
    do {
        cout << "1.Add 2.Sub 3.Mul 4.Div 0.Exit: ";
        cin >> ch;
        if (ch >= 1 && ch <= 4) { cin >> a >> b; }
        switch (ch)
        {
            case 1: cout << a + b << endl; break;
            case 2: cout << a - b << endl; break;
            case 3: cout << a * b << endl; break;
            case 4:
                if (b == 0) cout << "Cannot divide by zero" << endl;
                else        cout << a / b << endl;
                break;
            case 0: cout << "Bye" << endl; break;
            default: cout << "Invalid choice" << endl;
        }
    } while (ch != 0);
    return 0;
}
```
Input `1 8 2`, `4 8 0`, `0`:
```output
1.Add 2.Sub 3.Mul 4.Div 0.Exit: 10
1.Add 2.Sub 3.Mul 4.Div 0.Exit: Cannot divide by zero
1.Add 2.Sub 3.Mul 4.Div 0.Exit: Bye
```
:::
:::

:::q E6 · Write a function that takes an array and its size and returns, through reference parameters, the count of even and odd numbers.
:::ans
```cpp
#include <iostream>
using namespace std;

void countEvenOdd(const int a[], int n, int &even, int &odd)
{
    even = odd = 0;
    for (int i = 0; i < n; i++)
        if (a[i] % 2 == 0) even++;
        else               odd++;
}

int main()
{
    int a[6] = {3, 8, 10, 7, 5, 2}, e, o;
    countEvenOdd(a, 6, e, o);
    cout << "Even: " << e << ", Odd: " << o << endl;
    return 0;
}
```
```output
Even: 3, Odd: 3
```
:::
:::

## Section F · Long Answer (5–8 marks)

:::q F1 · Explain the different ways of passing parameters to functions in C++ with a single program that demonstrates all three. State when each should be used.
:::ans
Three ways: **call by value**, **call by reference**, **call by address (pointer)** — see [Lesson 2.4](02_4_parameter_passing.html) for the full swap program and comparison table. Write the swap program with all three functions, show the output (`1 2` / `2 1` / `1 2`), and conclude:
- **Value** – when the function must not change the argument and the data is small (e.g. `int`).
- **Reference** – when the function must change the caller's variable(s) or return several values; `const &` for passing large objects efficiently without allowing change.
- **Pointer** – when "no object" (`nullptr`) is a valid possibility, when working with dynamic memory/arrays, or for C-compatibility.
:::
:::

:::q F2 · What is top-down design? Illustrate with a program that computes simple statistics (sum, average, maximum) of 5 numbers using separate functions.
:::ans
**Top-down design (stepwise refinement):** start with the overall task, break it into sub-tasks, refine each sub-task further until each is simple enough to code as one function. `main()` then just calls these functions — the program structure mirrors the problem structure. Benefits: modularity, reuse, easy testing, readability, team work.

```text
Statistics
├── readData
├── computeSum   ──► used by computeAverage
├── computeAverage
├── findMax
└── report
```

```cpp
#include <iostream>
using namespace std;

void readData(int a[], int n)
{
    int sample[5] = {12, 45, 7, 30, 18};   // in an exam you'd use cin
    for (int i = 0; i < n; i++) a[i] = sample[i];
}
int computeSum(const int a[], int n)
{
    int s = 0;
    for (int i = 0; i < n; i++) s += a[i];
    return s;
}
double computeAverage(const int a[], int n)
{
    return static_cast<double>(computeSum(a, n)) / n;   // function calling function
}
int findMax(const int a[], int n)
{
    int m = a[0];
    for (int i = 1; i < n; i++) if (a[i] > m) m = a[i];
    return m;
}
void report(const int a[], int n)
{
    cout << "Sum = " << computeSum(a, n) << endl;
    cout << "Average = " << computeAverage(a, n) << endl;
    cout << "Max = " << findMax(a, n) << endl;
}
int main()
{
    int data[5];
    readData(data, 5);
    report(data, 5);
    return 0;
}
```
```output
Sum = 112
Average = 22.4
Max = 45
```
:::
:::

:::q F3 · Compare recursion and iteration. Write both recursive and iterative versions of a function to find the sum of the first n natural numbers.
:::ans
Comparison table: see [Lesson 2.6](02_6_recursion.html) (calls itself vs loop; base case vs loop condition; stack memory & overhead vs efficient; stack overflow vs infinite loop; elegant for recursive structures vs better for simple repetition).

```cpp
#include <iostream>
using namespace std;

int sumRec(int n)
{
    if (n == 0) return 0;          // base case
    return n + sumRec(n - 1);      // recursive case
}

int sumIter(int n)
{
    int s = 0;
    for (int i = 1; i <= n; i++) s += i;
    return s;
}

int main()
{
    cout << sumRec(10) << " " << sumIter(10) << endl;
    return 0;
}
```
```output
55 55
```
:::
:::
