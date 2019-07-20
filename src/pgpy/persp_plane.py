# -*- coding: utf-8 -*-
"""
Perspective Euclidean Geometry
"""

from fractions import Fraction

from .ck_plane import ck
from .proj_plane import pg_line, pg_point, plucker, tri_func


class persp_euclid_plane(ck):
    def __init__(self, Ire, Iim, l_infty):
        """[summary]

        Arguments:
            Ire (type): [description]
            Iim (type): [description]
            l_infty (type): [description]
        """
        self.Ire = Ire
        self.Iim = Iim
        self.l_infty = l_infty

    def perp(self, v):
        """[summary]

        Arguments:
            v (type): [description]

        Raises:
            NotImplementedError -- [description]

        Returns:
            [type]: [description]
        """
        if isinstance(v, pg_line):
            alpha = v.dot(self.Ire)
            beta = v.dot(self.Iim)
            return plucker(alpha, self.Ire, beta, self.Iim)
        raise NotImplementedError()

    def is_parallel(self, l, m):
        """[summary]

        Arguments:
            l (type): [description]
            m (type): [description]

        Returns:
            [type]: [description]
        """
        return self.l_infty.incident(l * m)

    def midpoint(self, a, b):
        """[summary]

        Arguments:
            a (type): [description]
            b (type): [description]

        Returns:
            [type]: [description]
        """
        alpha = b.dot(self.l_infty)
        beta = a.dot(self.l_infty)
        return plucker(alpha, a, beta, b)

    def tri_midpoint(self, triangle):
        """[summary]

        Arguments:
            triangle (type): [description]

        Returns:
            [type]: [description]
        """
        return tri_func(self.midpoint, triangle)

    def omega(self, x):
        """[summary]

        Arguments:
            x (type): [description]

        Raises:
            NotImplementedError -- [description]

        Returns:
            [type]: [description]
        """
        if isinstance(x, pg_point):
            return x.dot(self.l_infty)**2
        elif isinstance(x, pg_line):
            return x.dot(self.Ire)**2 + x.dot(self.Iim)**2
        raise NotImplementedError()

    def measure(self, a1, a2):
        """[summary]

        Arguments:
            a1 (type): [description]
            a2 (type): [description]

        Returns:
            [type]: [description]
        """
        omg = self.omega(a1 * a2)
        den = self.omega(a1) * self.omega(a2)
        if isinstance(omg, int) and \
                isinstance(den, int):
            return Fraction(omg, den)
        return omg / den
