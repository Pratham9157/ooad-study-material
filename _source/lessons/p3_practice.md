:::tip
This set is the **Part I exam simulation**. It mixes inheritance, virtual functions, formatting, files and strings with earlier topics (constructors, static, operators, recursion). Do it in one sitting if you can (~2 hours) and score yourself.
:::

## Section A · True or False (justify in one line)

:::q A1 · A derived class can access the private members of its base class directly.
:::ans
**False.** Private members are inherited (exist in the object) but are not accessible in the derived class; use `protected` or public accessors.
:::
:::

:::q A2 · Constructors can be virtual.
:::ans
**False.** A constructor cannot be virtual (the object's type/vptr isn't set up yet). Destructors can be virtual.
:::
:::

:::q A3 · An abstract class can have constructors and data members.
:::ans
**True.** It just cannot be instantiated directly; its constructor runs when a derived object is created.
:::
:::

:::q A4 · `setw()` remains in effect for all subsequent outputs.
:::ans
**False.** `setw` affects only the next output item.
:::
:::

:::q A5 · In multiple inheritance, base class constructors are called in the order listed in the derived class's initializer list.
:::ans
**False.** They are called in the order the base classes are **declared** in the class header.
:::
:::

:::q A6 · Opening a file with `ofstream` in default mode erases its previous contents.
:::ans
**True.** Default mode `ios::out` truncates; use `ios::app` to keep the contents.
:::
:::

:::q A7 · A friend function of a base class is automatically a friend of the derived class.
:::ans
**False.** Friendship is not inherited.
:::
:::

:::q A8 · A static member function can be virtual.
:::ans
**False.** Static functions have no `this`/object, so they can't be dispatched through a vtable.
:::
:::

## Section B · MCQs

:::q B1 · Which feature enables run-time polymorphism in C++?
(a) function overloading (b) operator overloading (c) virtual functions (d) templates
:::ans
**(c) virtual functions** (called through base pointers/references).
:::
:::

:::q B2 · In `class D : protected B`, a public member of B becomes ____ in D.
(a) public (b) protected (c) private (d) inaccessible
:::ans
**(b) protected**.
:::
:::

:::q B3 · The diamond problem is solved by:
(a) virtual functions (b) virtual base classes (c) friend classes (d) abstract classes
:::ans
**(b) virtual base classes** (`class B : virtual public A`).
:::
:::

:::q B4 · Which of these is a pure virtual function?
(a) `virtual void f() {}` (b) `void f() = 0;` (c) `virtual void f() = 0;` (d) `virtual void f() = NULL;`
:::ans
**(c)**. (b) is not virtual, so `= 0` is illegal there.
:::
:::

:::q B5 · Which header is needed for `ifstream`?
(a) `<iostream>` (b) `<fstream>` (c) `<iomanip>` (d) `<file>`
:::ans
**(b) `<fstream>`**.
:::
:::

:::q B6 · `cout << setprecision(2) << 3.14159;` prints:
(a) 3.14 (b) 3.1 (c) 3 (d) 3.142
:::ans
**(b) 3.1** — without `fixed`, precision counts **significant digits**.
:::
:::

:::q B7 · Which stream is unbuffered?
(a) cout (b) clog (c) cerr (d) cin
:::ans
**(c) cerr**.
:::
:::

:::q B8 · `string s = "hello"; s.find("z")` returns:
(a) -1 (b) 0 (c) `string::npos` (d) error
:::ans
**(c) `string::npos`**.
:::
:::

:::q B9 · When a derived object is passed by value to a function taking a base object, it causes:
(a) dynamic binding (b) object slicing (c) compile error (d) memory leak
:::ans
**(b) object slicing**.
:::
:::

:::q B10 · Which mode positions the file pointer at the end on opening but allows moving elsewhere?
(a) `ios::app` (b) `ios::ate` (c) `ios::trunc` (d) `ios::out`
:::ans
**(b) `ios::ate`** (with `ios::app`, every write goes to the end).
:::
:::

## Section C · Predict the Output

