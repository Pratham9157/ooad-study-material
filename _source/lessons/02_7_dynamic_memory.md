**`new` asks for memory while the program is running; `delete` gives it back. This lets you create data whose size or lifetime isn't known in advance.**

This lesson isn't named in your syllabus, but **destructors, copy constructors, the assignment operator and virtual destructors** (Chapters 3–5) only make sense once you know it.

## The Problem: Sizes Fixed in Advance

So far, every variable was created automatically and its size was fixed when you wrote the code: `int marks[60];`. But:
- What if the class has 75 students this year? Or 12?
- What if an object must outlive the function that created it?

We need memory **on demand**, at run time.

## Two Kinds of Memory: Stack and Heap

```text
 STACK (automatic)                         HEAP / free store (dynamic)
 ┌─────────────────────────┐               ┌─────────────────────────────┐
 │ local variables          │               │ memory you request with new │
 │ created/destroyed        │               │ stays until YOU delete it   │
 │ automatically with { }   │               │ size can be decided at      │
 │ size fixed when coding   │               │ run time                    │
 └─────────────────────────┘               └─────────────────────────────┘
```

:::analogy
The **stack** is like a hotel room the event organiser books for you — it's ready when you arrive and cleaned when you leave, automatically. The **heap** is like **renting a storage unit yourself**: you can rent any size, whenever you want, and it's yours until **you** return the key. Forget to return it and you keep paying (a **memory leak**).
:::

## Using new and delete

```cpp
#include <iostream>
using namespace std;

int main()
{
    int *p = new int;           // ask the heap for one int
    *p = 42;
    int *q = new int(7);        // ask for one int and initialize it to 7
    cout << *p << " " << *q << endl;
    delete p;                   // give them back
    delete q;

    int n = 4;                  // size decided at run time
    int *arr = new int[n];      // an array on the heap
    for (int i = 0; i < n; i++) arr[i] = i * 10;
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
    delete[] arr;               // arrays need delete[]
    arr = nullptr;              // good habit: no dangling pointer
    return 0;
}
```

```output
42 7
0 10 20 30 
```

**The rule:** every `new` needs a matching `delete`; every `new[]` needs a matching `delete[]`.

## Three Classic Bugs

| Bug | What happens | Example |
|---|---|---|
| **Memory leak** | Memory is never given back | `int *p = new int; p = nullptr;` — the int is lost forever |
| **Dangling pointer** | A pointer still points to memory that was already freed | `delete p; cout << *p;` |
| **Double delete** | The same memory is freed twice → usually a crash | `delete p; delete p;` |

Remember **double delete** — it's exactly what goes wrong with "shallow copy" in Lesson 4.2.

## new/delete vs malloc/free

| `new` / `delete` (C++) | `malloc` / `free` (C) |
|---|---|
| Operators | Library functions |
| Return the correct pointer type | Return `void*` |
| **Call constructors and destructors** | Don't call them |
| Throw an exception on failure | Return `NULL` on failure |

:::key
- `new` allocates on the heap at run time; `delete` releases it.
- `new[]` ↔ `delete[]`.
- Leaks, dangling pointers and double deletes are the three classic dynamic-memory bugs.
- `new`/`delete` call constructors/destructors — that's why C++ uses them instead of `malloc`/`free`.
:::

:::mistakes
- Using `delete` on memory from `new[]` (must be `delete[]`).
- Forgetting `delete` → leak.
- Using a pointer after `delete`.
- Deleting something that wasn't created with `new`.
:::

:::exam
- *"Explain `new` and `delete` with an example."*
- *"Differentiate `new`/`delete` and `malloc`/`free`."*
- *"What is a memory leak? What is a dangling pointer?"*
:::

:::def
**Dynamic memory allocation** is allocating memory at run time from the heap (free store) using the `new` operator, which returns the address of the allocated memory; the memory remains allocated until it is released explicitly using `delete` (or `delete[]` for arrays).
:::

## Quick Check

:::q Q1 · What is wrong? `int *a = new int[10]; … delete a;`
:::ans
Memory from `new[]` must be released with `delete[] a;` — using plain `delete` is undefined behaviour.
:::
:::

:::q Q2 · Why is this a memory leak? `int *p = new int(5); p = new int(6);`
:::ans
The first int (5) is still allocated, but no pointer refers to it anymore, so it can never be deleted.
:::
:::
