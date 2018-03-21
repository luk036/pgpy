# -*- coding: utf-8 -*-
from __future__ import print_function
from pprint import pprint
import numpy as np
from fractions import *
from .proj_plane import * 

def dual(x):
    if isinstance(x, pg_point):
        return l_infty
    elif isinstance(x, pg_line):
        return pk_point(x.dot(B_infty), A_infty, x.dot(A_infty), B_infty)
    else:
        raise NotImplementedError()

def is_perpendicular(l, m):
    return m.incident(dual(l)) # not useful

def is_parallel(l, m):
    return l_infty.incident(l*m)

def altitude(p, l):
    return dual(l) * p

def midpoint(a, b):
    return pk_point(b.dot(l_infty), a, a.dot(l_infty), b)

def omega(x):
    if isinstance(x, pg_point):
        return x.dot(l_infty)**2
    elif isinstance(x, pg_line):
        return 2*x.dot(B_infty)*x.dot(A_infty)
    else:
        raise NotImplementedError()

def omegaB(l):
    return 2*l.dot(B_infty)*l.dot(A_infty)

def omegaA(p):
    return p.dot(l_infty)**2

def measure(a1, a2):
    omg = omega(a1*a2)
    if isinstance(omg, (int, np.int64) ):
        return Fraction(omg, omega(a1) * omega(a2))
    else:
        return omg / (omega(a1) * omega(a2))

def cross(l1, l2):
    return 1 - spread(l1, l2) # ???

def quadrance(a1, a2):
    return measure(a1, a2)

def spread(l1, l2):
    return measure(l1, l2)

def A(a, b, c):
    return (4*a*b) - (a + b - c)**2

if __name__ == "__main__":
    import sympy
    sympy.init_printing()

    # px = sympy.Symbol("px", integer=True)
    # py = sympy.Symbol("py", integer=True)
    # pz = sympy.Symbol("pz", integer=True)
    # qx = sympy.Symbol("qx", integer=True)
    # qy = sympy.Symbol("qy", integer=True)
    # qz = sympy.Symbol("qz", integer=True)
    # A_infty = pg_point([px, py, pz])
    # B_infty = pg_point([qx, qy, qz])
    # M = np.array([[600., 5., 0.],
    #               [5., 30., 100.],
    #               [0., 100., 1.]])
    # N = np.linalg.inv(M)
    # l_infty = pg_line([0., 100., 1.])
    # I = np.array([-1j, 1., 0.])
    # J = np.array([1j, 1., 0.])
    # A_infty = pg_point(N.dot(I))
    # B_infty = pg_point(N.dot(J))
    # print(A_infty.coord)
    # print(B_infty.coord)
    # B = np.array([[1., 0., 0.],
    #                 [0., 1., 0.],
    #                 [0., 0., 0.]])
    # BB = N.dot(B).dot(N)
    # print(N)
    # print(BB)

    A_infty = pg_point([-1j, 1, 1])
    B_infty = pg_point([1j, 1, 1])
    l_infty = A_infty * B_infty

    a1 = pg_point([1, 3, 1])
    a2 = pg_point([4, 2, 1])
    a3 = pg_point(3*a1 + 4*a2)
    q1 = quadrance(a2, a3)
    q2 = quadrance(a1, a3)
    q3 = quadrance(a1, a2)
    print((q1 + q2 + q3)**2 - 2*(q1*q1 + q2*q2 + q3*q3))

    a3 = pg_point([4, -2, 1])
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
    print(spread(t1, l1))
    # print(coincident(t1, t2, t3))
    tqf = ((q1 + q2 + q3)**2) - 2*(q1*q1 + q2*q2 + q3*q3)
    print(tqf, A(q1, q2, q3)) # get the same

    assert spread(l1, l1) == 0
    assert quadrance(a1, a1) == 0

    # ???
    c3 = ((q1 + q2 - q3)**2) / (4*q1*q2)
    print(c3, 1 - s3)
    tsf = ((s1 + s2 + s3)**2) - 2*(s1*s1 + s2*s2 + s3*s3) - 4*s1*s2*s3
    print(tsf)
