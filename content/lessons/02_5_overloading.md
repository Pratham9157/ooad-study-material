**Function overloading lets several functions share one name, as long as their parameter lists differ. The compiler picks the right one by looking at the arguments.**

## The Problem: Too Many Names for One Idea

Without overloading you'd write `areaOfSquare(int)`, `areaOfRectangle(int, int)`, `areaOfCircle(double)`. The user has to remember three names for one idea: *area*. With overloading, they're all just `area(…)`.

:::analogy
The word **"open"**: open a door, open a book, open a file. Same word, different action — and you know which action from *what* is being opened. The compiler does the same with the arguments you pass.
:::

## Function Overloading

Functions can share a name if they differ in the **number**, **type** or **order** of parameters:

```cpp
#include <iostream>
using namespace std;

int    area(int side)          { return side * side; }          // 1 int
int    area(int l, int b)      { return l * b; }                // 2 ints  (number differs)
double area(double r)          { return 3.14 * r * r; }         // 1 double (type differs)
void   show(int a, char c)     { cout << "int,char" << endl; }
void   show(char c, int a)     { cout << "char,int" << endl; }  // order differs

int main()
{
    cout << area(4) << " " << area(3, 5) << " " << area(2.0) << endl;
    show(1, 'x');
    show('x', 1);
    return 0;
}
```

```output
16 15 12.56
int,char
char,int
```

Because the choice is made **while compiling**, overloading is called **compile-time (static) polymorphism** — "one name, many forms".

### How the compiler chooses (simplified)

1. **Exact match** wins.
2. Otherwise a **promotion** (`char` → `int`, `float` → `double`).
3. Otherwise a **standard conversion** (`int` → `double`, `double` → `int`, …).
4. If two candidates are equally good → **ambiguity error**.

```cpp
#include <iostream>
using namespace std;
//@expect: compile-error

void f(int x)   { cout << "int" << endl; }
void f(float x) { cout << "float" << endl; }

int main()
{
    f(5);       // OK: exact match for int
    f(5.5f);    // OK: exact match for float
    f(5.5);     // ERROR: 5.5 is a DOUBLE. double->int and double->float are
                // equally good conversions, so the call is AMBIGUOUS
    return 0;
}
```

:::warn Return type alone is NOT enough
`int get();` and `double get();` cannot coexist. From the call `get();` the compiler can't tell which one you want. Overloads must differ in their **parameters**.
:::

## Default Arguments

A **default argument** is a value used automatically when the caller leaves that argument out.

```cpp
#include <iostream>
using namespace std;

double interest(double p, double rate = 8.0, int years = 1);   // defaults in the prototype

int main()
{
    cout << interest(1000) << endl;          // rate = 8, years = 1
    cout << interest(1000, 10) << endl;      // years = 1
    cout << interest(1000, 10, 2) << endl;   // nothing defaulted
    return 0;
}

double interest(double p, double rate, int years)   // don't repeat the defaults here
{
    return p * rate * years / 100;
}
```

```output
80
100
200
```

**Rules:**
1. Defaults must be given **from right to left**: `f(int a, int b = 5)` ✓, `f(int a = 5, int b)` ✗.
2. Give them **once** (usually in the prototype).
3. You can only leave out arguments **from the right**.

Defaults + overloading can clash: with `g(int)` and `g(int, int = 0)`, the call `g(5)` is **ambiguous**.

## Inline Functions

For tiny functions, the cost of "jumping" to a function can be more than the work itself. Writing `inline` **asks** the compiler to paste the function's body directly at each call.

```cpp
#include <iostream>
using namespace std;

inline int cube(int x) { return x * x * x; }

int main()
{
    cout << cube(3) << endl;
    return 0;
}
```

```output
27
```

- `inline` is only a **request**; the compiler may ignore it (e.g. for big or recursive functions).
- Functions defined inside a class are automatically inline (Chapter 3).
- Better than macros like `#define SQ(x) x*x`, which have no type checking and break on `SQ(2+3)` (gives 11, not 25).

:::key
- Overloading = same name, different parameter lists (number/type/order); chosen at compile time.
- Return type alone cannot distinguish overloads.
- Watch out for ambiguity (`5.5` is a `double`).
- Default arguments: right-to-left, specified once.
- `inline` is a request to expand small functions in place.
:::

:::mistakes
- Overloading on return type only.
- Thinking different parameter *names* make a different function (`f(int a)` and `f(int b)` are the same).
- Defaults in the middle/left of the parameter list.
- Repeating default values in both prototype and definition.
:::

:::exam
- *"What is function overloading? Write a program to overload `area()`/`volume()`."*
- *"Explain default arguments with rules."*
- *"Find the error"* — ambiguous calls, defaults in the wrong order, overloading by return type.
:::

:::def
**Function overloading** is defining multiple functions with the same name but different parameter lists (number, type or order of parameters) in the same scope; the compiler selects the appropriate one at compile time. A **default argument** is a value automatically assigned to a parameter when the corresponding argument is omitted in the call. An **inline function** is a function whose body the compiler is requested to substitute at the point of each call.
:::

## Quick Check

:::q Q1 · Can these two functions coexist? `int sum(int a, int b);` and `int sum(int x, int y);`
:::ans
No — they have the same parameter types; only the names differ. That's a redefinition error.
:::
:::

:::q Q2 · Which call is ambiguous with `void p(int); void p(double);`: `p(3)`, `p(3.0)`, `p('A')`?
:::ans
None of them. `p(3)` → int (exact), `p(3.0)` → double (exact), `p('A')` → int (char → int is a **promotion**, which beats the char → double conversion).
:::
:::

:::q Q3 · Is `void f(int a = 1, int b, int c = 3);` valid?
:::ans
No — `b` has no default but a parameter to its left does. Defaults must be trailing (right-to-left).
:::
:::
