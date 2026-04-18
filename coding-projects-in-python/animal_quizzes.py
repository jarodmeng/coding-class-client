#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 15:59:28 2025

@author: jarodm
"""

print("Guess the Animal!")
score = 0

answer_1 = input("Which bear lives at the North Pole?")
if answer_1 != "polar bear":
    answer_1 = input("Sorry. wrong answer. Try again.")
    if answer_1 != "polar bear":
        answer_1 = input("Sorry. wrong answer. Try again.")
        if answer_1 != "polar bear":
            print("The correct answer is polar bear")
        else:
            score = score + 1
            print("Correct answer")
    else:
        score = score + 1
        print("Correct answer")
else:
    score = score + 1
    print("Correct answer")

answer_2 = input("Which is the fastest land animal?")
if answer_2 != "cheetah":
    answer_2 = input("Sorry. wrong answer. Try again.")
    if answer_2 != "cheetah":
        answer_2 = input("Sorry. wrong answer. Try again.")
        if answer_2 != "cheetah":
            print("The correct answer is cheetah")
        else:
            score = score + 1
            print("Correct answer")
    else:
        score = score + 1
        print("Correct answer")
else:
    score = score + 1
    print("Correct answer")

answer_3 = input("Which is the largest animal?")
if answer_3 != "blue whale":
    answer_3 = input("Sorry. wrong answer. Try again.")
    if answer_3 != "blue whale":
        answer_3 = input("Sorry. wrong answer. Try again.")
        if answer_3 != "blue whale":
            print("The correct answer is blue whale")
        else:
            score = score + 1
            print("Correct answer")
    else:
        score = score + 1
        print("Correct answer")
else:
    score = score + 1
    print("Correct answer")
    
print("Your score is", score)