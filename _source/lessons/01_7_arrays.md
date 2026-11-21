**An array stores many values of the same type under one name, in a row of numbered slots. The numbering starts at 0.**

## The Problem: 60 Students, 60 Variables?

To store marks of 60 students you'd need `m1, m2, …, m60` — and to total them you'd write a 60-term sum. Loops can't help, because each variable has a different name. An **array** gives all of them one name and a number (**index**), so a loop can visit each one.

## Understanding Arrays

```cpp
int marks[5] = {70, 85, 90, 60, 75};
```

```text
 index:     0      1      2      3      4
          ┌──────┬──────┬──────┬──────┬──────┐
 marks →  │  70  │  85  │  90  │  60  │  75  │     5 ints side by side in memory
          └──────┴──────┴──────┴──────┴──────┘
```

- **Fixed size** — chosen when declared (here 5).
- **Same type** for every element.
- **Contiguous** — stored next to each other in memory.
- **Index from 0 to size − 1** — `marks[0]` is the first, `marks[4]` is the last.

:::analogy
A row of numbered lockers in a school corridor. All lockers are the same size (same type), they stand side by side (contiguous), and the first locker is numbered **0**. To reach a locker you only need its number.
:::

## Using Arrays with Loops

```cpp
#include <iostream>
using namespace std;

int main()
{
    int marks[5] = {70, 85, 90, 60, 75};
    int total = 0, highest = marks[0];
    for (int i = 0; i < 5; i++)            // i goes 0,1,2,3,4
    {
        total += marks[i];
        if (marks[i] > highest) highest = marks[i];
    }
    cout << "Total = " << total << ", Highest = " << highest << endl;

    int partial[5] = {1, 2};               // the rest become 0
    cout << partial[2] << " " << partial[4] << endl;

    int nums[] = {4, 8, 15};               // size worked out automatically: 3
    cout << sizeof(nums) / sizeof(nums[0]) << " elements" << endl;
    return 0;
}
```

```output
Total = 380, Highest = 90
0 0
3 elements
```

## Two-Dimensional Arrays (Tables)

`int m[2][3]` is a table with 2 rows and 3 columns — like a spreadsheet. Use one loop for rows and a nested loop for columns.

```cpp
#include <iostream>
using namespace std;

int main()
{
    int m[2][3] = {{1, 2, 3}, {4, 5, 6}};
    for (int r = 0; r < 2; r++)
    {
        for (int c = 0; c < 3; c++) cout << m[r][c] << " ";
        cout << endl;
    }
    return 0;
}
```

```output
1 2 3 
4 5 6 
```

## C-Strings: Arrays of Characters

Text can be stored as an array of `char` that ends with a special **null character `'\0'`**, which marks "the text stops here".

```cpp
#include <iostream>
using namespace std;

int main()
{
    char city[] = "Pune";            // stored as 'P','u','n','e','\0'  -> 5 bytes
    cout << city << " uses " << sizeof(city) << " bytes" << endl;
    cout << "First letter: " << city[0] << endl;
    return 0;
}
```

```output
Pune uses 5 bytes
First letter: P
```

(Later, in Lesson 6.4, you'll meet `string`, a much easier and safer way to handle text.)

:::key
- Array = fixed-size, same-type, contiguous, 0-indexed collection.
- Valid indices: 0 to size−1. Loop with `for (int i = 0; i < size; i++)`.
- Partly initialized arrays fill the rest with 0.
- C-strings end with `'\0'`, so `"Pune"` needs 5 bytes.
:::

:::mistakes
- Accessing `marks[5]` in a 5-element array — C++ does **not** check; it's undefined behaviour.
- Forgetting space for `'\0'` in a char array.
- Copying arrays with `a = b;` — not allowed; copy element by element.
- Using a variable as the size (`int n; cin >> n; int a[n];`) — not standard C++. Use `new` or `vector` (later).
:::

:::exam
- *Programs:* largest/smallest element, sum and average, reverse an array, linear search, matrix addition.
- MCQ: "What is the index of the last element of `int a[10]`?" → `9`.
:::

:::def
An **array** is a collection of a fixed number of elements of the same data type stored in contiguous memory locations and accessed using an index starting from 0.
:::

## Quick Check

:::q Q1 · What is printed? `int a[4] = {3}; cout << a[0] + a[3];`
:::ans
`3` — `a[0]` is 3 and the uninitialized elements are 0.
:::
:::

:::q Q2 · How many bytes does `char s[] = "Hello";` occupy?
:::ans
**6** — five letters + the `'\0'` terminator.
:::
:::
