#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:35:50 2025

@author: jarodm
"""

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
# this line prints out extraction of 1 element
print(months[2])
# this line prints out splicing of a list
print(months[2:3])
print(months[2:4])
# this line prints out an empty list
print(months[2:2])
# this line prints an error because splicing is done
# using a :, not a ,
print(months[2,3])