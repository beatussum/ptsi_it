#! /usr/bin/env python3


def TriSelecRecPartiel(l, a, b):
    if b > ( a + 1 ):
        min_index = a
        min_value = l[a]

        for i in range(a, b):
            if l[i] < min_value:
                min_index = i
                min_value = l[i]

        l[min_index], l[a] = l[a], l[min_index]

        TriSelecRecPartiel(l, a + 1, b)

def TriSelecRec(l):
    return TriSelecRecPartiel(l, 0, len(l))

def TriInsertRecPartiel(l, a, b):
    if b > ( a + 1 ):
        if l[0] > l[1]:
            l[0], l[1] = l[1], l[0]

        for j in range(b - 1, a, -1):
            if l[j - 1] > l[j]:
                l[j - 1], l[j] = l[j], l[j - 1]

        TriInsertRecPartiel(l, a + 1, b)

def TriInsertRec(l):
    return TriInsertRecPartiel(l, 0, len(l))