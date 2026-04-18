#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 23:35:41 2025

@author: jarodm
"""

import turtle

# Generate first n Fibonacci numbers
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# Draw Fibonacci spiral using turtle
def draw_fibonacci_spiral(n):
    try:
        turtle.bye()
    except:
        pass  # no window to close

    fib_nums = fibonacci(n)
    
    t = turtle.Turtle()
    t.pensize(2)
    t.speed("fastest")

    for i in range(n):
        length = fib_nums[i] * 5  # scale factor to make it visible
        t.forward(length)
        t.left(90)

    # Draw spiral arcs
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()

    for i in range(n):
        t.circle(-fib_nums[i] * 5, 90)  # quarter circle

    turtle.done()

# Run it with 10 Fibonacci numbers
draw_fibonacci_spiral(11)