# -*- coding: utf-8 -*-
import numpy as np
from fractions import Fraction
from .proj_plane import *
from .ck_plane import ck


class persp_euclid_plane(ck):
    def __init__(self, Ire, Iim, l_infty):
        self.Ire = Ire
        self.Iim = Iim
        self.l_infty = l_infty

    def perp(self, v):
        if isinstance(v, pg_point):
            return self.l_infty
        elif isinstance(v, pg_line):
            return plucker(v.dot(self.Ire), self.Ire, v.dot(self.Iim), self.Iim)
        raise NotImplementedError()

    def is_parallel(self, l, m):
        return self.l_infty.incident(l*m)

    def midpoint(self, a, b):
        return plucker(b.dot(self.l_infty), a, a.dot(self.l_infty), b)

    def omega(self, x):
        if isinstance(x, pg_point):
            return x.dot(self.l_infty)**2
        elif isinstance(x, pg_line):
            return x.dot(self.Ire)**2 + x.dot(self.Iim)**2
        raise NotImplementedError()

    def measure(self, a1, a2):
        omg = self.omega(a1*a2)
        den = self.omega(a1) * self.omega(a2)
        if isinstance(omg, (int, np.int64, np.int32)) and \
            isinstance(den, (int, np.int64, np.int32)):
            return Fraction(omg, den)
        return omg / den

    def cross(self, l1, l2):
        return 1 - self.spread(l1, l2)  # ???

    def quadrance(self, a1, a2):
        return self.measure(a1, a2)

    def spread(self, l1, l2):
        return self.measure(l1, l2)

    def tri_measure(self, T):
        return tri_func(self.measure, T)

    def tri_quadrance(self, a1, a2, a3):
        if not isinstance(a1, pg_point):
            raise AssertionError()
        return self.tri_measure([a1, a2, a3])

    def tri_spread(self, l1, l2, l3):
        if not isinstance(l1, pg_line):
            raise AssertionError()
        return self.tri_measure([l1, l2, l3])

    @staticmethod
    def Ar(a, b, c):
        return (4*a*b) - (a + b - c)**2
