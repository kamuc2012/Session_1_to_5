#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""

def division(val, by):
    try:
        print("{} / {} = {}".format(val, by, val/by))
    except ZeroDivisionError as ex:
        print("Exception:", ex)

division(5, 0)