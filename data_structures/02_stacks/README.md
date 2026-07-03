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

## Stack Implementations in Python

In [stacks.py](stacks.py), we explore three ways of implementing a stack in Python:

### 1. Using Built-in Lists

Python's native list is dynamic and optimized for fast end-of-list operations.

- **Push**: `list.append(item)` (Amortized O(1))
- **Pop**: `list.pop()` (O(1))
- **Peek**: `list[-1]` (O(1))

### 2. Custom Array-Based Stack (Fixed Capacity)

A custom class [Stack](stacks.py#L48) that utilizes a pre-allocated fixed-size list (`self.arr = [None] * capacity`).

- Useful when you want to enforce a hard memory/capacity limit.
- Throws "Stack Overflow" when exceeding capacity and "Stack Underflow" when popping from an empty stack.
- Elements are tracked using a `self.top` index pointer.

### 3. Linked List Stack

A custom class [LinkedListStack](stacks.py#L128) that uses dynamic node allocation.

- Avoids the fixed size limitation of arrays without needing consecutive memory blocks.
- The `self.top` pointer references the head [Node](stacks.py#L123) of the linked list.
- Dynamically increments and decrements a size counter to maintain O(1) query time for stack size.

---

## Array-Based Stack vs. Linked List Stack

| Feature | Array-Based Stack (`Stack`) | Linked List Stack (`LinkedListStack`) |
| :--- | :--- | :--- |
| **Memory Allocation** | Pre-allocated contiguous memory. | Dynamically allocated nodes. |
| **Capacity** | Fixed (raises Overflow if exceeded). | Dynamic (grows with system memory). |
| **Time Complexity** | **O(1)** for push/pop (highly optimized). | **O(1)** for push/pop (slight node allocation overhead). |
| **Space Overhead** | Wastes space if the stack is mostly empty. | Extra memory used for node references (`next` pointer). |

---

## Common Applications of Stacks

- **Function Call Stack:** Managing subroutine execution and recursive calls in programming runtimes.
- **Undo/Redo Mechanisms:** Storing the history of operations in text editors.
- **Expression Evaluation:** Used by compilers to parse math expressions and balance parenthetical brackets.
- **Backtracking Algorithms:** Used in maze-solving or depth-first search (DFS) state space traversal.

---

## Related Resources

- Review the Python implementations in [stacks.py](stacks.py).
- For overall linear data structures checklist, see the parent directory [data_structures README](../README.md).
