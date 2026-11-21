**A static data member is shared by all objects of a class (only one copy exists). A static member function belongs to the class itself, not to any one object.** This lesson also covers `const` member functions and recursive member functions.

## The Problem: Information That Belongs to the Whole Class

How many `Student` objects currently exist? You can't store that count inside each student — each would hold its own, different copy, and they'd go out of sync. The count isn't a property of *one* student; it's a property of the **class as a whole**.

:::analogy
In a classroom, every student has their own notebook (normal data member). But there is **one whiteboard** shared by everyone (static data member). If one student writes on the whiteboard, everyone sees it. The attendance count written on the whiteboard belongs to the class, not to any single student.
:::

## Static Data Members

```cpp
#include <iostream>
using namespace std;

class Student
{
    int roll;                       // one per object
    static int count;               // ONE shared copy (declared here)
public:
    Student(int r) : roll(r) { count++; }
    ~Student()                { count--; }
    static int getCount()     { return count; }     // static member function
};

int Student::count = 0;             // DEFINED here, outside the class (allocates the memory)

int main()
{
    cout << "Initially: " << Student::getCount() << endl;   // works with no objects at all
    Student a(1), b(2);
    {
        Student c(3);
        cout << "Inside block: " << Student::getCount() << endl;
    }                               // c destroyed → count--
    cout << "After block: " << a.getCount() << endl;        // can also be called via an object
    return 0;
}
```

```output
Initially: 0
Inside block: 3
After block: 2
```

```text
     a: roll=1        b: roll=2        c: roll=3
          \               |               /
           └──────►  Student::count  ◄───┘      (one shared copy)
```

**Facts:**
- Only **one** copy, shared by all objects; it exists even before any object is created.
- Must be **defined once outside the class**: `int Student::count = 0;` (C++17 also allows `inline static int count = 0;` inside).
- Default value is 0.

## Static Member Functions

- Belong to the class: call as `ClassName::f()` (an object also works).
- Have **no `this` pointer** → can access **only static members** directly.
- Cannot be `virtual` or `const`.

| Static data member | Normal data member |
|---|---|
| One copy for the whole class | One copy per object |
| Defined outside the class | Set in the constructor |
| Exists even without objects | Exists only inside an object |
| `Class::x` or `obj.x` | `obj.x` |

## const Member Functions and const Objects

A member function marked `const` **promises not to change** the object. A `const` object can call **only** `const` member functions. Mark every getter/display function `const`.

```cpp
#include <iostream>
using namespace std;

class Circle
{
    double r;
public:
    Circle(double radius) : r(radius) { }
    double area() const { return 3.14 * r * r; }   // read-only promise
    void setRadius(double x) { r = x; }            // modifies
};

int main()
{
    const Circle c(2);         // a const object
    cout << c.area() << endl;  // OK: area() is const
    // c.setRadius(5);         // ERROR: setRadius() isn't const
    return 0;
}
```

```output
12.56
```

## Member Functions Calling Each Other, and Recursive Member Functions

Inside a class, a member function can call another member function **directly by name** — no object or dot needed, because it uses the same `this`. A member function can even call **itself**: a **recursive member function**.

```cpp
#include <iostream>
using namespace std;

class MathUtil
{
    int n;
public:
    MathUtil(int x) : n(x) { }
    long long factorial(int k) const        // recursive member function
    {
        if (k <= 1) return 1;
        return k * factorial(k - 1);
    }
    int sumDigits(int k) const              // another recursive member
    {
        if (k == 0) return 0;
        return k % 10 + sumDigits(k / 10);
    }
    void report() const                     // calls the other members directly
    {
        cout << n << "! = " << factorial(n) << ", digit sum of " << n * 111
             << " = " << sumDigits(n * 111) << endl;
    }
};

int main()
{
    MathUtil m(5);
    m.report();
    return 0;
}
```

```output
5! = 120, digit sum of 555 = 15
```

:::key
- Static data member: one shared copy; define it outside the class.
- Static member function: no `this`, only static members, call as `Class::f()`.
- `const` member functions can't modify the object; const objects can call only them.
- Members can call each other by name; a recursive member function calls itself.
:::

:::mistakes
- Forgetting `int Student::count = 0;` → linker error "undefined reference".
- Writing `static` again in that definition (`static int Student::count = 0;`) → error.
- Using a non-static member (like `roll`) inside a static function → error.
- Changing a member inside a `const` function → error.
:::

:::exam
- *"Explain static data members and static member functions with an object-counter program."* (Very common.)
- *"Why can't a static member function access non-static members?"*
- Output questions mixing static counters with constructors/destructors.
:::

:::def
A **static data member** is a class member declared with `static` that is shared by all objects of the class; only one copy exists, and it must be defined outside the class. A **static member function** is a member function declared `static` that is not associated with any object, has no `this` pointer, can access only static members directly, and is invoked using the class name and scope resolution operator.
:::

## Quick Check

:::q Q1 · Predict: `class I { static int c; int id; public: I(){ id = ++c; } void s(){ cout << id << "/" << c << " "; } }; int I::c = 0;` with `I a, b; a.s(); I d; a.s(); d.s();`
:::ans
`1/2 1/3 3/3` — `id` is per object, `c` is shared.
:::
:::

:::q Q2 · Can a static member function be called before any object exists?
:::ans
Yes — e.g. `Student::getCount()`, because it belongs to the class, not to an object.
:::
:::
