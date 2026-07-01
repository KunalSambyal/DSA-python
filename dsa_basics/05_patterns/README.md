# 05 Loop Patterns

This directory contains implementations of common star and number patterns designed to build intuition for nested loops, row-column grids, and coordinate math.

---

## Pattern Guidelines

When printing loop patterns, always visualize them on a 2D coordinate grid (rows and columns):

1. **Outer Loop:** Represents the rows (usually tracked with variable `i` from `0` to `n - 1`).
2. **Inner Loop(s):** Represents columns (usually printing spaces, stars, or numbers based on mathematical formulas involving the current row `i` and total height `n`).

---

## Implemented Patterns

### 1. Right-Angled Triangle

- Height: `n`
- Row `i` (1-indexed) prints `i` stars.

### 2. Inverted Right-Angled Triangle

- Height: `n`
- Row `i` (1-indexed) prints `n - i + 1` stars.

### 3. Pyramid

- Height: `n`
- Row `i` (0-indexed) prints `n - i - 1` spaces followed by `2 * i + 1` stars.

### 4. Inverted Pyramid

- Height: `n`
- Row `i` (0-indexed) prints `n - i - 1` spaces followed by `2 * i + 1` stars (iterated in reverse from `n - 1` down to `0`).

### 5. Diamond

- Full height: `2*n - 1`
- Combination of a normal Pyramid of height `n` followed by an Inverted Pyramid of height `n - 1`.

### 6. Number Crown

- Height: `n`
- Prints increasing digits on the left, empty spaces in the center, and decreasing digits on the right.

---

## Related Resources

- **Implementation Code:** [patterns.py](patterns.py)
- **Reference Roadmap:** [Striver's A2Z DSA Sheet](https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z)
- **Parent Directory README:** [dsa_basics README](../README.md)
