**A stream is a flow of characters between your program and a device. Formatting tools (manipulators) control *how* values appear when they flow out — width, decimal places, alignment and so on.**

## The Problem: Messy Output

Print a marks table with plain `cout` and you get:

```text
Asha 91.5
Bharat 78.36
Chirag 66
```

Columns don't line up, decimals are inconsistent (`91.5`, `78.36`, `66`). Reports, bills and tables need **neat, controlled formatting**.

## Understanding Streams

A **stream** is a sequence of bytes flowing between the program and a device. The great thing about streams: **the same operators work for every device** — writing to a file looks exactly like writing to the screen (Lesson 6.3).

:::analogy
A stream is a **conveyor belt**. Whether it leads to the screen, a file or a printer, you put items on it the same way (`<<`). Formatting is like the packing rules at the start of the belt: "every box must be 10 cm wide", "write prices with 2 decimals".
:::

### The stream class hierarchy

```text
                      ios_base
                         │
                        ios            (format settings, error flags)
                  ┌──────┴──────┐
              istream        ostream
              (cin, >>)     (cout, cerr, clog, <<)
               │    └───┬───┘     │
               │     iostream     │
           ifstream     │      ofstream        <fstream>: file streams
                     fstream
```

| Predefined stream | Connected to | Buffered? |
|---|---|---|
| `cin` | keyboard (standard input) | yes |
| `cout` | screen (standard output) | yes |
| `cerr` | screen (standard error) | **no** — appears immediately |
| `clog` | screen (standard error) | yes |

## Formatting with Manipulators

Manipulators are inserted into the stream like values. The ones with arguments need `#include <iomanip>`.

| Manipulator | Effect | Stays in effect? |
|---|---|---|
| `setw(n)` | minimum field **width** n for the **next item only** | ❌ **no** |
| `setfill(c)` | character used for padding (default space) | ✅ yes |
| `setprecision(n)` | without `fixed`: n **significant digits**; with `fixed`: n digits **after the decimal point** | ✅ yes |
| `fixed` | normal decimal notation (`123.456000`) | ✅ yes |
| `scientific` | exponent notation (`1.23e+02`) | ✅ yes |
| `left` / `right` | alignment inside the field | ✅ yes |
| `showpoint` | always show the decimal point | ✅ yes |
| `boolalpha` | print `true`/`false` instead of `1`/`0` | ✅ yes |
| `hex` / `oct` / `dec` | number base | ✅ yes |
| `endl` | new line + flush | — |

Default precision is **6 significant digits**.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    double pi = 3.14159265, big = 1234.5678;
    cout << pi << " " << big << endl;                              // default: 6 significant digits
    cout << setprecision(3) << pi << " " << big << endl;           // 3 significant digits
    cout << fixed << setprecision(2) << pi << " " << big << endl;  // 2 digits after the point
    cout.unsetf(ios::floatfield); cout << setprecision(6);         // back to defaults

    cout << "[" << setw(6) << 42 << "]" << "[" << 42 << "]" << endl;   // setw affects ONE item
    cout << "[" << left << setw(6) << 42 << "]" << endl;
    cout << right << setfill('*') << setw(6) << 42 << endl;
    cout << setfill(' ');

    cout << boolalpha << true << " " << (3 > 5) << noboolalpha << endl;
    cout << hex << 255 << " " << oct << 8 << " " << dec << 255 << endl;
    return 0;
}
```

```output
3.14159 1234.57
3.14 1.23e+03
3.14 1234.57
[    42][42]
[42    ]
****42
true false
ff 10 255
```

Look at line 2: with 3 significant digits and no `fixed`, 1234.5678 can't fit, so C++ switches to scientific `1.23e+03`. That's a classic trick question.

## A Neat Table

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    const char *names[3] = {"Asha", "Bharat", "Chirag"};
    double marks[3] = {91.5, 78.36, 66};

    cout << left << setw(10) << "Name" << right << setw(8) << "Marks" << endl;
    cout << fixed << setprecision(1);
    for (int i = 0; i < 3; i++)
        cout << left << setw(10) << names[i] << right << setw(8) << marks[i] << endl;
    return 0;
}
```

```output
Name         Marks
Asha          91.5
Bharat        78.4
Chirag        66.0
```

## The Same with ios Member Functions

| Member function | Same as |
|---|---|
| `cout.width(n)` | `setw(n)` |
| `cout.precision(n)` | `setprecision(n)` |
| `cout.fill(c)` | `setfill(c)` |
| `cout.setf(ios::fixed, ios::floatfield)` | `fixed` |
| `cout.setf(ios::left, ios::adjustfield)` | `left` |
| `cout.unsetf(flag)` | turn a flag off |

```cpp
#include <iostream>
using namespace std;

int main()
{
    cout.setf(ios::fixed, ios::floatfield);
    cout.precision(2);
    cout.fill('.');
    cout.setf(ios::left, ios::adjustfield);
    cout.width(10); cout << "Apple";  cout << 45.5 << endl;
    cout.width(10); cout << "Banana"; cout << 7.25 << endl;
    return 0;
}
```

```output
Apple.....45.50
Banana....7.25
```

:::key
- Stream = byte flow; same operators for every device. `cerr` is unbuffered.
- `setw` affects only the next item; everything else is sticky.
- `setprecision`: significant digits normally, decimal places with `fixed`.
- Manipulators (`<iomanip>`) and `ios` member functions do the same jobs.
:::

:::mistakes
- Expecting `setw` to apply to every following item.
- Forgetting `#include <iomanip>`.
- Confusing the two meanings of `setprecision`.
- Thinking `setw` cuts long values — it never truncates, only pads.
:::

:::exam
- *"Explain formatted output using manipulators/ios functions with a program."*
- *Predict the output* with `setw`, `setfill`, `setprecision`, `fixed`.
- *"Explain the stream class hierarchy."*
:::

:::def
A **stream** is a sequence of bytes that flows between a program and an input or output device. **Manipulators** are special functions (such as `setw`, `setprecision`, `setfill`, `fixed`, `left`) inserted into a stream to control the format of input/output.
:::

## Quick Check

:::q Q1 · What is printed? `cout << setw(5) << 7 << 8;`
:::ans
`    78` — four spaces then `7` (width 5), then `8` with no padding (setw was used up).
:::
:::

:::q Q2 · `cout << fixed << setprecision(2) << 3.14159;` vs `cout << setprecision(2) << 3.14159;`?
:::ans
`3.14` (2 decimal places) vs `3.1` (2 significant digits).
:::
:::
