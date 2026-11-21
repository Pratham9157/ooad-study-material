**The Adapter pattern (structural) lets two classes with incompatible interfaces work together, by putting a "translator" object between them.**

What varies: **the external class's interface**. What stays the same: **the interface our code expects**.

## 1. The Problem: A Third-Party API That Doesn't Fit

Our library code collects fines through a simple interface it expects: `pay(rupees) → true/false`. The payment company we signed up with provides a library we **cannot change**:

```text
class QuickPayAPI {
    int makeTxn(long paise, string currency);   // amount in PAISE, returns a status CODE (200 = OK)
};
```

Different method name, different units (paise vs rupees), different result type (code vs bool). If we call `QuickPayAPI` directly all over our code:
- every caller must convert rupees → paise and codes → bool (**duplication**),
- our domain code becomes **tightly coupled** to one vendor,
- switching to another provider means **editing every call site**.

## 2. Understanding Adapter

> **GoF intent:** "Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces." (Also known as **Wrapper**.)

:::analogy
A **travel plug adapter**. Your Indian charger (client) expects a round-pin socket (target interface); the UK wall socket (adaptee) is different. The adapter in between converts one to the other — **neither the charger nor the wall changes**.
:::

### Participants

```text
 ┌──────────────┐  uses  ┌──────────────────────────┐            ┌──────────────────────────────────┐
 │ FineCollector│───────►│ «interface»              │            │ QuickPayAPI       (Adaptee)      │
 │   (Client)   │        │ PaymentGateway (Target)  │            │ + makeTxn(paise, currency) : int │
 └──────────────┘        │ + pay(rupees) : bool     │            └──────────────────────────────────┘
                         └────────────△─────────────┘                          ▲
                                      ┆ implements                             │ delegates to
                         ┌────────────┴─────────────┐                          │
                         │ QuickPayAdapter (Adapter)│──────────────────────────┘
                         │ + pay(rupees) : bool     │   converts rupees→paise, code→bool
                         └──────────────────────────┘
```

- **Target** — the interface the client expects (`PaymentGateway`).
- **Client** — uses only the Target (`FineCollector`).
- **Adaptee** — the existing class with the incompatible interface (`QuickPayAPI`).
- **Adapter** — implements Target by calling the Adaptee and translating (`QuickPayAdapter`).

## 3. How It Works

1. The client calls `gateway.pay(35.50)` on the Target interface.
2. The adapter receives it, converts 35.50 rupees → 3550 paise.
3. It calls `api.makeTxn(3550, "INR")` on the adaptee.
4. It converts the result code 200 → `true` and returns it.

## 4. Implementation

```cpp
#include <iostream>
#include <string>
using namespace std;

class QuickPayAPI                                   // ADAPTEE: third-party, can't change it
{
public:
    int makeTxn(long paise, const string &currency) const
    {
        cout << "QuickPay: charging " << paise << " paise in " << currency << endl;
        return 200;                                 // 200 = success
    }
};

class PaymentGateway                                // TARGET: what our code expects
{
public:
    virtual bool pay(double rupees) = 0;
    virtual ~PaymentGateway() { }
};

class QuickPayAdapter : public PaymentGateway       // ADAPTER
{
    QuickPayAPI api;                                // wraps the adaptee (object adapter)
public:
    bool pay(double rupees) override
    {
        long paise = static_cast<long>(rupees * 100 + 0.5);   // translate the units
        return api.makeTxn(paise, "INR") == 200;              // translate the result
    }
};

class FineCollector                                 // CLIENT: knows only the Target
{
    PaymentGateway &gateway;
public:
    FineCollector(PaymentGateway &g) : gateway(g) { }
    void collect(double amount)
    {
        cout << (gateway.pay(amount) ? "Fine paid" : "Payment failed") << endl;
    }
};

int main()
{
    QuickPayAdapter adapter;
    FineCollector collector(adapter);
    collector.collect(35.50);
    return 0;
}
```

```output
QuickPay: charging 3550 paise in INR
Fine paid
```

Switching to another provider = writing one new adapter class. `FineCollector` never changes.

### Object adapter vs class adapter

| Object adapter (used above) | Class adapter |
|---|---|
| Adapter **contains** an adaptee object (composition) | Adapter **inherits** from both Target and Adaptee (multiple inheritance) |
| Works with the adaptee and its subclasses | Tied to one concrete adaptee class |
| More flexible — preferred | Can override adaptee behaviour directly |

## 5. What We Gained

- **Reuse** of existing/third-party classes without modifying them.
- **Low coupling / Protected Variations:** the domain depends only on `PaymentGateway`.
- **Single place** for conversion logic.
- GRASP view: Adapter = **Indirection** + **Polymorphism** + **Protected Variations**.

## When to Use It

- You want to use an existing class whose interface doesn't match what you need.
- You integrate **third-party or legacy** code (Larman: adapters for external tax calculators, accounting and payment systems).
- You want several similar services behind **one** stable interface.

:::key
- Adapter converts one interface into the one clients expect; neither side changes.
- Participants: Target, Client, Adaptee, Adapter. Object adapter (composition) is preferred.
- Use for third-party/legacy integration.
:::

:::mistakes
- Modifying the adaptee instead of wrapping it.
- Confusing Adapter with Bridge (see the table in Lesson 14.5).
- Letting the client still call the adaptee directly in some places.
:::

:::exam
- *"Explain the Adapter pattern with structure, participants and an example."* → intent, plug analogy, class diagram, code + output, object vs class adapter.
:::

:::def
**Adapter** (structural): "Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces." Participants: Target, Client, Adaptee and Adapter.
:::

## Quick Check

:::q Q1 · Identify Target, Adaptee and Adapter: our code expects `Thermometer::getCelsius()`; the sensor library offers `FahrenheitSensor::readF()`; we write `SensorAdapter`.
:::ans
Target: **Thermometer**; Adaptee: **FahrenheitSensor**; Adapter: **SensorAdapter** (implements `getCelsius()` as `(readF() - 32) * 5 / 9`).
:::
:::
