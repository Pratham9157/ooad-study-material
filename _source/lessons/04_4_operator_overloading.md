**Operator overloading lets your own classes use normal operators like `+`, `==`, `++` and `<<`, so code with objects reads as naturally as code with numbers.**

## The Problem: Clumsy Code for Simple Ideas

Suppose you write a `Complex` number class. Without operator overloading, adding three complex numbers looks like this:

```cpp
Complex d = a.add(b).add(c);
if (d.isEqual(e)) d.print();
```

With integers you'd just write `a + b + c` and `d == e` and `cout << d`. Operator overloading lets you write **exactly that** for your own types.

:::analogy
The `+` sign already means different things in daily life: `2 + 3` adds numbers, "Hi" + "There" joins words, and on a recipe "flour + water" mixes ingredients. The meaning depends on **what** is being added. Operator overloading lets you teach `+` what it should mean for **your** objects.
:::

## How It Works

You write a special function named `operator` followed by the symbol: `operator+`, `operator==`, `operator<<`.

When the compiler sees `a + b` where `a` is an object, it translates it into a function call:

```text
   a + b      →   a.operator+(b)        (if operator+ is a MEMBER function)
   a + b      →   operator+(a, b)       (if it's a NON-member / friend function)
   -a         →   a.operator-()         (unary, member)
```

| | As a member function | As a friend / non-member |
|---|---|---|
| Unary operator (`-a`, `++a`) | 0 arguments (the object is `*this`) | 1 argument |
| Binary operator (`a + b`) | 1 argument (the left operand is `*this`) | 2 arguments |

## Rules

1. You can only overload **existing** operators — you can't invent `**` or `<>`.
2. At least one operand must be a **user-defined type** (you can't change how `int + int` works).
3. You **cannot change** precedence, associativity or the number of operands.
4. **Cannot be overloaded:** `::` (scope resolution), `.` (member access), `.*` (pointer-to-member), `?:` (ternary), `sizeof` (and `typeid`).
5. **Must be member functions:** `=`, `()`, `[]`, `->`.

## Example 1: Binary and Unary Operators as Members

```cpp
#include <iostream>
using namespace std;

class Complex
{
    double re, im;
public:
    Complex(double r = 0, double i = 0) : re(r), im(i) { }

    Complex operator+(const Complex &c) const     // a + b   → a.operator+(b)
    {
        return Complex(re + c.re, im + c.im);
    }
    bool operator==(const Complex &c) const       // a == b
    {
        return re == c.re && im == c.im;
    }
    Complex operator-() const                     // -a      (unary: no argument)
    {
        return Complex(-re, -im);
    }
    void show() const { cout << re << (im >= 0 ? "+" : "") << im << "i" << endl; }
};

int main()
{
    Complex a(3, 4), b(1, -2);
    Complex c = a + b;          // reads like normal maths
    c.show();
    (-a).show();
    cout << (c == Complex(4, 2)) << endl;
    return 0;
}
```

```output
4+2i
-3-4i
1
```

## Example 2: Prefix vs Postfix ++

Both are spelled `operator++`. To tell them apart, the **postfix** version takes a **dummy `int`** parameter (it's never used — it's just a marker).

- **Prefix `++a`**: increase, then return the **updated** object (by reference).
- **Postfix `a++`**: remember the old value, increase, return the **old** value (by value).

```cpp
#include <iostream>
using namespace std;

class Counter
{
    int count;
public:
    Counter(int c = 0) : count(c) { }
    Counter& operator++()          // PREFIX  ++c
    {
        ++count;
        return *this;
    }
    Counter operator++(int)        // POSTFIX c++   (int = dummy marker)
    {
        Counter old = *this;
        count++;
        return old;
    }
    int get() const { return count; }
};

int main()
{
    Counter c(5);
    Counter x = ++c;      // c becomes 6, x gets 6
    cout << c.get() << " " << x.get() << endl;
    Counter y = c++;      // y gets 6 (old), c becomes 7
    cout << c.get() << " " << y.get() << endl;
    return 0;
}
```

```output
6 6
7 6
```

## Example 3: << and >> (Printing and Reading Objects)

`cout << d` has `cout` on the **left**, not our object — so `operator<<` can't be a member of our class. We write it as a **friend** (Lesson 4.5) or non-member function that takes the stream and the object, and **returns the stream** so chaining (`cout << a << b`) works.

```cpp
#include <iostream>
using namespace std;

class Distance
{
    int feet, inches;
public:
    Distance(int f = 0, int i = 0) : feet(f), inches(i) { }
    friend ostream& operator<<(ostream &out, const Distance &d);
    friend istream& operator>>(istream &in, Distance &d);
};

ostream& operator<<(ostream &out, const Distance &d)
{
    out << d.feet << "' " << d.inches << "\"";
    return out;                       // return the stream → chaining works
}

istream& operator>>(istream &in, Distance &d)
{
    in >> d.feet >> d.inches;
    return in;
}

int main()
{
    //@input: 5 9
    Distance d1(6, 2), d2;
    cin >> d2;
    cout << "d1 = " << d1 << ", d2 = " << d2 << endl;
    return 0;
}
```

Input `5 9`:

```output
d1 = 6' 2", d2 = 5' 9"
```

:::key
- Operator overloading = defining `operatorX` functions so objects work with normal operators (compile-time polymorphism).
- Member: binary takes 1 argument, unary 0. Friend: binary 2, unary 1.
- Can't overload `:: . .* ?: sizeof`; `= () [] ->` must be members; can't change precedence or arity.
- Postfix `++` has a dummy `int` and returns the old value.
- `<<`/`>>` are non-member (friend) functions returning the stream by reference.
:::

:::mistakes
- Giving a member binary operator two parameters.
- Forgetting the dummy `int` for postfix, or returning the new value from postfix.
- Writing `operator<<` as a member (then you'd have to write `d << cout`).
- Not returning `ostream&` → `cout << a << b` won't chain.
- Trying to overload `::`, `.`, `?:` or `sizeof`.
:::

:::exam
- *"What is operator overloading? State its rules."*
- *"Overload `+` for a Complex/Time/Distance class."*
- *"Overload prefix and postfix `++`."*
- *"List operators that cannot be overloaded."*
:::

:::def
**Operator overloading** is the mechanism of giving an existing C++ operator an additional meaning for objects of a user-defined class, by defining a function named `operator` followed by the operator symbol. It is a form of compile-time polymorphism; it cannot create new operators or change precedence, associativity or the number of operands.
:::

## Quick Check

:::q Q1 · How many parameters does `operator+` take as a member? As a friend?
:::ans
Member: **1** (the left operand is `*this`). Friend: **2**.
:::
:::

:::q Q2 · Why does `5 + obj` fail if `operator+` is a member, and how do you fix it?
:::ans
`5 + obj` would be `5.operator+(obj)`, but `5` is an `int`, not an object. Make `operator+` a **friend/non-member** taking two parameters (then 5 can be converted via a constructor).
:::
:::

:::q Q3 · Name four operators that cannot be overloaded.
:::ans
`::`, `.`, `.*`, `?:` (also `sizeof`, `typeid`).
:::
:::
