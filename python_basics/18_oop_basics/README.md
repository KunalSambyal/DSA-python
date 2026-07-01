# Object-Oriented Programming (OOP) Basics

Object-Oriented Programming (OOP) is a programming paradigm that uses **Classes** and **Objects** to organize code, making it reusable, modular, and easy to scale.

---

## 1. Classes and Objects

* **Class**: A blueprint or template for creating objects.
* **Object**: An instance of a class.

```python
class Dog:
    pass

my_dog = Dog()  # Instantiating a new object
```

### The `__init__()` Method and `self`
The `__init__()` function is a special method (constructor) that runs automatically every time a new object is created from a class.
* **`self`**: Represents the current instance of the class and is used to access instance variables.

```python
class Dog:
    def __init__(self, name):
        self.name = name  # Instance variable
```

---

## 2. Class Variables vs. Instance Variables

* **Instance Variables**: Unique to each object instance, defined inside `__init__()`.
* **Class Variables**: Shared by all instances of a class, defined directly in the class body.

```python
class Dog:
    species = "Canis lupus familiaris"  # Class variable (shared)

    def __init__(self, name):
        self.name = name  # Instance variable (unique)

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.species)  # Output: Canis lupus familiaris
print(dog1.name)     # Output: Buddy
print(dog2.name)     # Output: Max
```

---

## 3. Special Dunder Methods (`__str__` and `__repr__`)

Dunder (double underscore) methods are special built-in methods. 
* **`__str__`**: Controls what `print(object)` or `str(object)` displays (user-friendly string).
* **`__repr__`**: Controls the official string representation of the object (often used for debugging).

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"Dog named {self.name} ({self.breed})"

    def __repr__(self):
        return f"Dog(name='{self.name}', breed='{self.breed}')"

my_dog = Dog("Buddy", "Labrador")
print(my_dog)       # Output via __str__: Dog named Buddy (Labrador)
print(repr(my_dog)) # Output via __repr__: Dog(name='Buddy', breed='Labrador')
```

---

## 4. Inheritance and `super()`

Inheritance allows a Child class to inherit attributes and methods from a Parent class. Use the `super()` function to call the parent class's constructor or methods.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling parent's __init__
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy", "Labrador")
print(my_dog.eat())   # Output: Buddy is eating. (Inherited method)
print(my_dog.bark())  # Output: Buddy says Woof!
```

---

## 5. Class Methods and Static Methods

* **`@classmethod`**: Receives the class (`cls`) as the first argument instead of the instance (`self`). Can access class variables and modify class state.
* **`@staticmethod`**: Does not receive `self` or `cls`. It behaves like a normal function utility attached to the class namespace.

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(5, 10))  # Output: 15 (called directly on Class)
```

---

## 6. The `@property` Decorator (Getters and Setters)

The `@property` decorator allows you to access a method like a normal attribute, while still enabling validation checks when setting values.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # _ prefix implies internal/protected attribute

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

c = Circle(5)
print(c.radius)  # Output: 5 (accessed as an attribute, not c.radius())
c.radius = 10    # Valid update
# c.radius = -1  # Raises ValueError: Radius cannot be negative
```

---

## Common Mistakes

### Forgetting `self` as the First Parameter
Every instance method must accept `self` as its first parameter to represent the object calling it. If you forget to include `self` in the method signature, Python will raise a `TypeError` when you call the method on an instance.

```python
# Incorrect:
class Dog:
    def bark():
        return "Woof!"

# Correct:
class Dog:
    def bark(self):
        return "Woof!"
```

---

## Further Reading

- [Official Python Docs — Classes](https://docs.python.org/3/tutorial/classes.html)
- [Official Python Docs — Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
