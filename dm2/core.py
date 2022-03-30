#! /usr/bin/env python3


import random

point  = tuple[int, int]
points = list[point]

def random_in(lst: list):
    return lst[random.randint(0, len(lst) - 1)]
