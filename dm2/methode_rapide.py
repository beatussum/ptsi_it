#! /usr/bin/env python3


from core import point, points

import copy
import matplotlib.pyplot as plt
import numpy
import random
from typing import Any, Callable

"""
Question 9
"""

def OrdreLex(P: point, Q: point) -> bool:
    x, y = P
    a, b = Q

    if x < a:
        return True
    elif x == a:
        return y < b
    else:
        return False

"""
Question 10
"""

def TriOrdre(L: list, ordre: Callable[[Any, Any], bool]) -> list:
    def fusion(lsta: list, lstb: list) -> list:
        if len(lsta) == 0:
            return lstb
        elif len(lstb) == 0:
            return lsta
        elif ordre(lsta[0], lstb[0]):
            return [lsta[0]] + fusion(lsta[1:], lstb)
        else:
            return [lstb[0]] + fusion(lsta, lstb[1:])


    if len(L) < 2:
        return L
    elif len(L) == 2:
        a, b = L

        if ordre(a, b):
            return [a, b]
        else:
            return [b, a]
    else:
        a = TriOrdre(L[:(len(L) // 2)], ordre)
        b = TriOrdre(L[(len(L) // 2):], ordre)

        return fusion(a, b)

"""
Question 11

TODO: une seule boucle ?
"""

def EstCAERapide(L: points) -> bool:
    def recherche_dichotomique(lst: points, l: point) -> bool:
        a = 0
        b = len(lst) - 1

        while a <= b:
            c = ( a + b ) // 2

            if OrdreLex(lst[c], l):
                a = c + 1
            elif OrdreLex(l, lst[c]):
                b = c - 1
            else:
                return True

        return False

    for ((a, b), (x, y)) in zip(L, L[1:]):
        if ( abs(x - a) + abs(y - b) ) != 1:
            return False

    L = TriOrdre(L, OrdreLex)

    for i in range(len(L)):
        if recherche_dichotomique(L[i + 1:], L[i]):
            return False

    return True

"""
Question 12
"""

def rotation(M: point, C: point, a: int) -> point:
    x, y = M
    u, v = C

    alpha = 0
    beta  = 0
    r     = max(abs(x - u), abs(y - v))

    if y - v > 0:
        a += 1
    elif x - u < 0:
        a += 2
    elif y - v < 0:
        a += 3

    if ( a % 4 ) == 0:
        alpha = 1
    elif ( a % 4 ) == 1:
        beta = 1
    elif ( a % 4 ) == 2:
        alpha = -1
    else:
        beta = -1

    return [r * alpha + u, r * beta + v]

"""
Question 13
"""

def GenereCAEPivot(n: int, r: int) -> points:
    ret = [(0, k) for k in range(n)]

    if n >= 2:
        while r != 0:
            pivot = random.randint(0, n - 1)
            rot   = random.randint(1, 3)
            tmp   = copy.deepcopy(ret)

            for i in range(pivot + 1, n):
                tmp[i] = rotation(tmp[i], tmp[pivot], rot)

            if EstCAERapide(tmp):
                print(pivot, rot)

                ret = tmp
                r  -= 1

    return ret

"""
Question 14
"""

def AfficheCAEPivot(n: int, r: int):
    chemin = None

    while chemin == None:
        chemin = GenereCAEPivot(n, r)

    x, y = numpy.transpose(chemin)

    plt.figure("Affichage d'un chemin \"auto-évitant\".")

    plt.plot(x, y, "-+k", label = "chemin")
    plt.plot(x[0], y[0], "ro", label = "point de départ")
    plt.plot(x[-1], y[-1], "go", label = "point d'arrivée")

    plt.title("Affichage d'un chemin \"auto-évitant\".")
    plt.grid()
    plt.legend()
    plt.xticks(numpy.arange(min(x), max(x) + 1, 1))
    plt.yticks(numpy.arange(min(y), max(y) + 1, 1))

    plt.show()
