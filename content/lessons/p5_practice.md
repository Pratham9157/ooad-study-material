:::tip
Sections A–F practise Units 5–6. Section G is a **full mock end-term paper** covering all six units — attempt it timed (3 hours) as your final rehearsal, then check the answers.
:::

## Section A · Definitions & Short Answers

:::q A1 · What is a system sequence diagram? How is it different from a (design) sequence diagram?
:::ans
An **SSD** shows, for **one scenario of a use case**, the **system events** that external actors generate, their order, and inter-system events, treating the **system as a black box** (one lifeline). A **design sequence diagram** opens the box and shows the **software objects inside** collaborating via messages to handle a system operation. SSD = requirements artifact (Use-Case Model); sequence diagram = design artifact (Design Model).
:::
:::

:::q A2 · Compare sequence and communication diagrams. When would you prefer a communication diagram?
:::ans
Both are interaction diagrams and semantically equivalent. Sequence: fence format, time flows downward, clear message ordering, rich notation (frames, activations). Communication: network format, objects linked, messages numbered (1, 1.1, 1.2), space-efficient, emphasizes links/structure, ordering harder to read. Prefer communication diagrams for **quick whiteboard sketches**, when you want to **show the links (structure) supporting the interaction**, or when the interaction is simple and time order isn't the focus.
:::
:::

:::q A3 · Define state, event and transition. Write the general syntax of a transition label.
:::ans
**State** — the condition of an object at a moment in time, between events. **Event** — a significant occurrence that may trigger a transition. **Transition** — a relationship between two states: when the event occurs (and guard holds), the object moves from the source state to the target state. Label syntax: **`event [guard] / action`**.
:::
:::

:::q A4 · Differentiate fork/join from decision/merge in activity diagrams.
:::ans
**Decision** (diamond) — one incoming flow, several **guarded** outgoing flows; **only one** branch is taken. **Merge** (diamond) — brings alternative branches back together. **Fork** (thick bar) — one incoming, several outgoing flows that run **in parallel**. **Join** (thick bar) — several incoming parallel flows; continues only when **all** have arrived (synchronization).
:::
:::

:::q A5 · Differentiate device node and execution environment node in deployment diagrams.
:::ans
**Device node** — a **physical** computing resource with processing and memory (server, PC, phone). **Execution environment node (EEN)** — a **software** computing resource running inside a device that hosts executable elements (OS, JVM, web server like Tomcat, database server, browser). Artifacts are deployed on nodes; nodes are connected by communication paths.
:::
:::

:::q A6 · What does GRASP stand for? List the nine GRASP patterns.
:::ans
**General Responsibility Assignment Software Patterns.** Creator, Information Expert, Low Coupling, Controller, High Cohesion, Polymorphism, Pure Fabrication, Indirection, Protected Variations.
:::
:::

:::q A7 · State the problem and solution of the Creator pattern.
:::ans
**Problem:** Who should be responsible for creating a new instance of some class? **Solution:** Assign class B the responsibility to create instances of class A if B **contains or compositely aggregates** A, B **records** A, B **closely uses** A, or B **has the initializing data** for A (the more the better; prefer containment/aggregation).
:::
:::

:::q A8 · What is the Controller pattern? What are the two kinds of controllers? What is a bloated controller?
:::ans
Controller: assign the responsibility of receiving/coordinating a **system operation** to a non-UI class representing either (1) the **overall system, a root object, a device or a major subsystem** (**facade controller**) or (2) a **use case scenario** (**use case/session controller**, e.g. `ProcessSaleHandler`). A **bloated controller** receives too many system events and/or does the work itself instead of delegating, with many attributes — low cohesion. Fix: add use case controllers; delegate.
:::
:::

:::q A9 · Define coupling and cohesion. Which should be high and which low?
:::ans
**Coupling** — how strongly one element is connected to / has knowledge of / relies on other elements → keep **low**. **Cohesion** — how strongly related and focused the responsibilities of an element are → keep **high**.
:::
:::

:::q A10 · Give the intent of: Factory Method, Adapter, Bridge, Strategy, Observer.
:::ans
- **Factory Method:** Define an interface for creating an object, but let subclasses decide which class to instantiate; defers instantiation to subclasses.
- **Adapter:** Convert the interface of a class into another interface clients expect; lets classes with incompatible interfaces work together.
- **Bridge:** Decouple an abstraction from its implementation so that the two can vary independently.
- **Strategy:** Define a family of algorithms, encapsulate each one, and make them interchangeable; lets the algorithm vary independently from clients.
- **Observer:** Define a one-to-many dependency so that when one object changes state, all its dependents are notified and updated automatically.
:::
:::

