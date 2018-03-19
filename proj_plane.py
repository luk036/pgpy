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
    return p * q

def meet(l, m):
    return l * m

def coincident(p, q, r):
    return r.incident(p * q)

# note: `lambda` is a preserved keyword in python
def pk_point(lambda1, p, mu1, q):
    return pg_point(lambda1 * p + mu1 * q)

# note: `lambda` is a preserved keyword in python
def pk_line(lambda1, l, mu1, m):
    return pg_line(lambda1 * l + mu1 * m)

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

def dot(p, l):
    return p.dot(l)

class line_involution:
    """ Definition: $\tau(\tau(a)) == a$ """
    def __init__(self, m, o):
        self.m = m
        self.o = o
        self.c = dot(m, o)

    def __call__(self, p):
        return pk_point(self.c, p, -2 * dot(self.m, p), self.o)

def x_ratio(A, B, l, m):
    dAl = dot(A, l)
    dAm = dot(A, m)
    dBl = dot(B, l)
    dBm = dot(B, m)
    if isinstance(dAl, (int, np.int64) ):
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
    ac = dot(A, OC)
    ad = dot(A, OD)
    bc = dot(B, OC)
    bd = dot(B, OD)
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
    if b1: assert b2
    else: assert not b2

if __name__ == "__main__":
    p = pg_point([1, 3, 2])
    q = pg_point([4, 3, 5])
    print(join(p, q))

    l = pg_line([5, 7, 8])
    m = pg_line([-5, 1, 6])
    print(meet(l, m))


    import sympy
    sympy.init_printing()
    pv = sympy.symbols("p:3", integer=True)
    qv = sympy.symbols("q:3", integer=True)
    lambda1, mu1 = sympy.symbols("lambda1 mu1", integer=True)
    p = pg_point(pv)
    q = pg_point(qv)
    r = pk_point(lambda1, p, mu1, q)
    sv = sympy.symbols("s:3", integer=True)
    tv = sympy.symbols("t:3", integer=True)
    lambda2, mu2 = sympy.symbols("lambda2 mu2", integer=True)
    s = pg_point(sv)
    t = pg_point(tv)
    u = pk_point(lambda2, s, mu2, t)

    # Prove Pappus Theorem
    G = meet(join(p, t), join(q, s))
    H = meet(join(p, u), join(r, s))
    I = meet(join(q, u), join(r, t))
    ans = G.dot(join(H, I))
    ans = sympy.simplify(ans)
    print(ans) # get 0

    # p, q, s, t
    lambda3, mu3 = sympy.symbols("lambda3 mu3", integer=True)
    p2 = pk_point(lambda1, p, mu1, t)
    q2 = pk_point(lambda2, q, mu2, t)
    s2 = pk_point(lambda3, s, mu3, t)

    # Prove Desargue Theorem
    G = meet(join(p, q), join(p2, q2))
    H = meet(join(q, s), join(q2, s2))
    I = meet(join(s, p), join(s2, p2))
    ans = G.dot(join(H, I))
    ans = sympy.simplify(ans)
    print(ans) # get 0

