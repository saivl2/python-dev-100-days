# 🐍 Day 3: Summary Notes
### 🔄 1. Flow of Control

**Flow of control** means how Python decides **which lines of code to run** and in what order.

Without conditions, Python runs top to bottom. But using conditionals, we can alter this flow.



```python
print("Start")

if True:
    print("Inside if block")

print("End")
```

**Output:**
```
Start  
Inside if block  
End
```

---

### 🧩 2. `if`, `elif`, `else` Statements

Used to perform **decision-making**.

```python
temperature = 25

if temperature > 30:
    print("It's hot outside.")
elif temperature >= 20:
    print("Nice weather.")
else:
    print("It's cold!")
```

- `if` → First condition
- `elif` → Additional condition(s)
- `else` → Executes if no above conditions are true

---

### 🧮 3. Comparison Operators

Used to compare two values and return a Boolean (`True`/`False`).

| Operator | Meaning              | Example       | Result     |
|----------|----------------------|---------------|------------|
| `==`     | Equal to             | `5 == 5`      | `True`     |
| `!=`     | Not equal to         | `5 != 3`      | `True`     |
| `>`      | Greater than         | `10 > 2`      | `True`     |
| `<`      | Less than            | `3 < 5`       | `True`     |
| `>=`     | Greater or equal     | `5 >= 5`      | `True`     |
| `<=`     | Less or equal        | `4 <= 7`      | `True`     |

Example:

```python
x = 7
y = 10

print(x == y)   # False
print(x <= y)   # True
```

---

### 🧱 4. Nested Conditionals

You can **nest `if` statements** inside another `if` block. This is useful when you need to check further conditions **only if a previous one is met**.

```python
score = 92

if score >= 50:
    print("You passed!")

    if score >= 90:
        print("Excellent performance!")
    else:
        print("Good job, keep improving.")
else:
    print("You failed. Try again.")
```

---

### 🔗 5. Logical Operators

Logical operators combine multiple conditions:

| Operator | Description                      | Example                    | Result     |
|----------|----------------------------------|----------------------------|------------|
| `and`    | True if **both** are true        | `5 > 3 and 10 > 2`         | `True`     |
| `or`     | True if **at least one** is true | `5 > 3 or 10 < 2`          | `True`     |
| `not`    | Inverts the result               | `not (5 > 3)`              | `False`    |

Examples:

```python
age = 22
has_ticket = True

# AND
if age > 18 and has_ticket:
    print("You can enter.")

# OR
if age > 18 or has_ticket:
    print("At least one condition is true.")

# NOT
if not age < 18:
    print("You are an adult.")
```
Conditional logic is **the backbone of decision-making** in Python. It allows us to control how the program responds to different inputs and situations.

---
