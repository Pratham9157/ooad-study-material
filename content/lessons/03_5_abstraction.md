**Abstraction means focusing on *what* something does and ignoring *how* it does it. You show the essential features and hide the details.**

Your syllabus says "review of abstraction" — because you've already met one kind (procedural abstraction, Lesson 2.1). This lesson reviews it and adds the more powerful kind: **data abstraction**.

## The Problem: Too Much Detail Overwhelms Us

If you had to understand the engine, gearbox and electronics to drive a car, nobody could drive. Software is the same: if every programmer using a `Stack` had to know whether it's built on an array or a linked list, and how indices are updated, programs would be fragile and hard to write. We need a way to use things through a **simple interface**.

:::analogy
**Driving a car.** The car offers a simple interface — steering, accelerator, brake, gear lever. You know *what* each does. *How* the engine burns fuel is hidden. Manufacturers can switch from petrol to electric engines, and you still drive the same way. That's abstraction.
:::

## Two Kinds of Abstraction

**1. Procedural abstraction** — hiding *how a task is done* inside a function. You call `sqrt(16)` and get 4 without knowing the algorithm. (Lesson 2.1.)

**2. Data abstraction** — hiding *how data is stored and managed* inside a class, and exposing only **operations**. The user of the class works with the operations; the representation is a secret.

A type defined purely by its operations is called an **Abstract Data Type (ADT)**. Example: a **Stack** is "a pile where you can `push` on top, `pop` from the top, and check `isEmpty`". That definition says nothing about arrays or pointers.

## Data Abstraction in Code

```cpp
#include <iostream>
using namespace std;

class Stack                              // users see only push / pop / isEmpty
{
private:
    int items[100];                      // HIDDEN representation: an array + an index
    int top = -1;
public:
    void push(int x) { if (top < 99) items[++top] = x; }
    int  pop()       { return items[top--]; }
    bool isEmpty()   { return top == -1; }
};

int main()
{
    Stack s;                             // main doesn't know (or care) that there's an array
    s.push(10); s.push(20); s.push(30);
    while (!s.isEmpty()) cout << s.pop() << " ";
    cout << endl;
    return 0;
}
```

```output
30 20 10 
```

Tomorrow you could rewrite `Stack` to use a linked list. As long as `push`, `pop` and `isEmpty` behave the same, `main` doesn't change. **That's the payoff of abstraction: you can change the inside without breaking the outside.**

## How to Achieve Abstraction in C++

- **Classes with a public interface and private data** (as above).
- **Functions** (procedural abstraction).
- **Abstract classes and interfaces** (pure virtual functions — Lesson 5.5) — they define *what* operations exist without saying *how*.
- **Header files** — users see declarations; implementations live elsewhere.

## Abstraction vs Encapsulation (A Favourite Exam Question)

They work together but are not the same:

| Abstraction | Encapsulation |
|---|---|
| A **design-level** idea: decide *what* to show | An **implementation-level** mechanism: *how* to hide and bundle |
| Focuses on the **outside view** (the interface) | Focuses on the **inside** (wrapping data + code, restricting access) |
| Solves the problem at the **design** stage | Solves it at the **implementation** stage |
| Achieved with abstract classes, interfaces, ADTs | Achieved with classes + `private`/`public` |
| "The car shows only a steering wheel and pedals" | "The engine is sealed under the bonnet" |

One-line memory hook: **abstraction hides complexity; encapsulation hides data.** Encapsulation is one of the main *tools* used to achieve abstraction.

:::key
- Abstraction = essential features only; hide *how*.
- Procedural abstraction hides *how a task is done*; data abstraction hides *how data is represented*.
- An ADT is defined by its operations, not its representation.
- Abstraction (design, outside view) ≠ encapsulation (implementation, inside protection), but they cooperate.
:::

:::mistakes
- Saying abstraction and encapsulation are identical.
- Thinking abstraction means "abstract class" only — abstract classes are just one way to achieve it.
- Exposing internal details (like the array or `top` index) as public — breaks abstraction.
:::

:::exam
- *"What is abstraction? Explain data abstraction with an example."*
- *"Differentiate abstraction and encapsulation."* → the table + car example.
- *"What is an abstract data type?"*
:::

:::def
**Abstraction** is the process of representing the essential features of an entity without including its background details or implementation. **Data abstraction** separates the interface of a type (its operations) from its implementation (its data representation); a type defined in this way is an **abstract data type (ADT)**.
:::

## Quick Check

:::q Q1 · A `Queue` class offers `enqueue`, `dequeue`, `isEmpty` and hides an array inside. Which concept does hiding the array illustrate, and which concept does offering only those three operations illustrate?
:::ans
Hiding the array (private data) = **encapsulation/data hiding**; offering only the essential operations = **(data) abstraction**.
:::
:::

:::q Q2 · Why can a class's internal representation be changed without affecting the programs that use it?
:::ans
Because of abstraction: users depend only on the public interface (operations), not on the private representation, so the inside can change as long as the interface behaves the same.
:::
:::
