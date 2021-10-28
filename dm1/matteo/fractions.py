#! /usr/bin/env python3


## 2.1

def Signe(frac):
    a, b = frac

    if ( a < 0 ) == ( b < 0 ):
        a = abs(a)
        b = abs(b)
    else:
        a = - abs(a)
        b = abs(b)

    return [a, b]

## 2.2

def maxmin(a, b):
    if a > b:
        return a, b
    else:
        return b, a

def gcd(a, b):
    a, b = maxmin(a, b)

    if (a, b) == (0, 0):
        raise ZeroDivisionError()
    elif ( a == 1 ) or ( b == 1 ):
        return 1
    elif ( a == b ) or ( b == 0 ):
        return abs(a)
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
