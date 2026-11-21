**The Singleton pattern (creational) guarantees that a class has exactly one object, and gives everyone a single global way to reach it.**

## 1. The Problem: "There Must Be Only One"

The library has one set of rules — fine per day, loan limit. If different parts of the program each create their own `LibraryConfig` object, they might load different values, or one part changes a setting the others never see. Some things should exist **exactly once**: the configuration, the services factory, a logger.

```text
 Without Singleton:   IssueHandler → new LibraryConfig()   (fine = 5)
                      ReturnHandler → new LibraryConfig()  (fine = 5 … until someone edits this copy)
                      → two configs that can drift apart
```

## 2. Understanding Singleton

> **GoF intent:** "Ensure a class only has one instance, and provide a global point of access to it."

How:
1. Make the **constructor private** → nobody outside can write `new LibraryConfig()`.
2. Provide a **static** method `getInstance()` that creates the object the first time and returns **the same one** every time after.
3. Forbid copying (delete the copy constructor and assignment operator).

:::analogy
A country has **one president** at a time. You can't just appoint another one; everyone who needs "the president" reaches the same person through the official office. `getInstance()` is that official office.
:::

## 3. Implementation

```cpp
#include <iostream>
using namespace std;

class LibraryConfig
{
    int finePerDay = 5;
    LibraryConfig() { cout << "Config created once" << endl; }   // 1. private constructor
public:
    LibraryConfig(const LibraryConfig &) = delete;               // 3. no copies
    LibraryConfig& operator=(const LibraryConfig &) = delete;
    static LibraryConfig& getInstance()                          // 2. global access point
    {
        static LibraryConfig instance;                           // created on first call only
        return instance;
    }
    int getFinePerDay() const { return finePerDay; }
};

int main()
{
    LibraryConfig &a = LibraryConfig::getInstance();
    LibraryConfig &b = LibraryConfig::getInstance();
    cout << a.getFinePerDay() << " " << (&a == &b) << endl;      // same object → 1
    // LibraryConfig c;                                          // ERROR: constructor is private
    return 0;
}
```

```output
Config created once
5 1
```

The constructor message prints **once**, and both references point to the **same** object.

## 4. What We Gained (and the Costs)

**Gains:** exactly one instance; controlled, lazy creation (made only when first needed); a well-known access point.

**Costs (be honest in long answers):** it's essentially a global variable — hidden dependencies, harder unit testing, and care needed with multiple threads. Use it only for things that truly must be unique.

## When to Use It

- Exactly one object is needed system-wide: configuration, a **services factory** (Larman uses `ServicesFactory.getInstance()`), a logger, a connection pool.

:::key
- Singleton: one instance + global access via a static `getInstance()`.
- Private constructor, static method, copying disabled.
- Commonly combined with factories; use sparingly.
:::

:::mistakes
- Leaving the constructor public (then anyone can create more instances).
- Forgetting to disable copying (a copy is a second instance).
- Using Singleton for everything "for convenience".
:::

:::exam
- Sometimes asked as *"Explain the Singleton pattern"* or as part of *"applying GoF patterns"* (factory accessed via Singleton).
:::

:::def
**Singleton** (creational): "Ensure a class only has one instance, and provide a global point of access to it." It is implemented with a private constructor and a static method that creates the single instance on first use and returns it thereafter.
:::

## Quick Check

:::q Q1 · Why must the Singleton's constructor be private?
:::ans
So no code outside the class can create additional instances; the only way to get the object is `getInstance()`.
:::
:::
