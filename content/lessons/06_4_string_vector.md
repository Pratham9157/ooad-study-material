**The C++ Standard Library gives you ready-made classes. Two you'll use everywhere are `string` (easy, safe text) and `vector` (an array that can grow).** They're also perfect examples of the OOP ideas you've learned.

## The Problem: C-Strings and Arrays Are Painful

- `char name[20]` — what if the name is 25 characters? Overflow. Joining two names needs `strcat`; comparing needs `strcmp`; and `a == b` compares *addresses*, not text!
- `int marks[60]` — what if there are 75 students? The size is fixed; you can't add more.

The standard classes solve these: they **manage their own memory** (constructors/destructors), **grow automatically**, and use **overloaded operators** (`+`, `==`, `[]`) so code reads naturally.

:::analogy
A C-string/array is a **fixed-size box** — if things don't fit, too bad. `string` and `vector` are like an **expandable suitcase**: put more in and it grows; it also tells you how much is inside and keeps itself tidy.
:::

## The string Class

```cpp
#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s = "Object";
    string t = "Oriented";
    string full = s + " " + t;               // + joins strings (overloaded operator)
    cout << full << " (" << full.length() << " chars)" << endl;

    cout << full.substr(7, 3) << endl;       // 3 chars starting at index 7
    cout << full.find("Ori") << endl;        // index of the first match
    cout << (full.find("xyz") == string::npos ? "not found" : "found") << endl;

    full.replace(0, 6, "Subject");           // replace 6 chars from index 0
    cout << full << endl;
    cout << (s == "Object") << " " << full[0] << endl;   // == compares TEXT; [] gives a char
    cout << stoi("125") + 5 << " " << to_string(3) + "D" << endl;   // conversions
    return 0;
}
```

```output
Object Oriented (15 chars)
Ori
7
not found
Subject Oriented
1 S
130 3D
```

| Operation | Example |
|---|---|
| length | `s.length()` or `s.size()` |
| join | `s + t`, `s += "!"`, `s.append(t)` |
| compare | `s == t`, `s < t`, `s.compare(t)` |
| access | `s[i]`, `s.at(i)` (`at` checks the bounds) |
| part of it | `s.substr(pos, len)` |
| search | `s.find(x)` → index or `string::npos` |
| edit | `insert(pos, x)`, `erase(pos, len)`, `replace(pos, len, x)` |
| other | `empty()`, `clear()`, `c_str()`, `stoi()`, `to_string()` |

| C-string (`char[]`) | `string` class |
|---|---|
| Fixed size, needs room for `'\0'` | Grows automatically |
| `strcpy`, `strcat`, `strcmp`, `strlen` | `=`, `+`, `==`, `.length()` |
| Easy to overflow | Safe — manages its own memory |

## The vector Class

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    vector<int> v;                 // an empty vector of ints
    v.push_back(10);               // add at the end — it grows
    v.push_back(20);
    v.push_back(30);
    cout << "size=" << v.size() << " first=" << v[0] << " last=" << v.back() << endl;

    v.pop_back();                  // remove the last element
    for (int i = 0; i < (int)v.size(); i++) cout << v[i] << " ";
    cout << endl;

    vector<string> names = {"Asha", "Ravi"};
    names.push_back("Meena");
    for (const string &n : names)  // range-based for: visit every element
        cout << n << " ";
    cout << endl;
    return 0;
}
```

```output
size=3 first=10 last=30
10 20 
Asha Ravi Meena 
```

| Array | `vector` |
|---|---|
| Size fixed when written | Grows/shrinks at run time (`push_back`, `pop_back`) |
| Doesn't know its own size | `size()` |
| Can't be copied with `=` | Copied with `=` (deep copy handled for you) |
| No bounds checking | `at(i)` checks bounds |

**Range-based for loop:** `for (Type x : container)` visits each element. Use `const Type &x` to avoid copying, `Type &x` to modify.

We'll use `vector` a lot in Part II — e.g. a `Member` keeps a `vector` of its `Loan`s, and an Observer subject keeps a `vector` of observers.

:::key
- `string`: grows, uses `+`, `==`, `[]`, `length()`, `substr`, `find` (→ `npos` if absent).
- `vector<T>`: resizable array with `push_back`, `pop_back`, `size`, `[]`, `at`.
- Both manage their own memory and use operator overloading — OOP in action.
:::

:::mistakes
- Forgetting `#include <string>` / `#include <vector>`.
- Writing `v[5]` on a vector of size 3 — it doesn't grow automatically; use `push_back`.
- Expecting `find` to return -1 when not found — it returns `string::npos`.
- Comparing C-strings with `==` (compares addresses).
:::

:::exam
- *"Explain the `string` class and its important functions with a program."*
- *"Differentiate C-strings and the `string` class."*
- Output questions on `substr`, `find`, `length`.
:::

:::def
The **standard C++ classes** are ready-made classes provided by the C++ Standard Library. The **`string`** class represents a sequence of characters with automatic memory management and overloaded operators for assignment, concatenation and comparison; the **`vector`** class template represents a dynamic array whose size can change at run time.
:::

## Quick Check

:::q Q1 · What is printed? `string s = "Programming"; cout << s.length() << " " << s.substr(3, 4) << " " << s.find('g');`
:::ans
`11 gram 3`
:::
:::

:::q Q2 · After `vector<int> v; v.push_back(4); v.push_back(9); v.pop_back();`, what is `v.size()`?
:::ans
`1` (only 4 remains).
:::
:::
