# -*- coding: utf-8 -*-
from __future__ import print_function
from pprint import pprint
from .proj_plane import pg_point, pg_line, join, meet, x_ratio, involution


class ck:
    def __init__(self, dual):
        self.dual = dual

    def is_perpendicular(self, l, m):
        return m.incident(self.dual(l))

    def altitude(self, p, l):
        return p * self.dual(l)

    def orthocenter(self, a1, a2, a3):
        t1 = self.altitude(a1, a2*a3)
        t2 = self.altitude(a2, a1*a3)
        return t1*t2

#    def omega(self, l):
#        return l.dot(self.dual(l))

    def measure(self, a1, a2):
        """test"""
        # omg = a1.dot(self.dual(a2))
        return 1 - x_ratio(a1, a2, self.dual(a2), self.dual(a1))
        # if isinstance(omg, (int, np.int64) ):
        #     return 1 - Fraction(omg, self.omega(a1)) * Fraction(omg, self.omega(a2))
        # else:
        #     return 1 - (omg * omg) / (self.omega(a1) * self.omega(a2))

    def line_reflect(self, m):
        return involution(m, self.dual(m))

    # def measure(self, a1, a2):
    #     omg = self.omega(a1*a2)
    #     if isinstance(omg, (int, np.int64) ):
    #         return Fraction(omg, self.omega(a1) * self.omega(a2))
    #     else:
    #         return omg / (self.omega(a1) * self.omega(a2))

    def quadrance(self, a1, a2):
        assert isinstance(a1, pg_point)
        return self.measure(a1, a2)

    def spread(self, l1, l2):
        assert isinstance(l1, pg_line)
        return self.measure(l1, l2)


def check_sine_law(s1, q1, s2, q2):
  return s1*q2 == s2*q1

