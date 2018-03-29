# -*- coding: utf-8 -*-
from __future__ import print_function

from pprint import pprint
from fractions import *
import numpy as np


class pg_point(np.ndarray):
    def __new__(cls, inputarr):
        obj = np.asarray(inputarr).view(cls)
        return obj

    def __eq__(self, other):
        if type(other) is type(self):
            return (np.cross(self, other) == 0).all()
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def incident(self, l):
        return not self.dot(l)

    # def __add__(self, other):
    #     return pg_point(np.ndarray.__add__(self, other))

    # def __sub__(self, other):
    #     return pg_point(np.ndarray.__sub__(self, other))

    def __mul__(self, other):
        ''' meet '''
        l = np.cross(self, other)
        return pg_line(l)

    def aux(self):
        return pg_line(self)


class pg_line(np.ndarray):
    def __new__(cls, inputarr):
        obj = np.asarray(inputarr).view(cls)
        return obj

    def __eq__(self, other):
        if type(other) is type(self):
            return (np.cross(self, other) == 0).all()
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def incident(self, p):
        return not self.dot(p)

    # def __add__(self, other):
    #     return pg_line(np.ndarray.__add__(self, other))

    # def __sub__(self, other):
    #     return pg_line(np.ndarray.__sub__(self, other))

    def __mul__(self, other):
        ''' join '''
        return pg_point(np.cross(self, other))

    def aux(self):
        return pg_point(self)


def join(p, q):
    assert type(p) is pg_point
    return p * q


def meet(l, m):
    assert type(l) is pg_line
    return l * m


def coincident(p, q, r):
    return r.incident(p * q)

# note: `lambda` is a preserved keyword in python


def plucker(lambda1, p, mu1, q):
    T = type(p)
    return T(lambda1 * p + mu1 * q)

# note: `lambda` is a preserved keyword in python
# def plucker(lambda1, l, mu1, m):
# return pg_line(lambda1 * l + mu1 * m)


def coI_core(l, Lst):
    for p in Lst:
        if not l.incident(p):
            return False
    return True


def coI(Lst):
    if len(Lst) < 3:
        return True
    [p, q] = Lst[0:2]
    assert p != q
    return coI_core(p*q, Lst[2:])


def persp(L, M):
    if len(L) != len(M):
        return False
    if len(L) < 3:
        return True
    [pL, qL] = L[0:2]
    [pM, qM] = M[0:2]
    assert pL != qL
    assert pM != qM
    assert pL != pM
    assert qL != qM
    O = (pL * pM) * (qL * qM)
    for rL, rM in zip(L[2:], M[2:]):
        if not O.incident(rL * rM):
            return False
    return True


def harm_conj(A, B, C):
    # assert coincident(A,B,C)
    l = A * B
    P = l.aux()
    a = P * A
    b = P * B
    # c = P * C
    R = P + C
    Q = (A * R) * b
    S = (B * R) * a
    return (Q * S) * l

# def dot(p, l):
#    return p.dot(l)


class involution:
    """ Definition: $\tau(\tau(a)) == a$ """

    def __init__(self, m, o):
        self.m = m
        self.o = o
        self.c = m.dot(o)

    def __call__(self, p):
        return plucker(self.c, p, -2 * p.dot(self.m), self.o)


def x_ratio(A, B, l, m):
    dAl = A.dot(l)
    dAm = A.dot(m)
    dBl = B.dot(l)
    dBm = B.dot(m)
    if isinstance(dAl, (int, np.int64)):
        return Fraction(dAl, dAm) / Fraction(dBl, dBm)
    else:
        return dAl*dBm/(dAm*dBl)


def R(A, B, C, D):
    O = (C*D).aux()
    return x_ratio(A, B, O*C, O*D)


def isharmonic(A, B, C, D):
    O = (C*D).aux()
    OC = O * C
    OD = O * D
    ac = A.dot(OC)
    ad = A.dot(OD)
    bc = B.dot(OC)
    bd = B.dot(OD)
    return ac*bd + ad*bc == 0


def check_pappus(A, B, C, D, E, F):
    G = (A*E) * (B*D)
    H = (A*F) * (C*D)
    I = (B*F) * (C*E)
    assert coincident(G, H, I)


def check_desargue(A, B, C, D, E, F):
    a = B * C
    b = A * C
    c = B * A
    d = E * F
    e = D * F
    f = E * D

    b1 = persp([A, B, C], [D, E, F])
    b2 = persp([a, b, c], [d, e, f])
    if b1:
        assert b2
    else:
        assert not b2


