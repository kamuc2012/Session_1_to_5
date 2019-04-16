#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * (r*r*r)
"""

import math

diameter = 12

volume = (4/3) * math.pi * math.pow(diameter/2, 3)
print("Value of sphere with diameter 12 cm is", volume)