#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a Python Program(with class concepts) to find the area of the triangle using the below formula.

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass.
"""

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.s = (self.a + self.b + self.c) / 2

class Area(Triangle):
    def calculate(self):
        return (self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c)) ** 0.5

obj = Area(5, 6, 7)
print("Aria of triangle is {}".format(obj.calculate()))