# recursion_basics.py
"""
Introduction to Recursion for DSA in Python.
Covers:
1. Print 1 to N and N to 1
2. Factorial and Fibonacci (Functional Recursion)
3. Reverse an Array Recursively
4. Palindrome String Check Recursively
"""

def print_1_to_n(n):
    """Prints numbers from 1 to N recursively."""
    if n < 1:
        return
    print_1_to_n(n - 1)
    print(n, end=" ")

def print_n_to_1(n):
    """Prints numbers from N to 1 recursively."""
    if n < 1:
        return
    print(n, end=" ")
    print_n_to_1(n - 1)

def factorial(n):
    """Calculates the factorial of N recursively."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Calculates the Nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def reverse_array_recursive(arr, left=0, right=None):
    """Reverses an array in-place using recursion."""
    if right is None:
        right = len(arr) - 1
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse_array_recursive(arr, left + 1, right - 1)

def is_palindrome_string_recursive(s, left=0, right=None):
    """Checks if a string is a palindrome recursively."""
    if right is None:
        right = len(s) - 1
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return is_palindrome_string_recursive(s, left + 1, right - 1)

def demo_recursion():
    print("=" * 60)
    print(" RECURSION BASICS FOR DSA ")
    print("=" * 60)
    
    # 1. Print 1 to N and N to 1
    n = 5
    print(f"Printing 1 to {n} recursively:")
    print_1_to_n(n)
    print("\n")
    
    print(f"Printing {n} to 1 recursively:")
    print_n_to_1(n)
    print("\n")
    
    # 2. Factorial & Fibonacci
    fact_val = 5
    fib_idx = 6
    print(f"Factorial of {fact_val}: {factorial(fact_val)}")
    print(f"{fib_idx}th Fibonacci Number: {fibonacci(fib_idx)}")
    
    # 3. Array Reversal
    arr = [1, 2, 3, 4, 5]
    print(f"\nOriginal Array: {arr}")
    reverse_array_recursive(arr)
    print(f"Reversed Array recursively: {arr}")
    
    # 4. Palindrome check
    string_pal = "radar"
    string_not_pal = "hello"
    print(f"\nIs '{string_pal}' a palindrome?: {is_palindrome_string_recursive(string_pal)}")
    print(f"Is '{string_not_pal}' a palindrome?: {is_palindrome_string_recursive(string_not_pal)}")

if __name__ == "__main__":
    demo_recursion()
