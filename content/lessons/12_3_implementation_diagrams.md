**Implementation diagrams describe how the software is organised and deployed: package diagrams group it logically, component diagrams show replaceable software parts and their interfaces, and deployment diagrams show what runs on which hardware.**

## The Problem: Big Systems Need a Bird's-Eye View

A real library system has hundreds of classes, separate modules (UI, loans, payments, database access), and runs on several machines (librarians' PCs, an application server, a database server). Class and sequence diagrams are too detailed to answer: *How is the code organised? Which parts can be swapped? What runs where?* Three diagrams answer exactly these questions.

:::analogy
Think of a company. The **package diagram** is the **organisation chart** (departments and who depends on whom). The **component diagram** is the **list of service desks** and what each offers/needs ("HR provides payroll, needs attendance data"). The **deployment diagram** is the **floor plan of offices** — which team sits in which building, connected by which roads.
:::

## 1. Package Diagrams

A **package** is a grouping of model elements (classes, use cases, other packages) — like a folder or a C++ `namespace`. A **package diagram** shows packages and the **dependencies** between them.

**Notation:** a **tabbed folder** with the package name; **dependency** = dashed arrow from the package that **uses** to the package **used**. Nested packages can be drawn inside. Full names use `::` — `Domain::Loans::Loan`.

**Typical use — layered architecture (Larman):**

```text
  ┌─────┐
  │ UI  │────────────────────────────┐     UI layer: windows, web pages, console menus
  ├─────┴──────────────────────────┐ │
  │  IssueBookPage  ReturnBookPage │ │
  └────────────────────────────────┘ │
                 ┆ depends on        │
                 ▼                   │
  ┌────────┐                         │
  │ Domain │────────────────────────┐│     Domain (application logic): Member, Loan, BookCopy,
  ├────────┴───────────────────────┐││     Catalog, IssueBookHandler ...
  │  Loans    Catalog    Payments  │││
  └────────────────────────────────┘││
                 ┆ depends on        │
                 ▼                   │
  ┌───────────────────┐              │
  │ Technical Services│─────────────┐│     persistence (database access), logging,
  ├───────────────────┴───────────┐ ││     security, email, payment adapters
  │ Persistence  Logging  Security│ ││
  └───────────────────────────────┘ ││
```

**Layering rules:** higher layers use lower layers, **never the reverse**; the domain layer contains no UI code (**model–view separation**).

**When to use package diagrams:** to show the **logical architecture** (layers, subsystems) of large systems; to **organise a big model** into manageable parts; to **control dependencies** (spot cycles or a domain package depending on UI); to plan team work and build order.

## 2. Component Diagrams

A **component** is a **modular, replaceable** part of a system that **encapsulates** its contents and is defined by the interfaces it **provides** and **requires**.

**Notation:**
- Component — rectangle with «component» (and a small two-tab icon).
- **Provided interface** — a **lollipop** (circle on a stick): services the component **offers**.
- **Required interface** — a **socket** (half-circle): services it **needs**.
- **Assembly connector** — a lollipop fitted into a socket: the provider satisfies the requirement.
- Ports (small squares on the edge), dependencies (dashed arrows).

```text
  ┌──────────────────┐                 ┌───────────────────────┐                 ┌─────────────────────┐
  │ «component»      │ ILoanService    │ «component»           │   IPayment      │ «component»         │
  │  Web UI          │──────(  O───────│  Loan Management      │──────(  O───────│  Payment Adapter    │
  └──────────────────┘ needs   provides└───────────────────────┘ needs  provides └─────────────────────┘
                       (socket)(lollipop)                                 (Payment Adapter can be replaced by
                                                                           any component providing IPayment)
```

**When to use component diagrams:** when the system is built from **replaceable, independently deployable parts** (libraries, services, plug-ins, microservices) and you want to show **which interfaces each part provides and requires** — e.g. "any payment provider can be plugged in as long as it provides `IPayment`". Less useful for small systems.

## 3. Deployment Diagrams

A **deployment diagram** shows the **physical architecture**: the **nodes** (hardware or software environments), the **artifacts** (actual files) deployed on them, and the **communication paths** between nodes.

**Notation:**
- **Node** — a 3-D box. Two kinds:
  - **Device node** — physical hardware with processing and memory («device» Server, PC, Phone).
  - **Execution environment node (EEN)** — software that runs inside a device and hosts other software («executionEnvironment» Web Server, JVM, Database Server, OS, Browser).
- **Artifact** — a concrete file: `lms.war`, `lms.exe`, `library.sql` («artifact»).
- **Communication path** — a line between nodes, labelled with the protocol (`«HTTPS»`, `«TCP/IP»`).

```text
     ┌──────────────────────┐            ┌────────────────────────────────┐            ┌──────────────────────────┐
    ╱                      ╱│           ╱                                ╱│           ╱                          ╱│
   ┌──────────────────────┐ │  «HTTPS»  ┌────────────────────────────────┐ │ «TCP/IP» ┌──────────────────────────┐ │
   │ «device»             │ │───────────│ «device» App Server            │ │──────────│ «device» DB Server       │ │
   │ Librarian PC         │ │           │ «executionEnvironment» Tomcat  │ │          │ «executionEnvironment»   │ │
   │ «executionEnv.»      │ │           │   «artifact» lms.war           │ │          │   MySQL                  │ │
   │  Web Browser         │╱            │                                │╱           │   «artifact» library.sql │╱
   └──────────────────────┘             └────────────────────────────────┘            └──────────────────────────┘
```

**When to use deployment diagrams:** to show **how and where** a system is deployed (distributed, client–server, cloud); to plan installation, performance, scalability and security; to communicate with operations/infrastructure teams. Not needed for a single-machine program.

## Comparison

| Package diagram | Component diagram | Deployment diagram |
|---|---|---|
| **Logical** grouping of model elements/code | **Replaceable software parts** and their interfaces | **Physical** hardware/environments and deployed files |
| Packages + dependencies | Components, provided (lollipop) / required (socket) interfaces | Device & execution-environment nodes, artifacts, communication paths |
| "How is the code organised and layered?" | "What are the pluggable parts and how are they wired?" | "What runs where?" |

:::key
- Package diagram: folders + dashed dependency arrows; logical architecture/layers.
- Component diagram: replaceable parts; lollipop = provided, socket = required interface.
- Deployment diagram: device nodes, execution-environment nodes, artifacts, communication paths.
:::

:::mistakes
- Confusing a **component** (logical software unit) with an **artifact** (physical file).
- Confusing a **device node** (hardware) with an **execution environment node** (software platform).
- Swapping lollipop (provided) and socket (required).
- Dependencies pointing upward from lower layers to the UI.
:::

:::exam
- *"Explain package, component and deployment diagrams with notation and examples. When is each used?"* (Often one long question.)
- *"Draw a deployment diagram for a web application."*
:::

:::def
A **package diagram** shows how model elements are organised into packages and the dependencies between packages. A **component diagram** shows the components of a system — modular, replaceable units defined by provided and required interfaces — and their connections. A **deployment diagram** shows the physical architecture: nodes (devices and execution environments), the artifacts deployed on them, and the communication paths between nodes.
:::

## Quick Check

:::q Q1 · Which diagram answers: "Is the MySQL database on the same machine as the web server?"
:::ans
The **deployment diagram**.
:::
:::

:::q Q2 · Is a Java Virtual Machine a device node or an execution environment node?
:::ans
An **execution environment node** — it is software that runs inside a device and hosts other software.
:::
:::
