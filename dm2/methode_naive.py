#! /usr/bin/env python3


import core
from core import point, points

import matplotlib.pyplot as plt
import numpy

"""
Question 4
"""

def PositionsPossibles(P: point, L: points) -> points:
    x, y    = P
    voisins = []

    for v in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if v not in L:
            voisins.append(v)

    return voisins

"""
Question 5
"""

def CheminNaif(n: int) -> points:
    ret = [(0, 0)]

    if n > 1:
        for _ in range(n - 1):
            possibles = PositionsPossibles(ret[-1], ret)

            if len(possibles) == 0:
                return None
            else:
                ret.append(core.random_in(possibles))

    return ret

"""
Question 7
"""

def AfficheCheminNaif(n: int):
    chemin = None

    while chemin == None:
        chemin = CheminNaif(n)

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


"""
Question 8
"""

def AfficheErreurCheminNaif(N: int, M: int):
    counter = {}

    for n in range(1, N + 1):
        c = 0

        for _ in range(M):
            if CheminNaif(n) == None:
                c += 1

        counter[n] = (c / M) * 100

    x = counter.keys()
    y = counter.values()

    plt.figure("Affichage du taux d'échec de la fonction `CheminNaif()`.")

    plt.bar(x, y)

    plt.title("Affichage du taux d'échec de la fonction `CheminNaif()`.")
    plt.xlabel("$ n $ (sans unité)")
    plt.ylabel("proportion d'echec (en pourcentage)")

    plt.show()
