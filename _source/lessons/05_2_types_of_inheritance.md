**Classes can be arranged in different inheritance shapes: a single chain, a family tree with many children, a child with several parents, or a mix. Each shape has a name — and one shape creates a famous problem.**

## The Five Shapes

```text
 Single           Multilevel        Multiple             Hierarchical          Hybrid (here: the "diamond")
   A                 A              A       B                 A                      A
   │                 │               \     /               /  |  \                 /   \
   B                 B                  C                 B   C   D               B     C
                     │                                                             \   /
                     C                                                               D
```

| Type | Meaning | Real-world example |
|---|---|---|
| **Single** | one base → one derived | `Car : Vehicle` |
| **Multilevel** | a chain: C derives from B, which derives from A | `Person → Student → GraduateStudent` |
| **Multiple** | one class with **two or more** bases | `SmartPhone : Phone, Camera` |
| **Hierarchical** | **many** classes from **one** base | `Circle, Square, Triangle : Shape` |
| **Hybrid** | a combination of the above | multiple + hierarchical → diamond |

:::analogy
Family trees. **Single**: a parent and a child. **Multilevel**: grandparent → parent → child (the child inherits from both, through the parent). **Hierarchical**: one parent, several siblings. **Multiple**: a child who inherits traits from two different parents. **Hybrid**: any mix of these.
:::

## Multilevel Inheritance

```cpp
#include <iostream>
using namespace std;

class Person   { protected: char name[20] = "Arjun"; };
class Student  : public Person  { protected: int roll = 21; };
class Graduate : public Student
{
public:
    void show() { cout << name << " " << roll << " graduated" << endl; }  // members from 2 levels up
};

int main()
{
    Graduate g;
    g.show();
    return 0;
}
```

```output
Arjun 21 graduated
```

## Multiple Inheritance

```cpp
#include <iostream>
using namespace std;

class Phone  { public: void call()  { cout << "Calling..." << endl; } };
class Camera { public: void click() { cout << "Photo clicked" << endl; } };

class SmartPhone : public Phone, public Camera      // two parents
{
public:
    void browse() { cout << "Browsing" << endl; }
};

int main()
{
    SmartPhone s;
    s.call(); s.click(); s.browse();
    return 0;
}
```

```output
Calling...
Photo clicked
Browsing
```

## Hierarchical Inheritance

```cpp
#include <iostream>
using namespace std;

class Shape
{
protected:
    double dim;
public:
    void setDim(double d) { dim = d; }
};
class Square : public Shape { public: double area() { return dim * dim; } };
class Circle : public Shape { public: double area() { return 3.14 * dim * dim; } };

int main()
{
    Square s; s.setDim(4);
    Circle c; c.setDim(1);
    cout << s.area() << " " << c.area() << endl;
    return 0;
}
```

```output
16 3.14
```

## Ambiguity in Multiple Inheritance

If both parents have a member with the **same name**, the child can't tell which one you mean:

```cpp
#include <iostream>
using namespace std;

class Printer { public: void start() { cout << "Printer start" << endl; } };
class Scanner { public: void start() { cout << "Scanner start" << endl; } };
class AllInOne : public Printer, public Scanner { };

int main()
{
    AllInOne m;
    // m.start();          // ERROR: ambiguous — which start()?
    m.Printer::start();    // fix: say which parent with ::
    m.Scanner::start();
    return 0;
}
```

```output
Printer start
Scanner start
```

## The Diamond Problem and Virtual Base Classes

In the diamond shape, `D` inherits from `B` and `C`, which **both** inherit from `A`. Without special care, `D` ends up containing **two separate copies** of `A`:

```text
        A (int data)                    Without "virtual":        With "virtual":
       / \                              D = [ B::A::data ]        D = [ one shared A ]
      B   C                                 [ C::A::data ]
       \ /                              obj.data → AMBIGUOUS       obj.data → fine
        D
```

**Solution:** make `A` a **virtual base class** by inheriting with the keyword `virtual`. Then `B` and `C` share **one** `A`.

```cpp
#include <iostream>
using namespace std;

class A
{
public:
    int data;
    A() { cout << "A constructed" << endl; }
};
class B : virtual public A { };      // virtual base
class C : virtual public A { };      // virtual base
class D : public B, public C { };

int main()
{
    D obj;                           // A is constructed only ONCE
    obj.data = 10;                   // no ambiguity
    cout << obj.B::data << " " << obj.C::data << endl;   // same variable
    return 0;
}
```

```output
A constructed
10 10
```

Without `virtual`, "A constructed" would print **twice** and `obj.data` would be a compile error.

:::key
- Five types: single, multilevel, multiple, hierarchical, hybrid.
- Name clash in multiple inheritance → resolve with `obj.Base::member()`.
- Diamond problem: two copies of the common grandparent → fix with **virtual base classes** (`class B : virtual public A`).
:::

:::mistakes
- Confusing a **virtual base class** (fixes the diamond) with a **virtual function** (run-time polymorphism, Lesson 5.4).
- Mixing up multilevel (a chain) and multiple (two parents).
- Drawing inheritance arrows from parent to child — in UML the arrow points **to the parent** (Lesson 8.3).
:::

:::exam
- *"Explain the types of inheritance with diagrams and syntax."* (Very common — draw all five.)
- *"What is the diamond problem? How is it solved?"* → explanation + virtual base class program.
:::

:::def
A **virtual base class** is a base class declared with the keyword `virtual` in the inheritance list (`class B : virtual public A`), which ensures that only one shared copy of its members is inherited by a class that derives from it through multiple paths, thereby resolving the ambiguity of the diamond problem.
:::

## Quick Check

:::q Q1 · `class X : public A, public B` — which type of inheritance? `class B : public A; class C : public B` — which type?
:::ans
The first is **multiple**; the second is **multilevel**.
:::
:::

:::q Q2 · In the diamond without `virtual`, how many times is A's constructor called when creating a D?
:::ans
**Twice** — once through B and once through C.
:::
:::
