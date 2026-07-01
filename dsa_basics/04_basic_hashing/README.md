# 04 Basic Hashing

This directory contains code and notes on hashing — a search optimization technique where items are mapped directly to unique keys using a hash function.

---

## Core Concepts

### 1. Hashing Definition

Hashing is a method to store and retrieve data in constant time **O(1)** on average by mapping keys to indices of a table.

### 2. Frequency Counting

Instead of using nested loops to search and count occurrences of elements in **O(n^2)** time, we use a Hash Map (Python dictionary) to count occurrences in a single pass.

---

## Key Hashing Implementations

### 1. Frequency Map Creation

Traverse the array once and store the counts in a dictionary.

- **Time Complexity:** **O(n)** where `n` is the number of elements in the array.
- **Space Complexity:** **O(k)** where `k` is the number of unique elements.

### 2. Frequency Queries

Retrieve the count of a specific query key from the dictionary.

- **Time Complexity:** **O(1)** on average.
- **Space Complexity:** **O(1)**.

### 3. Min/Max Frequency Finder

Iterate through the frequency map to identify keys with the highest and lowest values.

- **Time Complexity:** **O(k)** where `k` is the number of unique elements.
- **Space Complexity:** **O(1)**.

---

## Related Resources

- **Implementation Code:** [basic_hashing.py](basic_hashing.py)
- **Parent Directory README:** [dsa_basics README](../README.md)
