#!/usr/bin/env python3
# Python Practice File for Winston and Ido
# This is where you can try out all the code from your lessons!

import sys

def main():
    print("Welcome to Python Practice! 🐍")
    print("=" * 40)
    print("Choose which lesson to practice:")
    print("1. Functions - The Recipe Box")
    print("2. Variables - The Labeled Boxes") 
    print("3. Lists - The Shopping Bags")
    print("4. Simple Math - The Calculator Symbols")
    print("5. Challenge Problems")
    print("6. Run All Lessons")
    print("0. Exit")
    
    choice = input("\nEnter your choice (0-6): ").strip()
    
    if choice == "1":
        lesson1_functions()
    elif choice == "2":
        lesson2_variables()
    elif choice == "3":
        lesson3_lists()
    elif choice == "4":
        lesson4_math()
    elif choice == "5":
        challenge_problems()
    elif choice == "6":
        run_all_lessons()
    elif choice == "0":
        print("Goodbye! Keep practicing! 👋")
        return
    else:
        print("Invalid choice. Please try again.")
        main()

def lesson1_functions():
    print("\n🍳 LESSON 1: FUNCTIONS")
    print("-" * 30)
    print("INSTRUCTIONS:")
    print("1. Look at the example functions below")
    print("2. Uncomment the 'YOUR TURN' sections by removing the # symbols")
    print("3. Edit the code to complete the problems")
    print("4. Run the file to test if your code works!")
    print("-" * 30)
    
    # Example function from the lesson
    def say_hello(name):
        return "Hello, " + name + "!"
    
    # Try it out!
    print("Example function:")
    print(say_hello("Winston"))
    print(say_hello("Ido"))
    
    print("\n" + "="*50)
    print("YOUR TURN: Uncomment and edit the code below!")
    print("="*50)
    
    # Problem 1: Make a function called double_number
    # def double_number(number):
    #     # Your code here - what should this function do?
    #     # Hint: return the number multiplied by 2
    #     pass  # Replace this with your code
    
    # Test your function (uncomment when ready)
    # print("Testing double_number function:")
    # test_cases = [
    #     (5, 10),    # 5 should become 10
    #     (0, 0),     # 0 should stay 0
    #     (7, 14),    # 7 should become 14
    #     (-3, -6)    # -3 should become -6
    # ]
    # 
    # all_passed = True
    # for input_val, expected in test_cases:
    #     result = double_number(input_val)
    #     if result == expected:
    #         print(f"✅ double_number({input_val}) = {result} (CORRECT)")
    #     else:
    #         print(f"❌ double_number({input_val}) = {result}, expected {expected} (WRONG)")
    #         all_passed = False
    # 
    # if all_passed:
    #     print("🎉 All double_number tests passed!")
    # else:
    #     print("💪 Keep trying! Fix the errors above.")
    
    # Problem 2: Make a function called my_favorite_color
    # def my_favorite_color(color):
    #     # Your code here - what should this function do?
    #     # Hint: return "My favorite color is " + color + "!"
    #     pass  # Replace this with your code
    
    # Test your function (uncomment when ready)
    # print("\nTesting my_favorite_color function:")
    # test_cases = [
    #     ("blue", "My favorite color is blue!"),
    #     ("red", "My favorite color is red!"),
    #     ("green", "My favorite color is green!")
    # ]
    # 
    # all_passed = True
    # for input_color, expected in test_cases:
    #     result = my_favorite_color(input_color)
    #     if result == expected:
    #         print(f"✅ my_favorite_color('{input_color}') = '{result}' (CORRECT)")
    #     else:
    #         print(f"❌ my_favorite_color('{input_color}') = '{result}', expected '{expected}' (WRONG)")
    #         all_passed = False
    # 
    # if all_passed:
    #     print("🎉 All my_favorite_color tests passed!")
    # else:
    #     print("💪 Keep trying! Fix the errors above.")
    
    # Problem 3: Make a function called add_numbers
    # def add_numbers(a, b):
    #     # Your code here - add a and b together
    #     pass  # Replace this with your code
    
    # Test your function (uncomment when ready)
    # print("\nTesting add_numbers function:")
    # test_cases = [
    #     (3, 4, 7),      # 3 + 4 = 7
    #     (10, 7, 17),    # 10 + 7 = 17
    #     (0, 5, 5),      # 0 + 5 = 5
    #     (-2, 3, 1),     # -2 + 3 = 1
    #     (100, 200, 300) # 100 + 200 = 300
    # ]
    # 
    # all_passed = True
    # for a, b, expected in test_cases:
    #     result = add_numbers(a, b)
    #     if result == expected:
    #         print(f"✅ add_numbers({a}, {b}) = {result} (CORRECT)")
    #     else:
    #         print(f"❌ add_numbers({a}, {b}) = {result}, expected {expected} (WRONG)")
    #         all_passed = False
    # 
    # if all_passed:
    #     print("🎉 All add_numbers tests passed!")
    # else:
    #     print("💪 Keep trying! Fix the errors above.")
    
    print("\n✅ Instructions complete! Edit the code above and run again to test!")
    input("Press Enter to continue...")
    main()

