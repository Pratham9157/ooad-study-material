**A class diagram shows the classes in a system, what each one knows (attributes) and does (operations), and how they're related. It is the most widely used UML diagram.**

## The Problem: Code Is a Bad Map

To understand how a 50-class system fits together by reading C++ files, you'd have to open every file and keep the relationships in your head. A class diagram is a **map**: one picture showing all the classes and their connections — useful for planning before coding and for understanding existing code.

:::analogy
A class diagram is like a **floor plan** of a building. It doesn't show people walking around (that's behaviour — sequence diagrams), but it shows every room (class), what's in it (attributes/operations) and which rooms connect to which (relationships).
:::

## The Class Box

```text
 ┌────────────────────────────────────┐
 │             BookCopy               │  ← 1. name (italic = abstract class)
 ├────────────────────────────────────┤
 │ - copyId : string                  │  ← 2. attributes
 │ - available : bool = true          │
 │ - totalCopies : int    (underlined = static)
 ├────────────────────────────────────┤
 │ + isAvailable() : bool             │  ← 3. operations
 │ + markIssued() : void              │
 │ + getTotal() : int     (underlined = static)
 └────────────────────────────────────┘
```

**Attribute:** `visibility name : type = default` — e.g. `- balance : double = 0`
**Operation:** `visibility name(param : Type) : ReturnType` — e.g. `+ withdraw(amt : double) : bool`

| Symbol | Visibility | C++ |
|---|---|---|
| `+` | public | `public:` |
| `-` | private | `private:` |
| `#` | protected | `protected:` |
| `~` | package | (no direct equivalent) |

Other notation: **underlined** = static; *italic* name or `{abstract}` = abstract; `«interface»` = interface; `/name` = derived attribute (computed from others, e.g. `/age`). Only the name compartment is required.

## From Class Box to C++ (and Back)

```cpp
#include <iostream>
#include <string>
using namespace std;

class BookCopy
{
private:
    string copyId;                         // - copyId : string
    bool available = true;                 // - available : bool = true
    static int totalCopies;                // - totalCopies : int   (underlined)
public:
    BookCopy(const string &id) : copyId(id) { totalCopies++; }
    bool isAvailable() const { return available; }   // + isAvailable() : bool
    void markIssued() { available = false; }         // + markIssued() : void
    static int getTotal() { return totalCopies; }    // + getTotal() : int (underlined)
};
int BookCopy::totalCopies = 0;

int main()
{
    BookCopy c1("C-101"), c2("C-102");
    c1.markIssued();
    cout << c1.isAvailable() << " " << c2.isAvailable() << " " << BookCopy::getTotal() << endl;
    return 0;
}
```

```output
0 1 2
```

## Relationships on a Class Diagram

All six relationships from Chapter 8 appear on class diagrams: association (with multiplicity), aggregation ◇, composition ◆, dependency (dashed arrow), generalization (solid ▷), realization (dashed ▷). Revise the [cheat sheet in Lesson 8.3](08_3_dependency_generalization_realization.html).

## Two Uses of the Same Notation

| Domain model (conceptual perspective) | Design class diagram, DCD (software perspective) |
|---|---|
| Real-world **concepts** | **Software** classes (may include controllers, factories…) |
| Attributes, usually without types | Attributes **with types and visibility** |
| **No operations** | **Operations** with parameters and return types |
| No navigability arrows | Navigability arrows, dependencies |
| Built early (analysis) | Built during design, alongside interaction diagrams |

The next three lessons are about the **domain model**. DCDs return in Lesson 14.8 (mapping design to code).

## Object Diagrams (a Snapshot)

An **object diagram** shows **objects** (instances) and their **links** at one moment. Names are written `objectName : ClassName` (underlined in real UML) and attributes show **values**.

```text
  ┌──────────────────────┐   borrows   ┌─────────────────────────┐
  │ asha : Member        │─────────────│ c101 : BookCopy         │
  │ name = "Asha"        │             │ copyId = "C-101"        │
  │ memberId = 7         │             │ available = false       │
  └──────────────────────┘             └─────────────────────────┘
```

Useful to illustrate a confusing class diagram with a concrete example.

## When to Use Class Diagrams

- **Domain modelling** — to understand and communicate the problem's concepts (the domain model).
- **Design** — DCDs showing the software classes, drawn **in parallel with** interaction diagrams.
- **Documentation / reverse engineering** — to understand existing code.
- Tip (Fowler): don't try to use every notation, and don't diagram every class — focus on the important parts.

:::key
- Class box: name / attributes / operations; visibility `+ - # ~`; static underlined; abstract italic; derived `/`.
- Same notation for domain models (conceptual, no operations) and DCDs (software, with operations and types).
- Object diagram = snapshot of objects and links with values.
:::

:::mistakes
- Putting operations in a **domain model**.
- Forgetting visibility symbols or types in a **design** class diagram.
- Writing the return type before the name (C++ style) — UML puts it **after**: `getTotal() : int`.
:::

:::exam
- *"Explain the class diagram notation with an example."*
- *"Convert this class diagram to C++"* / *"Draw the class diagram for this code."*
- *"When should class diagrams be used?"*
:::

:::def
A **class diagram** is a UML structure diagram that shows the classes of a system with their attributes and operations, and the relationships among them (association, aggregation, composition, dependency, generalization, realization). An **object diagram** shows a snapshot of objects and their links at a particular moment.
:::

## Quick Check

:::q Q1 · Write the UML for a private attribute `balance` of type double with default 0, and a public operation `deposit` taking `amt: double` and returning nothing.
:::ans
`- balance : double = 0` and `+ deposit(amt : double) : void`.
:::
:::

:::q Q2 · How is a static member shown in a class diagram? An abstract class?
:::ans
Static: **underlined**. Abstract class: name in *italics* (or `{abstract}`).
:::
:::