## Section B · MCQs

:::q B1 · Which frame operator represents a loop in a sequence diagram?
(a) alt (b) opt (c) loop (d) ref
:::ans
**(c) loop**.
:::
:::

:::q B2 · In a communication diagram, the message numbered `2.1.3` is:
(a) the third message sent by the object handling message 2.1 (b) the 213th message (c) a message sent in parallel with 2 (d) a return message
:::ans
**(a)** — nested decimal numbering: inside 2.1, the 3rd message.
:::
:::

:::q B3 · A return message in a sequence diagram is drawn as a:
(a) solid line with filled arrowhead (b) dashed line with open arrowhead (c) solid line with open arrowhead (d) dashed line with no arrowhead
:::ans
**(b)**. (a) is a synchronous message, (c) is asynchronous.
:::
:::

:::q B4 · Which GRASP pattern says "assign a responsibility to the class that has the information needed to fulfil it"?
(a) Creator (b) Controller (c) Information Expert (d) Pure Fabrication
:::ans
**(c) Information Expert**.
:::
:::

:::q B5 · Observer belongs to which GoF category?
(a) Creational (b) Structural (c) Behavioural (d) Architectural
:::ans
**(c) Behavioural**.
:::
:::

:::q B6 · Bridge belongs to which category?
(a) Creational (b) Structural (c) Behavioural (d) GRASP
:::ans
**(b) Structural**.
:::
:::

:::q B7 · The pattern that avoids a "class explosion" when two dimensions vary independently is:
(a) Adapter (b) Bridge (c) Singleton (d) Observer
:::ans
**(b) Bridge** (m × n classes → m + n).
:::
:::

:::q B8 · Which diagram best shows which software artifacts run on which servers?
(a) Component (b) Package (c) Deployment (d) Activity
:::ans
**(c) Deployment**.
:::
:::

:::q B9 · A lollipop symbol in a component diagram denotes:
(a) required interface (b) provided interface (c) port (d) artifact
:::ans
**(b) provided interface** (the socket/half-circle is a required interface).
:::
:::

:::q B10 · Which is the best choice of Controller for system events of the "Process Sale" use case when the system has many use cases?
(a) The SaleWindow GUI class (b) ProcessSaleHandler (c) A Database class (d) The Cashier actor
:::ans
**(b) ProcessSaleHandler** — a use case controller (UI classes and actors are not controllers).
:::
:::

## Section C · Identify the Pattern

