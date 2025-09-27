# Lesson 2: Variables - The Labeled Boxes 📦

## What is a Variable? 🏷️

A variable is like a **labeled box** where you can store things!

Imagine you have boxes with labels:
- Box labeled "my_age" contains the number 10
- Box labeled "my_name" contains the word "Winston"
- Box labeled "my_favorite_number" contains the number 7

In Python, it looks like this:

```python
my_age = 10
my_name = "Winston"
my_favorite_number = 7
```

## Let's See It in Action! 🎬

```python
# Create some boxes (variables)
name = "Ido"
age = 10
favorite_color = "green"

# Look inside the boxes
print(name)           # Prints: Ido
print(age)            # Prints: 10
print(favorite_color) # Prints: green
```

## Changing What's in the Box 🔄

You can change what's inside a variable anytime:

```python
score = 5
print(score)  # Prints: 5

score = 8     # Put something new in the box
print(score)  # Prints: 8
```

## Different Types of Boxes 📦

Variables can hold different types of things:

```python
# Numbers
my_number = 42
my_decimal = 3.14

# Words (we call these "strings")
my_name = "Winston"
my_greeting = "Hello!"

# Lists (like a shopping bag)
my_toys = ["doll", "car", "ball"]
my_numbers = [1, 2, 3, 4, 5]
```

## In Our Prime Factor Function 🔍

Look at this part of our function:

```python
def get_prime_factors(n):
    factors = []        # ← Empty box for our factors
    i = 3              # ← Box with number 3
    while i * i <= n:  # ← Using the box in math
        # ... more code ...
        i += 2         # ← Changing what's in the box
```

- `factors = []` - Create an empty box called "factors"
- `i = 3` - Create a box called "i" and put 3 in it
- `i += 2` - Take what's in the "i" box, add 2, and put it back

## Practice Problems 🎯

### Problem 1: Create Your Own Variables
Create variables to store:
- Your name
- Your age
- Your favorite food
- Your favorite number

Then print them all out!

### Problem 2: Math with Variables
```python
# Create these variables
a = 10
b = 5

# Now calculate and print:
# 1. a + b
# 2. a - b  
# 3. a * b
# 4. a / b
```

### Problem 3: Changing Variables
```python
# Start with this
count = 0
print("Starting count:", count)

# Add 1 to count
count = count + 1
print("After adding 1:", count)

# Add 1 more
count = count + 1
print("After adding 1 more:", count)

# What will this print?
count += 1  # This is the same as count = count + 1
print("After += 1:", count)
```

### Problem 4: Variable Mixing
```python
# Create these variables
first_name = "Winston"
last_name = "Smith"
age = 10

# Create a new variable that combines first_name and last_name
full_name = first_name + " " + last_name
print("Full name:", full_name)

# Create a sentence using all variables
sentence = "My name is " + full_name + " and I am " + str(age) + " years old."
print(sentence)
```

## Special Variable Rules 📋

1. **Variable names can't start with numbers**
   - ✅ `my_variable = 5`
   - ❌ `2my_variable = 5`

2. **Use underscores or letters**
   - ✅ `my_name`, `age`, `favorite_color`
   - ❌ `my name` (spaces not allowed)

3. **Be descriptive**
   - ✅ `student_age = 10`
   - ❌ `x = 10` (not clear what x means)

## What You Learned Today 📚

- Variables are like labeled boxes
- You can put different types of things in variables
- You can change what's in a variable
- Variables help us remember and use information

## Next Lesson
Tomorrow we'll learn about **Lists** - special boxes that can hold many things in order!
