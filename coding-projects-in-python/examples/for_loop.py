#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 14:36:42 2025

@author: jarodm
"""

# First way of using range() function
# range(stop)
# The default start is 0 and the default step is 1
# for counter in range(11):
#     print(counter)
# for counter in range(0, 11, 1):
#     print(counter)

# Second way of using range() function
# range(start, stop)
# The default step is 1
# for counter in range(1, 11):
#     print(counter)

# Third way of using range() function
# range(start, stop, step)
# for counter in range(1, 11, 2):
#     print(counter)
    
# A range() function to print output
# 10, 20, 30, 40, ..., 100
# for counter in range(10, 101, 10):
#     print(counter)
# for counter in range(1, 11):
#     print(counter * 10)

# For loop using a list
# for counter in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     print(counter)
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for counter in numbers[0:5]:
    print(counter)