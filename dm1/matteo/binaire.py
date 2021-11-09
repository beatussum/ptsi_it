#! /usr/bin/env python3


import numpy

## 1.1

def StrToCode(msg):
    return [ ord(i) for i in msg ]

## 1.2

def Bin(n):
    ret = []

    while True:
        ret.insert(0, n % 2)
        n //= 2

        if n == 0:
            break

    return ret

## 1.3

def Dec(b):
    ret = 0

    for i in range(1, len(b) + 1):
        ret += b[i] * 2**( len(b) - i )

    return ret

## 1.4

def CodesToBin(decimals):
    ret = []

    for i in decimals:
        b = Bin(i)
        b = ( [0] * ( 8 - len(b) ) ) + b

        ret += b

    return ret

## 1.5

def BinToCodes(bins):
    ret = []

    for i in range(len(bins) // 8):
        ret.append(Dec(bins[i * 8:(i + 1) * 8]))

    return ret

## 1.6

def CodesToBinTab(decimals):
    ret = numpy.empty((len(decimals), 8), int)

    for i in range(len(decimals)):
        ret[i] = CodesToBin([decimals[i]])

    return ret

## 1.7

def StrToBin(string):
    return CodesToBin(StrToCode(string))

## 1.8

def IsBin(lst):
    if ( len(lst) % 8 ) != 0:
        return False

    for i in lst:
        if ( i != 0 ) and ( i != 1 ):
            return False

    return True

## 1.9

def CodeToStr(codes):
    ret = ""

    for i in codes:
        ret += chr(i)

    return ret

def BinToStr(lst):
    if not IsBin(lst):
            return "La liste est invalide!"
    else:
        return CodeToStr(BinToCodes(lst))
