#! /usr/bin/env python3


## 2.1

"""
1. On observe quatre cas possibles: [-a,b],[a,b],[-a,-b],[a,-b].
Ainsi les seuls cas où il est nécessaire de changer l'affichage de la
fraction sont quand b est négatif. Ces deux cas sont donc traités en
retournant [-a,-b].
"""

def Signe(frac):
    a, b = frac

    if b < 0:
        a *= -1
        b *= -1

    return [a, b]

## 2.2

"""
2. Tant que le reste de la division euclidienne de "a" par "b" n'est pas nul,
la fonction PGCD va assigner à "a" le nombre "b", et à "b" le reste de la
division euclidienne précédente. La fonction retourne au final "a", le PGCD
de "a" et "b".
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

"""
La fonction Irred va tout d'abord convertir la fraction à l'aide de la
fonction Signe définie précédemment afin d'obtenir une fraction avec un
dénominateur strictement positif, puis elle attribue à "a" et (respectivement
à "b") le quotient de la division euclidienne de "a" (respectivement "b") par
"g".
"""

def Irred(frac):
    a, b = Signe(frac)

    g = gcd(a, b)
    a //= g
    b //= g

    if b == 1:
        return a
    else:
        return [a, b]

## 2.3

"""
3. La fonction Prod renvoie simplement le produit de deux fractions sous forme
irréductible en multipliant leurs dénominateurs et leurs numérateurs entre
eux.
"""

def Prod(fl, fr):
    a, b = fl
    c, d = fr

    return Irred([a * c, b * d])

## 2.4

"""
4.La fonction Somme retourne une fraction avec pour dénominateur le produit
des dénominateurs des deux fractions, et pour numérateur la somme des
produits croisés des deux fractions.
"""

def Somme(fl, fr):
    a, b = fl
    c, d = fr

    return Irred([ a * d + c * b, b * d])

## 2.5

"""
5.La fonction Somme2 retourne le résultat de la fonction Somme de manière
plus visuelle à l'aide d'une phrase.
"""

def Somme2(fl, fr):
    a, b = fr
    c, d = fl

    print(f"On a {a}/{b} + {c}/{d} = {Somme(fl, fr)}.")
