# -*- coding: utf-8 -*-
"""
Projective Line
"""

from fractions import Fraction

from .pg_common import cross2


class pl_point(list):
    """Point in Projective line"""

    def __new__(cls, *args, **kwargs):
        """[summary]

        Returns:
            [type]: [description]
        """
        return list.__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """[summary]

        Arguments:
            other (type): [description]

        Returns:
            [type]: [description]
        """
        if isinstance(self, type(other)):
            return cross2(self, other) == 0
        return False

    def __ne__(self, other):
        """[summary]

        Arguments:
            other (type): [description]

        Returns:
            [type]: [description]
        """
        return not self.__eq__(other)


def ratio_ratio(a, b, c, d):
    """[summary]

    Arguments:
        a (type): [description]
        b (type): [description]
        c (type): [description]
        d (type): [description]

    Returns:
        [type]: [description]
    """
    return Fraction(a, b) / Fraction(c, d)


def R1(A, B, C, D):
    """[summary]

    Arguments:
        A (type): [description]
        B (type): [description]
        C (type): [description]
        D (type): [description]

    Returns:
        [type]: [description]
    """
    ac = cross2(A, C)
    ad = cross2(A, D)
    bc = cross2(B, C)
    bd = cross2(B, D)
    return ratio_ratio(ac, ad, bc, bd)


def is_harmonic1(A, B, C, D):
    """[summary]

    Arguments:
        A (type): [description]
        B (type): [description]
        C (type): [description]
        D (type): [description]

    Returns:
        [type]: [description]
    """
    return R1(A, B, C, D) == -1
