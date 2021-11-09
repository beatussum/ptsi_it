#! /usr/bin/env python3


## 2.1

def Signe(frac):
    a, b = frac

    if b < 0:
        a *= -1
        b *= -1

    return [a, b]

## 2.2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

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

def Prod(fl, fr):
    a, b = fl
    c, d = fr

    return Irred([a * c, b * d])

## 2.4

def Somme(fl, fr):
    a, b = fl
    c, d = fr

    return Irred([ a * d + c * b, b * d])

## 2.5

def Somme2(fl, fr):
    a, b = fr
    c, d = fl

    print(f"On a {a}/{b} + {c}/{d} = {Somme(fl, fr)}.")
