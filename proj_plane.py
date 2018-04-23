# -*- coding: utf-8 -*-
from __future__ import print_function

from pprint import pprint
import numpy as np
from .proj_line import ratio_ratio, R1


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

    def __mul__(self, other):
        ''' meet '''
        l = np.cross(self, other)
        return pg_line(l)

    def dual(self):
        return pg_line

#    def aux(self):
#        return pg_line(self)


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

    def __mul__(self, other):
        ''' join '''
        return pg_point(np.cross(self, other))

    def dual(self):
        return pg_point

#    def aux(self):
#        return pg_point(self)


def join(p, q):
    assert isinstance(p, pg_point)
    return p * q


def meet(l, m):
    assert isinstance(l, pg_line)
    return l * m


# Note: `lambda` is a preserved keyword in python
def plucker(lambda1, p, mu1, q):
    T = type(p)
    return T(lambda1 * p + mu1 * q)


def coincident(p, q, r):
    return r.incident(p * q)


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

def tri(a1, a2, a3):
    l1 = a2 * a3
    l2 = a1 * a3
    l3 = a1 * a2
    return l1, l2, l3
    
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
    lC = C * (A * B).aux()
    return plucker(B.dot(lC), A, A.dot(lC), B)


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
    return ratio_ratio(dAl, dAm, dBl, dBm)


def R(A, B, C, D):
    # not sure???
    if A[1]*B[2] != B[1]*A[2]: 
        # Project points to yz-plane
        a, b, c, d = A[1:], B[1:], C[1:], D[1:]
    else:
        # Project points to xz-plane
        a, b, c, d = A[(0,2)], B[(0,2)], C[(0,2)], D[(0,2)]
    return R1(a, b, c, d)


# def R(A, B, C, D):
#     O = (C*D).aux()
#     return x_ratio(A, B, O*C, O*D)


def isharmonic(A, B, C, D):
    return R(A, B, C, D) == -1


def check_pappus(co1, co2):
    A, B, C = co1
    D, E, F = co2
    G = (A*E) * (B*D)
    H = (A*F) * (C*D)
    I = (B*F) * (C*E)
    assert coincident(G, H, I)


def check_desargue(tri1, tri2):
    A, B, C = tri1
    D, E, F = tri2
    a, b, c = tri(A, B, C)
    d, e, f = tri(D, E, F)

    b1 = persp([A, B, C], [D, E, F])
    b2 = persp([a, b, c], [d, e, f])
    if b1:
        assert b2
    else:
        assert not b2
