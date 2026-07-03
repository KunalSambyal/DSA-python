# stacks.py
"""
Comprehensive guide to Stacks in Python.
Covers:
1. Stack implementation using built-in list
2. Stack Application: Balanced Parentheses Checker
"""


# =====================================================================
# 1. Stack using Built-in Python List
# =====================================================================
def demo_list_stack():
    print("=" * 60)
    print(" 1. STACK USING PYTHON LIST ")
    print("=" * 60)

    # Creation
    stack = []

    # Push operations
    stack.append("A")
    stack.append("B")
    stack.append("C")
    print(f"Stack after pushes: {stack}")

    # Peek operation
    if stack:
        top_item = stack[-1]
        print(f"Peek (top item): {top_item}")

    # Pop operations
    popped_item = stack.pop()
    print(f"Popped item: {popped_item}")
    print(f"Stack after pop: {stack}")

    # Check Empty
    is_empty = len(stack) == 0
    print(f"Is stack empty?: {is_empty}")

    # Size
    print(f"Stack size: {len(stack)}")


# =====================================================================
# 2. Stack Implementation using a Custom Class
# =====================================================================
class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.top = -1

    def push(self, value):
        if self.top == self.capacity - 1:
            raise Exception("Stack Overflow")
        self.top += 1
        self.arr[self.top] = value
    
    def pop(self):
        if self.top < 0:
            raise Exception("Stack Underflow")
        value = self.arr[self.top]
        self.arr[self.top] = None  # Clear reference to avoid memory leaks
        self.top -= 1
        return value

    def peek(self):
        if self.top < 0:
            raise Exception("Stack is empty")
        return self.arr[self.top]

    def display(self):
        if self.top < 0:
            print("Stack is empty")
        else:
            print("Stack elements from top to bottom:")
            for i in range(self.top, -1, -1):
                print(self.arr[i])

    def size(self):
        return self.top + 1

    def is_full(self):
        return self.top == self.capacity - 1
    
    def is_empty(self):
        return self.top == -1
    
def demo_custom_stack():
    print("\n" + "=" * 60)
    print(" 2. STACK USING CUSTOM CLASS ")
    print("=" * 60)

    stack_capacity = 5
    stack = Stack(stack_capacity)

    # Push operations
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()

    # Peek operation
    print(f"Peek (top item): {stack.peek()}")

    # Pop operation
    popped_item = stack.pop()
    print(f"Popped item: {popped_item}")
    stack.display()

    # Check Empty
    print(f"Is stack empty?: {stack.is_empty()}")

    # Size and Capacity
    print(f"Stack capacity: {stack.capacity}")
    print(f"Stack size (current elements): {stack.size()}")
        

# =====================================================================
# 3. Stack Application: Balanced Parentheses Checker
# =====================================================================
def is_balanced(expression: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if char in mapping.values():  # Opening bracket
            stack.append(char)
        elif char in mapping.keys():  # Closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()

    return len(stack) == 0


def demo_balanced_brackets():
    print("\n" + "=" * 60)
    print(" 2. STACK APPLICATION: BALANCED PARENTHESES ")
    print("=" * 60)

    expr1 = "{[()()]}"
    expr2 = "{[(])}"
    expr3 = "(((())"

    print(f"Is '{expr1}' balanced?: {is_balanced(expr1)}")  # True
    print(f"Is '{expr2}' balanced?: {is_balanced(expr2)}")  # False
    print(f"Is '{expr3}' balanced?: {is_balanced(expr3)}")  # False


if __name__ == "__main__":
    demo_list_stack()
    demo_custom_stack()
    demo_balanced_brackets()
