# -*- coding: utf-8 -*-
from .proj_plane import pg_point, pg_line, x_ratio, involution, tri_dual, tri_func
from abc import ABCMeta, abstractmethod


class ck():
    __meta_class = ABCMeta

    @abstractmethod
    def perp(self, v):
        """abstract method"""

    @abstractmethod
    def measure(self, a1, a2):
        """abstract method"""

    def is_perpendicular(self, l, m):
        """Check if two lines perpendicular

        Arguments:
            l {pg_object} -- line
            m {pg_object} -- line

        Returns:
            bool -- True if l and m are perpendicular
        """
        return m.incident(self.perp(l))

    def altitude(self, p, l):
        return p * self.perp(l)

    def tri_altitude(self, tri):
        l1, l2, l3 = tri_dual(tri)
        a1, a2, a3 = tri
        t1 = self.altitude(a1, l1)
        t2 = self.altitude(a2, l2)
        t3 = self.altitude(a3, l3)
        return t1, t2, t3

    def orthocenter(self, tri):
        a1, a2, a3 = tri
        t1 = self.altitude(a1, a2*a3)
        t2 = self.altitude(a2, a1*a3)
        return t1*t2

    def reflect(self, m):
        return involution(m, self.perp(m))

    def quadrance(self, a1, a2):
        if not isinstance(a1, pg_point):
            raise AssertionError()
        return self.measure(a1, a2)

    def spread(self, l1, l2):
        if not isinstance(l1, pg_line):
            raise AssertionError()
        return self.measure(l1, l2)

    def tri_measure(self, tri):
        return tri_func(self.measure, tri)

    def tri_quadrance(self, triangle):
        if not isinstance(triangle[0], pg_point):
            raise AssertionError()
        return self.tri_measure(triangle)

    def tri_spread(self, trilateral):
        if not isinstance(trilateral[0], pg_line):
            raise AssertionError()
        return self.tri_measure(trilateral)


def check_sine_law(Q, S):
    q1, q2, q3 = Q
    s1, s2, s3 = S
    return s1*q2 == s2*q1 and s2*q3 == s3*q2


class ellck(ck):

    def perp(self, v):
        return v.dual()(v)

    def measure(self, a1, a2):
        return 1 - x_ratio(a1, a2, self.perp(a2), self.perp(a1))


class hyck(ck):

    def perp(self, v):
        [x, y, z] = v
        return v.dual()([x, y, -z])

    def measure(self, a1, a2):
        return 1 - x_ratio(a1, a2, self.perp(a2), self.perp(a1))


def check_cross_TQF(Q):
    """coincident implies TQF = 0"""
    q1, q2, q3 = Q
    return (q1 + q2 + q3)**2 - 2*(q1**2 + q2**2 + q3**2) - 4*q1*q2*q3


def check_cross_law(S, q3):
    s1, s2, s3 = S
    return (s1*s2*q3 - (s1 + s2 + s3) + 2)**2 - 4*(1 - s1)*(1 - s2)*(1 - s3)
