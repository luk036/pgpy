# -*- coding: utf-8 -*-
from fractions import Fraction
from .proj_plane import pg_point, pg_line, plucker
from .ck_plane import ck


class persp_euclid_plane(ck):
    def __init__(self, Ire, Iim, l_infty):
        self.Ire = Ire
        self.Iim = Iim
        self.l_infty = l_infty

    def perp(self, v):
        if isinstance(v, pg_line):
            alpha = v.dot(self.Ire)
            beta = v.dot(self.Iim)
            return plucker(alpha, self.Ire, beta, self.Iim)
        raise NotImplementedError()

    def is_parallel(self, l, m):
        return self.l_infty.incident(l*m)

    def midpoint(self, a, b):
        alpha = b.dot(self.l_infty)
        beta = a.dot(self.l_infty)
        return plucker(alpha, a, beta, b)

    def omega(self, x):
        if isinstance(x, pg_point):
            return x.dot(self.l_infty)**2
        elif isinstance(x, pg_line):
            return x.dot(self.Ire)**2 + x.dot(self.Iim)**2
        raise NotImplementedError()

    def measure(self, a1, a2):
        omg = self.omega(a1*a2)
        den = self.omega(a1) * self.omega(a2)
        if isinstance(omg, int) and \
                isinstance(den, int):
            return Fraction(omg, den)
        return omg / den
