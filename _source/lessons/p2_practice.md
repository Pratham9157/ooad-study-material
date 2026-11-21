:::tip
These questions mix everything up to Chapter 4. Constructor/destructor **order** questions and **copy constructor call count** questions are examiners' favourites — trace them carefully, writing each line of output as you go.
:::

## Section A · Definitions & Short Answers

:::q A1 · Define class and object. How are they related?
:::ans
A **class** is a user-defined data type / blueprint that defines data members and member functions common to a set of objects. An **object** is an instance of a class — a run-time entity with state, behaviour and identity. Relation: an object is to its class what a variable is to its type (`int x;` ↔ `Student s;`). A class takes no memory for data members until objects are created; each object has its own copy of the data members and shares the member functions.
:::
:::

:::q A2 · Differentiate between encapsulation and abstraction.
:::ans
**Abstraction** = exposing only essential features (what an object does) and hiding unnecessary details — a **design-level** concept (e.g., public interface, abstract classes). **Encapsulation** = binding data and the functions that operate on it into one unit (class) and restricting direct access (private members) — an **implementation-level** mechanism. Encapsulation is how we **achieve** abstraction and data hiding in C++. Example: a car's pedals/steering = abstraction; the engine sealed under the bonnet = encapsulation.
:::
:::

:::q A3 · List the characteristics of a constructor.
:::ans
Same name as the class; no return type (not even void); invoked automatically when an object is created; normally public; can be overloaded; can have default arguments; cannot be virtual, static or const; not inherited; address cannot be taken; if none is defined, the compiler provides a default constructor (but not if any constructor is user-defined).
:::
:::

:::q A4 · What is a copy constructor? When is it invoked? Why is its argument passed by reference?
:::ans
A **copy constructor** initializes a new object using an existing object of the same class: `X(const X &obj)`. **Invoked** when (1) an object is initialized from another (`X b = a;`, `X b(a);`), (2) an object is passed **by value** to a function, (3) an object is returned by value (may be elided by the compiler). The argument must be a **reference** because passing by value would require a copy, which calls the copy constructor again → infinite recursion (compile error).
:::
:::

:::q A5 · Distinguish between shallow copy and deep copy.
:::ans
**Shallow copy** copies member values as they are; for a pointer member only the **address** is copied, so both objects share the same heap memory (changes affect both; destructors delete it twice → crash). The compiler-generated copy constructor/assignment do this. **Deep copy** allocates **new memory** for the copy and copies the **contents**, so each object owns independent memory. Requires a user-defined copy constructor and assignment operator.
:::
:::

:::q A6 · What is the `this` pointer? Give two uses.
:::ans
`this` is an implicit constant pointer, available in every non-static member function, holding the address of the object that invoked the function. Uses: (1) resolve name conflicts (`this->x = x;`), (2) return the invoking object (`return *this;`) for chaining, (3) compare objects/self-assignment check (`if (this == &other)`).
:::
:::

:::q A7 · What is a friend function? State its properties.
:::ans
A non-member function declared with keyword `friend` inside a class, allowed to access that class's private and protected members. Properties: not in class scope; invoked like a normal function (not via object); no `this` pointer; accesses members via object arguments; can be declared in public or private section; friendship is not inherited, not transitive, not mutual; can be a friend of multiple classes.
:::
:::

:::q A8 · List the operators that cannot be overloaded.
:::ans
`::` (scope resolution), `.` (member access), `.*` (pointer-to-member access), `?:` (conditional), `sizeof`, `typeid` (also `alignof`, `noexcept`). Additionally `=`, `()`, `[]`, `->` can be overloaded **only** as member functions.
:::
:::

:::q A9 · What is a static data member? Why must it be defined outside the class?
:::ans
A data member declared with `static` that is **shared by all objects** of the class (one copy). The declaration inside the class does not allocate storage; the **definition outside** (`int X::count = 0;`) allocates it once for the whole program. Without it, you get a linker error. (C++17 allows `inline static int count = 0;` inside the class instead.)
:::
:::

:::q A10 · Why can't a static member function access non-static members?
:::ans
A static member function is not called on any particular object and has **no `this` pointer**. Non-static members belong to individual objects; without `this`, the function wouldn't know **which** object's members to use.
:::
:::

