**A structure (`struct`) groups related variables of *different* types under one name, so they travel together as one unit.** It is the first step from plain variables towards classes.

## The Problem: Related Data Scattered Everywhere

A student has a roll number (int), a name (text), a CGPA (decimal). With what we know so far:

```cpp
int roll1 = 101;  char name1[20] = "Asha";  double cgpa1 = 8.9;
int roll2 = 102;  char name2[20] = "Ravi";  double cgpa2 = 7.5;
```

Problems: nothing says these three variables belong together; passing "a student" to a function needs three parameters; storing 60 students needs three separate arrays kept in sync. An array can't help — it needs every element to be the **same** type.

## Understanding Structures

A `struct` creates a **new data type** that bundles several members:

```cpp
struct Student
{
    int roll;
    char name[20];
    double cgpa;
};               // <- the semicolon is required!
```

Now `Student` is a type, just like `int`. `Student s1;` creates one variable that contains a roll, a name and a CGPA. We reach each member with the **dot operator**: `s1.roll`.

:::analogy
A **student ID card**. Your name, roll number, photo and branch are different kinds of information, but they're printed on one card and carried around together. A `struct` is the card's *design*; each actual card is a variable of that struct type.
:::

## Creating, Initializing and Using Structures

```cpp
#include <iostream>
using namespace std;

struct Date { int d, m, y; };          // a small struct

struct Student
{
    int roll;
    char name[20];
    double cgpa;
    Date dob;                           // a struct INSIDE a struct (nested)
};

int main()
{
    Student s1 = {101, "Asha", 8.9, {15, 8, 2004}};   // initialize in member order
    Student s2;
    s2.roll = 102;                                     // assign members one by one
    s2.cgpa = 7.5;

    cout << s1.roll << " " << s1.name << " " << s1.cgpa << " born "
         << s1.dob.d << "/" << s1.dob.m << "/" << s1.dob.y << endl;

    Student s3 = s1;          // copying a whole struct copies every member
    s3.roll = 999;            // s1 is not affected
    cout << s1.roll << " " << s3.roll << " " << s3.name << endl;

    Student cls[2] = {{1, "Ravi", 9.1, {1, 2, 2004}},     // an ARRAY of structures
                      {2, "Meena", 8.4, {3, 4, 2004}}};
    for (int i = 0; i < 2; i++) cout << cls[i].name << " ";
    cout << endl;
    return 0;
}
```

```output
101 Asha 8.9 born 15/8/2004
101 999 Asha
Ravi Meena 
```

## Structures as Function Arguments

You can pass a struct to a function exactly like any variable — by value, by reference or by pointer (Lesson 2.4). With a pointer, use the **arrow operator** `->` to reach members.

```cpp
#include <iostream>
using namespace std;

struct Point { int x, y; };

void print(Point p)                 // by value: works on a copy
{
    cout << "(" << p.x << ", " << p.y << ")" << endl;
}

void moveRight(Point &p, int dx)    // by reference: changes the original
{
    p.x += dx;
}

void moveUp(Point *p, int dy)       // by pointer: use ->  (same as (*p).y)
{
    p->y += dy;
}

Point midpoint(Point a, Point b)    // a function can also RETURN a struct
{
    Point m = {(a.x + b.x) / 2, (a.y + b.y) / 2};
    return m;
}

int main()
{
    Point p = {1, 2}, q = {5, 8};
    moveRight(p, 3);
    moveUp(&p, 10);
    print(p);
    print(midpoint(p, q));
    return 0;
}
```

```output
(4, 12)
(4, 10)
```

## From Structures to Classes

A plain structure groups **data**. But it doesn't stop anyone from setting `s1.cgpa = 57.0` (impossible CGPA!), and the functions that work on students live separately. Classes fix both: they add **functions inside** the type and **access control** (`private`). In fact, in C++ a `struct` *can* contain functions too — the only difference from a `class` is the default access (see Lesson 3.4).

:::key
- `struct` groups variables of different types into one new type; end it with `;`.
- Access members with `.` (and with `->` through a pointer).
- Brace-initialize in member order; copying a struct copies every member.
- Structs can be nested, stored in arrays, passed to and returned from functions.
:::

:::mistakes
- Forgetting the semicolon after the closing brace.
- Initializing members in the wrong order.
- Comparing two structs with `==` → error (unless you overload it, Lesson 4.4).
- Using `.` with a pointer (`p.x`) instead of `p->x`.
- Passing big structs by value when a `const &` would do.
:::

:::exam
- *"What is a structure? How is it declared, initialized and accessed?"*
- *"Write a program using an array of structures to store and display student records."*
- *"Explain structures as function arguments."*
:::

:::def
A **structure** is a user-defined data type that groups variables of different data types (called members) under a single name. Members are accessed using the dot operator (`.`), or the arrow operator (`->`) through a pointer.
:::

## Quick Check

:::q Q1 · What's the difference between an array and a structure?
:::ans
An **array** holds many elements of the **same** type accessed by index; a **structure** holds members of **different** types accessed by name.
:::
:::

:::q Q2 · Given `Point *ptr = &p;`, write two ways to access `x`.
:::ans
`ptr->x` and `(*ptr).x`.
:::
:::
