# patterns.py
"""
Star and Number patterns for loop practice in Python.
These patterns help build intuition for nested loops, row-column coordinate systems,
and tracking indexes.
"""

def right_angled_triangle(n):
    """
    Prints a right-angled triangle pattern of height N:
    *
    **
    ***
    """
    for i in range(1, n + 1):
        print("*" * i)

def inverted_right_angled_triangle(n):
    """
    Prints an inverted right-angled triangle of height N:
    ***
    **
    *
    """
    for i in range(n, 0, -1):
        print("*" * i)

def pyramid(n):
    """
    Prints a centered pyramid of height N:
      *  
     *** 
    *****
    """
    for i in range(n):
        # Spaces: n - i - 1, Stars: 2 * i + 1
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

def inverted_pyramid(n):
    """
    Prints an inverted centered pyramid of height N:
    *****
     ***
      *
    """
    for i in range(n - 1, -1, -1):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

def diamond(n):
    """
    Prints a diamond pattern of width 2*N - 1:
      *
     ***
      *
    """
    pyramid(n)
    # Print inverted pyramid with height n-1 below it for perfect symmetry
    for i in range(n - 2, -1, -1):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

def number_crown(n):
    """
    Prints a number crown pattern of height N:
    1      1
    12    21
    123  321
    12344321
    """
    for i in range(1, n + 1):
        # Left numbers
        left = "".join(str(x) for x in range(1, i + 1))
        # Center spaces: 2 * (n - i)
        spaces = " " * (2 * (n - i))
        # Right numbers
        right = "".join(str(x) for x in range(i, 0, -1))
        print(left + spaces + right)

def demo_patterns():
    print("=" * 60)
    print(" LOOP PATTERNS FOR DSA PRACTICE ")
    print("=" * 60)
    
    n = 5
    
    print("\n1. Right-Angled Triangle:")
    right_angled_triangle(n)
    
    print("\n2. Inverted Right-Angled Triangle:")
    inverted_right_angled_triangle(n)
    
    print("\n3. Pyramid:")
    pyramid(n)
    
    print("\n4. Inverted Pyramid:")
    inverted_pyramid(n)
    
    print("\n5. Diamond:")
    diamond(n)
    
    print("\n6. Number Crown:")
    number_crown(n - 1)

if __name__ == "__main__":
    demo_patterns()
