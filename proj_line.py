# -*- coding: utf-8 -*-
from __future__ import print_function

from pprint import pprint
from fractions import Fraction
import numpy as np


def cross1_l(p, q):
    return p.x * q.y - p.y * q.x


class pl_point:
    def __init__(self, p):
        self.x = p[0]
        self.y = p[1]

    def __eq__(self, other):
        if isinstance(self, type(other)):
            return cross1_l(self, other) == 0
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


def ratio_ratio(a, b, c, d):
    if isinstance(a, (int, np.int64)):
        return Fraction(a, b) / Fraction(c, d)
    return a * d / (b * c)


# def R1(A, B, C, D):
#     ac = cross1_l(A, C)
#     ad = cross1_l(A, D)
#     bc = cross1_l(B, C)
#     bd = cross1_l(B, D)
#     return ratio_ratio(ac, ad, bc, bd)


# def isharmonic(A, B, C, D):
#     ac = cross1_l(A, C)
#     ad = cross1_l(A, D)
#     bc = cross1_l(B, C)
#     bd = cross1_l(B, D)
#     return ac*bd + ad*bc == 0
