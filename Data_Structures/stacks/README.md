# Stacks in Python

A stack is a linear data structure that follows the **Last-In-First-Out (LIFO)** principle. This means the last element added to the stack is the first one to be removed. A physical analogy is a stack of plates—you can only place (push) a new plate on the top, and you can only take (pop) the top plate off.

For executable examples, refer to the reference script: [stacks.py](stacks.py).

---

## Core Stack Operations

All core operations of a stack run in constant time:

- **push(item)**: Adds an element to the top of the stack. Time Complexity: **O(1)**.
- **pop()**: Removes and returns the top element of the stack. Time Complexity: **O(1)**.
- **peek() / top()**: Returns the top element without removing it. Time Complexity: **O(1)**.
- **is_empty()**: Checks if the stack has no elements. Time Complexity: **O(1)**.
- **size()**: Returns the total number of elements in the stack. Time Complexity: **O(1)**.

---

## Stack Implementation in Python

In Python, the standard and most efficient way to implement a stack is using the built-in list.

- **Push:** `list.append(item)`
- **Pop:** `list.pop()`
- **Peek:** `list[-1]`

---

## Common Applications of Stacks

- **Function Call Stack:** Managing subroutine execution and recursive calls in programming runtimes.
- **Undo/Redo Mechanisms:** Storing the history of operations in text editors.
- **Expression Evaluation:** Used by compilers to parse math expressions and balance parenthetical brackets.
- **Backtracking Algorithms:** Used in maze-solving or depth-first search (DFS) state space traversal.

---

## Related Resources

- Review the Python implementations in [stacks.py](stacks.py).
- For overall linear data structures checklist, see the parent directory [Data_Structures README](../README.md).
