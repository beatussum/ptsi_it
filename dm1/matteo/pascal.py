#! /usr/bin/env python3


import numpy, sys, time

## Fonctions utilitaires

"""
Affiche un message sur l'erreur standard.
"""

def printerr(msg):
    print(msg, file = sys.stderr)

"""
Implémentation d'un chronomètre.

À la création de l'instance, une date est stockée ; à sa déstruction, on
affiche la différence entre le temps présent et le temps précédemment conservé.
En d'autres termes, on affiche le temps de vie de l'instance qui, dans le
contexte d'utilisation, correspond au temps d'exécution d'une fonction donnée.
"""

class Timer:
    def __init__(self, procname):
        self.procname = procname
        self.btime = time.time()

    def __del__(self):
        delta = time.time() - self.btime
        printerr(f"{self.procname}\u00A0: le processus a mis {delta} secondes.")

"""
Implémentation de la fonction factorielle.

Cette implémentation utilise une fonction récursive et suit donc la définition
de la fonction mathématique originelle.

On a donc `n - 1` opérations.
"""

def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)

"""
Implémentation du calcul d'un coefficient binomial.

On a donc `( n - 1 ) + ( p - 1 ) + ( n - p - 1) + 2 = 2 n - 1` opérations.
"""

def bicoeff(n, p):
    return factorielle(n) / ( factorielle(p) * factorielle(n - p) )

## 3.1

"""
- On initialise un `Timer`.
- On initialise un tableau d'entier vide de dimension `(n + 1, n + 1)`.
- On boucle sur chaque ligne d'une tableau.
   - On boucle sur chaque colonne :
      - Si l'indice de la colonne est inférieur à celui de la colonne, alors on
        initialise la case en question par le coefficient binomial adéquate.
      - Sinon, la case est initialisé à zéro.
- On retourne le tableau.

On a donc pour chaque ligne d'indice `i`, `i` coefficient binomial à calculer.
Pour chaque coefficient binomial, on a `2 i - 1` opérations.
Pour les `n + 1` lignes, on a donc `( ( n + 1 ) ( n + 2 ) ( 4 n + 9 ) ) / 6`
opérations.
"""

def triangle_Pascal(n):
    t = Timer("triangle de Pascal (brute force)")

    ret = numpy.empty((n + 1, n + 1), int)

    for i in range(n + 1):
        for j in range(n + 1):
            if j <= i:
                ret[i, j] = bicoeff(i, j)
            else:
                ret[i, j] = 0

    return ret

## 3.3

"""
- On initialise un `Timer`.
- On initialise un tableau d'entier vide de dimension `(n + 1, n + 1)`.
- On boucle sur chaque ligne d'une tableau.
   - On boucle sur chaque colonne :
      - Si l'indice de la colonne est nul, on initialise à la case à `1`.
      - Si celui-ci est inférieur à l'indice de la ligne, on utilise la formule
        de Pascal pour initialiser la case en question.
      - Sinon, on initilise la case à `0`.
- On retourne le tableau.

Pour chaque ligne d'indice `i`, on a `i` sommes.
Pour chaque somme, on a une seule opération.
Pour les `n` lignes (faisant appel à une somme), on a donc `( n ( n + 1) ) / 2`
opérations.
"""

def triangle_Pascal2(n):
    t = Timer("triangle de Pascal (intelligent)")

    ret = numpy.empty((n + 1, n + 1), int)

    for i in range(n + 1):
        for j in range(n + 1):
            if j == 0:
                ret[i, j] = 1
            elif j <= i:
                ret[i, j] = ret[i - 1, j - 1] + ret[i - 1, j]
            else:
                ret[i, j] = 0

    return ret

## 3.4

"""
- On initialise un tableau avec un triangle de Pascal de dimension choisie.
- On boucle sur chaque ligne du tableau.
   - On boucle sur chaque colonne.
      - Si le nombre est pair, alors on imprime un espace.
      - Sinon, on imprime une étoile.
   - On imprime un retour à la ligne.
"""

def sierpinski(n):
    pascal = triangle_Pascal2(n - 1)

    for i in range(n):
        for j in range(i + 1):
            if ( pascal[i, j] % 2 ) == 0:
                print(" ", end = "")
            else:
                print("*", end = "")

        print()

## Tests

#print(triangle_Pascal(3))
#print(triangle_Pascal2(3))
#sierpinski(16)
