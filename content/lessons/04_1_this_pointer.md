**`this` is a hidden pointer, available inside every (non-static) member function, that points to the object the function was called on.**

## The Problem: One Copy of Code, Many Objects

In Lesson 3.3 we learned that every object has its own data, but **member functions are shared** — there's only one copy of `area()` for all rectangles. So when you call `r1.area()` and then `r2.area()`, how does the *same* code know to use r1's length the first time and r2's the second time?

Answer: C++ secretly passes the address of the calling object to the function. Inside, that address is called **`this`**.

```text
   r1.area();      is really treated like      area(&r1);   → inside, this = &r1
   r2.area();                                  area(&r2);   → inside, this = &r2
   and every "length" inside area() really means  this->length
```

:::analogy
In a classroom, the teacher says *"Open **your** notebook."* One sentence, but each student opens **their own** notebook. The word "your" changes meaning depending on who hears it. `this` is the program's "your": it means "the object that is executing this function right now".
:::

## Using this

Most of the time `this` is used silently. You write it explicitly in three situations:

**1. A parameter has the same name as a data member.**

```cpp
void setRoll(int roll) { this->roll = roll; }   // member = parameter
```
Without `this->`, `roll = roll;` just assigns the parameter to itself.

**2. Returning the object itself (`return *this;`) to allow method chaining.**
`*this` is "the object `this` points to". Returning it **by reference** lets calls be chained: `s.setRoll(12).setMarks(91.5);`

**3. Comparing with another object** — e.g. "am I the same object as `other`?" → `this == &other` (used in the assignment operator, Lesson 4.3).

```cpp
#include <iostream>
using namespace std;

class Student
{
    int roll;
    double marks;
public:
    Student& setRoll(int roll)          // parameter shares the member's name
    {
        this->roll = roll;               // this->roll is the MEMBER
        return *this;                    // give back the calling object
    }
    Student& setMarks(double marks)
    {
        this->marks = marks;
        return *this;
    }
    bool isSame(const Student &other) { return this == &other; }
    void show() { cout << roll << " " << marks << endl; }
};

int main()
{
    Student s, t;
    s.setRoll(12).setMarks(91.5);       // chaining works because each call returns s itself
    s.show();
    cout << s.isSame(s) << " " << s.isSame(t) << endl;
    return 0;
}
```

```output
12 91.5
1 0
```

## Facts About this

- Type: in a member function of class `X`, `this` is a pointer to `X` (textbooks write `X* const` — a constant pointer: you can't make `this` point elsewhere).
- Available only in **non-static** member functions. **Static** functions (Lesson 4.6) have no calling object, so no `this`.
- `this->x` and `(*this).x` mean the same thing.

:::key
- `this` = address of the object that called the member function.
- Every member name inside a method is really `this->member`.
- Uses: resolve name clashes, `return *this` for chaining, self-comparison.
- No `this` in static member functions.
:::

:::mistakes
- Writing `roll = roll;` when the parameter has the same name as the member.
- Writing `this.roll` (Java style). In C++ `this` is a pointer: `this->roll`.
- Returning `*this` **by value** for chaining — the next call then modifies a temporary copy.
- Using `this` inside a static function → error.
:::

:::exam
- *"What is the `this` pointer? Explain its uses with a program."* → name-clash + chaining program above.
:::

:::def
The **`this` pointer** is an implicit pointer available in every non-static member function that holds the address of the object on which the function was invoked. It is used to access the invoking object's members, to resolve name conflicts between data members and parameters, and to return the invoking object (`return *this`).
:::

## Quick Check

:::q Q1 · What is printed? `class P { int x; public: P(int x) { x = x; } void set(int x) { this->x = x; } int get() { return x; } };` with `P p(5); p.set(9); cout << p.get();`
:::ans
`9`. (The constructor's `x = x;` did nothing useful — a classic bug — but `set` correctly uses `this->x`.)
:::
:::

:::q Q2 · Why is `this` not available in a static member function?
:::ans
A static function is called on the class, not on an object, so there is no "calling object" whose address could be `this`.
:::
:::
