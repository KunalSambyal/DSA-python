# 02 Basic Mathematics

This directory contains code and notes on fundamental mathematical operations and algorithms commonly used in problem solving.

---

## Key Algorithms & Concepts

### 1. Count Digits

To count the number of digits in a base-10 number, we repeatedly divide the number by 10 until it becomes 0.

- **Time Complexity:** **O(log_10(n))**
- **Space Complexity:** **O(1)**

### 2. Reverse an Integer

Extract the last digit using modulo 10 (`n % 10`), append it to the reversed number (`rev * 10 + digit`), and divide `n` by 10.

- **Time Complexity:** **O(log_10(n))**
- **Space Complexity:** **O(1)**

### 3. Palindrome Check

Reverse the integer and check if the reversed number is equal to the original. Note that negative numbers are not palindromes.

- **Time Complexity:** **O(log_10(n))**
- **Space Complexity:** **O(1)**

### 4. Greatest Common Divisor (GCD) / Euclidean Algorithm

Repeatedly subtract or modulo the smaller number from the larger one until one of them becomes 0.

- **Time Complexity:** **O(log(min(a, b)))**
- **Space Complexity:** **O(1)**

### 5. Find All Divisors

Instead of scanning up to `n`, iterate up to `sqrt(n)`. If `i` divides `n`, both `i` and `n // i` are divisors.

- **Time Complexity:** **O(sqrt(n))**
- **Space Complexity:** **O(1)** (excluding the array storing divisors)

### 6. Prime Check

Loop from 2 to `sqrt(n)`. If any number divides `n`, it is composite; otherwise, it is prime.

- **Time Complexity:** **O(sqrt(n))**
- **Space Complexity:** **O(1)**

---

## Related Resources

- **Implementation Code:** [basic_math.py](basic_math.py)
- **Parent Directory README:** [dsa_basics README](../README.md)
