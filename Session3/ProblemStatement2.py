#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implement List comprehensions to produce the following lists.
"""

# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
list_1 = list("ACADGILD")
print(list_1)

# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
list_2 = list(i*j for i in "xyz" for j in range(1,5))
print(list_2)

# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
occurance = [1, 2, 2, 4]
list_3 = list(i*j for i in occurance for j in "xyz")
print(list_3)

# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
list_4 = list([i+j] for i in range(2,5) for j in range(0,3))
print(list_4)

# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
list_5 = list([i+j for i in range(2,6)] for j in range(0,4))
print(list_5)

# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
occurance = [1, 2, 3]
list_6 = list((i, j) for i in occurance for j in occurance)
print(list_6)