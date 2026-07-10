# queues.py
"""
Comprehensive guide to Queues in Python.
Covers:
1. Queue using built-in list
2. Queue using collections.deque
3. Queue using custom LinkedList structure
4. Queue Application: Generating Binary Numbers from 1 to N
"""

from collections import deque

# =====================================================================
# 1. Queue using Built-in Python List
# =====================================================================
def demo_list_queue():
    print("=" * 60)
    print(" 1. QUEUE USING PYTHON LIST ")
    print("=" * 60)

    # Creation
    queue = []

    # Enqueue operations
    queue.append("A")
    queue.append("B")
    queue.append("C")
    print(f"Queue after enqueues: {queue}")

    # Dequeue operations
    popped_item = queue.pop(0)  # O(N) operation due to shifting
    print(f"Dequeued item: {popped_item}")
    print(f"Queue after dequeue: {queue}")

    # Peek operation
    if queue:
        front_item = queue[0]
        print(f"Peek (front item): {front_item}")

    # Check Empty
    is_empty = len(queue) == 0
    print(f"Is queue empty?: {is_empty}")

    # Size
    print(f"Queue size: {len(queue)}")


# =====================================================================
# 2. Queue Implementation using collections.deque
# =====================================================================
class DequeQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue Underflow")
        return self.queue.popleft()  # O(1) operation

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[0]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements from front to back:")
            for item in self.queue:
                print(item)

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0


def demo_deque_queue():
    print("\n" + "=" * 60)
    print(" 2. QUEUE USING COLLECTIONS.DEQUE ")
    print("=" * 60)

    queue = DequeQueue()

    # Enqueue operations
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()

    # Peek operation
    print(f"Peek (front item): {queue.peek()}")

    # Dequeue operation
    dequeued_item = queue.dequeue()
    print(f"Dequeued item: {dequeued_item}")
    queue.display()

    # Check Empty
    print(f"Is queue empty?: {queue.is_empty()}")

    # Size
    print(f"Queue size: {queue.size()}")


# =====================================================================
# 3. Linked List Implementation of Queue
# =====================================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            raise Exception("Queue Underflow")
        value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return value

    def peek(self):
        if self.head is None:
            raise Exception("Queue is empty")
        return self.head.data

    def display(self):
        if self.head is None:
            print("Queue is empty")
        else:
            print("Queue elements from front to back:")
            curr = self.head
            while curr:
                print(curr.data)
                curr = curr.next

    def curr_size(self):
        return self.size

    def is_empty(self):
        return self.head is None


def demo_linked_list_queue():
    print("\n" + "=" * 60)
    print(" 3. QUEUE USING LINKED LIST ")
    print("=" * 60)

    queue = LinkedListQueue()

    # Enqueue operations
    queue.enqueue(100)
    queue.enqueue(200)
    queue.enqueue(300)
    queue.display()

    # Peek operation
    print(f"Peek (front item): {queue.peek()}")

    # Dequeue operation
    dequeued_item = queue.dequeue()
    print(f"Dequeued item: {dequeued_item}")
    queue.display()

    # Check Empty
    print(f"Is queue empty?: {queue.is_empty()}")

    # Size
    print(f"Queue size (current elements): {queue.curr_size()}")


# =====================================================================
# 4. Queue Application: Generating Binary Numbers from 1 to N
# =====================================================================
def generate_binary_numbers(n: int) -> list:
    result = []
    q = deque()
    q.append("1")

    for _ in range(n):
        curr = q.popleft()
        result.append(curr)
        q.append(curr + "0")
        q.append(curr + "1")

    return result


def demo_generate_binary_numbers():
    print("\n" + "=" * 60)
    print(" 4. QUEUE APPLICATION: GENERATE BINARY NUMBERS ")
    print("=" * 60)

    n = 10
    print(f"Binary numbers from 1 to {n}:")
    print(generate_binary_numbers(n))


if __name__ == "__main__":
    demo_list_queue()
    demo_deque_queue()
    demo_linked_list_queue()
    demo_generate_binary_numbers()
