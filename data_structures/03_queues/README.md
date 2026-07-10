# Queue Data Structure

A Queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. The element added first is the one that is removed first. Think of it as a line of people waiting for a service.

---

## Operations and Complexity

| Operation       | Description                                                       | Time Complexity (List) | Time Complexity (Deque) | Time Complexity (Linked List) | Space Complexity |
| :-------------- | :---------------------------------------------------------------- | :--------------------- | :---------------------- | :---------------------------- | :--------------- |
| `enqueue(item)` | Adds an element to the back (tail) of the queue.                  | **O(1)**               | **O(1)**                | **O(1)**                      | **O(1)**         |
| `dequeue()`     | Removes and returns the element at the front (head) of the queue. | **O(N)**               | **O(1)**                | **O(1)**                      | **O(1)**         |
| `peek()`        | Returns the front element without removing it.                    | **O(1)**               | **O(1)**                | **O(1)**                      | **O(1)**         |
| `is_empty()`    | Returns true if the queue contains no elements.                   | **O(1)**               | **O(1)**                | **O(1)**                      | **O(1)**         |
| `size()`        | Returns the total number of elements in the queue.                | **O(1)**               | **O(1)**                | **O(1)**                      | **O(1)**         |

---

## Implementations in Python

### 1. List-based Queue

- **Implementation:** Standard Python `list`.
- **Drawback:** Dequeue operation is **O(N)** because removing the first element (`list.pop(0)`) requires shifting all subsequent elements left in memory by one index.

### 2. Deque-based Queue (Recommended)

- **Implementation:** `collections.deque` (Double-ended queue).
- **Advantage:** Implemented as a doubly linked list under the hood in CPython. Both appending and popping from either end is a guaranteed **O(1)** operation.

### 3. Custom Linked List Queue

- **Implementation:** Custom Node class with `next` pointers.
- **Advantage:** Low-level pointer manipulation. Teaches how memory allocation and references work. Maintains a `tail` pointer to ensure enqueueing is **O(1)**.

### 4. Queue Application: Generating Binary Numbers

- **Application:** Generating binary representation of numbers from 1 to **N** sequentially. By utilizing a queue, we can generate these numbers in **O(N)** time without relying on string formatting or arithmetic conversion loops.
