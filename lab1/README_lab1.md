# Lab 1 — Python Basics

Introductory Python exercises covering core language concepts.  
All tasks are implemented as functions in a single interactive `zadania.py` file with a `match/case` menu (Python 3.10+).

Run with: `python zadania.py`, then enter a number 1–10 to call the task, `0` to exit.

---

## Tasks

| # | Task | Concepts |
|---|------|----------|
| 1 | **Sum of even numbers** — sum all even numbers from 1 to 100 | Generator expression, `sum()` |
| 2 | **Prime number checker** — `czy_pierwsza(n)` returns whether n is prime | Functions, loops, √n optimization |
| 3 | **String reversal** — reverse a string without `[::-1]` | String indexing, loops |
| 4 | **Temperature converter** — convert °C ↔ °F based on user choice | Functions, user input, `match/case` |
| 5 | **List without duplicates** — remove duplicates while preserving order | Sets, lists |
| 6 | **Factorial (recursion)** — compute n! recursively | Recursive functions, base cases |
| 7 | **Character frequency counter** — count occurrences of each character | Dictionaries, string iteration |
| 8 | **Number guessing game** — guess a random number 1–20 with hints | `random`, loops, user interaction |
| 9 | **Multiplication table** — display a formatted 10×10 times table | Nested loops, string formatting |
| 10 | **Text file analysis** — count lines, words, and characters in `dane.txt` | File I/O, string methods |

---

> **Note for Task 10:** place a `dane.txt` file in the same directory before running. The program defaults to that filename but will prompt you to change it.