# -*- coding: utf-8 -*-
from __future__ import print_function
from pprint import pprint
import numpy as np
from fractions import Fraction
from .proj_plane import *
from .ck_plane import ck

class persp_euclid_plane():
    def __init__(self, A_infty, B_infty, l_infty):
        self.A_infty = A_infty
        self.B_infty = B_infty
        self.l_infty = l_infty
        self.ck = ck(self.dual)

    def dual(self, x):
        if isinstance(x, pg_point):
            return self.l_infty
        elif isinstance(x, pg_line):
            return plucker(x.dot(self.B_infty), self.A_infty, x.dot(self.A_infty), self.B_infty)
        raise NotImplementedError()

    def is_parallel(self, l, m):
        return self.l_infty.incident(l*m)

    def is_perpendicular(self, l, m):
        return self.ck.is_perpendicular(l,m)

    def altitude(self, p, l):
        return self.ck.altitude(p, l)

    def tri_altitude(self, a1, a2, a3):
        return self.ck.tri_altitude(a1, a2, a3)

    def orthocenter(self, a1, a2, a3):
        return self.ck.orthocenter(a1, a2, a3)
        
    # def line_reflect(m):
    #    return involution(m, fB(m))

    def midpoint(self, a, b):
        return plucker(b.dot(self.l_infty), a, a.dot(self.l_infty), b)

    def omega(self, x):
        if isinstance(x, pg_point):
            return x.dot(self.l_infty)**2
        elif isinstance(x, pg_line):
            return 2*x.dot(self.B_infty)*x.dot(self.A_infty)
        raise NotImplementedError()

    def omegaB(self, l):
        return 2*l.dot(self.B_infty)*l.dot(self.A_infty)

    def omegaA(self, p):
        return p.dot(self.l_infty)**2

    def measure(self, a1, a2):
        omg = self.omega(a1*a2)
        den = self.omega(a1) * self.omega(a2)
        if isinstance(omg, (int, np.int64)) and isinstance(den, (int, np.int64)):
            return Fraction(omg, den)
        return omg / den

    def cross(self, l1, l2):
        return 1 - self.spread(l1, l2)  # ???

    def quadrance(self, a1, a2):
        return self.measure(a1, a2)

    def spread(self, l1, l2):
        return self.measure(l1, l2)

    def tri_quadrance(self, a1, a2, a3):
        q1 = self.quadrance(a2, a3)
        q2 = self.quadrance(a1, a3)
        q3 = self.quadrance(a1, a2)
        return q1, q2, q3

    def tri_spread(self, l1, l2, l3):
        s1 = self.spread(l2, l3)
        s2 = self.spread(l1, l3)
        s3 = self.spread(l1, l2)
        return s1, s2, s3

    def Ar(self, a, b, c):
        return (4*a*b) - (a + b - c)**2

