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
# 2. Stack Application: Balanced Parentheses Checker
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
    demo_balanced_brackets()
