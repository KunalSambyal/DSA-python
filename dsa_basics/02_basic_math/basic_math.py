# basic_math.py
"""
Introduction to Basic Mathematics for DSA in Python.
Covers:
1. Digit Extraction, Count, and Reversal
2. Palindrome Number Check
3. GCD & LCM (Euclidean Algorithm)
4. Divisors Extraction in O(sqrt(n))
5. Prime Number Check in O(sqrt(n))
"""

def count_digits(n):
    """Counts the number of digits in an integer."""
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def reverse_integer(n):
    """Reverses the digits of an integer. Handles negative numbers."""
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n > 0:
        last_digit = n % 10
        rev = (rev * 10) + last_digit
        n //= 10
    return sign * rev

def is_palindrome_number(n):
    """Checks if an integer reads the same backward as forward."""
    if n < 0:
        return False
    return n == reverse_integer(n)

def find_gcd(a, b):
    """Finds the Greatest Common Divisor (GCD) using the Euclidean Algorithm."""
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a if b == 0 else b

def find_lcm(a, b):
    """Finds the Least Common Multiple (LCM) using the relation: a * b = GCD(a, b) * LCM(a, b)."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // find_gcd(a, b)

def get_divisors(n):
    """Finds all divisors of an integer in O(sqrt(n)) time."""
    divisors = []
    n = abs(n)
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
        i += 1
    return sorted(divisors)

def is_prime(n):
    """Checks if a number is prime in O(sqrt(n)) time."""
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def demo_basic_math():
    print("=" * 60)
    print(" BASIC MATHEMATICS FOR DSA ")
    print("=" * 60)
    
    # Digit operations
    num = -1234
    print(f"Number: {num}")
    print(f"Digit Count: {count_digits(num)}")
    print(f"Reversed Number: {reverse_integer(num)}")
    
    # Palindrome check
    pal_num = 12321
    print(f"\nIs {pal_num} a palindrome?: {is_palindrome_number(pal_num)}")
    print(f"Is {num} a palindrome?: {is_palindrome_number(num)}")
    
    # GCD & LCM
    a, b = 20, 15
    print(f"\nNumbers: {a}, {b}")
    print(f"GCD: {find_gcd(a, b)}")
    print(f"LCM: {find_lcm(a, b)}")
    
    # Divisors
    div_num = 36
    print(f"\nDivisors of {div_num}: {get_divisors(div_num)}")
    
    # Primality
    prime_num = 17
    composite_num = 24
    print(f"\nIs {prime_num} prime?: {is_prime(prime_num)}")
    print(f"Is {composite_num} prime?: {is_prime(composite_num)}")

if __name__ == "__main__":
    demo_basic_math()
