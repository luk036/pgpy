# -*- coding: utf-8 -*-
from __future__ import print_function
from pprint import pprint
import numpy as np
from fractions import *
from .proj_plane import *


class persp_euclid_plane:
    def __init__(self, A_infty, B_infty, l_infty):
        self.A_infty = A_infty
        self.B_infty = B_infty
        self.l_infty = l_infty

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
        den = self.omega(a1) * self.omega(a2)
        if isinstance(omg, (int, np.int64)) and isinstance(den, (int, np.int64)):
            return Fraction(omg, den)
        else:
            return omg / den

    def cross(self, l1, l2):
        return 1 - self.spread(l1, l2)  # ???

    def quadrance(self, a1, a2):
        return self.measure(a1, a2)

    def spread(self, l1, l2):
        return self.measure(l1, l2)

    def Ar(self, a, b, c):
        return (4*a*b) - (a + b - c)**2


