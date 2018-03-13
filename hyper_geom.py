# -*- coding: utf-8 -*-
from __future__ import print_function
from pprint import pprint
import numpy as np
from fractions import *
from proj_geom import * 

def dual(v):
    [x, y, z] = v
    if isinstance(v, pg_point):
        return pg_line([x, y, -z])
    elif isinstance(v, pg_line):
        return pg_point([x, y, -z])
    else:
        raise NotImplementedError()

def is_perpendicular(l, m):
    return m.incident(dual(l))

def altitude(p, l):
    return p * dual(l)

def orthocenter(a1, a2, a3):
    t1 = altitude(a1, a2*a3)
    t2 = altitude(a2, a1*a3)
    return t1*t2

def omega(l):
    return dot(l, dual(l))

def measure(a1, a2):
    omg = dot(a1, dual(a2))
    if isinstance(omg, int):
        return 1 - Fraction(omg, omega(a1)) * Fraction(omg, omega(a2))
    else:
        return 1 - (omg * omg) / (omega(a1) * omega(a2))
        
def quadrance(a1, a2):
    return measure(a1, a2)

def spread(l1, l2):
    return measure(l1, l2)

class reflect:
    def __init__(self, m, o):
        self.m = m
        self.o = o
        self.c = dot(m, o)

    def __call__(self, p):
        return pk_point(self.c, p, -2 * dot(self.m, p), self.o)

if __name__ == "__main__":
    import sympy
    sympy.init_printing()
    import sympy
    sympy.init_printing()
    pv = sympy.symbols("p:3", integer=True)
    qv = sympy.symbols("q:3", integer=True)

    a1 = pg_point(pv)
    a2 = pg_point(qv)

    lambda1, mu1 = sympy.symbols("lambda1 mu1", integer=True)
    a3 = pk_point(lambda1, a1, mu1, a2)
    
    q1 = quadrance(a2,a3)
    q2 = quadrance(a1,a3)
    q3 = quadrance(a1,a2)
    tqf = (q1 + q2 + q3)**2 - 2*(q1*q1 + q2*q2 + q3*q3) - 4*q1*q2*q3
    tqf = sympy.simplify(tqf)
    print(tqf) # get 0

    sv = sympy.symbols("s:3", integer=True)
    a3 = pg_point(sv)
    l1 = join(a2, a3)
    l2 = join(a1, a3)
    l3 = join(a1, a2)
    t1 = altitude(a1, l1)
    t2 = altitude(a2, l2)
    t3 = altitude(a3, l3)
    o = t1*t2
    ans = np.dot(t3, o)
    ans = sympy.simplify(ans)
    print(ans) # get 0