def lesson2_variables():
    print("\n📦 LESSON 2: VARIABLES")
    print("-" * 30)
    print("INSTRUCTIONS:")
    print("1. Look at the example variables below")
    print("2. Uncomment the 'YOUR TURN' sections by removing the # symbols")
    print("3. Edit the code to complete the problems")
    print("4. Run the file to test if your code works!")
    print("-" * 30)
    
    # Create some variables (labeled boxes)
    my_name = "Winston"
    my_age = 10
    my_favorite_food = "pizza"
    my_favorite_number = 7
    
    # Look inside the boxes
    print("Example variables:")
    print("My name:", my_name)
    print("My age:", my_age)
    print("My favorite food:", my_favorite_food)
    print("My favorite number:", my_favorite_number)
    
    print("\n" + "="*50)
    print("YOUR TURN: Uncomment and edit the code below!")
    print("="*50)
    
    # Problem 1: Create variables for your information
    # your_name = "Ido"  # Change this to your name
    # your_age = 10      # Change this to your age
    # your_favorite_sport = "soccer"  # Add your favorite sport
    
    # Test your variables (uncomment when ready)
    # print("Testing your personal information:")
    # 
    # # Test 1: Check if variables are strings
    # if isinstance(your_name, str) and len(your_name) > 0:
    #     print(f"✅ your_name = '{your_name}' (CORRECT - it's a string)")
    # else:
    #     print(f"❌ your_name = {your_name} (WRONG - should be a non-empty string)")
    # 
    # if isinstance(your_age, int) and your_age > 0:
    #     print(f"✅ your_age = {your_age} (CORRECT - it's a positive number)")
    # else:
    #     print(f"❌ your_age = {your_age} (WRONG - should be a positive number)")
    # 
    # if isinstance(your_favorite_sport, str) and len(your_favorite_sport) > 0:
    #     print(f"✅ your_favorite_sport = '{your_favorite_sport}' (CORRECT - it's a string)")
    # else:
    #     print(f"❌ your_favorite_sport = {your_favorite_sport} (WRONG - should be a non-empty string)")
    
    # Problem 2: Math with variables
    # a = 10
    # b = 5
    # 
    # # Test math operations
    # print("\nTesting math with variables:")
    # math_tests = [
    #     (a + b, 15, "addition"),
    #     (a - b, 5, "subtraction"),
    #     (a * b, 50, "multiplication"),
    #     (a / b, 2.0, "division")
    # ]
    # 
    # all_passed = True
    # for result, expected, operation in math_tests:
    #     if result == expected:
    #         print(f"✅ {a} {operation[0]} {b} = {result} (CORRECT)")
    #     else:
    #         print(f"❌ {a} {operation[0]} {b} = {result}, expected {expected} (WRONG)")
    #         all_passed = False
    # 
    # if all_passed:
    #     print("🎉 All math tests passed!")
    # else:
    #     print("💪 Keep trying! Fix the errors above.")
    
    # Problem 3: Create variables for your family
    # family_size = 4  # How many people in your family?
    # pets = 2         # How many pets do you have?
    # total_legs = family_size * 2 + pets * 4  # Calculate total legs!
    # 
    # # Test family calculations
    # print("\nTesting family calculations:")
    # expected_legs = family_size * 2 + pets * 4
    # 
    # if total_legs == expected_legs:
    #     print(f"✅ Total legs calculation: {family_size} people + {pets} pets = {total_legs} legs (CORRECT)")
    # else:
    #     print(f"❌ Total legs calculation: {total_legs}, expected {expected_legs} (WRONG)")
    # 
    # # Test if variables are reasonable numbers
    # if family_size > 0 and family_size < 20:
    #     print(f"✅ family_size = {family_size} (CORRECT - reasonable number)")
    # else:
    #     print(f"❌ family_size = {family_size} (WRONG - should be between 1 and 19)")
    # 
    # if pets >= 0 and pets < 10:
    #     print(f"✅ pets = {pets} (CORRECT - reasonable number)")
    # else:
    #     print(f"❌ pets = {pets} (WRONG - should be between 0 and 9)")
    
    print("\n✅ Instructions complete! Edit the code above and run again to test!")
    input("Press Enter to continue...")
    main()