## Section B · MCQs

:::q B1 · Which is the default access specifier for members of a class?
(a) public (b) private (c) protected (d) none
:::ans
**(b) private** (for `struct` it is public).
:::
:::

:::q B2 · A destructor:
(a) can be overloaded (b) can take arguments (c) can be virtual (d) returns int
:::ans
**(c) can be virtual**.
:::
:::

:::q B3 · `Box b();` in `main` does what?
(a) creates object b with default constructor (b) declares a function b returning Box (c) compile error always (d) creates an array
:::ans
**(b)** — the "most vexing parse". It declares a function.
:::
:::

:::q B4 · The postfix increment operator is distinguished from prefix by:
(a) a `char` dummy argument (b) an `int` dummy argument (c) return type (d) the `friend` keyword
:::ans
**(b)** — `X operator++(int)`.
:::
:::

:::q B5 · How many arguments does a binary operator function take when overloaded as a friend?
(a) 0 (b) 1 (c) 2 (d) 3
:::ans
**(c) 2** (as a member it takes 1).
:::
:::

:::q B6 · Which of the following must be overloaded as a member function?
(a) `+` (b) `<<` (c) `=` (d) `==`
:::ans
**(c) `=`** (also `()`, `[]`, `->`).
:::
:::

:::q B7 · A static member function can be called using:
(a) only an object (b) only the class name with `::` (c) either class name with `::` or an object (d) only through `this`
:::ans
**(c)**.
:::
:::

:::q B8 · Which statement is FALSE about friend functions?
(a) They can access private data (b) They are invoked using an object and dot operator (c) They have no `this` pointer (d) Friendship is not inherited
:::ans
**(b)** is false — a friend is called like a normal function.
:::
:::

:::q B9 · The size of an object of an empty class in C++ is:
(a) 0 (b) 1 (c) 4 (d) undefined
:::ans
**(b) 1** byte.
:::
:::

:::q B10 · Which is used to define a member function outside the class?
(a) `.` (b) `->` (c) `::` (d) `#`
:::ans
**(c)** the scope resolution operator `::`.
:::
:::

## Section C · Predict the Output

:::q C1 · Predict the output.
```cpp
#include <iostream>
using namespace std;
class T
{
    int id;
public:
    T(int i) : id(i) { cout << "C" << id << " "; }
    ~T() { cout << "D" << id << " "; }
};
T t0(0);
int main()
{
    T t1(1);
    for (int i = 2; i <= 3; i++)
    {
        T t(i);
    }
    T t4(4);
    cout << "| ";
    return 0;
}
```
:::ans
```output
C0 C1 C2 D2 C3 D3 C4 | D4 D1 D0 
```
The loop object is created and destroyed in **each** iteration. At the end of `main`, locals die in reverse order (t4, t1); the global t0 dies last, after `main` returns.
:::
:::

:::q C2 · How many times is the copy constructor called? Show the output.
```cpp
#include <iostream>
using namespace std;
class A
{
public:
    A() { cout << "D "; }
    A(const A &) { cout << "C "; }
};
void f(A x) { }
void g(A &x) { }
int main()
{
    A a1;
    A a2 = a1;
    A a3(a2);
    f(a1);
    g(a1);
    a3 = a1;
    cout << endl;
    return 0;
}
```
:::ans
```output
D C C C 
```
Copy constructor: 3 times — `a2 = a1` (initialization), `a3(a2)`, and `f(a1)` (pass by value). `g(a1)` passes a reference (no copy). `a3 = a1` is **assignment**, not copy construction.
:::
:::

:::q C3 · Predict the output.
```cpp
#include <iostream>
using namespace std;
class Item
{
    static int count;
    int id;
public:
    Item() { id = ++count; }
    void show() { cout << id << "/" << count << " "; }
};
int Item::count = 0;
int main()
{
    Item a, b;
    a.show();
    Item c;
    a.show(); b.show(); c.show();
    cout << endl;
    return 0;
}
```
:::ans
```output
1/2 1/3 2/3 3/3 
```
`id` is per object; `count` is shared. When `a.show()` is first called only a and b exist → count 2.
:::
:::