:::q C1 · Predict the output.
```cpp
#include <iostream>
using namespace std;
class A
{
public:
    A()  { cout << "A"; }
    ~A() { cout << "~A"; }
};
class B : public A
{
public:
    B()  { cout << "B"; }
    ~B() { cout << "~B"; }
};
class C : public B
{
public:
    C()  { cout << "C"; }
    ~C() { cout << "~C"; }
};
int main()
{
    C obj;
    cout << " ";
    return 0;
}
```
:::ans
```output
ABC ~C~B~A
```
Multilevel: construction from the top base down; destruction in reverse.
:::
:::

:::q C2 · Predict the output.
```cpp
#include <iostream>
using namespace std;
class Base
{
public:
    virtual void show() { cout << "Base show" << endl; }
    void print() { cout << "Base print" << endl; }
};
class Derived : public Base
{
public:
    void show() { cout << "Derived show" << endl; }
    void print() { cout << "Derived print" << endl; }
};
int main()
{
    Derived d;
    Base *bp = &d;
    Base &br = d;
    Base b = d;
    bp->show();
    bp->print();
    br.show();
    b.show();
    return 0;
}
```
:::ans
```output
Derived show
Base print
Derived show
Base show
```
`show` is virtual → pointer/reference calls use the actual object (Derived). `print` is non-virtual → pointer type decides (Base). `Base b = d;` slices → a pure Base object.
:::
:::

:::q C3 · Predict the output.
```cpp
#include <iostream>
using namespace std;
class P
{
public:
    P(int x) { cout << "P" << x << " "; }
};
class Q
{
public:
    Q() { cout << "Q "; }
};
class R : public Q, public P
{
    P member;
public:
    R() : member(2), P(1) { cout << "R" << endl; }
};
int main()
{
    R r;
    return 0;
}
```
:::ans
```output
Q P1 P2 R
```
Order: base classes in **declaration order** (Q, then P), then **member objects** in declaration order (`member`), then the constructor body. The initializer-list order is irrelevant (GCC warns about it).
:::
:::

:::q C4 · Predict the output.
```cpp
#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    double x = 25.6789;
    cout << setw(8) << x << "|" << endl;
    cout << fixed << setprecision(1) << x << "|" << endl;
    cout << setfill('#') << setw(7) << x << "|" << endl;
    cout << left << setw(7) << 42 << "|" << endl;
    return 0;
}
```
:::ans
```output
 25.6789|
25.7|
###25.7|
42#####|
```
Line 1: default 6 significant digits → `25.6789` (7 chars) padded to width 8. Line 2: fixed, 1 decimal → `25.7`. Line 3: fill `#`, width 7, right-justified. Line 4: `left` puts padding on the right; fill `#` is still in effect.
:::
:::

:::q C5 · Predict the output.
```cpp
#include <iostream>
using namespace std;
class Shape
{
public:
    virtual int sides() { return 0; }
    void describe() { cout << "Sides: " << sides() << endl; }
};
class Triangle : public Shape { public: int sides() { return 3; } };
class Square   : public Shape { public: int sides() { return 4; } };
int main()
{
    Triangle t; Square s; Shape g;
    t.describe();
    s.describe();
    g.describe();
    return 0;
}
```
:::ans
```output
Sides: 3
Sides: 4
Sides: 0
```
Even though `describe()` is a non-virtual base function, it calls `sides()` through `this` (a base pointer), so the virtual call is dispatched to the real object's version.
:::
:::

:::q C6 · Predict the output.
```cpp
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string s = "Programming";
    cout << s.length() << " " << s.substr(3, 4) << " " << s.find('g') << endl;
    s.erase(0, 3);
    s += "!";
    cout << s << " " << s[0] << endl;
    return 0;
}
```
:::ans
```output
11 gram 3
gramming! g
```
`substr(3, 4)` = 4 chars from index 3 → "gram". First 'g' is at index 3. After erasing 3 chars: "gramming", plus "!".
:::
:::

:::q C7 · Predict the output.
```cpp
#include <iostream>
using namespace std;
class Counter
{
    static int total;
public:
    Counter() { total++; }
    static int get() { return total; }
};
int Counter::total = 0;
class Special : public Counter
{
public:
    Special() { cout << "Special#" << get() << " "; }
};
int main()
{
    Counter c1;
    Special s1, s2;
    cout << Counter::get() << endl;
    return 0;
}
```
:::ans
```output
Special#2 Special#3 3
```
Static members are inherited and **shared**. Each `Special` first runs `Counter()` (increments total), then its own body.
:::
:::