def lesson3_lists():
    print("\n🛍️ LESSON 3: LISTS")
    print("-" * 30)
    print("INSTRUCTIONS:")
    print("1. Look at the example lists below")
    print("2. Uncomment the 'YOUR TURN' sections by removing the # symbols")
    print("3. Edit the code to complete the problems")
    print("4. Run the file to test if your code works!")
    print("-" * 30)
    
    # Create some lists (shopping bags)
    fruits = ["apple", "banana", "orange"]
    toys = ["doll", "car", "ball"]
    numbers = [1, 2, 3, 4, 5]
    
    print("Example lists:")
    print("Fruits:", fruits)
    print("Toys:", toys)
    print("Numbers:", numbers)
    
    # Count items in lists
    print("Number of fruits:", len(fruits))
    print("Number of toys:", len(toys))
    
    # Look at specific items (remember: counting starts at 0!)
    print("First fruit:", fruits[0])
    print("Second fruit:", fruits[1])
    print("Third fruit:", fruits[2])
    
    # Add items to lists
    fruits.append("grape")
    print("After adding grape:", fruits)
    
    print("\n" + "="*50)
    print("YOUR TURN: Uncomment and edit the code below!")
    print("="*50)
    
    # Problem 1: Create a list of your favorite foods
    # my_favorite_foods = ["pizza", "ice cream", "chocolate"]
    
    # Test your favorite foods list (uncomment when ready)
    # print("Testing favorite foods list:")
    # 
    # # Test 1: Check if it's a list
    # if isinstance(my_favorite_foods, list):
    #     print("✅ my_favorite_foods is a list (CORRECT)")
    # else:
    #     print("❌ my_favorite_foods is not a list (WRONG)")
    # 
    # # Test 2: Check if it has at least 3 items
    # if len(my_favorite_foods) >= 3:
    #     print(f"✅ List has {len(my_favorite_foods)} items (CORRECT - at least 3)")
    # else:
    #     print(f"❌ List has {len(my_favorite_foods)} items (WRONG - need at least 3)")
    # 
    # # Test 3: Check if all items are strings
    # all_strings = all(isinstance(item, str) for item in my_favorite_foods)
    # if all_strings:
    #     print("✅ All items are strings (CORRECT)")
    # else:
    #     print("❌ Not all items are strings (WRONG)")
    # 
    # print(f"Your foods: {my_favorite_foods}")
    
    # Problem 2: Create a list of your favorite numbers
    # my_favorite_numbers = [7, 14, 21, 28]
    
    # Test your favorite numbers list (uncomment when ready)
    # print("\nTesting favorite numbers list:")
    # 
    # # Test 1: Check if it's a list
    # if isinstance(my_favorite_numbers, list):
    #     print("✅ my_favorite_numbers is a list (CORRECT)")
    # else:
    #     print("❌ my_favorite_numbers is not a list (WRONG)")
    # 
    # # Test 2: Check if it has at least 4 items
    # if len(my_favorite_numbers) >= 4:
    #     print(f"✅ List has {len(my_favorite_numbers)} items (CORRECT - at least 4)")
    # else:
    #     print(f"❌ List has {len(my_favorite_numbers)} items (WRONG - need at least 4)")
    # 
    # # Test 3: Check if all items are numbers
    # all_numbers = all(isinstance(item, (int, float)) for item in my_favorite_numbers)
    # if all_numbers:
    #     print("✅ All items are numbers (CORRECT)")
    # else:
    #     print("❌ Not all items are numbers (WRONG)")
    # 
    # print(f"Your numbers: {my_favorite_numbers}")
    
    # Problem 3: Add more items to your lists
    # my_favorite_foods.append("cookies")
    # my_favorite_numbers.append(35)
    
    # Test adding items (uncomment when ready)
    # print("\nTesting adding items to lists:")
    # 
    # # Test if foods list grew by 1
    # if len(my_favorite_foods) >= 4:  # Should have at least 4 items now
    #     print("✅ Foods list grew after adding item (CORRECT)")
    # else:
    #     print("❌ Foods list didn't grow properly (WRONG)")
    # 
    # # Test if numbers list grew by 1
    # if len(my_favorite_numbers) >= 5:  # Should have at least 5 items now
    #     print("✅ Numbers list grew after adding item (CORRECT)")
    # else:
    #     print("❌ Numbers list didn't grow properly (WRONG)")
    # 
    # print(f"Updated foods: {my_favorite_foods}")
    # print(f"Updated numbers: {my_favorite_numbers}")
    
    # Problem 4: Create a shopping list
    # shopping_list = []
    # shopping_list.append("milk")
    # shopping_list.append("bread")
    # shopping_list.append("apples")
    
    # Test shopping list (uncomment when ready)
    # print("\nTesting shopping list:")
    # 
    # # Test 1: Check if it's a list
    # if isinstance(shopping_list, list):
    #     print("✅ shopping_list is a list (CORRECT)")
    # else:
    #     print("❌ shopping_list is not a list (WRONG)")
    # 
    # # Test 2: Check if it has exactly 3 items
    # if len(shopping_list) == 3:
    #     print(f"✅ Shopping list has {len(shopping_list)} items (CORRECT)")
    # else:
    #     print(f"❌ Shopping list has {len(shopping_list)} items, expected 3 (WRONG)")
    # 
    # # Test 3: Check specific items
    # expected_items = ["milk", "bread", "apples"]
    # if shopping_list == expected_items:
    #     print("✅ Shopping list has correct items (CORRECT)")
    # else:
    #     print(f"❌ Shopping list = {shopping_list}, expected {expected_items} (WRONG)")
    # 
    # print(f"Your shopping list: {shopping_list}")
    
    # Problem 5: Look at specific items in your list
    # first_item = shopping_list[0]
    # last_item = shopping_list[-1]  # -1 means the last item
    
    # Test accessing specific items (uncomment when ready)
    # print("\nTesting access to specific items:")
    # 
    # # Test first item
    # if first_item == "milk":
    #     print(f"✅ First item is '{first_item}' (CORRECT)")
    # else:
    #     print(f"❌ First item is '{first_item}', expected 'milk' (WRONG)")
    # 
    # # Test last item
    # if last_item == "apples":
    #     print(f"✅ Last item is '{last_item}' (CORRECT)")
    # else:
    #     print(f"❌ Last item is '{last_item}', expected 'apples' (WRONG)")
    # 
    # print(f"First item: {first_item}")
    # print(f"Last item: {last_item}")
    
    print("\n✅ Instructions complete! Edit the code above and run again to test!")
    input("Press Enter to continue...")
    main()

