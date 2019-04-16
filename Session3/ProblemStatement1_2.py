#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()
"""

# to check if number is odd or not
def is_odd(a):
    return a % 2

# function will accept function and list and return the list (filtered) as output
def myfilter(func, ls):
    return_list = []
    for i in ls:
        if func(i):
            return_list.append(i)
    return return_list

ls = [1, 2, 3, 4, 5]
print("List of odd integers:", myfilter(is_odd, ls))