:::q C8 · Predict the output.
```cpp
#include <iostream>
using namespace std;
class Base
{
public:
    Base() { cout << "Base() "; show(); }
    virtual void show() { cout << "Base::show "; }
    virtual ~Base() { }
};
class Derived : public Base
{
public:
    Derived() { cout << "Derived() "; show(); }
    void show() override { cout << "Derived::show "; }
};
int main()
{
    Derived d;
    cout << endl;
    return 0;
}
```
:::ans
```output
Base() Base::show Derived() Derived::show 
```
**Tricky:** while the Base constructor is running, the object is still only a `Base` (the Derived part doesn't exist yet), so a virtual call inside a constructor uses the **Base** version. Virtual dispatch does not reach "down" into derived classes from constructors/destructors.
:::
:::

:::q C9 · Predict the output.
```cpp
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ofstream f("t.txt");
    f << 10 << " " << 20 << " " << 30;
    f.close();
    ifstream in("t.txt");
    int x, sum = 0, n = 0;
    while (in >> x) { sum += x; n++; }
    cout << n << " numbers, sum " << sum << endl;
    return 0;
}
```
:::ans
```output
3 numbers, sum 60
```
:::
:::

:::q C10 · Predict the output.
```cpp
#include <iostream>
using namespace std;
class A { public: int v = 1; };
class B : public A { public: int v = 2; };
int main()
{
    B b;
    A *p = &b;
    cout << b.v << " " << b.A::v << " " << p->v << endl;
    return 0;
}
```
:::ans
```output
2 1 1
```
Data members are **never** virtual: `B::v` hides `A::v`, and access through `A*` uses `A::v`.
:::
:::

## Section D · Find the Errors

:::q D1 · Why does this fail to compile?
```cpp
#include <iostream>
using namespace std;
//@expect: compile-error
class Animal
{
public:
    virtual void sound() = 0;
    virtual void move() = 0;
};
class Fish : public Animal
{
public:
    void move() { cout << "swim"; }
};
int main()
{
    Fish f;
    f.move();
    return 0;
}
```
:::ans
`Fish` overrides only `move()`, not `sound()`, so `Fish` is still **abstract** and cannot be instantiated. Fix: implement `void sound() override { … }` in `Fish`.
:::
:::

:::q D2 · Find the error.
```cpp
#include <iostream>
using namespace std;
//@expect: compile-error
class Base
{
    int x;
public:
    Base(int a) : x(a) { }
};
class Derived : public Base
{
public:
    Derived() { }
};
int main() { Derived d; return 0; }
```
:::ans
`Base` has no default constructor, and `Derived()` does not call `Base(int)` → error. Fix: `Derived() : Base(0) { }`.
:::
:::

:::q D3 · What's wrong with this loop and what does it typically cause?
```cpp
ifstream fin("data.txt");
int x;
while (!fin.eof())
{
    fin >> x;
    cout << x << endl;
}
```
:::ans
`eof()` becomes true only **after** a read attempt fails. After the last number is read, `eof()` may still be false (e.g. if a newline follows), so the body runs once more; `fin >> x` fails and the **last value is printed twice** (or a 0/garbage value is printed). Also it never checks that the file opened. Fix: `while (fin >> x) cout << x << endl;`
:::
:::

:::q D4 · The programmer expected "Circle" but got "Shape". Why?
```cpp
class Shape { public: void name() const { cout << "Shape"; } };
class Circle : public Shape { public: void name() const { cout << "Circle"; } };
void print(const Shape &s) { s.name(); }
// print(Circle());
```
:::ans
`name()` is not declared `virtual` in `Shape`, so the call is statically bound to `Shape::name`. Fix: `virtual void name() const` in the base (and preferably `override` in `Circle`).
:::
:::

## Section E · Programming Questions

:::q E1 · Create an abstract class `Employee` with pure virtual `double salary()` and a virtual `show()`. Derive `FullTime` (monthly pay) and `PartTime` (hours × rate). Store objects in an array of base pointers and print each salary polymorphically. Use a virtual destructor.
:::ans
```cpp
#include <iostream>
#include <string>
using namespace std;

class Employee
{
protected:
    string name;
public:
    Employee(const string &n) : name(n) { }
    virtual double salary() const = 0;              // pure virtual
    virtual void show() const { cout << name << ": " << salary() << endl; }
    virtual ~Employee() { }
};

class FullTime : public Employee
{
    double monthly;
public:
    FullTime(const string &n, double m) : Employee(n), monthly(m) { }
    double salary() const override { return monthly; }
};

class PartTime : public Employee
{
    int hours;
    double rate;
public:
    PartTime(const string &n, int h, double r) : Employee(n), hours(h), rate(r) { }
    double salary() const override { return hours * rate; }
    void show() const override
    {
        cout << name << " (part-time, " << hours << "h): " << salary() << endl;
    }
};

int main()
{
    Employee *staff[3] = { new FullTime("Asha", 50000),
                           new PartTime("Ravi", 40, 300),
                           new FullTime("Meena", 62000) };
    double total = 0;
    for (int i = 0; i < 3; i++)
    {
        staff[i]->show();
        total += staff[i]->salary();
    }
    cout << "Total payroll: " << total << endl;
    for (int i = 0; i < 3; i++) delete staff[i];
    return 0;
}
```
```output
Asha: 50000
Ravi (part-time, 40h): 12000
Meena: 62000
Total payroll: 124000
```
:::
:::

:::q E2 · Write a program to write 3 student records (roll, name, marks) to a text file, then read the file and display only students with marks above 75, formatted in a table.
:::ans
```cpp
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
using namespace std;

int main()
{
    ofstream out("marks.txt");
    if (!out) { cout << "Error opening file" << endl; return 1; }
    out << 1 << " " << "Asha"  << " " << 82.5 << endl;
    out << 2 << " " << "Ravi"  << " " << 68   << endl;
    out << 3 << " " << "Meena" << " " << 91   << endl;
    out.close();

    ifstream in("marks.txt");
    if (!in) { cout << "Error opening file" << endl; return 1; }
    int roll; string name; double marks;
    cout << left << setw(6) << "Roll" << setw(8) << "Name" << "Marks" << endl;
    cout << fixed << setprecision(1);
    while (in >> roll >> name >> marks)
        if (marks > 75)
            cout << left << setw(6) << roll << setw(8) << name << marks << endl;
    in.close();
    return 0;
}
```
```output
Roll  Name    Marks
1     Asha    82.5
3     Meena   91.0
```
:::
:::

:::q E3 · Demonstrate multilevel inheritance: `Account` → `SavingsAccount` (adds interest rate) → `FixedDeposit` (adds years). Pass constructor parameters up the chain and compute maturity amount (simple interest).
:::ans
```cpp
#include <iostream>
using namespace std;

class Account
{
protected:
    double principal;
public:
    Account(double p) : principal(p) { cout << "Account created" << endl; }
};

class SavingsAccount : public Account
{
protected:
    double rate;
public:
    SavingsAccount(double p, double r) : Account(p), rate(r)
    {
        cout << "Savings created" << endl;
    }
};

class FixedDeposit : public SavingsAccount
{
    int years;
public:
    FixedDeposit(double p, double r, int y) : SavingsAccount(p, r), years(y)
    {
        cout << "FD created" << endl;
    }
    double maturity() const { return principal + principal * rate * years / 100; }
};

int main()
{
    FixedDeposit fd(10000, 7, 3);
    cout << "Maturity amount: " << fd.maturity() << endl;
    return 0;
}
```
```output
Account created
Savings created
FD created
Maturity amount: 12100
```
:::
:::

:::q E4 · Write a program that reads a line of text and prints the number of vowels, consonants, digits and spaces, and the text reversed — using the `string` class.
:::ans
```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main()
{
    //@input: OOAD exam on 25th Nov
    string line;
    getline(cin, line);
    int v = 0, c = 0, d = 0, sp = 0;
    for (char ch : line)
    {
        char lo = tolower(ch);
        if (isalpha(ch))
        {
            if (lo == 'a' || lo == 'e' || lo == 'i' || lo == 'o' || lo == 'u') v++;
            else c++;
        }
        else if (isdigit(ch)) d++;
        else if (ch == ' ') sp++;
    }
    string rev(line.rbegin(), line.rend());
    cout << "Vowels=" << v << " Consonants=" << c << " Digits=" << d << " Spaces=" << sp << endl;
    cout << rev << endl;
    return 0;
}
```
Input `OOAD exam on 25th Nov`:
```output
Vowels=7 Consonants=8 Digits=2 Spaces=4
voN ht52 no maxe DAOO
```
(If `rbegin()/rend()` weren't covered in your class, reverse with a loop: `for (int i = line.size() - 1; i >= 0; i--) rev += line[i];`)
:::
:::

## Section F · Long Answer Questions

:::q F1 · What is a virtual function? Explain how run-time polymorphism is achieved, with the vtable mechanism and a program.
:::ans
Structure your answer:
1. **Definition** of virtual function ([Lesson 5.4](05_4_polymorphism_virtual.html)).
2. **Problem without virtual** — base pointer to derived object calls base version (static binding). Small code + output.
3. **Solution with virtual** — same code with `virtual` → derived version (dynamic binding). Code + output (e.g., Shape/Circle/Square array of base pointers).
4. **Mechanism** — vtable per class, vptr per object, call via vptr → vtable → function. Draw the diagram.
5. **Rules** — member, non-static, accessed via pointer/reference, same signature, constructors can't be virtual, virtual destructor recommended, pure virtual → abstract class.
6. **Static vs dynamic binding** table.
:::
:::

:::q F2 · Explain the different types of inheritance with diagrams and syntax. Explain the ambiguity in hybrid inheritance and how it is resolved.
:::ans
Draw the five diagrams (single, multilevel, multiple, hierarchical, hybrid) with syntax for each ([Lesson 5.2](05_2_types_of_inheritance.html)). Then explain the **diamond problem** — two copies of the grandparent's members in the grandchild → ambiguity + wasted memory — and resolve with **virtual base classes** (`class B : virtual public A`, `class C : virtual public A`), showing that A's constructor runs once and `obj.data` is no longer ambiguous. Also mention name-clash ambiguity in multiple inheritance resolved with `obj.Base1::f()`.
:::
:::

:::q F3 · Explain file handling in C++: stream classes, opening modes, and the steps for reading/writing a file, with an example.
:::ans
1. Stream class hierarchy diagram (`ios` → `istream`/`ostream` → `iostream`; `ifstream`, `ofstream`, `fstream`).
2. Two ways to open: constructor `ofstream f("a.txt");` or `f.open("a.txt", mode);`.
3. Modes table (`in`, `out`, `app`, `ate`, `trunc`, `binary`) and combining with `|`.
4. Steps: include `<fstream>` → create object → open → check (`if (!f)`) → read/write → close.
5. Error-state functions: `good`, `eof`, `fail`, `bad`.
6. Program: write records, then read them back with `while (fin >> …)` ([Lesson 6.3](06_3_files.html)) + output.
7. Mention text vs binary (`read`/`write`) and random access (`seekg`, `tellg`).
:::
:::

:::q F4 · Explain the formatting of output in C++ using ios member functions and manipulators, with a program showing at least six of them.
:::ans
Explain flags vs member functions vs manipulators; table of manipulators with sticky/non-sticky behaviour ([Lesson 6.1](06_1_streams_formatting.html)); table of ios functions (`width`, `precision`, `fill`, `setf`, `unsetf`); the meaning of precision with/without `fixed`. Then the demo program from Lesson 6.1 with its output.
:::
:::

:::q F5 · Differentiate: (a) overloading vs overriding, (b) early vs late binding, (c) abstract vs concrete class, (d) `struct` vs `class`, (e) copy constructor vs assignment operator.
:::ans
(a) [Lesson 5.3](05_3_ctor_order_overriding.html) table. (b) [Lesson 5.4](05_4_polymorphism_virtual.html) table. (c) [Lesson 5.5](05_5_abstract_classes.html) table. (d) [Lesson 3.4](03_4_encapsulation.html) table (default access + default inheritance). (e) [Lesson 4.3](04_3_assignment_operator.html) table. Write at least 4 points each, in table form.
:::
:::
