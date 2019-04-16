#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()
"""

def do_sum(a, b):
    return a + b

def myreduce(func, ls):
    val = None
    if len(ls) > 0:
        val = ls[0]
        for i in ls[1:]:
            val = func(val, i)
    return val

ls = [1, 2, 3, 4, 5]
print(myreduce(do_sum, ls))