# -*- coding: utf-8 -*-
from __future__ import print_function
from pprint import pprint
import numpy as np
from fractions import *
from proj_geom import * 

def dot1(x, y):
    return x[0] * y[0] + x[1] * y[1]

def cross(x, y):
    return x[0] * y[1] - x[1] * y[0]

def dot2(x, y):
    return x[0] * y[0] + x[2] * y[2]

def fB(l):
    [a, b] = l[0:2]
    return pg_point([a, b, 0])

def is_perpendicular(l, m):
    return dot1(l, m) == 0

def is_parallel(l, m):
    return cross(l, m) == 0

def altitude(a, l):
    return join(a, fB(l))

def omgB(x, y):
    return x[0] * y[0] + x[1] * y[1]

def det(x, y):
    return x[0] * y[1] - x[1] * y[0]

def quad1(x1, z1, x2, z2):
    if isinstance(x1, int):
        return (Fraction(x1,z1) - Fraction(x2,z2))**2
    else:
        return (x1/z1 - x2/z2)**2 

def quadrance(a1, a2):
    return quad1(a1[0], a1[2], a2[0], a2[2]) + \
            quad1(a1[1], a1[2], a2[1], a2[2])

def spread(l1, l2):
    d = det(l1, l2)
    if isinstance(d, int):
        return Fraction(d, omgB(l1, l1)) * Fraction(d, omgB(l2, l2))
    else:
        return d * d / (omgB(l1, l1) * omgB(l2, l2))

def cross(l1, l2):
    d = omgB(l1, l2)
    if isinstance(d, int):
        return Fraction(d, omgB(l1, l1)) * Fraction(d, omgB(l2, l2))
    else:
        return d * d / (omgB(l1, l1) * omgB(l2, l2))

def uc_point(lambda1, mu1):
    return pg_point([lambda1**2 - mu1**2, 
            2*lambda1*mu1, lambda1**2 + mu1**2])

def Ar(a, b, c):
    ''' Archimedes's function '''
    return (4*a*b) - (a + b - c)**2

def cqq(a, b, c, d):
    ''' Cyclic quadrilateral quadrea theorem '''
    t1 = 4*a*b
    t2 = 4*c*d
    m = (t1 + t2) - (a + b - c - d)**2
    p = m*m - 4*t1*t2
    return m, p

def Ptolemy(Q12, Q23, Q34, Q14, Q13, Q24):
    return Ar(Q12*Q34, Q23* Q14, Q13*Q24) == 0

if __name__ == "__main__":
    import sympy
    sympy.init_printing()

    # px = sympy.Symbol("px", integer=True)
    # py = sympy.Symbol("py", integer=True)
    # pz = sympy.Symbol("pz", integer=True)
    # qx = sympy.Symbol("qx", integer=True)
    # qy = sympy.Symbol("qy", integer=True)
    # qz = sympy.Symbol("qz", integer=True)
    # sx = sympy.Symbol("sx", integer=True)
    # sy = sympy.Symbol("sy", integer=True)
    # sz = sympy.Symbol("sz", integer=True)
    # a1 = pg_point([px, py, pz])
    # a2 = pg_point([qx, qy, qz])
    # lambda1 = sympy.Symbol("lambda1", integer=True)
    # mu1 = sympy.Symbol("mu1", integer=True)
    # a3 = pk_point(lambda1, a1, mu1, a2)

    a1 = pg_point([1, 3, 1])
    a2 = pg_point([4, 2, 1])
    a3 = pg_point(3*a1 + 4*a2)
    q1 = quadrance(a2, a3)
    q2 = quadrance(a1, a3)
    q3 = quadrance(a1, a2)
    tqf = (q1 + q2 + q3)**2 - 2*(q1*q1 + q2*q2 + q3*q3) # get 0
    #tqf = sympy.simplify(tqf)
    print(tqf) # get 0
    
    a3 = pg_point([4, -3, 1])
    # a3 = pg_point([sx, sy, sz])
    l1 = join(a2, a3)
    l2 = join(a1, a3)
    l3 = join(a1, a2)
    q1 = quadrance(a2, a3)
    q2 = quadrance(a1, a3)
    # q3 = quadrance(a1, a2)
    s1 = spread(l2, l3)
    s2 = spread(l1, l3)
    s3 = spread(l1, l2)
    print(q1/s1, q2/s2, q3/s3)
    t1 = altitude(a1, l1)
    t2 = altitude(a2, l2)
    t3 = altitude(a3, l3)
    print(spread(t1, l1)) # get 1.0
    print(coincident(t1, t2, t3)) # True

    tqf = ((q1 + q2 + q3)**2) - 2*(q1*q1 + q2*q2 + q3*q3)
    print(tqf, Ar(q1, q2, q3)) # get the same

    assert spread(l1, l1) == 0
    assert quadrance(a1, a1) == 0

    c3 = ((q1 + q2 - q3)**2) / (4*q1*q2)
    print(c3, 1 - s3) # get the same
 
    tsf = (s1 + s2 + s3)**2 - 2*(s1*s1 + s2*s2 + s3*s3) - 4*s1*s2*s3
    # tsf = sympy.simplify(tsf)
    print(tsf) # get 0

    # a1 = pg_point([1, 0, -1])
    # a2 = pg_point([3, 4, 5])
    # a3 = pg_point([-12, 5, 13])
    # a4 = pg_point([0, 1, 1])
    # a1 = uc_point(1, 0)
    # a2 = uc_point(3, 4)
    # a3 = uc_point(-12, 5)
    # a4 = uc_point(0, 1)
    lambda1, mu1 = sympy.symbols("lambda1 mu1", integer=True)
    lambda2, mu2 = sympy.symbols("lambda2 mu2", integer=True)
    lambda3, mu3 = sympy.symbols("lambda3 mu3", integer=True)
    lambda4, mu4 = sympy.symbols("lambda4 mu4", integer=True)
    a1 = uc_point(lambda1, mu1)
    a2 = uc_point(lambda2, mu2)
    a3 = uc_point(lambda3, mu3)
    a4 = uc_point(lambda4, mu4)
    q12 = quadrance(a1, a2)
    q23 = quadrance(a2, a3)
    q34 = quadrance(a3, a4)
    q14 = quadrance(a1, a4)
    q24 = quadrance(a2, a4)
    q13 = quadrance(a1, a3)
    #print(q12, q23, q34, q14, q24, q13)
    t = Ar(q12*q34, q23*q14, q13*q24)
    t = sympy.simplify(t)
    print(t) # get 0
