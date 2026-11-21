**An association is a lasting connection between objects of two classes — "a Member *borrows* BookCopies", "a Teacher *teaches* Students". It's the most common relationship in any design.**

## Why Relationships Matter

Objects rarely work alone. A library system is not just a pile of `Member`, `Book` and `Loan` classes — the interesting part is **how they're connected**: which member has which loans, which book has which copies. Getting relationships right is half of object-oriented design.

There are six relationships you need to know. This chapter covers them all:

| Relationship | Meaning in one phrase | Lesson |
|---|---|---|
| **Association** | "is connected to / knows about" | 8.1 |
| **Aggregation** | "has" (parts can live independently) | 8.2 |
| **Composition** | "is made of" (parts live and die with the whole) | 8.2 |
| **Dependency** | "uses temporarily" | 8.3 |
| **Generalization** | "is a" (inheritance) | 8.3 |
| **Realization** | "implements" (an interface) | 8.3 |

## The Problem: Objects That Need to Know About Each Other

A `Teacher` object needs to know which `Course`s they teach; a `Course` might need to know its teacher. If we don't model this connection explicitly, every piece of code that wants "the courses of teacher X" would have to search the whole system. An **association** says: *these two kinds of objects are structurally linked, and the link lasts*.

:::analogy
Think of a **friendship**: two people know each other, can contact each other, and the relationship lasts over time — but neither *owns* the other, and either can exist without the other. That's an association.
:::

## Understanding Association

In UML an association is a **solid line** between two classes, optionally with:
- a **name** (usually a verb) and a reading-direction arrow ▶: `Teacher ── teaches ▶ ── Course`,
- **multiplicity** at each end (how many),
- **role names** at the ends (e.g. `instructor`, `courses`),
- an **arrowhead** for **navigability** (which side can "see" the other).

```text
   ┌──────────┐ 1        teaches ▶        1..* ┌──────────┐
   │ Teacher  │───────────────────────────────│  Course  │
   └──────────┘ instructor             courses └──────────┘
   "One teacher teaches one or more courses; each course is taught by exactly one teacher."
```

### Multiplicity: "how many?"

| Notation | Meaning |
|---|---|
| `1` | exactly one |
| `0..1` | zero or one (optional) |
| `*` or `0..*` | zero or more |
| `1..*` | one or more |
| `2..5` | between 2 and 5 |

**How to read it:** the number written **next to a class** says how many of *that* class are linked to **one** object at the other end. In the diagram above, `1..*` sits next to Course → one teacher has 1 or more courses. `1` sits next to Teacher → one course has exactly one teacher.

### Navigability: who knows whom?

- No arrows (or arrows both ways) → **bidirectional**: each side can reach the other.
- An arrowhead `──►` → **unidirectional**: only the tail side knows the head side.
  `Loan ──► BookCopy` means a loan knows its copy, but a copy doesn't keep a list of loans.

### Kinds by direction and count

- **One-to-one** — `Person 1 ── 1 Passport`
- **One-to-many** — `Teacher 1 ── * Course`
- **Many-to-many** — `Student * ── * Course`
- **Reflexive** (a class associated with itself) — `Employee` *manages* `Employee`.

## Association in C++

An association becomes a **member that points to (or references) the other object** — not a copy of it. One-to-many uses a collection of pointers.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Course;                                 // forward declaration

class Teacher
{
    string name;
    vector<Course*> courses;                  // one-to-many: a teacher knows its courses
public:
    Teacher(const string &n) : name(n) { }
    void addCourse(Course *c) { courses.push_back(c); }
    string getName() const { return name; }
    void listCourses() const;
};

class Course
{
    string title;
    Teacher *instructor = nullptr;            // each course knows its one teacher
public:
    Course(const string &t) : title(t) { }
    void setInstructor(Teacher *t) { instructor = t; t->addCourse(this); }   // keep both sides in sync
    string getTitle() const { return title; }
    void show() const { cout << title << " is taught by " << instructor->getName() << endl; }
};

void Teacher::listCourses() const
{
    cout << name << " teaches:";
    for (Course *c : courses) cout << " " << c->getTitle();
    cout << endl;
}

int main()
{
    Teacher t("Dr. Rao");                     // both objects exist independently
    Course c1("OOAD"), c2("DBMS");
    c1.setInstructor(&t);
    c2.setInstructor(&t);
    c1.show();
    t.listCourses();
    return 0;
}
```

```output
OOAD is taught by Dr. Rao
Dr. Rao teaches: OOAD DBMS
```

Notice: neither object **creates or destroys** the other. They are created separately and simply **linked** by pointers. That's the hallmark of a plain association.

:::key
- Association = a lasting structural link between objects; neither owns the other.
- UML: solid line + name + multiplicities (+ optional role names and navigability arrow).
- Multiplicity next to a class = how many of that class per one object on the other side.
- In C++: a pointer/reference member (or a collection of them for "many").
:::

:::mistakes
- Reading multiplicities from the wrong end.
- Leaving out multiplicities in an exam diagram.
- Copying the other object by value instead of pointing to it (then the "link" is just a stale copy).
- Using association where the relationship is really "is-a" (that's generalization).
:::

:::exam
- *"What is association? Explain multiplicity and navigability with an example."*
- *"Read this diagram"* — interpret multiplicities like `Customer 1 ── 0..* Order`.
:::

:::def
An **association** is a structural relationship between two classes indicating that objects of one class are connected to objects of the other for some duration. It is drawn as a solid line, optionally labelled with a name, role names, **multiplicity** (how many objects participate) and **navigability** (the direction in which objects can be reached).
:::

## Quick Check

:::q Q1 · Interpret `Customer 1 ──── places ──── 0..* Order`.
:::ans
One customer places **zero or more** orders; each order is placed by **exactly one** customer.
:::
:::

:::q Q2 · What does an arrowhead on an association line mean?
:::ans
**Navigability** — the object at the tail can reach (knows about) the object at the arrowhead, but not necessarily the reverse.
:::
:::
