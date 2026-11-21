**When a derived object is created, the base part is built first and the derived part second; destruction happens in reverse. And a derived class can *override* (redefine) a base function to behave its own way.**

## Part 1 — Constructors and Destructors in Inheritance

### Why order matters

A derived object contains a base-class part *inside* it. The derived constructor may want to use base members — so the base part must already be properly built.

:::analogy
**Building a house.** First the foundation (base class), then the walls on top (derived class). When demolishing, you take the walls down first, then the foundation. Construction goes bottom-up; destruction goes top-down.
:::

**Rules:**
1. Constructors: **base first, then derived**. Multilevel: from the top-most ancestor down.
2. Destructors: **reverse** — derived first, then base.
3. Multiple inheritance: base constructors run in the order the bases are **listed in the class declaration** (not the order you write in the initializer list).
4. If the base needs arguments, the derived constructor passes them through its **initializer list**: `Derived(int a, int b) : Base(a), y(b) { }`.

```cpp
#include <iostream>
using namespace std;

class A { public: A() { cout << "A "; }  ~A() { cout << "~A "; } };
class B { public: B() { cout << "B "; }  ~B() { cout << "~B "; } };
class C : public B, public A           // DECLARED order: B, then A
{
public:
    C() : A(), B() { cout << "C "; }   // list order doesn't matter
    ~C() { cout << "~C "; }
};

int main()
{
    {
        C obj;
        cout << "| ";
    }
    cout << endl;
    return 0;
}
```

```output
B A C | ~C ~A ~B 
```

### Passing arguments to the base constructor

```cpp
#include <iostream>
using namespace std;

class Employee
{
protected:
    int id;
    double salary;
public:
    Employee(int i, double s) : id(i), salary(s)
    {
        cout << "Employee(" << id << ") constructed" << endl;
    }
};

class Manager : public Employee
{
    double bonus;
public:
    Manager(int i, double s, double b) : Employee(i, s), bonus(b)   // hand i, s to the base
    {
        cout << "Manager constructed" << endl;
    }
    double totalPay() { return salary + bonus; }
};

int main()
{
    Manager m(7, 50000, 12000);
    cout << "Total pay: " << m.totalPay() << endl;
    return 0;
}
```

```output
Employee(7) constructed
Manager constructed
Total pay: 62000
```

## Part 2 — Function Overriding

### The problem

A base class `Animal` has `sound()` printing "Some sound". A `Dog` *is an* animal, but it should bark. Inheriting the generic version isn't good enough — the child needs its **own version** of the same function.

### The idea

**Function overriding** = the derived class provides a function with the **same name and same parameters** as a base-class function. Calls on a derived object use the derived version. The base version is still reachable with `Base::function()`.

```cpp
#include <iostream>
using namespace std;

class Animal
{
public:
    void sound() { cout << "Some sound" << endl; }
    void eat()   { cout << "Animal eats" << endl; }
};

class Dog : public Animal
{
public:
    void sound()                    // overrides Animal::sound
    {
        Animal::sound();            // optionally reuse the parent's version
        cout << "Bark" << endl;
    }
};

int main()
{
    Dog d;
    d.sound();          // Dog's version
    d.eat();            // inherited unchanged
    d.Animal::sound();  // explicitly call the parent's version
    return 0;
}
```

```output
Some sound
Bark
Animal eats
Some sound
```

### Name hiding (a subtle trap)

If the derived class declares a function with the same **name**, it hides **all** base functions of that name — even ones with different parameters.

```cpp
#include <iostream>
using namespace std;
//@expect: compile-error

class Base    { public: void show(int x) { cout << x; } };
class Derived : public Base { public: void show() { cout << "D"; } };

int main()
{
    Derived d;
    d.show();      // OK
    d.show(5);     // ERROR: Base::show(int) is hidden by Derived::show()
    return 0;      // fix: put  using Base::show;  inside Derived
}
```

## Overloading vs Overriding

| Function overloading | Function overriding |
|---|---|
| Same name, **different** parameters | Same name, **same** parameters |
| Usually in the **same** class | In **base and derived** classes |
| No inheritance needed | Requires inheritance |
| Resolved at **compile time** | With `virtual`, resolved at **run time** (next lesson) |
| Return type may differ | Return type must match |

:::key
- Construction: base → derived (multiple bases in declaration order). Destruction: reverse.
- Pass base-constructor arguments via the derived initializer list.
- Overriding = same signature in the derived class; `Base::f()` still reaches the parent's version.
- A derived function name hides all base overloads with that name.
:::

:::mistakes
- Thinking the derived constructor runs first.
- Forgetting to call a parameterized base constructor when the base has no default constructor → error.
- Writing `Employee(i, s);` inside the constructor **body** — that creates a temporary, it doesn't initialize the base.
- Using initializer-list order instead of declaration order for multiple inheritance.
- Confusing overloading and overriding.
:::

:::exam
- *Output questions* on constructor/destructor order in multilevel and multiple inheritance (very common).
- *"How are arguments passed to base class constructors?"*
- *"Differentiate function overloading and overriding."*
:::

:::def
In inheritance, **base class constructors are executed before derived class constructors**, and destructors are executed in the reverse order. **Function overriding** is the redefinition, in a derived class, of a base class member function with the same name and signature, so that the derived version is used for derived objects.
:::

## Quick Check

:::q Q1 · Predict: `class A{public:A(){cout<<"A";}~A(){cout<<"~A";}}; class B:public A{public:B(){cout<<"B";}~B(){cout<<"~B";}};` with `int main(){ B b; }`
:::ans
`AB~B~A`
:::
:::

:::q Q2 · `Base` has only `Base(int)`. Why does `class D : public Base { public: D() { } };` fail?
:::ans
`D()` implicitly tries to call `Base()`, which doesn't exist. Fix: `D() : Base(0) { }`.
:::
:::
