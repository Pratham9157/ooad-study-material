**Character I/O reads and writes text one character (or one full line) at a time — including spaces and newlines, which `cin >>` normally skips.**

## The Problem: cin >> Ignores Spaces

`cin >>` skips whitespace and stops at the next space. That's great for numbers, but useless when you need to:
- count spaces in a sentence,
- read a full name like "Riya Sharma",
- process text character by character.

## The Tools

| Function | What it does |
|---|---|
| `cin.get(ch)` | reads **one** character, **including** spaces and `\n` |
| `cout.put(ch)` | writes one character |
| `getline(cin, str)` | reads a whole line into a `string` (the `\n` is discarded) |
| `cin.getline(arr, n)` | reads a line into a char array (up to n−1 characters) |
| `cin.ignore(n, '\n')` | skips up to n characters, or until a newline |
| `cin.peek()` | looks at the next character without removing it |
| `cin.putback(ch)` | puts a character back into the input |

:::analogy
`cin >>` is like reading a book **word by word**, ignoring the gaps between words. `cin.get()` is like reading **letter by letter, gaps included**. `getline` is reading **one whole line** of the page at once.
:::

## Reading Character by Character

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main()
{
    //@input: Hi there!
    char ch;
    int letters = 0, spaces = 0;
    while (cin.get(ch) && ch != '\n')     // reads spaces too
    {
        if (ch == ' ') spaces++;
        else if (isalpha(ch)) letters++;
        cout.put(toupper(ch));            // echo in capitals
    }
    cout << endl << "letters=" << letters << " spaces=" << spaces << endl;
    return 0;
}
```

Input `Hi there!`:

```output
HI THERE!
letters=7 spaces=1
```

## The Famous cin >> + getline Trap

When you type `21` and press Enter, the input contains `21\n`. `cin >> age` takes `21` but **leaves the `\n` behind**. A following `getline` sees that `\n` immediately and returns an **empty line**.

```text
 keyboard buffer:   2 1 \n R i y a   S h a r m a \n
 cin >> age     →   takes "21", leaves  \n R i y a ...
 getline(cin,s) →   sees \n first → s = ""   ← bug!
 fix: cin.ignore() first, to throw away that leftover \n
```

```cpp
#include <iostream>
#include <string>
using namespace std;

int main()
{
    //@input: 21
    //@input: Riya Sharma
    int age;
    string name;
    cin >> age;
    cin.ignore(1000, '\n');        // discard the leftover newline
    getline(cin, name);            // now reads the full line, spaces included
    cout << name << " is " << age << endl;
    return 0;
}
```

Input `21` then `Riya Sharma`:

```output
Riya Sharma is 21
```

:::key
- `cin.get(ch)` reads every character including whitespace; `cout.put(ch)` writes one.
- `getline(cin, s)` reads a full line into a `string`.
- After `cin >>`, call `cin.ignore()` before `getline`.
:::

:::mistakes
- Using `cin >> ch` to count spaces (it skips them).
- Forgetting `cin.ignore()` → `getline` returns an empty string.
- Mixing up `cin.getline(charArray, n)` and `getline(cin, stringVar)`.
- `cout << toupper(ch)` prints a number; use `cout.put(...)` or a `char` cast.
:::

:::exam
- *"Explain `get()`, `put()` and `getline()` with examples."*
- *"Write a program to count vowels/spaces/words in a line of text."*
:::

:::def
**Character I/O** refers to unformatted input and output of individual characters or lines using stream member functions such as `get()`, `put()` and `getline()`, which, unlike the extraction operator, do not skip whitespace.
:::

## Quick Check

:::q Q1 · Input is `A B`. What does `char a, b; cin >> a >> b;` store? What about `cin.get(a); cin.get(b);`?
:::ans
`cin >>`: a = 'A', b = 'B' (space skipped). `cin.get`: a = 'A', b = ' ' (the space).
:::
:::

:::q Q2 · Why might `getline` return an empty string right after `cin >> n`?
:::ans
`cin >> n` leaves the newline in the buffer; `getline` reads up to that newline immediately. Use `cin.ignore()` first.
:::
:::
