**The Factory Method pattern (creational) lets a base class define *when* an object is created and how it's used, while subclasses decide *which* concrete class to create.**

What varies: **the type of object being created**. What stays the same: **the code that uses it**.

## 1. The Problem: Sending Reminders

The library sends "your book is due tomorrow" reminders. At first only by email. Then SMS is added, then WhatsApp…

```cpp
#include <iostream>
#include <string>
using namespace std;

class ReminderService
{
public:
    void remind(const string &member, const string &channel)
    {
        if (channel == "email")      cout << "[Email] " << member << ", your book is due tomorrow." << endl;
        else if (channel == "sms")   cout << "[SMS] "   << member << ", your book is due tomorrow." << endl;
        // else if (channel == "whatsapp") ...  ← edit this class again for every new channel
    }
};

int main()
{
    ReminderService r;
    r.remind("Asha", "email");
    r.remind("Ravi", "sms");
    return 0;
}
```

```output
[Email] Asha, your book is due tomorrow.
[SMS] Ravi, your book is due tomorrow.
```

### What's wrong with this?

- **Violates Open/Closed:** every new channel means **editing** `ReminderService`.
- **Growing if-else chain:** creation logic and business logic are mixed together.
- **Tight coupling:** `ReminderService` must know every concrete kind of message.
- **Typos fail silently:** `remind("Neel", "SMS")` (capital S) does nothing.

We want the reminder logic to work with **any** kind of message, without knowing which concrete class is created.

## 2. Understanding Factory Method

> **GoF intent:** "Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses."

The base class has a **factory method** — a virtual function like `createReminder()` that returns a new object. The base class's other code calls it to get the object, **without knowing its concrete type**. Each subclass overrides the factory method to create a different concrete product.

:::analogy
A **logistics company** has a fixed process: plan → *get a vehicle* → load → deliver. The "get a vehicle" step varies: the **road** division gets a truck, the **sea** division gets a ship. Head office writes the process once; each division decides which vehicle to create.
:::

### Participants

```text
      ┌───────────────────────────────┐   creates   ┌─────────────────────┐
      │ ReminderService   (Creator)   │- - - - - - >│ Reminder (Product)  │
      │ + remind(name)                │             │ + send(msg) = 0     │
      │ # createReminder() = 0  ◄─────┼── factory   └──────────△──────────┘
      └───────────────△───────────────┘   method          ┌────┴─────────┐
            ┌─────────┴───────────┐                ┌──────────────┐ ┌─────────────┐
 ┌───────────────────────┐ ┌──────────────────────┐ │EmailReminder │ │ SmsReminder │
 │ EmailReminderService  │ │ SmsReminderService   │ └──────────────┘ └─────────────┘
 │  (ConcreteCreator)    │ │  (ConcreteCreator)   │  (ConcreteProducts)
 └───────────────────────┘ └──────────────────────┘
```

- **Product** — interface of the objects created (`Reminder`).
- **ConcreteProduct** — actual classes (`EmailReminder`, `SmsReminder`).
- **Creator** — declares the factory method and contains the code that uses the product (`ReminderService`).
- **ConcreteCreator** — overrides the factory method to return a specific product.

## 3. How It Works

1. Client calls `service.remind("Asha")` on some ReminderService.
2. `remind()` calls the **virtual** `createReminder()`.
3. Dynamic binding runs the **subclass's** version, which returns, say, an `EmailReminder`.
4. `remind()` uses it through the `Reminder` interface — it never names a concrete class.

## 4. Implementing It Step by Step

**Step 1 — the Product interface and concrete products. Step 2 — the Creator with the factory method. Step 3 — concrete creators. Step 4 — client code.**

```cpp
#include <iostream>
#include <string>
using namespace std;

// STEP 1: Product + ConcreteProducts
class Reminder
{
public:
    virtual void send(const string &msg) const = 0;
    virtual ~Reminder() { }
};
class EmailReminder : public Reminder
{
public:
    void send(const string &msg) const override { cout << "[Email] " << msg << endl; }
};
class SmsReminder : public Reminder
{
public:
    void send(const string &msg) const override { cout << "[SMS] " << msg << endl; }
};

// STEP 2: Creator with the FACTORY METHOD
class ReminderService
{
protected:
    virtual Reminder* createReminder() const = 0;    // factory method
public:
    void remind(const string &member) const          // fixed logic, uses ANY product
    {
        Reminder *r = createReminder();
        r->send(member + ", your book is due tomorrow.");
        delete r;
    }
    virtual ~ReminderService() { }
};

// STEP 3: ConcreteCreators decide WHICH product
class EmailReminderService : public ReminderService
{
protected:
    Reminder* createReminder() const override { return new EmailReminder(); }
};
class SmsReminderService : public ReminderService
{
protected:
    Reminder* createReminder() const override { return new SmsReminder(); }
};

// STEP 4: client code
int main()
{
    EmailReminderService email;
    SmsReminderService sms;
    ReminderService *services[2] = {&email, &sms};
    for (int i = 0; i < 2; i++) services[i]->remind("Asha");
    return 0;
}
```

```output
[Email] Asha, your book is due tomorrow.
[SMS] Asha, your book is due tomorrow.
```

Adding WhatsApp now means **adding two small classes** — `WhatsAppReminder` and `WhatsAppReminderService` — with **no edits** to existing code.

## 5. What We Gained

- **Open/Closed:** new products without modifying the creator's logic.
- **Low coupling:** `remind()` depends only on the `Reminder` interface.
- **Single responsibility:** creation is separated from use.
- **No string-based `if/else`** dispatch.
- *Cost:* one creator subclass per product type → more classes.

## When to Use It

- A class can't know in advance **which concrete class** it must create.
- You want **subclasses** to decide what gets created.
- You want to keep "how an object is used" separate from "which object is made".

:::note Larman's "Factory" ≠ Factory Method
Larman also uses a simpler, non-GoF **Factory** (also called *Simple/Concrete Factory*): one object whose only job is creating other objects — e.g. a `ServicesFactory` that reads a config file and returns the right adapter. It's a **Pure Fabrication**, often made a **Singleton**. Factory Method, by contrast, uses **subclass overriding**. Both appear in Lesson 14.8.
:::

:::key
- Factory Method: a virtual "create" method in the creator; subclasses decide the concrete product.
- Participants: Product, ConcreteProduct, Creator, ConcreteCreator.
- Gains: open/closed, low coupling, no type-switches. Cost: more classes.
:::

:::mistakes
- Calling Factory Method "structural" — it's **creational**.
- Making the creator's logic `switch` on type anyway (defeats the purpose).
- Confusing it with Larman's simple Factory object.
:::

:::exam
- *"Explain the Factory Method pattern with its structure and a C++ example."* → intent (word-for-word), problem, class diagram with 4 participants, code + output, consequences.
:::

:::def
**Factory Method** (creational): "Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses." Its participants are Product, ConcreteProduct, Creator (declaring the factory method) and ConcreteCreator (overriding it).
:::

## Quick Check

:::q Q1 · In the reminder example, which class is the Creator and which method is the factory method?
:::ans
Creator: **`ReminderService`**; factory method: **`createReminder()`**.
:::
:::

:::q Q2 · What must be added to support WhatsApp reminders?
:::ans
A `WhatsAppReminder` (ConcreteProduct) and a `WhatsAppReminderService` (ConcreteCreator) overriding `createReminder()`. No existing class changes.
:::
:::
