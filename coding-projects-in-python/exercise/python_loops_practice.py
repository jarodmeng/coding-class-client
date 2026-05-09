"""
Python Practice: Loops

For Winston and Ido

Instructions:
1. Fill in the blanks marked ___.
2. Run this file and check the printed answers.
3. Try to explain what changes each time the loop repeats.
"""


# ============================================================
# Question 1: Basic for loop — Animal Lineup
# ============================================================

animals = ["cat", "dog", "rabbit", "panda"]

print("Question 1: Animal Lineup")
print("-------------------------")

# Print each animal, one per line.

for animal in ___:
    print(animal)


print()
print()


# ============================================================
# Question 2: for loop with range — Count from 1 to 5
# ============================================================

print("Question 2: Count from 1 to 5")
print("-----------------------------")

# Print:
# 1
# 2
# 3
# 4
# 5

for number in range(___, ___):
    print(number)


print()
print()


# ============================================================
# Question 3: for loop with range step — Even Numbers
# ============================================================

print("Question 3: Even Numbers")
print("------------------------")

# Print:
# 2
# 4
# 6
# 8
# 10

for number in range(___, ___, ___):
    print(number)


print()
print()


# ============================================================
# Question 4: Accumulator — Total Score
# ============================================================

scores = [10, 20, 15, 5]
total = 0

print("Question 4: Total Score")
print("-----------------------")

# Add all scores into total.
# Expected final total: 50

for score in scores:
    total = ___

print("Total score:", total)


print()
print()


# ============================================================
# Question 5: Conditional inside loop — Count Big Numbers
# ============================================================

numbers = [3, 12, 7, 20, 5, 18]
big_count = 0

print("Question 5: Count Big Numbers")
print("-----------------------------")

# Count how many numbers are greater than 10.
# Expected answer: 3

for number in numbers:
    if ___:
        big_count = ___

print("How many big numbers?", big_count)


print()
print()


# ============================================================
# Question 6: while loop — Rocket Countdown
# ============================================================

count = 5

print("Question 6: Rocket Countdown")
print("----------------------------")

# Print:
# 5
# 4
# 3
# 2
# 1
# Blast off!

while ___:
    print(count)
    count = ___

print("Blast off!")


print()
print()


# ============================================================
# Question 7: while loop — Energy Charger
# ============================================================

energy = 0

print("Question 7: Energy Charger")
print("--------------------------")

# Keep adding 20 energy until energy reaches 100.
# Print energy each time.
#
# Expected:
# 20
# 40
# 60
# 80
# 100

while ___:
    energy = ___
    print(energy)


print()
print()


# ============================================================
# Question 8: A Bit Challenging — Treasure Collector
# ============================================================

items = ["coin", "rock", "ruby", "stick", "coin", "diamond", "leaf"]
treasure_count = 0

print("Question 8: Treasure Collector")
print("------------------------------")

# Count only the treasures.
# Treasures are:
# - "coin"
# - "ruby"
# - "diamond"
#
# Expected answer: 4
#
# Use a for loop and an if statement with OR.

for item in items:
    if ___:
        treasure_count = ___

print("Treasure count:", treasure_count)


# ============================================================
# Extra Thinking Questions
# ============================================================

print()
print("Extra Thinking Questions")
print("------------------------")
print("1. When is a for loop useful?")
print("2. When is a while loop useful?")
print("3. What is an accumulator?")
print("4. What can go wrong if a while loop never stops?")
print("5. How can if statements and loops work together?")
