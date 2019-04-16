#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a Python program to reverse a word after accepting the input from the user.
"""

user_input = input("Please enter anything: ")
user_input = user_input.strip()
print("Reverse:", user_input[::-1])