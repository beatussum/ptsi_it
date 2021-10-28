#! /usr/bin/env python3


import numpy, sys, time

## Fonctions utilitaires

def printerr(msg):
    print(msg, file = sys.stderr)

class Timer:
    def __init__(self, procname):
        self.procname = procname
        self.btime = time.time()

    def __del__(self):
        delta = time.time() - self.btime
        printerr(f"{self.procname}\u00A0: le processus a mis {delta} secondes.")

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

def bicoeff(n, p):
    return fact(n) / ( fact(p) * fact(n - p) )

## 3.1

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

print(triangle_Pascal(3))
print(triangle_Pascal2(3))
sierpinski(16)
