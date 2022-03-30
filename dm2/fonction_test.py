#! /usr/bin/env python3


from core import points

"""
Question 1
"""

def Repetitions(L: list) -> bool:
    counter = []

    for l in L:
        if l in counter:
            return True
        else:
            counter.append(l)

    return False

"""
Question 2
"""

def EstCAE(L: points) -> bool:
    for ((a, b), (x, y)) in zip(L, L[1:]):
        if ( abs(x - a) + abs(y - b) ) != 1:
            return False

    return not Repetitions(L)
