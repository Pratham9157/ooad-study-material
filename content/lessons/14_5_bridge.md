**The Bridge pattern (structural) splits one class hierarchy into two independent ones — the *abstraction* and the *implementation* — connected by a reference (the "bridge"), so each can grow without multiplying classes.**

What varies: **two independent dimensions** (here: *kind of notice* and *delivery channel*).

## 1. The Problem: Class Explosion

The library sends two kinds of notices — **Reminder** and **OverdueNotice** — through two channels — **Email** and **SMS**. Using inheritance alone:

```text
                    Notice
        ┌──────────┬─────┴──────┬────────────────┐
  EmailReminder  SmsReminder  EmailOverdueNotice  SmsOverdueNotice     ← 2 × 2 = 4 classes
```

Add WhatsApp → 6 classes. Add a "Welcome" notice → 9. With *m* notice types and *n* channels you need **m × n** classes, and the channel-sending code is duplicated in every one.

### What's wrong with this?

- **Class explosion** (m × n).
- **Duplication:** "how to send an SMS" is copied into every SMS class.
- **Rigid:** a notice is permanently tied to one channel at compile time.

## 2. Understanding Bridge

> **GoF intent:** "Decouple an abstraction from its implementation so that the two can vary independently."

Split the two dimensions into **two hierarchies**: the *Notice* hierarchy (**abstraction** — *what* to say) and the *Channel* hierarchy (**implementation** — *how* to deliver). Each notice **holds a reference** to a channel — that reference is the "bridge". Now you need **m + n** classes.

:::analogy
A **TV remote and a TV**. Remotes (basic remote, advanced remote with voice) are one hierarchy; TVs (Sony, Samsung) are another. Any remote can work with any TV through the infrared "bridge". You don't need a "SonyBasicRemote", "SamsungVoiceRemote", … for every combination.
:::

### Participants

```text
        Abstraction side                                       Implementation side
 ┌────────────────────────────┐   channel  (the "bridge")   ┌──────────────────────────┐
 │ Notice   (Abstraction)     │◇───────────────────────────►│ Channel  (Implementor)   │
 │ # channel : Channel&       │                              │ + deliver(to, text) = 0  │
 │ + send(member) = 0         │                              └────────────△─────────────┘
 └─────────────△──────────────┘                                    ┌──────┴────────┐
        ┌──────┴─────────┐                                 ┌──────────────┐ ┌────────────┐
 ┌─────────────┐ ┌──────────────┐                          │ EmailChannel │ │ SmsChannel │
 │ Reminder    │ │ OverdueNotice│  (Refined Abstractions)  └──────────────┘ └────────────┘
 └─────────────┘ └──────────────┘                          (Concrete Implementors)
```

- **Abstraction** — high-level interface; holds a reference to an Implementor (`Notice`).
- **Refined Abstraction** — variants of the abstraction (`Reminder`, `OverdueNotice`).
- **Implementor** — interface for the low-level operations (`Channel::deliver`).
- **Concrete Implementor** — actual implementations (`EmailChannel`, `SmsChannel`).

## 3. Implementation

```cpp
#include <iostream>
#include <string>
using namespace std;

class Channel                                        // IMPLEMENTOR
{
public:
    virtual void deliver(const string &to, const string &text) const = 0;
    virtual ~Channel() { }
};
class EmailChannel : public Channel                  // CONCRETE IMPLEMENTOR
{
public:
    void deliver(const string &to, const string &text) const override
    { cout << "Email to " << to << ": " << text << endl; }
};
class SmsChannel : public Channel                    // CONCRETE IMPLEMENTOR
{
public:
    void deliver(const string &to, const string &text) const override
    { cout << "SMS to " << to << ": " << text << endl; }
};

class Notice                                         // ABSTRACTION
{
protected:
    const Channel &channel;                          // ← the bridge
public:
    Notice(const Channel &c) : channel(c) { }
    virtual void send(const string &member) const = 0;
    virtual ~Notice() { }
};
class Reminder : public Notice                       // REFINED ABSTRACTION
{
public:
    Reminder(const Channel &c) : Notice(c) { }
    void send(const string &member) const override { channel.deliver(member, "Book due tomorrow"); }
};
class OverdueNotice : public Notice                  // REFINED ABSTRACTION
{
    int days;
public:
    OverdueNotice(const Channel &c, int d) : Notice(c), days(d) { }
    void send(const string &member) const override
    { channel.deliver(member, "Overdue by " + to_string(days) + " days, fine Rs " + to_string(days * 5)); }
};

int main()
{
    EmailChannel email;
    SmsChannel sms;
    Reminder r1(email), r2(sms);         // any notice works with any channel
    OverdueNotice o1(sms, 3);
    r1.send("Asha");
    r2.send("Ravi");
    o1.send("Meena");
    return 0;
}
```

```output
Email to Asha: Book due tomorrow
SMS to Ravi: Book due tomorrow
SMS to Meena: Overdue by 3 days, fine Rs 15
```

Adding WhatsApp = **one** new `Channel` class; adding a Welcome notice = **one** new `Notice` class.

## 4. What We Gained

- **m + n** classes instead of **m × n**.
- Abstraction and implementation **vary independently**.
- The implementation can be **chosen or switched at run time**.
- Implementation details are hidden from clients.
- Applies **"favour composition over inheritance"**.

## Adapter vs Bridge (A Favourite Question)

| Adapter | Bridge |
|---|---|
| Makes **existing, incompatible** interfaces work together | Separates abstraction from implementation **by design** |
| Applied **after** the classes exist (a retrofit) | Applied **up-front**, while designing |
| Usually wraps one adaptee for one target | Two hierarchies that **vary independently** |
| Intent: **interface conversion** | Intent: **independent variation**, avoid class explosion |

## When to Use It

- A class varies along **two (or more) independent dimensions**.
- You want to switch implementations at run time.
- You want to avoid a permanent compile-time binding between abstraction and implementation.

:::key
- Bridge = abstraction hierarchy + implementation hierarchy, linked by composition.
- Participants: Abstraction, Refined Abstraction, Implementor, Concrete Implementor.
- Solves m × n class explosion; designed in up-front (unlike Adapter).
:::

:::mistakes
- Confusing Bridge with Adapter (see table).
- Thinking "implementation" means C++ implementation code — here it means the **low-level platform-specific side** (channels).
:::

:::exam
- *"Explain the Bridge pattern with structure and an example."*
- *"Differentiate Adapter and Bridge."*
:::

:::def
**Bridge** (structural): "Decouple an abstraction from its implementation so that the two can vary independently." The abstraction holds a reference to an implementor interface; refined abstractions and concrete implementors can be extended independently.
:::

## Quick Check

:::q Q1 · Shapes (Circle, Square) must be drawn with two rendering engines (OpenGL, DirectX). Without Bridge, how many classes? With Bridge?
:::ans
Without Bridge: one class per combination — 2 × 2 = **4** (`OpenGLCircle`, `DirectXCircle`, `OpenGLSquare`, `DirectXSquare`). With Bridge: 2 shape classes + 2 renderer classes = **4** as well — the same today, but growth differs: with 3 shapes and 3 renderers it's **9** classes without Bridge versus **6** with it (m × n vs m + n).
:::
:::