:::q C1 · Name the GoF/GRASP pattern for each scenario.
1. A weather station must inform several display panels whenever readings change; displays can be added at run time.
2. Your application must use a legacy printer library whose method is `printText(char*, int len)` but your code expects `print(string)`.
3. A shopping cart can apply "no discount", "10% festival discount" or "buy-2-get-1" pricing, selectable at run time.
4. A document editor framework lets each kind of application (`DrawingApp`, `TextApp`) decide which `Document` subclass to create.
5. Shapes (Circle, Square) must be drawable with different rendering APIs (OpenGL, DirectX) without creating `OpenGLCircle`, `DirectXCircle`, …
6. A class `Sale` contains `SalesLineItem`s; who should create a `SalesLineItem`?
7. Who should calculate the subtotal of a `SalesLineItem` (quantity × price)?
8. The first object beyond the UI to receive `enterItem()`.
9. A class responsible only for saving objects to a database, not representing any domain concept.
10. Exactly one configuration manager object, accessible from anywhere.
:::ans
1. **Observer** 2. **Adapter** 3. **Strategy** 4. **Factory Method** 5. **Bridge** 6. **Creator** (Sale contains SalesLineItems) 7. **Information Expert** (SalesLineItem knows quantity and its ProductDescription's price) 8. **Controller** (`Register` facade or `ProcessSaleHandler`) 9. **Pure Fabrication** 10. **Singleton**
:::
:::

:::q C2 · Identify the pattern implemented here and name each participant.
```cpp
#include <iostream>
using namespace std;
class Sorter { public: virtual void sort(int a[], int n) = 0; virtual ~Sorter() { } };
class BubbleSort : public Sorter
{
public:
    void sort(int a[], int n) override
    {
        for (int i = 0; i < n - 1; i++)
            for (int j = 0; j < n - 1 - i; j++)
                if (a[j] > a[j + 1]) { int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t; }
        cout << "bubble ";
    }
};
class ReverseSort : public Sorter
{
public:
    void sort(int a[], int n) override
    {
        for (int i = 0; i < n - 1; i++)
            for (int j = 0; j < n - 1 - i; j++)
                if (a[j] < a[j + 1]) { int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t; }
        cout << "reverse ";
    }
};
class DataSet
{
    int a[4] = {3, 1, 4, 2};
    Sorter *s;
public:
    DataSet(Sorter *x) : s(x) { }
    void setSorter(Sorter *x) { s = x; }
    void process()
    {
        s->sort(a, 4);
        for (int v : a) cout << v;
        cout << endl;
    }
};
int main()
{
    BubbleSort b; ReverseSort r;
    DataSet d(&b);
    d.process();
    d.setSorter(&r);
    d.process();
    return 0;
}
```
What is the output?
:::ans
```output
bubble 1234
reverse 4321
```
Pattern: **Strategy**. Strategy = `Sorter`; ConcreteStrategies = `BubbleSort`, `ReverseSort`; Context = `DataSet` (delegates `sort` to its current strategy, which can be changed at run time with `setSorter`).
:::
:::

:::q C3 · What is the output, and which pattern is this?
```cpp
#include <iostream>
#include <vector>
using namespace std;
class Listener { public: virtual void onChange(int v) = 0; virtual ~Listener() { } };
class Doubler : public Listener { public: void onChange(int v) override { cout << "D" << v * 2 << " "; } };
class Printer : public Listener { public: void onChange(int v) override { cout << "P" << v << " "; } };
class Counter
{
    int value = 0;
    vector<Listener*> ls;
public:
    void add(Listener *l) { ls.push_back(l); }
    void inc() { value++; for (Listener *l : ls) l->onChange(value); }
};
int main()
{
    Counter c; Doubler d; Printer p;
    c.inc();
    c.add(&d);
    c.inc();
    c.add(&p);
    c.inc();
    cout << endl;
    return 0;
}
```
:::ans
```output
D4 D6 P3 
```
**Observer**: `Counter` is the subject, `Listener` the observer interface, `Doubler`/`Printer` concrete observers. The first `inc()` (value 1) has no listeners. Second (value 2): only Doubler → `D4`. Third (value 3): Doubler then Printer → `D6 P3`.
:::
:::

## Section D · Diagram Questions (draw on paper; model answers in text)

:::q D1 · Draw an SSD for the main success scenario of "Withdraw Cash" (ATM).
:::ans
```uml
   :Customer                                       :ATM System                     :Bank System
       │  insertCard(cardNo)                            │                                │
       │───────────────────────────────────────────────►│                                │
       │◄ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ request PIN ─│                                │
       │  enterPIN(pin)                                 │                                │
       │───────────────────────────────────────────────►│  verify(cardNo, pin)           │
       │                                                │───────────────────────────────►│
       │                                                │◄ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ok ─ ─│
       │◄ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ menu ─│                                │
       │  withdraw(amount)                              │                                │
       │───────────────────────────────────────────────►│  authorize(cardNo, amount)     │
       │                                                │───────────────────────────────►│
       │                                                │◄ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ approved ─│
       │◄ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ cash, card, receipt ─│                                │
```
Only actors + the system (and external systems) appear; events named at intent level.
:::
:::

:::q D2 · Draw a state machine diagram for an online Order: New → Paid → Shipped → Delivered, with cancellation possible before shipping and returns within 7 days of delivery.
:::ans
```uml
  ●──create──►┌─────────┐ pay [amount ok] / sendInvoice ┌────────┐ ship / assignCourier ┌─────────┐ deliver ┌───────────┐
              │   New   │──────────────────────────────►│  Paid  │─────────────────────►│ Shipped │────────►│ Delivered │
              └────┬────┘                               └───┬────┘                      └─────────┘         └─────┬─────┘
                   │ cancel                                 │ cancel / refund                                     │
                   ▼                                        ▼                         requestReturn [within 7 days]│  after(7 days)
              ┌─────────────────────────────────────────────────┐                                      ┌──────────▼┐     │
              │                  Cancelled                      │                                      │ Returned  │     ▼
              └──────────────────────┬──────────────────────────┘                                      └─────┬─────┘     ◉
                                     ▼                                                       refund / restock │
                                     ◉                                                                        ▼ ◉
```
Key points: initial ●, final ◉, labels `event [guard] / action`, time event `after(7 days)`, cancellation only from New and Paid (not after shipping).
:::
:::

:::q D3 · Draw an activity diagram (with swimlanes Customer / Restaurant / Delivery) for an online food order, showing the kitchen preparing food in parallel with assigning a delivery agent.
:::ans
```uml
     Customer                 │       Restaurant                │       Delivery
  ●                           │                                 │
  │                           │                                 │
 (Place order)                │                                 │
  │──────────────────────────►(Accept order?)◇                  │
                              │  [rejected]│  [accepted]        │
  (Get refund)◄───────────────┼────────────┘     │              │
  │                           │                  ▼              │
  ◉                           │      ━━━━━━━━━━━━┿━━━━━━━━━━━━━━━┿━━━━ (fork)
                              │      │                          │        │
                              │ (Prepare food)                  │ (Assign delivery agent)
                              │      │                          │        │
                              │      ━━━━━━━━━━━━┿━━━━━━━━━━━━━━━┿━━━━ (join)
                              │                  ▼              │
                              │           (Hand over food)──────┼──►(Deliver order)
                              │                                 │        │
  (Receive & rate) ◄──────────┼─────────────────────────────────┼────────┘
  │                           │                                 │
  ◉                           │                                 │
```
Must show: initial node, decision with guards, fork **and** join bars, swimlanes, final node(s).
:::
:::

:::q D4 · Draw a sequence diagram for "Sale.getTotal()" using Information Expert (Sale, SalesLineItem, ProductDescription), and write the corresponding C++ code.
:::ans
```uml
  :Register        :Sale                 :SalesLineItem[i]          :ProductDescription
     │ t := getTotal() │                         │                          │
     │────────────────►│ loop [i < lineItems.size]                          │
     │                 │── st := getSubtotal() ─►│                          │
     │                 │                         │── pr := getPrice() ─────►│
     │                 │                         │◄ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ pr ─│
     │                 │◄ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ st ─│                          │
     │◄ ─ ─ ─ ─ ─ ─ t ─│                         │                          │
```
```cpp
#include <iostream>
#include <vector>
using namespace std;

class ProductDescription
{
    double price;
public:
    ProductDescription(double p) : price(p) { }
    double getPrice() const { return price; }                 // Expert: knows price
};

class SalesLineItem
{
    int quantity;
    const ProductDescription *desc;
public:
    SalesLineItem(const ProductDescription *d, int q) : quantity(q), desc(d) { }
    double getSubtotal() const { return quantity * desc->getPrice(); }   // Expert: knows quantity
};

class Sale
{
    vector<SalesLineItem> lineItems;
public:
    void makeLineItem(const ProductDescription *d, int q)
    {
        lineItems.push_back(SalesLineItem(d, q));              // Creator: Sale contains line items
    }
    double getTotal() const                                    // Expert: knows its line items
    {
        double t = 0;
        for (const SalesLineItem &li : lineItems) t += li.getSubtotal();
        return t;
    }
};

int main()
{
    ProductDescription pen(10.5), book(250);
    Sale s;
    s.makeLineItem(&pen, 4);
    s.makeLineItem(&book, 2);
    cout << "Total = " << s.getTotal() << endl;
    return 0;
}
```
```output
Total = 542
```
:::
:::

:::q D5 · Draw a deployment diagram for a web-based Library system: users' browsers, an application server running Tomcat with `lms.war`, and a database server running MySQL.
:::ans
```uml
 ┌─────────────────────┐   «HTTPS»   ┌──────────────────────────────┐   «JDBC/TCP»   ┌───────────────────────────┐
 │ «device» Client PC  │─────────────│ «device» App Server          │────────────────│ «device» DB Server        │
 │ ┌─────────────────┐ │   1..*   1  │ ┌──────────────────────────┐ │ 1           1  │ ┌───────────────────────┐ │
 │ │«executionEnv.»  │ │             │ │ «executionEnvironment»   │ │                │ │ «executionEnvironment»│ │
 │ │ Web Browser     │ │             │ │  Tomcat                  │ │                │ │  MySQL Server         │ │
 │ └─────────────────┘ │             │ │  ┌────────────────────┐  │ │                │ │ ┌───────────────────┐ │ │
 └─────────────────────┘             │ │  │ «artifact» lms.war │  │ │                │ │ │«artifact» lms.sql │ │ │
                                     │ │  └────────────────────┘  │ │                │ │ └───────────────────┘ │ │
                                     │ └──────────────────────────┘ │                │ └───────────────────────┘ │
                                     └──────────────────────────────┘                └───────────────────────────┘
```
(Nodes are drawn as 3-D boxes on paper.)
:::
:::

## Section E · Write the Code

:::q E1 · Implement the Adapter pattern: a client uses `Thermometer::getCelsius()`, but the available sensor class `FahrenheitSensor` only offers `readF()`. Write the adapter.
:::ans
```cpp
#include <iostream>
using namespace std;

class Thermometer                                  // Target
{
public:
    virtual double getCelsius() const = 0;
    virtual ~Thermometer() { }
};

class FahrenheitSensor                             // Adaptee (can't modify)
{
public:
    double readF() const { return 98.6; }
};

class SensorAdapter : public Thermometer           // Adapter
{
    FahrenheitSensor sensor;
public:
    double getCelsius() const override { return (sensor.readF() - 32) * 5 / 9; }
};

void report(const Thermometer &t)                  // Client knows only the Target
{
    cout << "Temperature: " << t.getCelsius() << " C" << endl;
}

int main()
{
    SensorAdapter a;
    report(a);
    return 0;
}
```
```output
Temperature: 37 C
```
:::
:::

:::q E2 · Implement Factory Method: `Logistics` with factory method `createTransport()`; `RoadLogistics` creates `Truck`, `SeaLogistics` creates `Ship`; `planDelivery()` uses the transport.
:::ans
```cpp
#include <iostream>
using namespace std;

class Transport { public: virtual void deliver() const = 0; virtual ~Transport() { } };
class Truck : public Transport { public: void deliver() const override { cout << "Deliver by road in a truck" << endl; } };
class Ship  : public Transport { public: void deliver() const override { cout << "Deliver by sea in a ship" << endl; } };

class Logistics                                     // Creator
{
public:
    virtual Transport* createTransport() const = 0; // factory method
    void planDelivery() const
    {
        Transport *t = createTransport();
        t->deliver();
        delete t;
    }
    virtual ~Logistics() { }
};
class RoadLogistics : public Logistics { public: Transport* createTransport() const override { return new Truck(); } };
class SeaLogistics  : public Logistics { public: Transport* createTransport() const override { return new Ship(); } };

int main()
{
    RoadLogistics road;
    SeaLogistics sea;
    road.planDelivery();
    sea.planDelivery();
    return 0;
}
```
```output
Deliver by road in a truck
Deliver by sea in a ship
```
:::
:::

:::q E3 · Map this DCD to C++ (class definitions only, plus a short `main`): `Course 1 ── offers ──► * Section` (Course creates Sections; Section has `- number : int`, `- capacity : int`, `+ isFull(enrolled : int) : bool`); Course has `- title : string`, `+ addSection(n : int, cap : int)`, `+ sectionCount() : int`.
:::ans
```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Section
{
    int number;
    int capacity;
public:
    Section(int n, int cap) : number(n), capacity(cap) { }
    bool isFull(int enrolled) const { return enrolled >= capacity; }
};

class Course
{
    string title;
    vector<Section> sections;          // one-to-many -> collection; Course creates/contains Sections
public:
    Course(const string &t) : title(t) { }
    void addSection(int n, int cap) { sections.push_back(Section(n, cap)); }
    int sectionCount() const { return (int)sections.size(); }
};

int main()
{
    Course c("OOAD");
    c.addSection(1, 60);
    c.addSection(2, 45);
    cout << c.sectionCount() << endl;
    return 0;
}
```
```output
2
```
:::
:::

## Section F · Long Answer

:::q F1 · Explain the GRASP patterns Creator, Information Expert, Low Coupling, High Cohesion and Controller with examples and diagrams.
:::ans
For **each**: problem → solution → example (POS: Sale creates SalesLineItem; Sale.getTotal via Expert; Register vs Sale creating Payment for Low Coupling; cohesion levels for High Cohesion; Register/ProcessSaleHandler as Controller) → small sequence diagram → contraindications/benefits. Use the tables in [Lesson 13.2](13_2_grasp_expert_creator.html) and [Lesson 13.3](13_3_grasp_controller.html). Conclude: GRASP patterns are applied together while drawing interaction diagrams.
:::
:::

:::q F2 · Explain the Observer and Strategy patterns with structure diagrams, participants, C++ code and consequences.
:::ans
[Lesson 14.6](14_6_strategy.html) (Strategy) and [Lesson 14.7](14_7_observer.html) (Observer): intent, problem, structure diagram, participants, code + output, consequences. Mention Larman's examples (pricing strategies; Sale → UI windows for model–view separation).
:::
:::

:::q F3 · Explain state machine and activity diagrams with notation, an example of each and when to use them. How do they differ?
:::ans
[Lesson 12.1](12_1_state_machine.html) (notation table, BookCopy example, label syntax, when to use) and [Lesson 12.2](12_2_activity.html) (notation table, Return Book swimlane example, when to use), and the comparison table in [Lesson 12.2](12_2_activity.html).
:::
:::

:::q F4 · Explain package, component and deployment diagrams with notation and when to use each.
:::ans
[Lesson 12.3](12_3_implementation_diagrams.html): definitions, notation (tabbed folder + dashed dependency; component + lollipop/socket; nodes/artifacts/communication paths), examples (layered architecture; Web UI–Loan Management–Payment Adapter; browser–Tomcat–MySQL), "when to use" lists, and the comparison table.
:::
:::

## Section G · Full Mock End-Term Paper (all six units)

:::note Instructions (simulate the real exam)
Time: 3 hours. **Part A**: answer all (10 × 2 = 20). **Part B**: answer any five (5 × 6 = 30). **Part C**: answer any two (2 × 10 = 20). Write first, then open the answers.
:::

### Part A (answer all — 2 marks each)

:::q G-A1 · Differentiate between a class and a structure in C++.
:::ans
Default member access: **private** in a class, **public** in a struct; default inheritance: private for class, public for struct. Otherwise identical in C++ (both can have functions, constructors, inheritance).
:::
:::

:::q G-A2 · What is a constructor? Can it be overloaded?
:::ans
A special member function with the class's name and no return type, called automatically when an object is created, to initialize it. **Yes**, constructors can be overloaded (different parameter lists) — constructor overloading.
:::
:::

:::q G-A3 · Predict the output: `int a = 10; int *p = &a; *p += 5; cout << a << " " << (*p)++ << " " << a;`
:::ans
In C++17 the operands of `<<` are evaluated left to right, so it prints `15 15 16`. **Better exam answer:** point out that reading and modifying `a` in the same expression is risky (before C++17 the order was unspecified — results could differ); the safe, intended values are: after `*p += 5`, `a` is 15; `(*p)++` yields 15 and makes `a` 16.
:::
:::

:::q G-A4 · Why is the argument of a copy constructor passed by reference?
:::ans
Passing by value would itself require copying the argument, which calls the copy constructor again → infinite recursion. Hence `X(const X &)`.
:::
:::

:::q G-A5 · What is a pure virtual function?
:::ans
A virtual function with no definition in the base class, declared with `= 0` (e.g. `virtual void draw() = 0;`). It makes the class abstract and forces derived classes to override it.
:::
:::

:::q G-A6 · Name the four phases of the Unified Process.
:::ans
Inception, Elaboration, Construction, Transition.
:::
:::

:::q G-A7 · Differentiate «include» and «extend» (one line each).
:::ans
«include»: the base use case **always** incorporates the included use case (arrow base → included). «extend»: the extending use case **optionally** adds behaviour to the base at an extension point (arrow extension → base).
:::
:::

:::q G-A8 · What is a description class? Give an example.
:::ans
A class describing other things, so descriptive information isn't duplicated or lost — e.g. `ProductDescription` describing `Item`s; `Book` describing `BookCopy`s.
:::
:::

:::q G-A9 · What is an SSD?
:::ans
A system sequence diagram — for one use case scenario, it shows the system events actors send to the system (treated as a black box) and their order.
:::
:::

:::q G-A10 · State the intent of the Bridge pattern.
:::ans
Decouple an abstraction from its implementation so that the two can vary independently.
:::
:::

### Part B (any five — 6 marks each)

:::q G-B1 · Explain function overloading and default arguments with a program. When can they cause ambiguity?
:::ans
Definitions ([Lesson 2.5](02_5_overloading.html)) + program (e.g. overloaded `area()` and `interest()` with defaults) + ambiguity cases: `f(int)`/`f(float)` called with `5.5`; `g(int)` and `g(int, int = 0)` called with `g(5)`; defaults must be right-to-left.
:::
:::

:::q G-B2 · What is a friend function? Write a program that uses a friend function to add the private data of two different classes.
:::ans
Definition + characteristics ([Lesson 4.5](04_5_friends.html)) + program (Alpha/Beta `sumBoth` with forward declaration) + output 35.
:::
:::

:::q G-B3 · Predict the output and explain.
```cpp
#include <iostream>
using namespace std;
class A
{
public:
    A() { cout << "A "; }
    virtual void f() { cout << "A::f "; }
    virtual ~A() { cout << "~A "; }
};
class B : public A
{
public:
    B() { cout << "B "; }
    void f() override { cout << "B::f "; }
    ~B() { cout << "~B "; }
};
int main()
{
    A *p = new B;
    p->f();
    delete p;
    cout << endl;
    return 0;
}
```
:::ans
```output
A B B::f ~B ~A 
```
Base constructor runs before derived; `f` is virtual → `B::f`; the virtual destructor ensures `~B` runs before `~A` when deleting through a base pointer.
:::
:::

:::q G-B4 · Write a program to copy the contents of one text file into another, converting all letters to uppercase, and display the count of characters copied.
:::ans
```cpp
#include <iostream>
#include <fstream>
#include <cctype>
#include <string>
using namespace std;

int main()
{
    ofstream make("in.txt");
    make << "Hello OOAD\nexam 2026";
    make.close();

    ifstream in("in.txt");
    ofstream out("out.txt");
    if (!in || !out) { cout << "File error" << endl; return 1; }
    char ch;
    int count = 0;
    while (in.get(ch))
    {
        out.put(toupper(ch));
        count++;
    }
    in.close(); out.close();

    ifstream show("out.txt");
    string line;
    while (getline(show, line)) cout << line << endl;
    cout << "Characters copied: " << count << endl;
    return 0;
}
```
```output
HELLO OOAD
EXAM 2026
Characters copied: 20
```
:::
:::

:::q G-B5 · Explain aggregation and composition with UML notation, examples and C++ code.
:::ans
[Lesson 8.2](08_2_aggregation_composition.html): definitions, Larman's composition criteria, table, diagrams (◇ vs ◆ at whole), House/Room vs Team/Person program and output.
:::
:::

:::q G-B6 · Draw a use case diagram for an Online Examination System (actors: Student, Examiner, Admin) with include and extend relationships, and write a brief use case for "Take Exam".
:::ans
Use cases — Student: Register, Take Exam, View Result; Examiner: Create Question Paper, Evaluate Answers; Admin: Manage Users, Schedule Exam. «include»: Take Exam → Authenticate, View Result → Authenticate. «extend»: Request Re-evaluation → View Result (if the student is not satisfied). System boundary, actors outside, associations.
**Brief — Take Exam:** *The Student logs in and selects a scheduled exam. The System displays questions one at a time with a countdown timer; the Student answers and may revisit questions. When the Student submits or time expires, the System records the answers, auto-grades objective questions and confirms submission.*
:::
:::

:::q G-B7 · Explain the Controller pattern. Compare facade and use case controllers.
:::ans
Problem/solution ([Lesson 13.3](13_3_grasp_controller.html)), key point that UI must not handle system events, two kinds with examples (`Register`/`LibrarySystem` vs `ProcessSaleHandler`/`IssueBookHandler`), when to use which (few events vs many → bloated), bloated controller problem and cures, benefits (pluggable UI, use case state reasoning). Optionally include the C++ controller program.
:::
:::

### Part C (any two — 10 marks each)

:::q G-C1 · (a) Explain run-time polymorphism using virtual functions and the vtable mechanism. (b) Write a program with an abstract class `Account` (pure virtual `interest()`), derived `Savings` (4%) and `Current` (0%), stored in an array of base pointers.
:::ans
(a) [Lesson 5.4](05_4_polymorphism_virtual.html) (problem without virtual, solution, vtable/vptr diagram, rules, static vs dynamic binding).
(b)
```cpp
#include <iostream>
using namespace std;

class Account
{
protected:
    double balance;
public:
    Account(double b) : balance(b) { }
    virtual double interest() const = 0;
    virtual const char* type() const = 0;
    virtual ~Account() { }
};
class Savings : public Account
{
public:
    Savings(double b) : Account(b) { }
    double interest() const override { return balance * 0.04; }
    const char* type() const override { return "Savings"; }
};
class Current : public Account
{
public:
    Current(double b) : Account(b) { }
    double interest() const override { return 0; }
    const char* type() const override { return "Current"; }
};

int main()
{
    Account *acc[3] = {new Savings(10000), new Current(50000), new Savings(2500)};
    for (int i = 0; i < 3; i++)
        cout << acc[i]->type() << ": " << acc[i]->interest() << endl;
    for (int i = 0; i < 3; i++) delete acc[i];
    return 0;
}
```
```output
Savings: 400
Current: 0
Savings: 100
```
:::
:::

:::q G-C2 · For a Hotel Room Booking system: (a) identify conceptual classes by noun-phrase analysis from the statement "Guests book rooms of a room type for a date range; a booking may include several rooms; payment is made by card or cash; each hotel has many rooms." (b) Draw the domain model with multiplicities, a description class and a generalization. (c) Draw an SSD for "Book Room".
:::ans
(a) Nouns: guest, room, room type, date range, booking, payment, card, cash, hotel. Date range → attributes (checkIn, checkOut) of Booking. Room type → **description class** (`RoomType`: name, rate, capacity) describing many `Room`s. Payment → abstract superclass with `CardPayment`, `CashPayment`.
(b)
```uml
 ┌────────┐ 1   Has   1..* ┌────────┐ *   Described-by  1 ┌────────────┐
 │ Hotel  │◆───────────────│  Room  │─────────────────────│  RoomType  │  (description class)
 │ name   │                │ number │                     │ name, rate │
 └────────┘                └───┬────┘                     └────────────┘
                             1..* │ Reserves ▲
                                *  │
 ┌────────┐ 1  Makes   *  ┌──────────────┐ 1   Paid-by   0..1 ┌───────────┐
 │ Guest  │───────────────│   Booking    │───────────────────│ *Payment* │ (abstract)
 │ name   │               │ checkIn      │                    │ amount    │
 │ phone  │               │ checkOut     │                    └─────△─────┘
 └────────┘               └──────────────┘                  ┌──────┴───────┐
                                                     ┌────────────┐  ┌────────────┐
                                                     │CardPayment │  │CashPayment │
                                                     │ cardNumber │  │ tendered   │
                                                     └────────────┘  └────────────┘
```
(Booking * — 1..* Room: a booking reserves one or more rooms; a room appears in many bookings over time.) Subclasses satisfy the 100% and Is-a rules.
(c)
```uml
  :Guest/Receptionist                        :HotelSystem
        │ startBooking(guestId)                   │
        │────────────────────────────────────────►│
        │ ┌loop [more rooms]──────────────────────┼──┐
        │ │ addRoom(roomType, checkIn, checkOut)  │  │
        │ │──────────────────────────────────────►│  │
        │ │◄ ─ ─ ─ ─ ─ ─ ─ ─ room no, rate ─ ─ ─ ─│  │
        │ └───────────────────────────────────────┼──┘
        │ endBooking()                            │
        │────────────────────────────────────────►│
        │◄ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ total ─ ─ ─ ─│
        │ makePayment(amount, method)             │
        │────────────────────────────────────────►│
        │◄ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ confirmation ─ ─ ─ ─│
```
:::
:::

:::q G-C3 · (a) What are design patterns? Classify the GoF patterns. (b) Explain Factory Method and Adapter with structure, participants and C++ code. (c) How are GoF patterns related to GRASP?
:::ans
(a) Definition, four essential elements (name, problem, solution, consequences), GoF 1994 (Gamma, Helm, Johnson, Vlissides), creational/structural/behavioural table, class vs object scope.
(b) [Lesson 14.2](14_2_factory_method.html) (Factory Method: Reminder example + code + output) and [Lesson 14.4](14_4_adapter.html) (Adapter: QuickPay example + code + output), participants lists, object vs class adapter.
(c) GRASP = fundamental principles; GoF patterns are applications of them: Adapter = Indirection + Polymorphism + Protected Variations; Factory = Pure Fabrication (Larman's simple factory) / Factory Method uses Polymorphism + Low Coupling; Observer = Low Coupling (model–view separation); Strategy = Polymorphism + Protected Variations.
:::
:::

:::summary Final exam-day checklist
- Part I: trace output questions with a variable table; remember constructor/destructor order, copy-constructor calls, `setw`/`setprecision` behaviour, virtual vs non-virtual calls, slicing.
- Part II: arrow directions (include → included; extend → base; triangle → parent; diamond at whole), UP phase goals, domain model = no operations, SSD = black box, `event [guard] / action`, fork/join vs decision/merge, GRASP problem–solution lines, GoF intents word-for-word.
- Every diagram answer: neat, labelled, multiplicities/stereotypes, 2–3 lines of explanation.
:::
