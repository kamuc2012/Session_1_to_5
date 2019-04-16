#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
"""

def filter_words_by_length(list_of_words, n):
    return_list = []
    for i in list_of_words:
        if len(i) > n:
            return_list.append(i)

    if len(return_list) == 0:
        return "None"
    else:
        return return_list

list_of_words = ["My", "Name", "Is", "Kamlesh"]
n = 4

print("List of words:", list_of_words)
print("List of words having length greater than {}:".format(n), filter_words_by_length(list_of_words, n))