#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create the below pattern using nested for loop in Python.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

max_cols = 5

row = 1
while row <= max_cols:
    col = 1
    while col <= row:
        print("* ", end="")
        col += 1
    row += 1
    print("")

row -= 2
while row > 0:
    col = 1
    while col <= row:
        print("* ", end="")
        col += 1
    row -= 1
    print("")