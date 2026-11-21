**A design pattern is a proven, reusable solution to a problem that keeps coming up in software design. It's not code you copy — it's a template for how to arrange classes and objects.**

## The Problem: Reinventing the Wheel

Many design problems repeat across projects: "I need to support several payment providers with different APIs", "many screens must update when data changes", "the fine rules keep changing". Every team solving these from scratch makes the same mistakes. Experienced designers noticed the **same good solutions** appearing again and again — and gave them **names**.

:::analogy
Chess players learn named **openings** ("Sicilian Defence"). Nobody invents them during a game; they're proven sequences with known strengths and weaknesses, and naming them lets players discuss strategy quickly. Design patterns are the named openings of software design.
:::

## What Is a Design Pattern?

A design pattern describes:
1. **Name** — a shared vocabulary ("let's use an Adapter here").
2. **Problem** — when to apply it.
3. **Solution** — the classes, their responsibilities and collaborations (a template, not finished code).
4. **Consequences** — the benefits and trade-offs.

These four are the **essential elements** of a pattern (GoF).

## The Gang of Four (GoF) Catalogue

The classic book *Design Patterns: Elements of Reusable Object-Oriented Software* (1994) by **Gamma, Helm, Johnson and Vlissides** — the **"Gang of Four"** — describes **23 patterns** in three categories:

| Creational (5) — *how objects are created* | Structural (7) — *how classes/objects are composed* | Behavioural (11) — *how objects interact and share responsibilities* |
|---|---|---|
| Abstract Factory | **Adapter** ★ | Chain of Responsibility |
| Builder | **Bridge** ★ | Command |
| **Factory Method** ★ | Composite | Interpreter |
| Prototype | Decorator | Iterator |
| Singleton | Facade | Mediator |
| | Flyweight | Memento |
| | Proxy | **Observer** ★ |
| | | State |
| | | **Strategy** ★ |
| | | Template Method |
| | | Visitor |

★ = in your syllabus. We also cover **Singleton** because it's commonly used with factories.

GoF also classify patterns by **scope**: **class patterns** use inheritance (fixed at compile time — e.g. Factory Method, class Adapter); **object patterns** use composition (changeable at run time — most others).

## GRASP vs GoF

| GRASP | GoF design patterns |
|---|---|
| 9 basic **principles** for assigning responsibilities | 23 specific **solutions** to recurring design problems |
| Learning aid for fundamental OO design (Larman) | Catalogue of expert designs (Gamma et al.) |
| e.g. Expert, Creator, Controller | e.g. Adapter, Strategy, Observer |

GoF patterns can be explained with GRASP: an **Adapter** applies Indirection + Polymorphism + Protected Variations; a **Strategy** applies Polymorphism + Protected Variations.

## The Big Idea Behind Most Patterns

> **Identify what varies and separate it from what stays the same.** Hide the varying part behind an interface, so new variations can be added without touching the stable code.

You'll see this idea in every pattern of this chapter.

## A Word of Caution

Patterns are tools, not goals. **Don't force a pattern** where a simple class would do — that adds complexity for nothing (remember KISS and YAGNI). Use a pattern when you clearly recognise its problem.

:::key
- Pattern = named, proven solution template: name, problem, solution, consequences.
- GoF (1994): 23 patterns — creational (5), structural (7), behavioural (11).
- Syllabus: Factory Method (creational), Adapter & Bridge (structural), Strategy & Observer (behavioural).
- Core idea: separate what varies from what stays the same.
:::

:::mistakes
- Putting a pattern in the wrong category (Observer is behavioural, Bridge is structural, Factory Method is creational).
- Confusing GRASP (principles) with GoF (patterns).
- Forcing patterns everywhere.
:::

:::exam
- *"What is a design pattern? What are its essential elements? Classify the GoF patterns."*
- *"Differentiate GRASP and GoF patterns."*
:::

:::def
A **design pattern** is a general, reusable solution to a commonly occurring problem in software design, described by its name, the problem it addresses, the solution (classes, responsibilities and collaborations) and the consequences of applying it. The **Gang of Four (GoF)** catalogue contains 23 patterns classified as **creational**, **structural** and **behavioural**.
:::

## Quick Check

:::q Q1 · Classify: Factory Method, Adapter, Observer, Bridge, Strategy, Singleton.
:::ans
Creational: **Factory Method, Singleton**. Structural: **Adapter, Bridge**. Behavioural: **Observer, Strategy**.
:::
:::

:::q Q2 · Name the four essential elements of a pattern.
:::ans
**Name, problem, solution, consequences.**
:::
:::
