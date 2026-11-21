**Aggregation and composition are special associations that mean "whole–part". In aggregation the parts can live without the whole; in composition the parts belong to exactly one whole and live and die with it.**

## The Problem: Not All Connections Are Equal

A **Team** has **Players**. A **House** has **Rooms**. Both sound like "has-a" — but they're very different:
- If a team is disbanded, the players still exist and can join other teams.
- If a house is demolished, its rooms are demolished too. A room can't belong to two houses.

A plain association line doesn't capture this difference, yet it matters a lot for code: **who creates the parts? who deletes them?** That's why UML has two special forms of whole–part relationship.

:::analogy
**Aggregation** = a **music band** and its **musicians**: the band groups them, but if the band breaks up, each musician continues their career (and might be in two bands at once). **Composition** = a **human body** and its **heart**: the heart belongs to exactly one body and doesn't exist independently of it.
:::

## Aggregation (weak "has-a")

- A **whole–part** relationship where the **parts can exist independently** of the whole.
- Parts may be **shared** by several wholes.
- The whole does **not** create or destroy the parts.
- UML: **hollow diamond ◇** at the **whole's** end.

```text
   ┌──────────┐ 0..1             *  ┌──────────┐
   │   Team   │◇────────────────────│  Player  │      Team has Players; players outlive the team
   └──────────┘                     └──────────┘
```

## Composition (strong "is made of")

- A **strong whole–part** relationship:
  1. a part belongs to **only one** whole at a time,
  2. the part **cannot exist without** a whole,
  3. the whole is **responsible for creating and destroying** its parts — when the whole dies, so do the parts.
- UML: **filled diamond ◆** at the **whole's** end.

```text
   ┌──────────┐ 1               1..* ┌──────────┐
   │  House   │◆─────────────────────│   Room   │      House is made of Rooms; rooms die with the house
   └──────────┘                      └──────────┘
```

## Seeing the Difference in C++

- **Composition** → the part is a **member object** (or an owned pointer deleted in the destructor). It's created when the whole is created and destroyed with it.
- **Aggregation** → the whole stores a **pointer/reference** to a part created elsewhere, and never deletes it.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Room
{
    string name;
public:
    Room(const string &n) : name(n) { cout << "  Room " << name << " built" << endl; }
    ~Room() { cout << "  Room " << name << " demolished" << endl; }
};

class House                       // COMPOSITION: House ◆── Room
{
    Room kitchen, bedroom;        // parts are member objects: born and die with the house
public:
    House() : kitchen("Kitchen"), bedroom("Bedroom") { cout << "House built" << endl; }
    ~House() { cout << "House demolished" << endl; }
};

class Player
{
    string name;
public:
    Player(const string &n) : name(n) { }
    string getName() const { return name; }
};

class Team                        // AGGREGATION: Team ◇── Player
{
    Player *captain;              // just points to a Player that exists independently
public:
    Team(Player *p) : captain(p) { }
    ~Team() { cout << "Team disbanded (captain " << captain->getName() << " still exists)" << endl; }
};

int main()
{
    Player rohan("Rohan");        // the player exists BEFORE the team
    {
        House h;                  // rooms are created together with the house...
        Team t(&rohan);
    }                             // ...and destroyed with it; the team ends, the player doesn't
    cout << rohan.getName() << " is still here" << endl;
    return 0;
}
```

```output
  Room Kitchen built
  Room Bedroom built
House built
Team disbanded (captain Rohan still exists)
House demolished
  Room Bedroom demolished
  Room Kitchen demolished
Rohan is still here
```

## Side-by-Side Comparison

| | Association | Aggregation | Composition |
|---|---|---|---|
| Meaning | "knows / is connected to" | "has" (whole–part, weak) | "is made of" (whole–part, strong) |
| UML | plain solid line | hollow diamond ◇ at whole | filled diamond ◆ at whole |
| Part can exist alone? | yes | **yes** | **no** |
| Part shared by several wholes? | yes | possible | **no** — exactly one whole |
| Who creates/destroys the part? | someone else | someone else | **the whole** |
| C++ | pointer/reference | pointer to an external object | member object / owned pointer |
| Examples | Teacher–Course | Team–Player, Library–Member, Department–Professor | House–Room, Book–Chapter, Order–OrderLine, Body–Heart |

### How to decide: ask three questions

1. Is it really a **whole–part** relationship? If not → plain association.
2. Can the part **exist on its own**, or belong to **several** wholes? If yes → aggregation.
3. Does the part's **lifetime depend** on the whole (created and destroyed with it)? If yes → composition.

:::note Larman's advice
Larman notes that UML aggregation has vague meaning, so he suggests: **don't bother with (shared) aggregation — use a plain association or composition. "If in doubt, leave it out."** Composition is useful: it also hints at *who should create the parts* (the GRASP **Creator** pattern, Lesson 13.2). In exams, still know and draw both.
:::

:::key
- Both are whole–part forms of association; the diamond always sits at the **whole**.
- Aggregation (◇): parts independent and shareable.
- Composition (◆): part belongs to one whole; created and destroyed with it.
- C++: composition = member objects; aggregation = pointers to external objects.
:::

:::mistakes
- Putting the diamond at the **part's** end.
- Using composition when the part can exist alone (e.g. Department ◆ Professor — wrong; professors exist independently).
- Calling every "has-a" composition.
- Confusing composition (◆, filled) with aggregation (◇, hollow).
:::

:::exam
- *"Differentiate aggregation and composition with examples, UML notation and C++ code."* (Very common.)
- *"Identify the relationship"*: Car–Engine, Library–Book, Order–OrderLine, University–Department.
:::

:::def
**Aggregation** is a whole–part association in which the part can exist independently of the whole and may be shared; it is shown by a hollow diamond at the whole. **Composition** is a strong form of aggregation in which each part belongs to exactly one whole, cannot exist without it, and is created and destroyed by it; it is shown by a filled diamond at the whole.
:::

## Quick Check

:::q Q1 · Aggregation or composition? (a) Book–Chapter (b) Playlist–Song (c) University–Department (d) Car–Wheel
:::ans
(a) **Composition** — chapters belong to one book. (b) **Aggregation** — songs exist independently and appear in many playlists. (c) **Composition** — a department doesn't exist outside its university. (d) Usually **composition** in a manufacturing model, though **aggregation** is acceptable if wheels can be moved between cars — justify your choice.
:::
:::

:::q Q2 · In C++, how does a composition usually look different from an aggregation?
:::ans
Composition: the part is a **member object** (created/destroyed with the whole). Aggregation: the whole stores a **pointer/reference** to a part that was created elsewhere and is not deleted by the whole.
:::
:::
