# -*- coding: utf-8 -*-
from fractions import Fraction
# import numpy as np
from .pg_common import cross2


class pl_point(list):
    """Projective point in Projective line

    """
    def __new__(cls, *args, **kwargs):
        return list.__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        if isinstance(self, type(other)):
            return cross2(self, other) == 0
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


def ratio_ratio(a, b, c, d):
    if isinstance(a, int):
        return Fraction(a, b) / Fraction(c, d)
    return (a * d) / (b * c)


def R1(A, B, C, D):
    ac = cross2(A, C)
    ad = cross2(A, D)
    bc = cross2(B, C)
    bd = cross2(B, D)
    return ratio_ratio(ac, ad, bc, bd)


def isharmonic(A, B, C, D):
    return R1(A, B, C, D) == -1