:::q C4 · Predict the output.
```cpp
#include <iostream>
using namespace std;
class P
{
    int x;
public:
    P(int x) { x = x; }
    void set(int x) { this->x = x; }
    int get() { return x; }
};
int main()
{
    P p(5);
    p.set(9);
    cout << p.get() << endl;
    return 0;
}
```
:::ans
```output
9
```
In the constructor, `x = x;` assigns the **parameter to itself** — the member stays uninitialized (a classic bug, reading it would be garbage). But `set(9)` uses `this->x` correctly, so `get()` returns 9.
:::
:::

:::q C5 · Predict the output.
```cpp
#include <iostream>
using namespace std;
class Num
{
    int v;
public:
    Num(int a = 0) : v(a) { }
    Num operator+(const Num &o) const { return Num(v + o.v); }
    Num operator++(int) { Num t = *this; v += 10; return t; }
    Num& operator++()   { v += 1; return *this; }
    int get() const { return v; }
};
int main()
{
    Num a(5), b(7);
    Num c = a + b;
    Num d = c++;
    Num e = ++c;
    cout << c.get() << " " << d.get() << " " << e.get() << endl;
    return 0;
}
```
:::ans
```output
23 12 23
```
c = 12. `d = c++` → postfix returns old (12), c becomes 22. `e = ++c` → prefix: c becomes 23, returns c → e = 23.
:::
:::

:::q C6 · Predict the output.
```cpp
#include <iostream>
using namespace std;
class Base
{
public:
    Base()  { cout << "B"; }
    ~Base() { cout << "~B"; }
};
class Holder
{
    Base b1, b2;
public:
    Holder()  { cout << "H"; }
    ~Holder() { cout << "~H"; }
};
int main()
{
    Holder h;
    cout << " | ";
    return 0;
}
```
:::ans
```output
BBH | ~H~B~B
```
Member objects are constructed **before** the containing object's constructor body runs (in declaration order), and destroyed **after** its destructor body (reverse order). This is the C++ form of **composition**.
:::
:::

:::q C7 · Predict the output.
```cpp
#include <iostream>
using namespace std;
class Acc
{
    int bal;
public:
    Acc(int b) : bal(b) { }
    Acc& add(int x) { bal += x; return *this; }
    Acc  addCopy(int x) { bal += x; return *this; }
    int get() { return bal; }
};
int main()
{
    Acc a(100), b(100);
    a.add(10).add(20);
    b.addCopy(10).addCopy(20);
    cout << a.get() << " " << b.get() << endl;
    return 0;
}
```
:::ans
```output
130 110
```
`add` returns a **reference** → the second call works on `a` itself. `addCopy` returns a **copy** → the first call changes `b` to 110, but the second call modifies the temporary copy, not `b`.
:::
:::

:::q C8 · Predict the output.
```cpp
#include <iostream>
using namespace std;
class Box
{
    int w;
public:
    Box(int x = 2) : w(x) { cout << "ctor" << w << " "; }
    friend int twice(Box b) { return 2 * b.w; }
};
int main()
{
    Box arr[2];
    Box *p = new Box(9);
    cout << twice(*p) << " ";
    delete p;
    cout << endl;
    return 0;
}
```
:::ans
```output
ctor2 ctor2 ctor9 18 
```
An array of 2 objects calls the default (defaulted-argument) constructor twice. The friend function (defined inside the class, still not a member) is called normally. Passing `*p` by value uses the implicit copy constructor (prints nothing).
:::
:::

## Section D · Find the Errors

:::q D1 · Find all errors.
```cpp
#include <iostream>
using namespace std;
//@expect: compile-error
class Test
{
    int a;
    static int s;
public:
    Test(int x) { a = x; }
    static void show() { cout << a << s; }
};
int main()
{
    Test t;
    Test::show();
    return 0;
}
```
:::ans
1. `show()` is static but uses non-static `a` → error.
2. `Test t;` — only a parameterized constructor exists, so no default constructor → error.
3. `static int s;` is never defined outside the class (`int Test::s = 0;`) → linker error once the others are fixed.
:::
:::

:::q D2 · What's wrong?
```cpp
class Point
{
    int x, y;
public:
    Point operator+(Point a, Point b);
};
```
:::ans
As a **member**, binary `operator+` must take **one** parameter (the left operand is `*this`): `Point operator+(const Point &b) const;`. To take two parameters, declare it as a friend/non-member: `friend Point operator+(const Point &a, const Point &b);`.
:::
:::

