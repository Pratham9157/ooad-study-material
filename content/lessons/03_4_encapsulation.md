**Encapsulation means bundling an object's data together with the functions that use it — and hiding the data so the outside world can only use it through those functions.**

## The Problem: Anyone Can Break the Object

Imagine a `Student` class where marks are public:

```cpp
class Student { public: int marks; };
Student s;
s.marks = 250;    // marks out of 100? Nothing stops this.
s.marks = -40;    // or this.
```

Every piece of code that touches `marks` must remember to validate it — and one forgetful line breaks everything. We want the **object itself** to guarantee that its marks are always valid.

## The Idea: A Capsule With a Few Controlled Openings

Encapsulation has two parts:
1. **Bundling** — keep data and the functions that work on it together in one class.
2. **Data hiding** — make the data `private`, and provide `public` functions (the *interface*) that read/change it **safely**.

```cpp
#include <iostream>
using namespace std;

class Student
{
private:
    int marks = 0;                     // hidden: no direct access
public:
    bool setMarks(int m)               // the only way IN — with validation
    {
        if (m < 0 || m > 100) return false;
        marks = m;
        return true;
    }
    int getMarks() { return marks; }   // the only way OUT
};

int main()
{
    Student s;
    cout << s.setMarks(250) << " " << s.setMarks(87) << endl;   // 0 = rejected, 1 = accepted
    cout << "Marks: " << s.getMarks() << endl;
    // s.marks = 250;                  // ERROR: 'marks' is private
    return 0;
}
```

```output
0 1
Marks: 87
```

Now `marks` is **always** between 0 and 100 — guaranteed by the class, not by the hope that every caller remembers.

:::analogy
A **medicine capsule**: the powder (data) is sealed inside a shell; you can't touch it directly, you just swallow the capsule and it works. Or an **ATM**: the cash (data) is locked inside; you can only use the screen and keypad (public interface), and the machine checks your PIN and balance (validation) before giving cash.
:::

## Access Specifiers: Who Can See What

| Specifier | Inside the class's own functions | Inside derived classes | Outside (e.g. `main`) |
|---|---|---|---|
| `private` | ✓ | ✗ | ✗ |
| `protected` | ✓ | ✓ | ✗ |
| `public` | ✓ | ✓ | ✓ |

- **`private`** — the default in a `class`. For data.
- **`public`** — the interface. For the methods others should call.
- **`protected`** — like private, but also visible to child classes (Chapter 5).

The usual rule of thumb: **data private, methods public** (helpers private).

## Why Encapsulation Is Worth It

- **Data integrity** — invalid states become impossible.
- **Rules in one place** — validation lives inside the class.
- **Freedom to change** — you can change how data is stored inside (e.g. store percentage instead of marks) without breaking any code outside, as long as the public methods stay the same.
- **Easier debugging** — if `marks` is wrong, only the class's own methods could have changed it.

## struct vs class in C++

In C++, a `struct` can do everything a class can (functions, access specifiers, constructors, inheritance). The **only** differences are the defaults:

| `struct` | `class` |
|---|---|
| Members are **public** by default | Members are **private** by default |
| Inheritance is **public** by default | Inheritance is **private** by default |
| Conventionally for simple data groups | Conventionally for objects with hidden data and behaviour |

(In the C language, structs couldn't contain functions or access specifiers at all.)

:::key
- Encapsulation = bundle data + methods in a class, and hide the data (`private`).
- Data hiding is achieved by encapsulation + access specifiers.
- `private` (class default), `protected` (also for children), `public` (everyone).
- Getters/setters let the class validate every change.
- struct vs class differs only in default access (public vs private).
:::

:::mistakes
- Making all data `public` "to make things easier" — defeats encapsulation.
- Saying "struct can't have functions in C++" — it can (that's C).
- Thinking `protected` members are accessible from `main` — they are not.
- Writing getters/setters that do no validation at all *and* calling that "data hiding" — the point is controlled access.
:::

:::exam
- *"What is encapsulation? How is data hiding achieved in C++?"*
- *"Explain access specifiers with a program."*
- *"Differentiate struct and class in C++."*
:::

:::def
**Encapsulation** is the wrapping of data members and the member functions that operate on them into a single unit, the class. **Data hiding** is restricting direct access to an object's data by declaring it `private`, so that it can be accessed only through the class's public member functions.
:::

## Quick Check

:::q Q1 · Can `main()` access a `protected` member of a class through an object?
:::ans
No. `protected` members are accessible inside the class and its derived classes only.
:::
:::

:::q Q2 · What is the default access of members in `struct S { int x; };` and `class C { int x; };`?
:::ans
`S::x` is **public**; `C::x` is **private**.
:::
:::

:::q Q3 · Give one advantage of making data private and using setter functions.
:::ans
The setter can **validate** values, so the object can never hold invalid data (e.g. marks outside 0–100).
:::
:::
