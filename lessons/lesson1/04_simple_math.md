# Lesson 4: Simple Math - The Calculator Symbols 🧮

## What is Math in Python? ➕

Python can do math just like a calculator! It has special symbols for different operations.

## The Basic Math Symbols 🔢

```python
# Addition
result = 5 + 3
print(result)  # Prints: 8

# Subtraction  
result = 10 - 4
print(result)  # Prints: 6

# Multiplication
result = 6 * 7
print(result)  # Prints: 42

# Division
result = 15 / 3
print(result)  # Prints: 5.0
```

## Special Math Symbols We Use in Our Function 🔍

### The Modulo Symbol: `%` (What's Left Over?)
```python
# % means "what's left over when we divide"
print(10 % 3)  # Prints: 1 (because 10 ÷ 3 = 3 with 1 left over)
print(8 % 2)   # Prints: 0 (because 8 ÷ 2 = 4 with 0 left over)
print(7 % 2)   # Prints: 1 (because 7 ÷ 2 = 3 with 1 left over)
```

**When is a number even?** When `number % 2 == 0` (no remainder when divided by 2)

### The Integer Division Symbol: `//` (Throw Away Decimals)
```python
# // means "divide and throw away the decimal part"
print(10 // 3)  # Prints: 3 (not 3.333...)
print(8 // 2)   # Prints: 4
print(7 // 2)   # Prints: 3 (not 3.5)
```

### The Power Symbol: `**` (Exponents)
```python
# ** means "to the power of"
print(2 ** 3)   # Prints: 8 (2 × 2 × 2)
print(5 ** 2)   # Prints: 25 (5 × 5)
print(3 ** 4)   # Prints: 81 (3 × 3 × 3 × 3)
```

## In Our Prime Factor Function 🔍

Look at these special math operations:

```python
while n % 2 == 0:     # ← Is n even? (no remainder when divided by 2)
    n = n // 2        # ← Divide n by 2 and throw away decimals

while i * i <= n:     # ← Is i² less than or equal to n?
    i += 2            # ← Add 2 to i (same as i = i + 2)
```

## Practice Problems 🎯

### Problem 1: Basic Math Practice
```python
# Calculate these and print the results:
a = 12
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Integer division:", a // b)
print("Remainder:", a % b)
```

### Problem 2: Even or Odd?
```python
# Check if these numbers are even or odd:
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
```

### Problem 3: Powers and Roots
```python
# Calculate these powers:
print("2 to the power of 3:", 2 ** 3)
print("5 to the power of 2:", 5 ** 2)
print("3 to the power of 4:", 3 ** 4)

# Check if these are perfect squares:
numbers = [4, 9, 16, 25, 30]
for num in numbers:
    root = num ** 0.5  # Square root
    if root == int(root):  # If root is a whole number
        print(f"{num} is a perfect square (√{num} = {int(root)})")
    else:
        print(f"{num} is not a perfect square")
```

### Problem 4: Division Practice
```python
# Practice with division and remainders:
dividend = 17
divisor = 5

quotient = dividend // divisor    # How many times does 5 go into 17?
remainder = dividend % divisor    # What's left over?

print(f"{dividend} ÷ {divisor} = {quotient} with remainder {remainder}")
print(f"Check: {divisor} × {quotient} + {remainder} = {divisor * quotient + remainder}")
```

### Problem 5: Building a Simple Calculator
```python
# Create a simple calculator:
def simple_calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    elif operation == "//":
        return a // b
    elif operation == "%":
        return a % b
    else:
        return "Unknown operation"

# Test your calculator:
print(simple_calculator(10, 3, "+"))   # Should print: 13
print(simple_calculator(10, 3, "-"))   # Should print: 7
print(simple_calculator(10, 3, "*"))   # Should print: 30
print(simple_calculator(10, 3, "/"))   # Should print: 3.333...
print(simple_calculator(10, 3, "//"))  # Should print: 3
print(simple_calculator(10, 3, "%"))   # Should print: 1
```

## Math Order of Operations 📐

Python follows the same rules as regular math:

1. **Parentheses** `()` first
2. **Exponents** `**` second  
3. **Multiplication** `*` and **Division** `/` third
4. **Addition** `+` and **Subtraction** `-` last

```python
result = 2 + 3 * 4        # = 2 + 12 = 14
result = (2 + 3) * 4      # = 5 * 4 = 20
result = 2 ** 3 + 1       # = 8 + 1 = 9
result = 2 ** (3 + 1)     # = 2 ** 4 = 16
```

## What You Learned Today 📚

- `+` for addition, `-` for subtraction
- `*` for multiplication, `/` for division
- `//` for integer division (throw away decimals)
- `%` for remainder (what's left over)
- `**` for powers (exponents)
- Math follows order of operations rules

## Next Week Preview 🔮

Next week we'll learn about **Making Decisions** with `if` statements - how to tell Python to do different things based on what we find!

## Challenge Problem 🏆

Can you figure out what this code does?

```python
def mystery_math(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n * 3 + 1

# Try it with different numbers:
print(mystery_math(4))   # What does this print?
print(mystery_math(5))   # What does this print?
print(mystery_math(6))   # What does this print?
```
