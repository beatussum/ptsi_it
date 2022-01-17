#! /usr/bin/env python3


from copy import deepcopy

def TriInsertion(l):
    if len(l) >= 2:
        for i in range(2, len(l)):
            if l[0] > l[1]:
                l[0], l[1] = l[1], l[0]

            for j in range(i, 0, -1):
                if l[j - 1] > l[j]:
                    l[j - 1], l[j] = l[j], l[j - 1]

def TriInserttionBis(l):
    return TriInsertion(deepcopy(l))