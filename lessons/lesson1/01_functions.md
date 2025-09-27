# Lesson 1: Functions - The Recipe Box

## What is a Function? 🍳

Think of a function like a **recipe** in a cookbook! 

- A recipe has a **name** (like "Make Pancakes")
- It takes **ingredients** (like eggs, flour, milk)
- It gives you a **result** (delicious pancakes!)

In Python, functions work the same way:

```python
def make_pancakes(eggs, flour, milk):
    # This is the recipe (the instructions)
    return "Yummy pancakes!"
```

## Let's Break It Down 🔍

```python
def get_prime_factors(n):  # ← This is the function name
    # This is where the magic happens
    return factors  # ← This gives back the answer
```

- `def` = "I'm making a new recipe"
- `get_prime_factors` = "This recipe is called 'get_prime_factors'"
- `(n)` = "This recipe needs one ingredient called 'n'"
- `return` = "Here's what this recipe makes"

## Real-World Example 🏠

Imagine you have a function called `count_toys`:

```python
def count_toys(toy_box):
    return len(toy_box)

# Using the function:
my_toys = ["doll", "car", "ball"]
number_of_toys = count_toys(my_toys)
print(number_of_toys)  # This prints: 3
```

## Practice Problems 🎯

### Problem 1: Make Your Own Function
Create a function called `say_hello` that takes a name and says "Hello, [name]!"

**Hint:** 
```python
def say_hello(name):
    # Your code here
    return "Hello, " + name + "!"
```

### Problem 2: Math Function
Create a function called `double_number` that takes a number and returns double that number.

**Example:** If you give it 5, it should return 10.

### Problem 3: Favorite Color Function
Create a function called `my_favorite_color` that takes a color and returns "My favorite color is [color]!"

### Problem 4: Test Your Functions
Write code to test all three functions you created above.

**Example:**
```python
print(say_hello("Winston"))
print(double_number(7))
print(my_favorite_color("blue"))
```

## What You Learned Today 📚

- Functions are like recipes
- Functions have names and take ingredients (parameters)
- Functions give back results (return values)
- You can create your own functions with `def`

## Next Lesson
Tomorrow we'll learn about **Variables** - the labeled boxes that hold our information!
