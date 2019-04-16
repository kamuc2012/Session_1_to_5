#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a program which accepts a sequence of comma-separated numbers from console and generate a list.
"""

numbers = input("Please enter comma-separated numbers: ")

list_numbers = []
for i in numbers.split(","):
    list_numbers.append(int(i))

print("Comma Separated List:", list_numbers)