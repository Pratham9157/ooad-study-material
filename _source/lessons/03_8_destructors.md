**A destructor is a special member function that runs automatically when an object is destroyed, to clean up — usually to give back memory or close files the object was using.**

## The Problem: Objects That Leave a Mess

Suppose an object grabs heap memory with `new` in its constructor. When the object goes out of scope, the object itself disappears — **but the heap memory does not**. Nobody calls `delete`, so the memory leaks. Do this in a loop a million times and the program runs out of memory. We need cleanup that happens **automatically** at the end of an object's life.

:::analogy
**Checking out of a hotel.** When your stay ends, the room is cleaned and the key is returned — automatically, as part of leaving. The constructor is check-in (set everything up); the destructor is check-out (clean everything up).
:::

## Understanding Destructors

```cpp
~ClassName() { /* cleanup */ }
```

**Characteristics:**
1. Name = tilde `~` + class name.
2. **No return type and no parameters** → so it **cannot be overloaded** (one destructor per class).
3. Called **automatically**: when a local object goes out of scope, when a global object's program ends, or when `delete` is used on a heap object.
4. Objects are destroyed in the **reverse order** of their creation (last created, first destroyed — like a stack of plates).
5. **Can be `virtual`** (important for inheritance — Lesson 5.5).
6. If you don't write one, the compiler generates an empty one.

## Watching Constructors and Destructors Run

This is one of the most common "predict the output" questions. Read it slowly:

```cpp
#include <iostream>
using namespace std;

class Demo
{
    int id;
public:
    Demo(int i) : id(i) { cout << "Constructing " << id << endl; }
    ~Demo()             { cout << "Destroying " << id << endl; }
};

Demo g(0);                       // global: created BEFORE main starts

int main()
{
    cout << "main starts" << endl;
    Demo a(1);
    {
        Demo b(2);               // lives only inside this block
        cout << "inner block ends" << endl;
    }                            // b is destroyed HERE
    Demo *p = new Demo(3);       // heap object: lives until delete
    Demo c(4);
    delete p;                    // 3 destroyed now
    cout << "main ends" << endl;
    return 0;
}                                // c then a destroyed (reverse order); g after main
```

```output
Constructing 0
main starts
Constructing 1
Constructing 2
inner block ends
Destroying 2
Constructing 3
Constructing 4
Destroying 3
main ends
Destroying 4
Destroying 1
Destroying 0
```

**Rules used:**
- Global objects: constructed before `main`, destroyed after `main` ends.
- Block objects: destroyed at the closing `}` of their block.
- Heap objects: destroyed only when you `delete` them (never automatically!).
- Same scope: reverse order of construction (4 before 1).

## A Destructor That Prevents a Leak

```cpp
#include <iostream>
#include <cstring>
using namespace std;

class Name
{
    char *str;                              // points to heap memory
public:
    Name(const char *s)
    {
        str = new char[strlen(s) + 1];      // grab memory (+1 for '\0')
        strcpy(str, s);
        cout << "allocated " << str << endl;
    }
    ~Name()
    {
        cout << "freeing " << str << endl;
        delete[] str;                       // give it back automatically
    }
};

int main()
{
    Name n("Kavya");
    cout << "using the object..." << endl;
    return 0;                               // destructor runs here
}
```

```output
allocated Kavya
using the object...
freeing Kavya
```

## Constructor vs Destructor

| Constructor | Destructor |
|---|---|
| Initializes the object | Cleans up / releases resources |
| Name: `ClassName` | Name: `~ClassName` |
| Can have parameters | No parameters |
| Can be overloaded | Cannot be overloaded |
| Cannot be virtual | Can be virtual |
| Called when the object is created | Called when the object is destroyed |
| Order: in order of creation | Order: reverse of creation |

:::key
- Destructor `~Name()`: no return type, no parameters, one per class, runs automatically at end of life.
- Destruction order is the reverse of construction.
- Heap objects are destroyed only by `delete`.
- Use destructors to free memory/resources acquired in the constructor.
:::

:::mistakes
- Giving a destructor parameters or trying to overload it.
- Forgetting that objects created with `new` are never destroyed automatically.
- Getting the order wrong: block objects die at their `}`; globals die after `main`.
- Calling `delete` on an object that wasn't created with `new`.
:::

:::exam
- *"What is a destructor? Give its characteristics."*
- *"Differentiate constructor and destructor."* → the table.
- *Predict the output* with global, local, block and `new` objects (like the Demo program).
:::

:::def
A **destructor** is a special member function, named with a tilde followed by the class name, that takes no arguments and has no return type; it is invoked automatically when an object goes out of scope or is deleted, in order to release resources held by the object. Objects are destroyed in the reverse order of their construction.
:::

## Quick Check

:::q Q1 · Predict the output: `class T{int i; public: T(int x):i(x){cout<<"C"<<i;} ~T(){cout<<"D"<<i;}};` with `int main(){ T a(1); T b(2); }`
:::ans
`C1C2D2D1` — destroyed in reverse order.
:::
:::

:::q Q2 · Why can't a destructor be overloaded?
:::ans
Overloading needs different parameter lists, but a destructor takes **no parameters**, so there can be only one.
:::
:::
