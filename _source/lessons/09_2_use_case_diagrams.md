**A use case diagram is a one-page picture of the system's boundary, its actors and its use cases. Use cases can be related by «include», «extend» and generalization to avoid repetition.**

## The Problem: Seeing the Whole System at a Glance

Twenty written use cases are detailed, but nobody can see the big picture from them: *Which actors use what? What's inside the system and what's outside?* A **use case diagram** gives that overview — like a table of contents for the requirements.

## Notation

<<SVG:usecase>>

| Element | Symbol | Meaning |
|---|---|---|
| **Actor** | stick figure (or a box marked «actor» for systems) | someone/something outside that interacts |
| **Use case** | oval with a verb-noun name | a goal the system fulfils |
| **System boundary** | rectangle with the system's name | what's inside the system |
| **Association** | solid line actor — use case | the actor takes part in the use case |
| **«include»** | dashed arrow, base → included | always uses that common behaviour |
| **«extend»** | dashed arrow, extension → base | optionally adds behaviour |
| **Generalization** | solid line + hollow triangle → parent | a specialized version |

Primary actors are usually drawn on the **left**, supporting (system) actors on the **right**.

## Relating Use Cases

### The problem they solve

Both *Issue Book* and *Renew Book* start by validating the member (check ID, membership expiry, fine limit). Writing those steps in both use cases duplicates text — and every change must be made twice. And *Pay Fine* only happens *sometimes* during *Return Book*. UML provides three relationships for these situations.

### 1. «include» — mandatory, shared behaviour

The **base** use case **always** runs the **included** use case at some point — like calling a function. Used to **factor out common steps** shared by several use cases.

```text
 ( Issue Book ) - - - «include» - - ->  ( Validate Member )
 ( Renew Book ) - - - «include» - - ->  ( Validate Member )
      base                                    included
```

Arrow: dashed, **from the base to the included** use case.

### 2. «extend» — optional, conditional behaviour

The **extending** use case **may** add behaviour to the base at a named **extension point**, **under a condition**. The base use case is complete without it and **doesn't even know** about it.

```text
 ( Pay Fine ) - - - «extend» - - ->  ( Return Book )
   extending                           base      extension point: "after scanning"
                                                 condition: [copy is overdue]
```

Arrow: dashed, **from the extending use case to the base**.

### 3. Generalization — "a special kind of"

A **child** use case is a specialized version of a **parent** use case. Actors can be generalized too.

```text
 ( Pay Fine by Card ) ─────▷ ( Pay Fine )           Librarian ─────▷ Staff
 ( Pay Fine by UPI )  ─────▷                        Admin     ─────▷
```

:::analogy
- **«include»** is like **"wash hands"** in every recipe: every recipe *always* includes it, so you write it once and refer to it.
- **«extend»** is like **"add extra cheese (if the customer asks)"** on a pizza order: optional, conditional, and the basic pizza recipe is complete without it.
- **Generalization** is like **"payment"** and its kinds **card payment / cash payment**: special versions of the same general goal.
:::

| | «include» | «extend» | Generalization |
|---|---|---|---|
| Meaning | base **always** uses it | extension **may** add to base | child is a kind of parent |
| Optional? | no (mandatory) | yes (conditional) | — |
| Arrow direction | base → included | **extension → base** | child → parent |
| Line | dashed + «include» | dashed + «extend» | solid + hollow triangle |
| Does base know the other? | yes | **no** | — |
| Base complete alone? | no | yes | — |
| Like… | a function call | a plug-in / optional add-on | inheritance |

**Larman's advice:** use «include» when steps are repeated in several use cases; use «extend» when you **can't modify** the base text (otherwise just add an extension inside the base use case); and **don't spend much time** on relationships — the written text is what matters.

Terms: a **concrete** use case is started by an actor (*Issue Book*); an **abstract** one never runs alone (*Validate Member*). The **base** use case is the one that includes or is extended; the **addition** use case is the included/extending one.

## When to Draw Use Case Diagrams

- At the start, to show **system scope** and **who uses what** (a context diagram).
- To communicate with stakeholders who won't read all the text.
- Not as a replacement for written use cases, and **not** to show order or flow of steps (use activity/sequence diagrams for that).

:::key
- Diagram = actors + use cases + system boundary + associations.
- «include»: mandatory, common behaviour; arrow base → included.
- «extend»: optional/conditional; arrow extension → base; base doesn't know about it.
- Generalization: child ▷ parent (use cases or actors).
- The diagram is an overview; the text is the real use case.
:::

:::mistakes
- **Arrow directions** — the #1 error. «include» points to the included; «extend» points to the base.
- Using «extend» for mandatory behaviour or «include» for optional behaviour.
- Drawing arrows to show the *sequence* of use cases — use case diagrams show no order.
- Connecting two actors to each other or two use cases with a plain line.
- Putting actors inside the system boundary.
:::

:::exam
- *"Draw a use case diagram for an ATM / library / online shopping / hospital system."* — include ≥1 «include» and ≥1 «extend», a boundary, primary and supporting actors.
- *"Differentiate include, extend and generalization."* → the table.
:::

:::def
A **use case diagram** shows the actors, the use cases and their relationships within a system boundary. An **«include»** relationship means the base use case always incorporates the behaviour of the included use case; an **«extend»** relationship means the extending use case optionally adds behaviour to the base use case at an extension point under a condition; **generalization** means a child use case (or actor) is a specialization of a parent.
:::

## Quick Check

:::q Q1 · *Place Order* always requires *Verify Payment*. Include or extend? Draw the arrow direction.
:::ans
**«include»** — mandatory. `( Place Order ) - - «include» - -> ( Verify Payment )`.
:::
:::

:::q Q2 · *Apply Coupon* happens only if the customer has a coupon during *Checkout*. Include or extend? Arrow direction?
:::ans
**«extend»** — optional. `( Apply Coupon ) - - «extend» - -> ( Checkout )`.
:::
:::
