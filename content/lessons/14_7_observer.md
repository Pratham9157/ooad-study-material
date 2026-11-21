**The Observer pattern (behavioural) lets many objects "subscribe" to one object; whenever that object changes, it automatically notifies all its subscribers.**

What varies: **who is interested and how they react**. What stays the same: **the object being watched**.

## 1. The Problem: "Tell Everyone Who Cares"

When a copy of *Clean Code* is returned, several things should happen: members on the waiting list get notified, the lobby display updates its "available now" count, maybe the mobile app refreshes. A first attempt:

```cpp
#include <iostream>
using namespace std;

class LobbyDisplay { public: void refresh(int n) { cout << "  [Display] " << n << " on shelf" << endl; } };
class Mailer       { public: void tellAsha()      { cout << "  Mail to Asha: available" << endl; } };

class BookTitle
{
    int available = 0;
    LobbyDisplay &display;       // the book must know EVERY interested class...
    Mailer &mailer;
public:
    BookTitle(LobbyDisplay &d, Mailer &m) : display(d), mailer(m) { }
    void returnCopy()
    {
        available++;
        display.refresh(available);   // ...and call each one by hand
        mailer.tellAsha();            // add an app notifier? edit this class again
    }
};

int main()
{
    LobbyDisplay d; Mailer m;
    BookTitle book(d, m);
    book.returnCopy();
    return 0;
}
```

```output
  [Display] 1 on shelf
  Mail to Asha: available
```

### What's wrong with this?

- **Tight coupling:** `BookTitle` (a domain class) depends on UI and mail classes.
- **Not extensible:** every new interested party means editing `BookTitle`.
- **Fixed at compile time:** members can't start or stop "watching" a book while the program runs.

## 2. Understanding Observer

> **GoF intent:** "Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically." (Also known as **Publish–Subscribe** or **Dependents**.)

:::analogy
**YouTube subscriptions.** A channel (the subject) doesn't know or care what each subscriber does with a new video. When it uploads, it simply notifies **all current subscribers**. Anyone can subscribe or unsubscribe at any time, and the channel never changes its code for a new subscriber.
:::

### Participants

```text
 ┌──────────────────────────────┐ observers    ┌────────────────────────────┐
 │ BookTitle  (Subject)         │◇────────────►│ Observer  (interface)      │
 │ - observers : vector<Obs*>   │ 0..*         │ + update(title, copies) = 0│
 │ + attach(o) / detach(o)      │              └─────────────△──────────────┘
 │ + returnCopy()               │                     ┌──────┴────────────┐
 │ - notifyAll() ── for each o: │              ┌──────────────┐  ┌──────────────┐
 │                  o->update() │              │WaitingMember │  │ LobbyDisplay │
 └──────────────────────────────┘              └──────────────┘  └──────────────┘
                                                  (Concrete Observers)
```

- **Subject** — keeps a list of observers; provides `attach`, `detach`, and `notify` (`BookTitle`).
- **Observer** — an interface with an `update()` method.
- **Concrete Observers** — react to updates in their own way (`WaitingMember`, `LobbyDisplay`).

## 3. How It Works

1. Observers **attach** (subscribe) to the subject.
2. The subject's state changes (a copy is returned).
3. The subject calls `notifyAll()`, which calls `update()` on **every** attached observer.
4. Each observer reacts in its own way. Observers can **detach** at any time.

## 4. Implementation

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Observer                                        // OBSERVER interface
{
public:
    virtual void update(const string &title, int copies) = 0;
    virtual ~Observer() { }
};

class BookTitle                                       // SUBJECT
{
    string title;
    int available = 0;
    vector<Observer*> observers;                      // knows observers ONLY through the interface
    void notifyAll()
    {
        for (Observer *o : observers) o->update(title, available);
    }
public:
    BookTitle(const string &t) : title(t) { }
    void attach(Observer *o) { observers.push_back(o); }
    void detach(Observer *o)
    {
        for (int i = 0; i < (int)observers.size(); i++)
            if (observers[i] == o) { observers.erase(observers.begin() + i); break; }
    }
    void returnCopy() { available++; notifyAll(); }   // state change → notify everyone
};

class WaitingMember : public Observer                 // CONCRETE OBSERVER
{
    string name;
public:
    WaitingMember(const string &n) : name(n) { }
    void update(const string &title, int copies) override
    {
        cout << "  " << name << ": '" << title << "' is available (" << copies << " copy)" << endl;
    }
};

class LobbyDisplay : public Observer                  // a completely different kind of observer
{
public:
    void update(const string &title, int copies) override
    {
        cout << "  [Display] " << title << " -> " << copies << " on shelf" << endl;
    }
};

int main()
{
    BookTitle book("Clean Code");
    WaitingMember asha("Asha"), ravi("Ravi");
    LobbyDisplay screen;
    book.attach(&asha); book.attach(&ravi); book.attach(&screen);

    cout << "Copy returned:" << endl;
    book.returnCopy();
    book.detach(&asha);                                // Asha unsubscribes
    cout << "Another copy returned:" << endl;
    book.returnCopy();
    return 0;
}
```

```output
Copy returned:
  Asha: 'Clean Code' is available (1 copy)
  Ravi: 'Clean Code' is available (1 copy)
  [Display] Clean Code -> 1 on shelf
Another copy returned:
  Ravi: 'Clean Code' is available (2 copy)
  [Display] Clean Code -> 2 on shelf
```

## 5. What We Gained

- **Loose coupling:** the subject only knows the `Observer` interface — not displays, mailers or apps.
- **Open/Closed:** new kinds of observers need no change to the subject.
- **Dynamic subscriptions:** attach/detach at run time.
- **Broadcast:** one change → all interested objects informed.
- *Costs:* observers may receive many/unexpected updates; update order isn't guaranteed by design; observers must detach before being destroyed (dangling pointers).

## When to Use It

- A change in one object must be reflected in **others**, and you don't know in advance how many or which.
- **Model–view separation** (Larman): when a `Sale`'s total changes, UI windows refresh — but the domain `Sale` must not depend on UI classes.
- Event systems, notifications, pub-sub messaging, spreadsheets updating charts.

:::key
- Observer = one-to-many notification; subject keeps observers and calls `update()` on all.
- Participants: Subject (attach/detach/notify), Observer interface (update), Concrete Observers.
- Loose coupling, dynamic subscriptions; used for model–view separation.
:::

:::mistakes
- Letting the subject depend on **concrete** observer classes (defeats the purpose).
- Calling Observer "creational" or "structural" — it's **behavioural**.
- Forgetting `detach` before an observer object is destroyed.
:::

:::exam
- *"Explain the Observer pattern with structure and a C++ example."* → intent, problem, YouTube analogy, class diagram, code + output, consequences.
- *Identify the pattern* from code that keeps a `vector` of listeners and calls them on change.
:::

:::def
**Observer** (behavioural): "Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically." Participants: Subject (attach, detach, notify), Observer (update interface), ConcreteSubject and ConcreteObserver. Also known as Publish–Subscribe.
:::

## Quick Check

:::q Q1 · A weather station must update a phone app, a website and an LED board whenever readings change. Which pattern? Name the subject and observers.
:::ans
**Observer.** Subject: `WeatherStation`. Observers: `PhoneApp`, `Website`, `LedBoard` (all implementing `update()`).
:::
:::
