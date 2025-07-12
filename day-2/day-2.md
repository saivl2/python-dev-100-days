# 🐍 Day 2: Summary Notes

## 1. 🔢 Primitive Data Types

Python has four basic data types:

| Type     | Description                      | Example           |
|----------|----------------------------------|-------------------|
| `int`    | Whole numbers                    | `10`, `-5`        |
| `float`  | Decimal numbers                  | `3.14`, `-0.01`   |
| `str`    | Text (strings)                   | `"Hello"`         |
| `bool`   | Boolean values                   | `True`, `False`   |

```python
age = 25          # int
height = 5.7      # float
name = "Alice"    # str
is_happy = True   # bool
```

Use `type()` to check a variable’s type:

```python
print(type(age))      # <class 'int'>
print(type(name))     # <class 'str'>
```

---

## 2. ❌ Type Errors and ✅ Type Casting

Python doesn’t let you mix types carelessly:

```python
age = 25
print("You are " + age + " years old")  # ❌ TypeError
```

Fix using **type casting** (conversion):

```python
print("You are " + str(age) + " years old")  # ✅
```

### Casting functions:
- `int("3")` → `3`
- `float("2.5")` → `2.5`
- `str(100)` → `"100"`
- `bool(0)` → `False`, `bool("Hi")` → `True`

---

## 3. ➕ Math Operators

Python supports basic math:

| Operator | Description         | Example       |
|----------|---------------------|---------------|
| `+`      | Addition             | `3 + 2` → `5` |
| `-`      | Subtraction          | `5 - 1` → `4` |
| `*`      | Multiplication       | `2 * 3` → `6` |
| `/`      | Division             | `5 / 2` → `2.5` |
| `//`     | Floor Division       | `5 // 2` → `2` |
| `%`      | Modulo (remainder)   | `5 % 2` → `1` |
| `**`     | Power                | `2 ** 3` → `8` |

---

## 4. 🧮 Math Functions

Python has built-in math utilities:

```python
print(round(3.14159, 2))  # 3.14
print(round(7.6))         # 8
print(abs(-10))           # 10 (absolute value)
```

- `round(value, digits)` → Rounds to given decimal places
- `abs(number)` → Returns positive version

---

## 5. 💬 f-Strings (Formatted Strings)

f-strings let you insert variables into strings cleanly:

```python
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old.")
print(f"In 5 years, I'll be {age + 5}")
```

You can format numbers too:

```python
pi = 3.14159
print(f"Pi is approximately {pi:.2f}")  # Pi is approximately 3.14
```

---

## 6. ✂️ String Indexing

Strings are ordered collections of characters. You can access each character by its position (index):

```python
word = "Python"
print(word[0])     # 'P' (first character)
print(word[1])     # 'y'
print(word[-1])    # 'n' (last character)
print(word[0:3])   # 'Pyt' (slicing from index 0 to 2)
```

- Index starts at 0.
- Negative indices count from the end.
- You can slice with `[start:stop]` (stop is exclusive).

---

## 7. 🧠 Built-in Functions

Python gives you useful functions right out of the box:

| Function   | Description                      |
|------------|----------------------------------|
| `print()`  | Displays output                   |
| `input()`  | Takes user input (as string)      |
| `type()`   | Checks data type                  |
| `len()`    | Length of a string/collection     |
| `str()`, `int()`, `float()`, `bool()` | Type conversion |
| `round()`  | Rounds a number                   |
| `abs()`    | Absolute value                    |

```python
print(len("Python"))     # 6
print(type(3.14))        # <class 'float'>
```

---

## 8. 🧭 What Is a Function?

- A **function** is a block of code that performs a specific task.
- You **call** functions using parentheses: `function_name(arguments)`
- Examples:
```python
print("Hello")
type(10)
round(3.7)
```
---