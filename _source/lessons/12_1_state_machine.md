**A state machine diagram shows the life-cycle of one object: the states it can be in, the events it reacts to, and how each event moves it from one state to another.**

## The Problem: Same Request, Different Answers

Ask a library book copy to be **issued**:
- if it's on the shelf → it gets issued,
- if it's reserved for someone else → refuse (unless it's that person),
- if it's already on loan → refuse,
- if it's lost → refuse.

The same event (**issue**) has **different effects depending on the object's current state**. Code full of `if (status == …)` checks becomes confusing quickly. A state machine diagram lays out every state and every legal transition clearly.

:::analogy
A **traffic light** is a classic state machine: states *Red*, *Green*, *Yellow*; the event "timer expires" moves Red → Green → Yellow → Red. Pressing the pedestrian button means something different in each state. Another example: a **phone** — *Idle*, *Ringing*, *In Call* — "press the green button" means "answer" when Ringing, but "dial" when Idle.
:::

## Key Terms

- **State** — a condition of the object at a moment in time, between events (*Available*, *OnLoan*).
- **Event** — something significant that happens (*issue*, *return*, *due date passes*).
- **Transition** — the arrow from one state to another, taken when its event occurs (and its guard is true).

## The Notation

| Element | Symbol |
|---|---|
| Initial state (start) | filled black circle ● |
| State | rounded rectangle with the state name |
| Final state (end) | bull's-eye ◉ |
| Transition | arrow labelled **`event [guard] / action`** (each part optional) |
| Internal activities | inside a state: `entry / …`, `exit / …`, `do / …` |
| Self-transition | an arrow leaving and re-entering the same state |
| Composite state | a state containing nested sub-states |
| History | circled **H** — return to the last active sub-state |

**Transition label:** `event [guard] / action`
- **event** — what triggers it (`return`),
- **guard** — a condition that must be true (`[late]`),
- **action** — something quick done during the transition (`/ chargeFine`).
- Special events: `after(3 days)` (a time event), `when(today > dueDate)` (a change event).

## Example: The Life of a BookCopy

<<SVG:statemachine>>

Read it like a story: a copy is catalogued → *Available*. It can be *Reserved* (and released after 3 days), *issued* → *OnLoan* (entry: set the due date). If the due date passes → *Overdue* (entry: send a reminder). Returning an overdue copy charges a fine. Reporting it lost moves to *Lost*, and finally it's written off.

## From State Machine to C++

A common implementation: an `enum` for states, one method per event, and a `switch`/`if` on the current state.

```cpp
#include <iostream>
using namespace std;

enum class CopyState { Available, Reserved, OnLoan, Overdue, Lost };

class BookCopy
{
    CopyState state = CopyState::Available;
    double fines = 0;
public:
    void reserve()
    {
        if (state == CopyState::Available) state = CopyState::Reserved;
        else cout << "  [ignored] reserve" << endl;           // not valid in this state
    }
    void issue()
    {
        if (state == CopyState::Available || state == CopyState::Reserved) state = CopyState::OnLoan;
        else cout << "  [ignored] issue" << endl;
    }
    void dueDatePassed()                                    // change event: when(today > dueDate)
    {
        if (state == CopyState::OnLoan) state = CopyState::Overdue;
    }
    void giveBack()                                         // event: return
    {
        if (state == CopyState::OnLoan)       state = CopyState::Available;
        else if (state == CopyState::Overdue) { fines += 50; state = CopyState::Available; }  // / chargeFine
        else cout << "  [ignored] return" << endl;
    }
    void print() const
    {
        const char *names[] = {"Available", "Reserved", "OnLoan", "Overdue", "Lost"};
        cout << names[static_cast<int>(state)] << " (fines: " << fines << ")" << endl;
    }
};

int main()
{
    BookCopy c;
    c.print();
    c.issue();         c.print();
    c.dueDatePassed(); c.print();
    c.giveBack();      c.print();
    c.giveBack();                      // not valid when Available
    c.reserve();       c.print();
    return 0;
}
```

```output
Available (fines: 0)
OnLoan (fines: 0)
Overdue (fines: 0)
Available (fines: 50)
  [ignored] return
Reserved (fines: 50)
```

The same `giveBack()` event has three different effects depending on the state — exactly what the diagram shows.

## When to Use State Machine Diagrams

Use them for objects whose behaviour **depends on their state** — objects that react differently to the same event:
- **Reactive/event-driven devices** — ATM, vending machine, traffic light, elevator, phone.
- **Domain objects with a life-cycle** — Order (New → Paid → Shipped → Delivered), BookCopy, Loan application, Ticket.
- **Legal order of operations / protocols** — e.g. `endIssue()` is only legal after `startIssue()`; network connection states.
- **UI navigation** — which screen follows which.

**Don't** draw one for every class — most objects (e.g. a `Book` description) behave the same regardless of state.

:::key
- One object's life-cycle: states, events, transitions `event [guard] / action`.
- ● initial, ◉ final, rounded boxes = states, `entry/exit/do` activities inside states.
- Use for state-dependent, reactive objects, life-cycles and protocols.
- Code: enum of states + methods per event checking the current state.
:::

:::mistakes
- Naming states as actions ("Calculating fine") instead of conditions ("Overdue").
- Forgetting the initial state.
- Writing labels in the wrong order — it's `event [guard] / action`.
- Confusing it with an activity diagram: state machine = **one object's states**; activity = **flow of actions**.
:::

:::exam
- *"Explain the state machine diagram with notation. Draw one for an ATM / order / traffic light / phone."*
- *"When should state diagrams be used?"*
:::

:::def
A **state machine diagram** shows the life-cycle of an object: the states it can be in, the events it responds to, and the transitions between states triggered by events, optionally with guard conditions and actions (`event [guard] / action`). It is used to model objects with state-dependent behaviour.
:::

## Quick Check

:::q Q1 · Label this transition: event "withdraw", only if balance ≥ amount, action "dispense cash".
:::ans
`withdraw [balance >= amount] / dispenseCash`
:::
:::

:::q Q2 · Give two objects that deserve a state machine diagram and one that doesn't.
:::ans
Deserve: an **ATM session**, an **Order** (also traffic light, elevator…). Doesn't: a **ProductDescription** / **Book** description — its behaviour doesn't depend on state.
:::
:::
