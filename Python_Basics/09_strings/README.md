# Strings (Deep Dive)

A string is a sequence of characters. In Python, strings are created by enclosing characters in single quotes `'` or double quotes `"`.

---

## 1. Indexing and Slicing

Strings are ordered sequences, which means you can access individual characters using index numbers (starting from `0`), or select a range of characters using slicing.

* **Positive Indices**: Count from the beginning (start at `0`).
* **Negative Indices**: Count from the end (start at `-1`).
* **Slicing Syntax**: `string[start:end:step]`

```python
text = "Hello, World!"

# Indexing
print(text[0])   # Output: H
print(text[-1])  # Output: !

# Slicing
print(text[0:5])    # Output: Hello (excludes index 5)
print(text[7:])     # Output: World! (from index 7 to the end)
print(text[::2])    # Output: Hlo ol! (every second character)
print(text[::-1])   # Output: !dlroW ,olleH (reverses the string)
```

---

## 2. String Immutability

Python strings are **immutable**, meaning that once a string is created, its characters cannot be changed or replaced.

```python
text = "hello"

# The line below will raise a TypeError:
# text[0] = "H"

# To modify a string, you must create a new one:
text = "H" + text[1:]
print(text)  # Output: Hello
```

---

## 3. Escape Characters and Raw Strings

### Escape Characters
Escape characters allow you to print special characters that are otherwise difficult or impossible to type in a string:
* `\n`: Newline
* `\t`: Tab
* `\\`: Backslash
* `\"`: Double Quote

```python
print("Hello\nWorld")  # Prints Hello on one line and World on the next
```

### Raw Strings
If you prefix a string with `r` or `R`, Python will ignore all escape characters. This is extremely useful for file paths and regular expressions.

```python
# Normal string (interprets \n as newline)
print("C:\new_folder") 

# Raw string (prints exactly what is typed)
print(r"C:\new_folder")  # Output: C:\new_folder
```

---

## 4. Advanced f-Strings

f-strings do not just embed variable values; they can also evaluate expressions and format numbers.

```python
# Math expressions
print(f"5 + 5 is {5 + 5}")  # Output: 5 + 5 is 10

# Float precision formatting
pi = 3.14159265
print(f"Pi to 2 decimal places: {pi:.2f}")  # Output: Pi to 2 decimal places: 3.14

# Text alignment
print(f"{'right-aligned':>20}")  # Output:        right-aligned

# Nested quotes
user = {"name": "Alice"}
print(f"User's name is {user['name']}")
```

---

## 5. String Methods Reference

Here is a reference list of the most common string methods:

| Method | Description | Example |
|---|---|---|
| `upper()` | Converts string to uppercase. | `"hello".upper()` $\rightarrow$ `"HELLO"` |
| `lower()` | Converts string to lowercase. | `"HELLO".lower()` $\rightarrow$ `"hello"` |
| `title()` | Capitalizes the first letter of each word. | `"hello world".title()` $\rightarrow$ `"Hello World"` |
| `strip()` | Removes leading and trailing whitespace. | `" hello ".strip()` $\rightarrow$ `"hello"` |
| `lstrip()` / `rstrip()` | Removes left or right whitespace. | `" hello ".lstrip()` $\rightarrow$ `"hello "` |
| `split(sep)` | Splits string into a list using separator. | `"a,b".split(",")` $\rightarrow$ `['a', 'b']` |
| `join(iterable)` | Joins an iterable into a string. | `"-".join(["a", "b"])` $\rightarrow$ `"a-b"` |
| `replace(old, new)` | Replaces occurrences of a substring. | `"abc".replace("b", "x")` $\rightarrow$ `"axc"` |
| `find(sub)` | Returns the index of first occurrence. | `"hello".find("l")` $\rightarrow$ `2` (returns `-1` if not found) |
| `count(sub)` | Counts occurrences of a substring. | `"hello".count("l")` $\rightarrow$ `2` |
| `startswith(prefix)` | Checks if string starts with prefix. | `"hello".startswith("he")` $\rightarrow$ `True` |
| `endswith(suffix)` | Checks if string ends with suffix. | `"hello".endswith("lo")` $\rightarrow$ `True` |
| `isdigit()` | Returns `True` if all characters are digits. | `"123".isdigit()` $\rightarrow$ `True` |
| `isalpha()` | Returns `True` if all characters are alphabetic. | `"abc".isalpha()` $\rightarrow$ `True` |

---

## Further Reading

- [Official Python Docs — Text Sequence Type str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Official Python Docs — String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
