#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
"""

def is_vowel(ch):
    if len(ch) == 1:
        if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
            return True
        else:
            return False
    else:
        return False

ch = 'A'
print("If '{}' is a vowel character:".format(ch), is_vowel(ch))