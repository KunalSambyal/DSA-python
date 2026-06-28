# File Handling

File handling allows your program to persist data by creating, reading, updating, and deleting files on disk.

---

## 1. Opening a File: The `open()` Function and Modes

To work with files, use the `open(filename, mode)` function.

### File Modes
* **`"r"` (Read)**: Default. Opens a file for reading. Raises `FileNotFoundError` if the file doesn't exist.
* **`"w"` (Write)**: Opens a file for writing. Overwrites existing content or creates a new file.
* **`"a"` (Append)**: Appends data to the end of the file. Creates a new file if needed.
* **`"x"` (Create)**: Creates a new file. Raises `FileExistsError` if the file already exists.
* **`"b"` (Binary)**: Opens the file in binary mode (e.g., for images, PDFs).

---

## 2. Using the `with` Statement (Recommended)

Always open files using the `with` statement. It serves as a context manager that automatically closes the file once the block finishes, even if an error is raised inside.

```python
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
# File is automatically closed here!
```

---

## 3. Reading Methods

* `read()`: Reads the entire file content as a single string.
* `readline()`: Reads a single line from the file.
* `readlines()`: Reads all lines and returns them as a list of strings.
* **Looping**: Iterates through lines efficiently without loading the whole file into memory.

```python
# Reading line-by-line using a loop (preferred)
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())  # strip() removes extra newlines
```

---

## 4. Writing JSON and CSV Files

### Writing and Reading JSON
The `json` module provides `json.dump()` to write a Python dictionary to a file as JSON, and `json.load()` to parse JSON files back into dictionaries.

```python
import json

data = {"name": "Alice", "scores": [95, 87, 92]}

# Write JSON to disk
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Read JSON from disk
with open("data.json", "r") as f:
    loaded_data = json.load(f)
    print(loaded_data["name"])  # Output: Alice
```

### Writing and Reading CSV
Use Python's built-in `csv` module to write and read spreadsheets.

```python
import csv

# Writing to a CSV file
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Score"])  # Header
    writer.writerow(["Alice", 95])
    writer.writerow(["Bob", 87])

# Reading from a CSV file
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Score"])
```

---

## 5. Modern Path Handling: `pathlib`

The standard `pathlib` module is a modern, object-oriented alternative to `os.path` for navigating the filesystem.

```python
from pathlib import Path

# Create a path object
p = Path("my_folder") / "data.txt"

print(p.exists())  # Check if path exists (True/False)
print(p.suffix)  # Output: .txt (file extension)
print(p.stem)    # Output: data (file name without extension)
```

---

## Common Mistakes

### Opening a File Without `with`
If you open a file manually using `f = open()`, you must remember to call `f.close()`. If you don't, the file remains locked in memory by the OS, which can lead to memory leaks, file corruption, or error locks.

```python
# Incorrect (Risky):
f = open("sample.txt", "w")
f.write("Hello")
# If an error happens here, f.close() is never called!
f.close()

# Correct:
with open("sample.txt", "w") as f:
    f.write("Hello")
```

---

## Further Reading

- [Official Python Docs — Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Official Python Docs — pathlib](https://docs.python.org/3/library/pathlib.html)
