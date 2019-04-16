#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a program which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
in a comma-separated sequence on a single line.
"""

output = ""
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        output += str(i) + ", "

if output == "":
    print("No number found.")
else:
    output = output[:-2]
    print(output)