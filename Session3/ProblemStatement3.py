#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implement a function longestWord() that takes a list of words and returns the longest one.
"""

def longestWord(ls):
    if len(ls) > 0:
        longest_word = ls[0]
        for i in ls[1:]:
            if len(i) > len(longest_word):
                longest_word = i
        return longest_word
    else:
        print("The list is empty!")

list_of_words = ["My", "Name", "Is", "Kamlesh"]
print("List: ", list_of_words)
print("The longest word from the list is:", longestWord(list_of_words))