**A sequence diagram shows objects as vertical lines and the messages they send each other as arrows, in time order from top to bottom.** It's *the* diagram for designing how objects collaborate.

## The Problem: Who Does What, and When?

The SSD says the system must handle `enterCopy(copyId)`. But *inside* the system: which object receives it? Who finds the copy? Who checks availability? Who creates the `Loan`? In what order? These decisions are the real design work — and a sequence diagram lets you make and show them **before** writing code.

:::analogy
A sequence diagram is like a **comic strip of a phone-call chain**: the receptionist gets a call, calls the manager, who calls the store-room, who calls back… Each person is a column, each call is an arrow, and time flows down the page.
:::

## The Notation, Piece by Piece

| Element | How it's drawn | Meaning |
|---|---|---|
| **Lifeline box** | `:Member` (any member) or `m : Member` (named) | a participant object |
| **Lifeline** | dashed vertical line below the box | the object's existence over time (time flows **down**) |
| **Activation bar** | thin rectangle on the lifeline | the object is busy executing a method |
| **Synchronous message** | solid line, **filled** arrowhead | a normal method call — the caller waits |
| **Asynchronous message** | solid line, **open** arrowhead | caller doesn't wait (signals, threads) |
| **Return** | **dashed** line, open arrowhead | returning control/value (optional) |
| **Self message** | arrow looping back to the same lifeline | an object calls its own method |
| **Create** | dashed arrow to a box drawn **at that height**, labelled «create» | `new` — the object starts existing here |
| **Destroy** | an **X** at the end of the lifeline | the object is deleted |

**Message label:** `returnVar := messageName(arguments)` — e.g. `c := findCopy(copyId)`. A guard: `[condition] message()`.

### Frames for logic (combined fragments)

| Frame | Meaning | Code equivalent |
|---|---|---|
| `alt` | alternatives — only the branch whose guard is true runs (with `[else]`) | if / else |
| `opt` | optional — runs only if its guard is true | if (no else) |
| `loop` | repeats while the guard is true | for / while |
| `par` | parallel fragments | threads |
| `ref` | reference to another sequence diagram | calling a sub-routine |
| `sd` | names the whole diagram | — |

## Example: Designing enterCopy(copyId)

<<SVG:sequence>>

**Reading it top to bottom:**
1. The UI forwards `enterCopy(copyId)` to the **controller** `:IssueBookHandler` (GRASP Controller).
2. The handler asks `:Catalog` to find the copy (the catalog knows all copies — GRASP Expert).
3. It asks the copy `isAvailable()` (the copy knows its own status — Expert).
4. `alt [available]`: it tells the member `m` to `addLoan(c)`; the member **creates** a `:Loan` (GRASP Creator — a member records its loans); the new loan marks the copy issued. `[else]`: an error is returned.
5. Title and due date go back to the UI.

Each arrow **assigns a responsibility** to the receiving class — that's how sequence diagrams drive design (Chapter 13).

## From Sequence Diagram to C++ Code

Rules: a message **to** an object → that object's class **has that method**; the messages inside an activation → the **statements in that method**, in order; `create` → `new` / constructor; `alt`/`opt` → `if`; `loop` → `for`/`while`.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class BookCopy
{
    string copyId, title;
    bool available = true;
public:
    BookCopy(const string &id, const string &t) : copyId(id), title(t) { }
    bool isAvailable() const { return available; }
    void markIssued() { available = false; }
    string getId() const { return copyId; }
    string getTitle() const { return title; }
};

class Loan
{
    BookCopy *copy;
    int dueDay;
public:
    Loan(BookCopy *c, int due) : copy(c), dueDay(due)   // «create» Loan(c, due)
    {
        copy->markIssued();                              // Loan → c : markIssued()
    }
    int getDueDay() const { return dueDay; }
};

class Member
{
    string name;
    vector<Loan*> loans;
public:
    Member(const string &n) : name(n) { }
    int addLoan(BookCopy *c, int today)                  // m : addLoan(c)
    {
        Loan *l = new Loan(c, today + 14);               // Member creates the Loan
        loans.push_back(l);
        return l->getDueDay();
    }
    ~Member() { for (Loan *l : loans) delete l; }
};

class Catalog
{
    vector<BookCopy*> copies;
public:
    void add(BookCopy *c) { copies.push_back(c); }
    BookCopy* findCopy(const string &id) const           // c := findCopy(copyId)
    {
        for (BookCopy *c : copies)
            if (c->getId() == id) return c;
        return nullptr;
    }
};

class IssueBookHandler                                    // the controller
{
    Catalog &catalog;
    Member *current;
    int today;
public:
    IssueBookHandler(Catalog &cat, Member *m, int day) : catalog(cat), current(m), today(day) { }
    string enterCopy(const string &copyId)                // the system operation
    {
        BookCopy *c = catalog.findCopy(copyId);
        if (c != nullptr && c->isAvailable())             // alt [available]
        {
            int due = current->addLoan(c, today);
            return c->getTitle() + " due on day " + to_string(due);
        }
        return "error: copy not available";               // [else]
    }
};

int main()
{
    Catalog cat;
    BookCopy b1("C1", "Clean Code"), b2("C2", "Refactoring");
    cat.add(&b1); cat.add(&b2);
    Member asha("Asha");
    IssueBookHandler handler(cat, &asha, 10);
    cout << handler.enterCopy("C1") << endl;
    cout << handler.enterCopy("C1") << endl;   // already issued
    cout << handler.enterCopy("C9") << endl;   // doesn't exist
    return 0;
}
```

```output
Clean Code due on day 24
error: copy not available
error: copy not available
```

:::key
- Lifelines (boxes + dashed lines), time flows down; activation bars show who's busy.
- Sync = filled arrowhead; async = open arrowhead; return = dashed; create = dashed to a box at that height; destroy = X.
- Frames: `alt`, `opt`, `loop`, `par`, `ref`, `sd`.
- An arrow to B means B must have that method; message order = statement order in code.
:::

:::mistakes
- Drawing returns as solid lines.
- Drawing a created object's box at the top instead of at the create message's height.
- `alt` with one branch (use `opt`), or `opt` for repetition (use `loop`).
- Sending a message to an object that has no such method in the class diagram.
:::

:::exam
- *"Explain sequence diagram notation with an example."*
- *"Draw a sequence diagram for <operation>"* (e.g. withdraw cash, place order, issue book).
- *"Write C++ code from this sequence diagram."*
:::

:::def
A **sequence diagram** is a UML interaction diagram that shows a set of objects (as lifelines) and the messages exchanged between them, arranged in time sequence from top to bottom. It uses activation bars to show when an object is executing and combined fragments (alt, opt, loop, etc.) to show conditional and repeated behaviour.
:::

## Quick Check

:::q Q1 · Which frame for "repeat for each line item"? For "only if the customer is a member, apply a discount"?
:::ans
`loop` for the first; `opt` for the second.
:::
:::

:::q Q2 · In a sequence diagram, `:Register` sends `makePayment(cash)` to `:Sale`. What must exist in the code?
:::ans
Class `Sale` must have a method `makePayment(...)`, and `Register` must hold a reference/pointer to a `Sale` to call it.
:::
:::
