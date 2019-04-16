#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name.strip() + " " + last_name.strip()

print("="*10)
print("Your full name is:", full_name)
print("You full name in reverse order is:", full_name[::-1])