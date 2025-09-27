# Lesson 3: Lists - The Shopping Bags 🛍️

## What is a List? 🎒

A list is like a **shopping bag** that can hold many things in order!

Think of your backpack:
- First pocket: pencil
- Second pocket: eraser  
- Third pocket: ruler
- Fourth pocket: calculator

In Python, it looks like this:

```python
my_backpack = ["pencil", "eraser", "ruler", "calculator"]
```

## Let's Explore Lists! 🔍

```python
# Create a list
fruits = ["apple", "banana", "orange"]
print(fruits)  # Prints: ['apple', 'banana', 'orange']

# Count how many items
print(len(fruits))  # Prints: 3

# Look at specific items
print(fruits[0])  # Prints: apple (first item)
print(fruits[1])  # Prints: banana (second item)
print(fruits[2])  # Prints: orange (third item)
```

## Important: Counting Starts at 0! 🔢

In Python, we start counting at 0, not 1:

```python
my_list = ["A", "B", "C", "D"]
# Position:   0    1    2    3
#            ↑    ↑    ↑    ↑
#          first second third fourth
```

## Adding Things to Your List ➕

```python
toys = ["doll"]           # Start with one toy
toys.append("car")        # Add a car
toys.append("ball")       # Add a ball
print(toys)               # Prints: ['doll', 'car', 'ball']
```

## In Our Prime Factor Function 🔍

Look at this part:

```python
def get_prime_factors(n):
    factors = []          # ← Empty shopping bag
    while n % 2 == 0:     # ← While we can divide by 2
        factors.append(2) # ← Add 2 to our bag
        n = n // 2        # ← Make n smaller
```

- `factors = []` - Create an empty shopping bag
- `factors.append(2)` - Put a 2 in the bag
- Each time we find a factor, we add it to our bag!

## Practice Problems 🎯

### Problem 1: Create Your Own Lists
Create lists for:
- Your 3 favorite foods
- Your 5 favorite numbers
- Your family members' names

Print each list and count how many items are in each!

### Problem 2: List Positions
```python
colors = ["red", "green", "blue", "yellow", "purple"]

# Print each color and its position
print("Position 0:", colors[0])
print("Position 1:", colors[1])
print("Position 2:", colors[2])
print("Position 3:", colors[3])
print("Position 4:", colors[4])

# What happens if you try colors[5]?
```

### Problem 3: Building a List
```python
# Start with an empty list
my_numbers = []

# Add numbers one by one
my_numbers.append(1)
my_numbers.append(3)
my_numbers.append(5)
my_numbers.append(7)

print("My numbers:", my_numbers)
print("How many numbers:", len(my_numbers))
```

### Problem 4: List Math
```python
# Create a list of numbers
numbers = [2, 4, 6, 8, 10]

# Print each number doubled
print("Original numbers:", numbers)
print("Doubled numbers:")
for i in range(len(numbers)):
    doubled = numbers[i] * 2
    print(f"{numbers[i]} doubled is {doubled}")
```

### Problem 5: Shopping List Simulator
```python
# Start with an empty shopping list
shopping_list = []

# Add items to your shopping list
shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.append("apples")
shopping_list.append("cookies")

print("My shopping list:")
for i in range(len(shopping_list)):
    print(f"{i + 1}. {shopping_list[i]}")

print(f"\nTotal items to buy: {len(shopping_list)}")
```

## Special List Tricks 🎪

### Adding Multiple Items at Once
```python
# Instead of adding one by one:
fruits = []
fruits.append("apple")
fruits.append("banana")
fruits.append("orange")

# You can do this:
fruits = ["apple", "banana", "orange"]
```

### Checking if Something is in Your List
```python
toys = ["doll", "car", "ball"]
print("doll" in toys)    # Prints: True
print("truck" in toys)   # Prints: False
```

## What You Learned Today 📚

- Lists are like shopping bags that hold many things
- We count positions starting from 0
- Use `append()` to add things to a list
- Use `len()` to count how many things are in a list
- Lists help us organize and remember many things

## Next Lesson
Tomorrow we'll learn about **Simple Math** - the special symbols that help us do calculations!
