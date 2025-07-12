# 🐍 Day 1: Summary Notes


## 1. 🖨️ Print Statements

The `print()` function is used to display messages or outputs to the screen. It’s one of the most basic and essential tools when starting with Python.

- **Purpose**: Show messages, debug, or display results.
- **Automatic newline**: Each `print()` adds a new line by default.

```python
print("Hello, World!")         # Prints a greeting
print("Name:", "Alice")        # You can print multiple values
```

You can also separate multiple items with commas, and Python will insert spaces automatically.

---

## 2. 🔡 Escape Characters

Escape characters allow you to format your text output or include special characters inside a string.

| Escape | Meaning             |
|--------|---------------------|
| `\n`   | New line             |
| `\t`   | Tab space            |
| `\\`   | Backslash (`\`)      |
| `\"`   | Double quote         |
| `\'`   | Single quote         |

```python
print("Hello\tWorld!\nWelcome to Python!")
print("She said, \"Python is fun!\"")
```

These are useful for formatting long strings and making your output more readable.

---

## 3. 🧑‍💻 Input from User

You can take input from the user using the `input()` function. This function pauses the program and waits for the user to type something and press Enter.

- **Always returns a string**, even if the user types a number.
- You can store the input in a variable for later use.

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

To use the input as a number (e.g., age), convert it:

```python
age = int(input("Enter your age: "))
print("Next year, you'll be", age + 1)
```

---

## 4. ❌ Common Errors

When you’re just starting, you’ll run into errors often — and that’s okay! Here are some typical beginner mistakes:

| Error Type        | When it Happens                            |
|-------------------|---------------------------------------------|
| `SyntaxError`     | The code structure is wrong (e.g., missing `:` or `)`) |
| `IndentationError`| Improper use of spaces/tabs                 |
| `NameError`       | Using a variable that hasn’t been defined   |
| `TypeError`       | Using the wrong type with an operation      |

Example:
```python
print("Hello"     # ❌ Missing closing parenthesis → SyntaxError
name = "Alice"
print(nme)        # ❌ Typo → NameError
```

---

## 5. 🛠️ Debugging Tips

Don’t panic when you see red errors! Here's how to debug:

- **Read error messages**: Python tells you the exact line and type of error.
- **Check**:
  - Are all parentheses and quotes closed?
  - Are variable names spelled correctly?
  - Are you using consistent indentation (spaces vs. tabs)?
  - Did you use the correct data type?

Debugging is a skill — the more errors you see, the more you learn.

---

## 6. 📦 Variables

Variables let you **store data** and reuse it later. Think of them as containers with names.

### Naming Rules:
- Start with a letter or `_`, not a number.
- Can contain letters, digits, and underscores.
- **Case-sensitive**: `Name`, `name`, and `NAME` are all different.
- Avoid Python keywords (like `print`, `input`, `for`).

```python
user_name = "Alice"
user_age = 25
```

You can update a variable by reassigning it:

```python
user_age = user_age + 1
```

---

## 7. 🧵 Strings

Strings are text data, enclosed in either single or double quotes.

```python
greeting = "Hello"
quote = 'Python is fun!'
```

Python treats `'Hello'` and `"Hello"` the same, but be consistent. Use escape characters if you need quotes inside quotes.

---

## 8. ✂️ String Manipulation

You can modify, combine, or access parts of a string.

### Concatenation (joining strings):

```python
first = "Hello"
name = "Alice"
print(first + " " + name)
```

### Useful string operations:

```python
s = "Python"

print(len(s))      # Length of string → 6
print(s.upper())   # 'PYTHON'
print(s.lower())   # 'python'
print(s[0])        # First character → 'P'
print(s[-1])       # Last character → 'n'
```

Strings are **zero-indexed**, meaning the first character is at position 0.

---