def lesson4_math():
    print("\n🧮 LESSON 4: SIMPLE MATH")
    print("-" * 30)
    print("INSTRUCTIONS:")
    print("1. Look at the example math below")
    print("2. Uncomment the 'YOUR TURN' sections by removing the # symbols")
    print("3. Edit the code to complete the problems")
    print("4. Run the file to test if your code works!")
    print("-" * 30)
    
    # Basic math
    print("Example basic math:")
    print("5 + 3 =", 5 + 3)
    print("10 - 4 =", 10 - 4)
    print("6 * 7 =", 6 * 7)
    print("15 / 3 =", 15 / 3)
    
    # Special math symbols
    print("\nExample special math symbols:")
    print("10 % 3 =", 10 % 3, "(remainder when 10 ÷ 3)")
    print("8 % 2 =", 8 % 2, "(remainder when 8 ÷ 2)")
    print("7 % 2 =", 7 % 2, "(remainder when 7 ÷ 2)")
    
    print("10 // 3 =", 10 // 3, "(10 ÷ 3, throw away decimals)")
    print("8 // 2 =", 8 // 2, "(8 ÷ 2)")
    print("7 // 2 =", 7 // 2, "(7 ÷ 2, throw away decimals)")
    
    print("2 ** 3 =", 2 ** 3, "(2 to the power of 3)")
    print("5 ** 2 =", 5 ** 2, "(5 to the power of 2)")
    
    print("\n" + "="*50)
    print("YOUR TURN: Uncomment and edit the code below!")
    print("="*50)
    
    # Problem 1: Try some basic math
    # a = 12
    # b = 4
    # 
    # # Test basic math operations
    # print("Testing basic math operations:")
    # math_tests = [
    #     (a + b, 16, "addition"),
    #     (a - b, 8, "subtraction"),
    #     (a * b, 48, "multiplication"),
    #     (a / b, 3.0, "division")
    # ]
    # 
    # all_passed = True
    # for result, expected, operation in math_tests:
    #     if result == expected:
    #         print(f"✅ {a} {operation[0]} {b} = {result} (CORRECT)")
    #     else:
    #         print(f"❌ {a} {operation[0]} {b} = {result}, expected {expected} (WRONG)")
    #         all_passed = False
    # 
    # if all_passed:
    #     print("🎉 All basic math tests passed!")
    # else:
    #     print("💪 Keep trying! Fix the errors above.")
    
    # Problem 2: Try special math symbols
    # c = 15
    # d = 6
    # 
    # # Test special math operations
    # print("\nTesting special math operations:")
    # special_tests = [
    #     (c % d, 3, "modulo (remainder)"),
    #     (c // d, 2, "integer division"),
    #     (c ** 2, 225, "exponentiation (squared)")
    # ]
    # 
    # all_passed = True
    # for result, expected, operation in special_tests:
    #     if result == expected:
    #         print(f"✅ {c} {operation[0]} {d} = {result} (CORRECT)")
    #     else:
    #         print(f"❌ {c} {operation[0]} {d} = {result}, expected {expected} (WRONG)")
    #         all_passed = False
    # 
    # if all_passed:
    #     print("🎉 All special math tests passed!")
    # else:
    #     print("💪 Keep trying! Fix the errors above.")
    
    # Problem 3: Check if numbers are even or odd
    # numbers_to_check = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 
    # # Test even/odd checker
    # print("\nTesting even/odd checker:")
    # expected_results = [True, False, True, False, True, False, True, False, True]  # True = even, False = odd
    # 
    # all_passed = True
    # for i, num in enumerate(numbers_to_check):
    #     is_even = num % 2 == 0
    #     expected = expected_results[i]
    #     
    #     if is_even == expected:
    #         status = "even" if is_even else "odd"
    #         print(f"✅ {num} is {status} (CORRECT)")
    #     else:
    #         expected_status = "even" if expected else "odd"
    #         actual_status = "even" if is_even else "odd"
    #         print(f"❌ {num} is {actual_status}, expected {expected_status} (WRONG)")
    #         all_passed = False
    # 
    # if all_passed:
    #     print("🎉 All even/odd tests passed!")
    # else:
    #     print("💪 Keep trying! Fix the errors above.")
    
    # Problem 4: Calculate area and perimeter
    # length = 8
    # width = 5
    # area = length * width
    # perimeter = 2 * (length + width)
    # 
    # # Test geometry calculations
    # print("\nTesting geometry calculations:")
    # 
    # # Test area calculation
    # expected_area = 40
    # if area == expected_area:
    #     print(f"✅ Area calculation: {length} × {width} = {area} (CORRECT)")
    # else:
    #     print(f"❌ Area calculation: {area}, expected {expected_area} (WRONG)")
    # 
    # # Test perimeter calculation
    # expected_perimeter = 26
    # if perimeter == expected_perimeter:
    #     print(f"✅ Perimeter calculation: 2 × ({length} + {width}) = {perimeter} (CORRECT)")
    # else:
    #     print(f"❌ Perimeter calculation: {perimeter}, expected {expected_perimeter} (WRONG)")
    # 
    # # Test if both calculations are correct
    # if area == expected_area and perimeter == expected_perimeter:
    #     print("🎉 All geometry tests passed!")
    # else:
    #     print("💪 Keep trying! Fix the errors above.")
    # 
    # print(f"Rectangle: {length} × {width}")
    # print(f"Area: {area}")
    # print(f"Perimeter: {perimeter}")
    
    print("\n✅ Instructions complete! Edit the code above and run again to test!")
    input("Press Enter to continue...")
    main()

def challenge_problems():
    print("\n🏆 CHALLENGE PROBLEMS")
    print("-" * 30)
    print("INSTRUCTIONS:")
    print("1. Look at the example challenges below")
    print("2. Uncomment the 'YOUR TURN' sections by removing the # symbols")
    print("3. Edit the code to complete the challenges")
    print("4. Run the file to test if your code works!")
    print("-" * 30)
    
    # Challenge 1: Build a simple calculator
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
    
    # Test the calculator
    print("Example calculator tests:")
    print("10 + 3 =", simple_calculator(10, 3, "+"))
    print("10 - 3 =", simple_calculator(10, 3, "-"))
    print("10 * 3 =", simple_calculator(10, 3, "*"))
    print("10 / 3 =", simple_calculator(10, 3, "/"))
    print("10 // 3 =", simple_calculator(10, 3, "//"))
    print("10 % 3 =", simple_calculator(10, 3, "%"))
    
    print("\n" + "="*50)
    print("YOUR TURN: Uncomment and edit the code below!")
    print("="*50)
    
    # Challenge 1: Build a shopping list
    # shopping_list = []
    # shopping_list.append("milk")
    # shopping_list.append("bread")
    # shopping_list.append("apples")
    # shopping_list.append("cookies")
    
    # Test shopping list (uncomment when ready)
    # print("Testing shopping list simulator:")
    # 
    # # Test 1: Check if it's a list
    # if isinstance(shopping_list, list):
    #     print("✅ shopping_list is a list (CORRECT)")
    # else:
    #     print("❌ shopping_list is not a list (WRONG)")
    # 
    # # Test 2: Check if it has exactly 4 items
    # if len(shopping_list) == 4:
    #     print(f"✅ Shopping list has {len(shopping_list)} items (CORRECT)")
    # else:
    #     print(f"❌ Shopping list has {len(shopping_list)} items, expected 4 (WRONG)")
    # 
    # # Test 3: Check specific items
    # expected_items = ["milk", "bread", "apples", "cookies"]
    # if shopping_list == expected_items:
    #     print("✅ Shopping list has correct items (CORRECT)")
    # else:
    #     print(f"❌ Shopping list = {shopping_list}, expected {expected_items} (WRONG)")
    # 
    # print(f"Your shopping list: {shopping_list}")
    # print(f"Total items to buy: {len(shopping_list)}")
    
    # Challenge 2: Create a function to calculate the area of a circle
    # def circle_area(radius):
    #     # Formula: area = π * radius²
    #     # Use 3.14 for π
    #     pi = 3.14
    #     area = pi * radius * radius
    #     return area
    
    # Test circle area function (uncomment when ready)
    # print("\nTesting circle area function:")
    # 
    # # Test cases: (radius, expected_area)
    # test_cases = [
    #     (5, 78.5),    # 3.14 * 5² = 78.5
    #     (3, 28.26),   # 3.14 * 3² = 28.26
    #     (1, 3.14),    # 3.14 * 1² = 3.14
    #     (0, 0.0)      # 3.14 * 0² = 0.0
    # ]
    # 
    # all_passed = True
    # for radius, expected in test_cases:
    #     result = circle_area(radius)
    #     if abs(result - expected) < 0.01:  # Allow small floating point differences
    #         print(f"✅ circle_area({radius}) = {result} (CORRECT)")
    #     else:
    #         print(f"❌ circle_area({radius}) = {result}, expected {expected} (WRONG)")
    #         all_passed = False
    # 
    # if all_passed:
    #     print("🎉 All circle area tests passed!")
    # else:
    #     print("💪 Keep trying! Fix the errors above.")
    
    # Challenge 3: Create a function to check if a number is prime
    # def is_prime(number):
    #     if number < 2:
    #         return False
    #     for i in range(2, number):
    #         if number % i == 0:
    #             return False
    #     return True
    
    # Test prime checker function (uncomment when ready)
    # print("\nTesting prime number checker:")
    # 
    # # Test cases: (number, expected_result)
    # test_cases = [
    #     (2, True),   # 2 is prime
    #     (3, True),   # 3 is prime
    #     (4, False),  # 4 is not prime (2×2)
    #     (5, True),   # 5 is prime
    #     (6, False),  # 6 is not prime (2×3)
    #     (7, True),   # 7 is prime
    #     (8, False),  # 8 is not prime (2×4)
    #     (9, False),  # 9 is not prime (3×3)
    #     (10, False), # 10 is not prime (2×5)
    #     (1, False),  # 1 is not prime
    #     (0, False)   # 0 is not prime
    # ]
    # 
    # all_passed = True
    # for number, expected in test_cases:
    #     result = is_prime(number)
    #     if result == expected:
    #         status = "prime" if result else "not prime"
    #         print(f"✅ {number} is {status} (CORRECT)")
    #     else:
    #         expected_status = "prime" if expected else "not prime"
    #         actual_status = "prime" if result else "not prime"
    #         print(f"❌ {number} is {actual_status}, expected {expected_status} (WRONG)")
    #         all_passed = False
    # 
    # if all_passed:
    #     print("🎉 All prime number tests passed!")
    # else:
    #     print("💪 Keep trying! Fix the errors above.")
    
    print("\n✅ Instructions complete! Edit the code above and run again to test!")
    input("Press Enter to continue...")
    main()

def run_all_lessons():
    print("\n🚀 RUNNING ALL LESSONS")
    print("=" * 50)
    
    lesson1_functions()
    lesson2_variables()
    lesson3_lists()
    lesson4_math()
    challenge_problems()
    
    print("\n🎉 Congratulations! You've completed all lessons!")
    print("You're well on your way to becoming a Python programmer!")
    input("Press Enter to return to main menu...")
    main()

# =============================================================================
# MAIN EXECUTION - This runs when you start the program
# =============================================================================

if __name__ == "__main__":
    main()
