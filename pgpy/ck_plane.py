# -*- coding: utf-8 -*-
from .proj_plane import pg_point, pg_line, x_ratio, involution, tri, tri_func
from abc import ABCMeta, abstractmethod


class ck():
    __meta_class = ABCMeta

    @abstractmethod
    def perp(self, v):
        """abstract method"""
        pass

    def is_perpendicular(self, l, m):
        return m.incident(self.perp(l))

    def altitude(self, p, l):
        return p * self.perp(l)

    def tri_altitude(self, a1, a2, a3):
        l1, l2, l3 = tri([a1, a2, a3])
        t1 = self.altitude(a1, l1)
        t2 = self.altitude(a2, l2)
        t3 = self.altitude(a3, l3)
        return t1, t2, t3

    def orthocenter(self, a1, a2, a3):
        t1 = self.altitude(a1, a2*a3)
        t2 = self.altitude(a2, a1*a3)
        return t1*t2

    def reflect(self, m):
        return involution(m, self.perp(m))

    def measure(self, a1, a2):
        return 1 - x_ratio(a1, a2, self.perp(a2), self.perp(a1))

    def quadrance(self, a1, a2):
        if not isinstance(a1, pg_point):
        return self.measure(a1, a2)

    def spread(self, l1, l2):
        if not isinstance(l1, pg_line):
            raise AssertionError()
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


def check_sine_law(s1, q1, s2, q2):
    return s1*q2 == s2*q1


class ellck(ck):

    def perp(self, v):
        return v.dual()(v.base)


class hyck(ck):

    def perp(self, v):
        [x, y, z] = v
        return v.dual()([x, y, -z])


def check_cross_TQF(q1, q2, q3):
    return (q1 + q2 + q3)**2 - 2 * (q1 * q1 + q2 * q2 + q3 * q3) - 4 * q1 * q2 * q3


def check_cross_law(s1, s2, s3, q3):
    return (s1 * s2 * q3 - (s1 + s2 + s3) + 2)**2 == 4 * (1 - s1) * (1 - s2) * (1 - s3)
