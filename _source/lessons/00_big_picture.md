Before diving into syntax and diagrams, let's understand **what this whole subject is about** and **why the topics are arranged the way they are**. Ten minutes here will make every later chapter easier to place in your head.

## What Problem Does OOAD Solve?

Imagine your college asks you to build a **Library Management System**. Members borrow books, return them late, pay fines; librarians add books and register members.

If you open an editor and immediately start typing code, you will soon get stuck:

- *Which pieces of data do I need?* Books? Copies of books? Members? Loans?
- *Which part of the program should calculate a fine?* The member? The book? Some "fine calculator"?
- *What happens when the library later wants e-books, SMS reminders, or a new payment method?* Will half the code need rewriting?

Small programs survive without planning. **Real software does not.** It is built by teams, lives for years, and keeps changing. **Object-Oriented Analysis and Design (OOAD)** is a disciplined way of *thinking before coding*, so that the software is easy to understand, build and change.

## The Three Words: Analysis, Design, Programming

| Step | Question it answers | Library example |
|---|---|---|
| **Analysis** (OOA) | *What* is the problem? What things exist in this world? | "There are Members, Books, Copies, Loans and Fines. A member borrows a copy." |
| **Design** (OOD) | *How* will software objects solve it? Who does what? | "A `Loan` object knows its due date, so the `Loan` should calculate its own fine." |
| **Programming** (OOP) | Write the design in a language. | `class Loan { … int fine() const; };` |

A popular one-liner (from Larman): **analysis = "do the right thing"**, **design = "do the thing right"**.

:::analogy
Building a house. **Analysis** is talking to the family: how many people, do they need a study room, a garden? **Design** is the architect's blueprint: where the walls, pipes and wires go. **Programming** is the actual construction. Nobody pours concrete before the blueprint exists — yet beginners often write code before thinking.
:::

## Why "Object-Oriented"?

The core idea is simple: **organise software the same way the real world is organised — as a set of objects that each have their own data and their own behaviour, and that cooperate by talking to each other.**

In the library, a real loan has a due date. So in software, a `Loan` object *holds* its due date and *knows how to* calculate its fine. When the rules change, you know exactly where to look. That's the whole spirit of this course.

## How This Course Is Organised (and Why)

```text
PART I — Learning the language of objects (Units 1–3)
  Ch 1  C++ Foundations ............ variables, decisions, loops          (the alphabet)
  Ch 2  Functions .................. breaking work into pieces            (words)
  Ch 3  OOP Fundamentals ........... classes, objects, constructors       (sentences)
  Ch 4  Advanced Class Features .... this, copy ctor, operators, friends
  Ch 5  Inheritance & Polymorphism . reuse and "many forms"
  Ch 6  Streams & Files ............ input/output, files, string, vector

PART II — Designing with objects (Units 4–6)
  Ch 7  Intro to OOAD .............. OOA/OOD, Unified Process, UML        (the method)
  Ch 8  Class Relationships ........ association, composition, ...        (how objects connect)
  Ch 9  Use Cases .................. what the system must do              (requirements)
  Ch 10 Class Diagrams & Domain Model  the vocabulary of the problem
  Ch 11 Interaction Diagrams ....... how objects talk over time
  Ch 12 State/Activity/Impl. diagrams  life-cycles, workflows, deployment
  Ch 13 Design Principles & GRASP .. who should do what?                  (good judgement)
  Ch 14 Design Patterns ............ proven solutions to common problems  (expert recipes)
```

Your syllabus starts with "Unit 1: OOP fundamentals", but every OOP example needs basic C++ first. So we learn the basics (Chapters 1–2) and then cover Unit 1 completely in Chapter 3.

## One Example, All the Way Through

Part II follows **one running example — the Library Management System** — from start to finish:

```text
Use cases  ──►  Domain model  ──►  Sequence diagrams  ──►  GRASP decisions  ──►  Design patterns  ──►  C++ code
"Issue Book"    Member, Loan,      who calls whom when     "Loan calculates     Strategy for fines,     class Loan {...}
                BookCopy, Book     a book is issued         its own fine"        Observer for alerts
```

Seeing the same system evolve makes it much easier to understand how the diagrams and patterns connect — which is exactly what long-answer exam questions test.

:::key
- OOAD = thinking about **what** the problem is (analysis) and **how** objects will solve it (design) **before** coding.
- Object orientation models software as **objects with their own data and behaviour** that **cooperate**.
- Part I teaches the C++ needed to express objects; Part II teaches how to design with them.
:::

## Quick Check

:::q Q1 · In one line each, what are analysis and design?
:::ans
**Analysis** — investigating the problem and requirements: *what* the system must do and what concepts exist ("do the right thing"). **Design** — a conceptual solution: *how* software objects will collaborate to meet the requirements ("do the thing right").
:::
:::

:::q Q2 · In the library system, which object would you expect to calculate a loan's fine, and why?
:::ans
The **`Loan`** — it holds the due date and return date, i.e. the information needed. (Later you'll learn this is the **Information Expert** principle.)
:::
:::
