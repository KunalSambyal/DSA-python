# 03 Basic Recursion

This directory contains code and notes on recursion — when a function calls itself directly or indirectly to solve a smaller instance of the same problem.

---

## Core Concepts

### 1. Call Stack & Stack Overflow

Each recursive call creates an activation record (frame) on the call stack. If the recursion doesn't hit a base case and terminate, it will continue allocating stack frames until the stack memory is exhausted, causing a **Stack Overflow** error.

### 2. Base Case

The condition that stops the recursion from calling itself further. Every valid recursive function must have at least one base case.

---

## Key Recursion Implementations

### 1. Linear Recursion (Printing 1 to N / N to 1)

- **Time Complexity:** **O(n)** because the function is called `n` times.
- **Space Complexity:** **O(n)** due to the recursive call stack height of `n`.

### 2. Factorial of N

Multiply `n` by `factorial(n - 1)`.

- **Time Complexity:** **O(n)**
- **Space Complexity:** **O(n)** call stack space.

### 3. Fibonacci Sequence

Sum of two preceding terms (`fib(n - 1) + fib(n - 2)`).

- **Time Complexity:** **O(2^n)** (without memoization, as it creates an exponential tree of calls).
- **Space Complexity:** **O(n)** maximum call stack depth.

### 4. Reverse an Array Recursively

Swap the elements at the `left` and `right` indices, and recursively call the function with `left + 1` and `right - 1`.

- **Time Complexity:** **O(n)**
- **Space Complexity:** **O(n)** call stack space.

### 5. String Palindrome Check Recursively

Compare the boundary characters. If they match, recursively check the inner substring.

- **Time Complexity:** **O(n)**
- **Space Complexity:** **O(n)** call stack space.

---

## Related Resources

- **Implementation Code:** [recursion_basics.py](recursion_basics.py)
- **Reference Roadmap:** [Striver's A2Z DSA Sheet](https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z)
- **Parent Directory README:** [dsa_basics README](../README.md)
