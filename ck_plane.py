# -*- coding: utf-8 -*-
from __future__ import print_function
from pprint import pprint
from .proj_plane import pg_point, pg_line, join, meet, x_ratio, involution, tri


class ck:
    def __init__(self, dual):
        self.dual = dual

    def is_perpendicular(self, l, m):
        return m.incident(self.dual(l))

    def altitude(self, p, l):
        return p * self.dual(l)

    def tri_altitude(self, a1, a2, a3):
        l1, l2, l3 = tri(a1, a2, a3)
        t1 = self.altitude(a1, l1)
        t2 = self.altitude(a2, l2)
        t3 = self.altitude(a3, l3)
        return t1, t2, t3

    def orthocenter(self, a1, a2, a3):
        t1 = self.altitude(a1, a2*a3)
        t2 = self.altitude(a2, a1*a3)
        return t1*t2

    def reflect(self, m):
        return involution(m, self.dual(m))

    def measure(self, a1, a2):
        return 1 - x_ratio(a1, a2, self.dual(a2), self.dual(a1))

    def quadrance(self, a1, a2):
        assert isinstance(a1, pg_point)
        return self.measure(a1, a2)

    def spread(self, l1, l2):
        assert isinstance(l1, pg_line)
        return self.measure(l1, l2)

    def tri_measure(self, a1, a2, a3):
        m1 = self.measure(a2, a3)
        m2 = self.measure(a1, a3)
        m3 = self.measure(a1, a2)
        return m1, m2, m3

    def tri_quadrance(self, a1, a2, a3):
        assert isinstance(a1, pg_point)
        return self.tri_measure(a1, a2, a3)

    def tri_spread(self, l1, l2, l3):
        assert isinstance(l1, pg_line)
        return self.tri_measure(l1, l2, l3)


def check_sine_law(s1, q1, s2, q2):
    return s1*q2 == s2*q1
