**Files let a program save data permanently and read it back later. In C++, files are just streams: you use `<<` and `>>` on them exactly like on `cout` and `cin`.**

## The Problem: Everything Disappears When the Program Ends

All the variables and objects we've created live in RAM. Close the program and the library's members, loans and fines are **gone**. Real software needs **persistent storage** — data that survives between runs. That's what files are for.

:::analogy
Variables are like notes on a **whiteboard** — wiped at the end of class. A file is like a **notebook** — the notes remain tomorrow, and anyone (or any program) can read them again.
:::

## The Five Steps of File Handling

1. `#include <fstream>`
2. **Create** a stream object: `ofstream` (write), `ifstream` (read), `fstream` (both).
3. **Open** the file (in the constructor or with `.open()`).
4. **Check** that it opened (`if (!file)`).
5. **Read/write** with `<<`, `>>`, `getline`, `get`, `put` — then **close**.

| Class | Purpose | Default mode |
|---|---|---|
| `ofstream` | write to a file | `ios::out` (creates the file, erases old content) |
| `ifstream` | read from a file | `ios::in` |
| `fstream` | read and/or write | specify, e.g. `ios::in \| ios::out` |

**Open modes** (combine with `|`):

| Mode | Meaning |
|---|---|
| `ios::in` | open for reading |
| `ios::out` | open for writing (erases existing content) |
| `ios::app` | **append** — every write goes to the end |
| `ios::ate` | open and jump to the end |
| `ios::trunc` | erase existing content |
| `ios::binary` | binary mode (raw bytes) |

## Write, Read, Append

```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    ofstream fout("students.txt");          // steps 2+3: create and open for writing
    if (!fout) { cout << "Cannot open file" << endl; return 1; }   // step 4
    fout << "101 Asha 8.9" << endl;         // step 5: exactly like cout
    fout << "102 Ravi 7.4" << endl;
    fout << "103 Meena 9.2" << endl;
    fout.close();

    ifstream fin("students.txt");           // open for reading
    int roll; string name; double cgpa;
    while (fin >> roll >> name >> cgpa)     // the loop stops when a read FAILS (end of file)
        cout << name << " (" << roll << ") -> " << cgpa << endl;
    fin.close();

    ofstream fapp("students.txt", ios::app);   // append: keep old data
    fapp << "104 Neel 6.8" << endl;
    fapp.close();

    fin.open("students.txt");               // reopen and count lines
    string line;
    int count = 0;
    while (getline(fin, line)) count++;
    cout << "Lines now: " << count << endl;
    return 0;
}
```

```output
Asha (101) -> 8.9
Ravi (102) -> 7.4
Meena (103) -> 9.2
Lines now: 4
```

## A Classic Exam Program: Count Characters, Words and Lines

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ofstream out("poem.txt");
    out << "Twinkle twinkle\nlittle star\n";
    out.close();

    ifstream in("poem.txt");
    char ch;
    int chars = 0, words = 0, lines = 0;
    bool inWord = false;
    while (in.get(ch))                       // character by character
    {
        chars++;
        if (ch == '\n') lines++;
        if (ch == ' ' || ch == '\n' || ch == '\t') inWord = false;
        else if (!inWord) { inWord = true; words++; }   // a new word starts
    }
    cout << "chars=" << chars << " words=" << words << " lines=" << lines << endl;
    return 0;
}
```

```output
chars=28 words=4 lines=2
```

## Checking the Stream's State

| Function | True when |
|---|---|
| `good()` | no errors |
| `eof()` | the end of the file was reached during a read |
| `fail()` | a read failed, or the file couldn't be opened |
| `bad()` | a serious, unrecoverable error |
| `!stream` | same as `fail()` |

## Binary Files (Brief)

Text files store numbers as characters. **Binary files** store the raw bytes of variables or objects, using `write()` and `read()`:

```cpp
#include <iostream>
#include <fstream>
using namespace std;

struct Record { int roll; char name[16]; double cgpa; };

int main()
{
    Record out[2] = {{1, "Asha", 8.9}, {2, "Ravi", 7.4}};
    ofstream fo("records.dat", ios::binary);
    fo.write(reinterpret_cast<const char*>(out), sizeof(out));
    fo.close();

    Record r;
    ifstream fi("records.dat", ios::binary);
    while (fi.read(reinterpret_cast<char*>(&r), sizeof(r)))
        cout << r.roll << " " << r.name << " " << r.cgpa << endl;
    return 0;
}
```

```output
1 Asha 8.9
2 Ravi 7.4
```

**Random access:** `seekg(pos)`/`seekp(pos)` move the read/write position; `tellg()`/`tellp()` report it.

:::key
- Files = persistent storage; file streams work like `cin`/`cout`.
- Steps: include `<fstream>` → create → open → check → read/write → close.
- `ofstream` erases by default; use `ios::app` to add to the end.
- Loop on the read itself: `while (fin >> x)` or `while (getline(fin, line))`.
:::

:::mistakes
- `while (!fin.eof())` as the read loop — `eof()` becomes true only **after** a failed read, so the last item is often processed **twice**.
- Not checking whether the file opened.
- Opening with `ofstream` and expecting old content to survive.
- Forgetting `#include <fstream>`.
:::

:::exam
- *"Explain file handling in C++: classes, modes and steps, with a program."* (Very common.)
- *"Write a program to copy one file to another / count words / store and display student records."*
- *"Explain the file open modes."*
:::

:::def
**File handling** is the process of storing data permanently in files and retrieving it, using the stream classes `ifstream` (input), `ofstream` (output) and `fstream` (both) from `<fstream>`. A file must be opened (associating a stream with it) in a specified **mode** before it is read or written, and closed afterwards.
:::

## Quick Check

:::q Q1 · Which mode keeps existing contents and writes new data at the end?
:::ans
`ios::app`.
:::
:::

:::q Q2 · Why is `while (fin >> x)` better than `while (!fin.eof())`?
:::ans
It checks the success of the read **itself**, so the loop stops exactly when a read fails; with `eof()` the check happens before the read, so the last value is processed twice.
:::
:::
