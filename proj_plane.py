# -*- coding: utf-8 -*-
from __future__ import print_function

from pprint import pprint
from fractions import *
import numpy as np

def coinc(l, Lst):
    for p in Lst:
        if not l.incident(p):
            return False
    return True

def coI(Lst):
    if len(Lst) < 3:
        return True
    p, q = Lst[0], Lst[1]
    assert p != q
    return coinc(p*q, Lst[2:])

def persp_core(O, L, M):
    for rL, rM in zip(L, M):
        if not O.incident(rL * rM):
            return False
    return True

def persp(L, M):
    if len(L) != len(M):
        return False
    if len(L) < 3:
        return True
    pL, qL = L[0], L[1]
    pM, qM = M[0], M[1]
    assert pL != qL 
    assert pM != qM
    assert pL != pM
    assert qL != qM
    O = (pL * pM) * (qL * qM)
    return persp_core(O, L[2:], M[2:])

def proj_core(O, L, M):
    for rL, rM in zip(L, M):
        if O * rL != rM:
            return False
    return True

def harm_conj(A, B, C):
    # assert coincident(A,B,C)
    l = A * B
    P = l.aux()
    a = P * A
    b = P * B
    c = P * C
    R = aux2(P, C)
    Q = (A * R) * b
    S = (B * R) * a
    return (Q * S) * l 