:::q D3 · Find the error.
```cpp
#include <iostream>
using namespace std;
//@expect: compile-error
class Circle
{
    double r;
public:
    Circle(double x) : r(x) { }
    double area() { return 3.14 * r * r; }
};
int main()
{
    const Circle c(1.0);
    cout << c.area();
    return 0;
}
```
:::ans
`c` is a `const` object, but `area()` is not a `const` member function → error ("passing 'const Circle' as 'this' argument discards qualifiers"). Fix: `double area() const { … }`.
:::
:::

:::q D4 · Find the error.
```cpp
class A
{
    const int k;
public:
    A(int v) { k = v; }
};
```
:::ans
A `const` data member cannot be **assigned**; it must be **initialized** in the member initializer list: `A(int v) : k(v) { }`.
:::
:::

## Section E · Programming Questions

:::q E1 · Define a class `Time` (hours, minutes) with a constructor, an overloaded `+` operator to add two times (normalize minutes ≥ 60) and a `show()` function.
:::ans
```cpp
#include <iostream>
using namespace std;

class Time
{
    int h, m;
public:
    Time(int hh = 0, int mm = 0) : h(hh), m(mm) { }
    Time operator+(const Time &t) const
    {
        int total = (h + t.h) * 60 + m + t.m;   // work in minutes
        return Time(total / 60, total % 60);
    }
    void show() const { cout << h << "h " << m << "m" << endl; }
};

int main()
{
    Time t1(2, 45), t2(1, 30);
    Time t3 = t1 + t2;
    t3.show();
    return 0;
}
```
```output
4h 15m
```
:::
:::

:::q E2 · Write a class `Employee` that counts how many Employee objects currently exist, using a static data member and a static member function. Demonstrate creation and destruction.
:::ans
```cpp
#include <iostream>
using namespace std;

class Employee
{
    int id;
    static int alive;
public:
    Employee(int i) : id(i) { alive++; }
    ~Employee() { alive--; }
    static int count() { return alive; }
};
int Employee::alive = 0;

int main()
{
    Employee e1(1);
    {
        Employee e2(2), e3(3);
        cout << "Inside: " << Employee::count() << endl;
    }
    cout << "Outside: " << Employee::count() << endl;
    Employee *p = new Employee(4);
    cout << "After new: " << Employee::count() << endl;
    delete p;
    cout << "After delete: " << Employee::count() << endl;
    return 0;
}
```
```output
Inside: 3
Outside: 1
After new: 2
After delete: 1
```
:::
:::

:::q E3 · Write a program using a friend function to find the greater of the private data of two different classes `X` and `Y`.
:::ans
```cpp
#include <iostream>
using namespace std;

class Y;                                  // forward declaration

class X
{
    int a;
public:
    X(int v) : a(v) { }
    friend void findGreater(const X &, const Y &);
};

class Y
{
    int b;
public:
    Y(int v) : b(v) { }
    friend void findGreater(const X &, const Y &);
};

void findGreater(const X &x, const Y &y)
{
    if (x.a > y.b) cout << "X has greater value: " << x.a << endl;
    else           cout << "Y has greater or equal value: " << y.b << endl;
}

int main()
{
    X x(40);
    Y y(65);
    findGreater(x, y);
    return 0;
}
```
```output
Y has greater or equal value: 65
```
:::
:::

:::q E4 · Write a class `Vector2` with overloaded `==`, unary `-` and `<<` (as friend). Show their use.
:::ans
```cpp
#include <iostream>
using namespace std;

class Vector2
{
    int x, y;
public:
    Vector2(int a = 0, int b = 0) : x(a), y(b) { }
    bool operator==(const Vector2 &v) const { return x == v.x && y == v.y; }
    Vector2 operator-() const { return Vector2(-x, -y); }
    friend ostream& operator<<(ostream &os, const Vector2 &v)
    {
        os << "(" << v.x << ", " << v.y << ")";
        return os;
    }
};

int main()
{
    Vector2 a(2, -3), b(2, -3), c = -a;
    cout << a << " " << c << endl;
    cout << (a == b) << " " << (a == c) << endl;
    return 0;
}
```
```output
(2, -3) (-2, 3)
1 0
```
:::
:::

