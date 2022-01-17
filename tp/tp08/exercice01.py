#! /usr/bin/env python3


from copy import deepcopy

def TriSelection(l):
    for i in range(len(l)):
        min_index = i
        min_value = l[i]

        for j in range(i, len(l)):
            if l[j] < min_value:
                min_index = j
                min_value = l[j]

        l[min_index] = l[i]
        l[i]         = min_value

def TriSelectionBis(l):
    return TriSelection(deepcopy(l))