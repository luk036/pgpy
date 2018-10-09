# -*- coding: utf-8 -*-
# import numpy as np
from .proj_line import ratio_ratio, R1
from abc import abstractmethod
from .pg_common import cross, dot_c, plucker_c

class pg_object(list):
    @abstractmethod
    def dual(self):
        """abstract method"""
        pass

    def __new__(cls, *args, **kwargs):
        return list.__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        if type(other) is type(self):
            return cross(self, other) == (0, 0, 0)
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def dot(self, l):
        return dot_c(self, l)

    def incident(self, l):
        return not dot_c(self, l)

    def __mul__(self, other):
        T = self.dual()
        return T(cross(self, other))

    def aux(self):
        T = self.dual()
        return T(self)


class pg_point(pg_object):
    def __new__(cls, *args, **kwargs):
        return pg_object.__new__(cls, *args, **kwargs)

    def dual(self):
        return pg_line


class pg_line(pg_object):
    def __new__(cls, *args, **kwargs):
        return pg_object.__new__(cls, *args, **kwargs)

    def dual(self):
        return pg_point


def join(p, q):
    if not isinstance(p, pg_point):
        raise AssertionError()
    return p * q


def meet(l, m):
    if not isinstance(l, pg_line):
        raise AssertionError()
    return l * m


def coincident(p, q, r):
    return r.incident(p * q)


def coI_core(l, Lst):
    for p in Lst:
        if not l.incident(p):
            return False
    return True


def coI(p, q, *rest):
    if not p != q:
        raise AssertionError()
    return coI_core(p*q, rest)


# Note: `lambda` is a preserved keyword in python
def plucker(lambda1, p, mu1, q):
    T = type(p)
    return T(plucker_c(lambda1, p, mu1, q))


def tri_dual(Tri):
    a1, a2, a3 = Tri
    l1 = a2 * a3
    l2 = a1 * a3
    l3 = a1 * a2
    return l1, l2, l3


def tri_func(func, Tri):
    a1, a2, a3 = Tri
    m1 = func(a2, a3)
    m2 = func(a1, a3)
    m3 = func(a1, a2)
    return m1, m2, m3


def persp(L, M):
    if len(L) != len(M):
        return False
    if len(L) < 3:
        return True
    [pL, qL] = L[0:2]
    [pM, qM] = M[0:2]
    if pL == qL or pM == qM or pL == pM or qL == qM:
        raise AssertionError()
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
        a, b, c, d = A[(0, 2)], B[(0, 2)], C[(0, 2)], D[(0, 2)]
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
    trid1 = tri_dual(tri1)
    trid2 = tri_dual(tri2)

    b1 = persp(tri1, tri2)
    b2 = persp(trid1, trid2)
    if b1:
        assert b2
    else:
        assert not b2
