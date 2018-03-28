# -*- coding: utf-8 -*-
from __future__ import print_function
from pprint import pprint
import numpy as np
from fractions import *
from .proj_plane import *


class persp_euclid_plane:
    def __init__(self, A_infty, B_infty):
        self.A_infty = A_infty
        self.B_infty = B_infty
        self.l_infty = A_infty*B_infty

    def dual(self, x):
        if isinstance(x, pg_point):
            return self.l_infty
        elif isinstance(x, pg_line):
            return plucker(x.dot(self.B_infty), self.A_infty, x.dot(self.A_infty), self.B_infty)
        else:
            raise NotImplementedError()

    def is_perpendicular(self, l, m):
        return m.incident(self.dual(l))  # not useful

    def is_parallel(self, l, m):
        return self.l_infty.incident(l*m)

    def altitude(self, p, l):
        return self.dual(l) * p

    def orthocenter(self, a1, a2, a3):
        t1 = self.altitude(a1, a2*a3)
        t2 = self.altitude(a2, a1*a3)
        return t1*t2

    # def line_reflect(m):
    #    return involution(m, fB(m))

    def midpoint(self, a, b):
        return plucker(b.dot(self.l_infty), a, a.dot(self.l_infty), b)

    def omega(self, x):
        if isinstance(x, pg_point):
            return x.dot(self.l_infty)**2
        elif isinstance(x, pg_line):
            return 2*x.dot(self.B_infty)*x.dot(self.A_infty)
        else:
            raise NotImplementedError()

    def omegaB(self, l):
        return 2*l.dot(self.B_infty)*l.dot(self.A_infty)

    def omegaA(self, p):
        return p.dot(self.l_infty)**2

    def measure(self, a1, a2):
        omg = self.omega(a1*a2)
        if isinstance(omg, (int, np.int64)):
            return Fraction(omg, self.omega(a1) * self.omega(a2))
        else:
            return omg / (self.omega(a1) * self.omega(a2))

    def cross(self, l1, l2):
        return 1 - self.spread(l1, l2)  # ???

    def quadrance(self, a1, a2):
        return self.measure(a1, a2)

    def spread(self, l1, l2):
        return self.measure(l1, l2)

    def Ar(self, a, b, c):
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

    A_inf = pg_point([-1j, 1, 1])
    B_inf = pg_point([1j, 1, 1])
    P = persp_euclid_plane(A_inf, B_inf)

    a1 = pg_point([1, 3, 1])
    a2 = pg_point([4, 2, 1])
    a3 = pg_point(3*a1 + 4*a2)
    q1 = P.quadrance(a2, a3)
    q2 = P.quadrance(a1, a3)
    q3 = P.quadrance(a1, a2)
    print((q1 + q2 + q3)**2 - 2*(q1*q1 + q2*q2 + q3*q3))

    a3 = pg_point([4, -2, 1])
    l1 = join(a2, a3)
    l2 = join(a1, a3)
    l3 = join(a1, a2)
    q1 = P.quadrance(a2, a3)
    q2 = P.quadrance(a1, a3)
    # q3 = quadrance(a1, a2)
    s1 = P.spread(l2, l3)
    s2 = P.spread(l1, l3)
    s3 = P.spread(l1, l2)

    print(q1/s1, q2/s2, q3/s3)
    t1 = P.altitude(a1, l1)
    t2 = P.altitude(a2, l2)
    t3 = P.altitude(a3, l3)
    print(P.spread(t1, l1))
    # print(coincident(t1, t2, t3))
    tqf = ((q1 + q2 + q3)**2) - 2*(q1*q1 + q2*q2 + q3*q3)
    print(tqf, P.Ar(q1, q2, q3))  # get the same

    assert P.spread(l1, l1) == 0
    assert P.quadrance(a1, a1) == 0

    # ???
    c3 = ((q1 + q2 - q3)**2) / (4*q1*q2)
    print(c3, 1 - s3)
    tsf = ((s1 + s2 + s3)**2) - 2*(s1*s1 + s2*s2 + s3*s3) - 4*s1*s2*s3
    print(tsf)