:::q E5 · Write a class `Array` that stores `n` integers dynamically. Provide a constructor, a deep-copy constructor, an overloaded assignment operator, a destructor and a `display()` function. Show that copies are independent.
:::ans
```cpp
#include <iostream>
using namespace std;

class Array
{
    int *a;
    int n;
public:
    Array(int size) : n(size)
    {
        a = new int[n];
        for (int i = 0; i < n; i++) a[i] = i + 1;
    }
    Array(const Array &o) : n(o.n)                 // deep copy
    {
        a = new int[n];
        for (int i = 0; i < n; i++) a[i] = o.a[i];
    }
    Array& operator=(const Array &o)               // deep assignment
    {
        if (this != &o)
        {
            delete[] a;
            n = o.n;
            a = new int[n];
            for (int i = 0; i < n; i++) a[i] = o.a[i];
        }
        return *this;
    }
    ~Array() { delete[] a; }
    void set(int i, int v) { a[i] = v; }
    void display() const
    {
        for (int i = 0; i < n; i++) cout << a[i] << " ";
        cout << endl;
    }
};

int main()
{
    Array x(3);
    Array y = x;        // copy constructor
    Array z(5);
    z = x;              // assignment operator
    y.set(0, 100);
    z.set(2, 300);
    x.display(); y.display(); z.display();
    return 0;
}
```
```output
1 2 3 
100 2 3 
1 2 300 
```
:::
:::

## Section F · Long Answer

:::q F1 · Explain the basic concepts of OOP with suitable examples.
:::ans
Write each concept with a definition + real-world example + one-line C++ illustration (see [Lesson 3.1](03_1_why_oop.html)): **Object** (state, behaviour, identity), **Class** (blueprint; user-defined type), **Abstraction** (essential features only), **Encapsulation** (bundling data + functions), **Data hiding** (private members), **Inheritance** (reusability, is-a: `class Car : public Vehicle`), **Polymorphism** (compile-time: overloading; run-time: virtual functions), **Dynamic binding** (late binding at run time), **Message passing** (`obj.method(args)`). End with benefits: reuse, security, maintainability, real-world modelling, extensibility.
:::
:::

:::q F2 · Explain the types of constructors in C++ with one program that uses all of them, and explain constructor overloading.
:::ans
Types: **default**, **parameterized**, **copy**, constructor with **default arguments**. Constructor overloading = several constructors with different parameter lists; the right one is chosen from the arguments at object creation.

```cpp
#include <iostream>
using namespace std;

class Student
{
    int roll;
    double cgpa;
public:
    Student()                       : roll(0), cgpa(0)   { cout << "default" << endl; }
    Student(int r, double c = 6.0)  : roll(r), cgpa(c)   { cout << "parameterized" << endl; }
    Student(const Student &s)       : roll(s.roll), cgpa(s.cgpa) { cout << "copy" << endl; }
    void show() const { cout << roll << " " << cgpa << endl; }
};

int main()
{
    Student a;            // default
    Student b(7, 9.1);    // parameterized
    Student c(8);         // parameterized using default argument
    Student d = b;        // copy
    a.show(); b.show(); c.show(); d.show();
    return 0;
}
```
```output
default
parameterized
parameterized
copy
0 0
7 9.1
8 6
7 9.1
```
:::
:::

:::q F3 · What is operator overloading? Explain the rules and overload both prefix and postfix `--` for a class `Stock`.
:::ans
Definition + rules: see [Lesson 4.4](04_4_operator_overloading.html). Program:

```cpp
#include <iostream>
using namespace std;

class Stock
{
    int qty;
public:
    Stock(int q) : qty(q) { }
    Stock& operator--()        { --qty; return *this; }          // prefix
    Stock  operator--(int)     { Stock old = *this; qty--; return old; } // postfix
    int get() const { return qty; }
};

int main()
{
    Stock s(10);
    Stock a = --s;    // s=9, a=9
    Stock b = s--;    // b=9, s=8
    cout << s.get() << " " << a.get() << " " << b.get() << endl;
    return 0;
}
```
```output
8 9 9
```
:::
:::
