# Tokens

A token is the smallest individual unit in a Python program. When Python reads your code, it breaks it down into these tokens to understand and execute it.

There are five main types of tokens in Python:

## 1. Keywords

Keywords are reserved words that have a fixed, predefined meaning in Python. You cannot use them as names for variables, functions, or classes.

* **Examples**: `if`, `else`, `while`, `for`, `def`, `class`, `import`, `return`, `True`, `False`, `None`.

## 2. Identifiers

Identifiers are names given to identify variables, functions, classes, modules, or other objects.

### Rules for Naming Identifiers

* Must start with a letter (a-z, A-Z) or an underscore (`_`).
* Cannot start with a number.
* Can only contain alphanumeric characters and underscores (`a-z`, `A-Z`, `0-9`, and `_`).
* Are case-sensitive (e.g., `age`, `Age`, and `AGE` are three different identifiers).
* Cannot be a keyword.

## 3. Literals

Literals are the raw data or constant values assigned to variables.

* **String Literals**: `"Hello"`, `'Python'`
* **Numeric Literals**: `10` (integer), `3.14` (float)
* **Boolean Literals**: `True`, `False`
* **Special Literal**: `None` (denotes the absence of a value)

## 4. Operators

Operators are symbols that trigger operations on variables and values.

* **Examples**: `+`, `-`, `*`, `/`, `=`, `==`, `>`, `<`.

## 5. Delimiters / Punctuators

Delimiters are characters used to separate, group, or organize statements and expressions.

* **Examples**: `(`, `)`, `[`, `]`, `{`, `}`, `,`, `:`, `.`, `;`.

---

## Example Breakdown

Consider the following line of code:

```python
x = 10
```

* `x` is an **Identifier** (variable name).
* `=` is an **Operator** (assignment).
* `10` is a **Literal** (numeric integer value).
