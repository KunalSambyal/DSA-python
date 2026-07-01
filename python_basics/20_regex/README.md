# Regular Expressions (Regex)

A Regular Expression (Regex) is a sequence of characters that forms a search pattern. It is used to check if a string contains a specified pattern, perform text search, and manipulate text.

Python has a built-in package called `re` to work with Regular Expressions.

---

## 1. Common `re` Functions

* `re.search(pattern, string)`: Returns a Match object if there is a match anywhere in the string.
* `re.findall(pattern, string)`: Returns a list containing all matches.
* `re.split(pattern, string)`: Returns a list where the string has been split at each match.
* `re.sub(pattern, replace, string)`: Replaces matches with a specified string.

```python
import re

txt = "The rain in Spain"

# search()
x = re.search("rain", txt)
if x:
    print("Match found!")

# findall()
print(re.findall("ai", txt))  # Output: ['ai', 'ai']
```

---

## 2. Capture Groups

Parentheses `()` are used in regular expressions to define groups of characters. You can extract individual parts of a matched string using the `group()` method on a Match object.

* `group(0)`: Returns the entire matched string.
* `group(1)`: Returns the first parenthesized subgroup.
* `group(2)`: Returns the second parenthesized subgroup.

```python
import re

text = "My phone number is 123-456-7890"
pattern = r"(\d{3})-(\d{3})-(\d{4})"  # Three capture groups

match = re.search(pattern, text)

if match:
    print(match.group(0))  # Full match: 123-456-7890
    print(match.group(1))  # Area code: 123
    print(match.group(2))  # Prefix: 456
    print(match.group(3))  # Line number: 7890
```

---

## 3. Reusing Patterns: `re.compile()`

If you plan to reuse the same regular expression pattern multiple times in your script, it is highly recommended to pre-compile the pattern using `re.compile()`. This optimizes performance and keeps your code cleaner.

```python
import re

# Compile the pattern once
phone_pattern = re.compile(r"\d{3}-\d{3}-\d{4}")

lines = [
    "Call 123-456-7890 for support",
    "Or dial 987-654-3210 for sales"
]

# Use the compiled pattern
for line in lines:
    matches = phone_pattern.findall(line)
    print(matches)
```

---

## 4. Meta-characters Reference

* `[]`: A set of characters (e.g. `[a-m]`).
* `.`: Any character except newline.
* `^`: Starts with (e.g. `^Hello`).
* `$`: Ends with (e.g. `World$`).
* `*`: Zero or more occurrences.
* `+`: One or more occurrences.
* `\d`: Returns a match where the string contains digits (numbers 0-9).
* `\s`: Returns a match where the string contains a white space character.
* `\w`: Returns a match where the string contains word characters (alphanumeric and underscore).

---

## Further Reading

- [Official Python Docs — Regular Expression Operations](https://docs.python.org/3/library/re.html)
- [Official Python Docs — Regular Expression HowTo Guide](https://docs.python.org/3/howto/regex.html)
