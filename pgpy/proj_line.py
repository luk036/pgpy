# -*- coding: utf-8 -*-
from fractions import Fraction
import numpy as np


def cross1_l(p, q):
    return p[0] * q[1] - p[1] * q[0]


class pl_point(np.ndarray):
    """Projective point in Projective line

    """
    def __new__(cls, inputarr):
        obj = np.asarray(inputarr).view(cls)
        return obj

    def __eq__(self, other):
        if isinstance(self, type(other)):
            return cross1_l(self, other) == 0
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


def ratio_ratio(a, b, c, d):
    if isinstance(a, (int, np.int64)):
        return Fraction(a, b) / Fraction(c, d)
    return (a * d) / (b * c)


def R1(A, B, C, D):
    ac = cross1_l(A, C)
    ad = cross1_l(A, D)
    bc = cross1_l(B, C)
    bd = cross1_l(B, D)
    return ratio_ratio(ac, ad, bc, bd)


def isharmonic(A, B, C, D):
    return R1(A, B, C, D) == -1
