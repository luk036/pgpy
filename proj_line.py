# -*- coding: utf-8 -*-
from __future__ import print_function

from pprint import pprint
from fractions import *
import numpy as np


def dot1(p, q):
    return p.x * q.x + p.y * q.y


def cross1(p, q):
    return p.x * q.y - p.y * q.x


class pl_point:
    def __init__(self, p):
        self.x = p[0]
        self.y = p[1]

    def __eq__(self, other):
        if type(other) is type(self):
            return cross1(self, other) == 0
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


def R1(A, B, C, D):
    ac = cross1(A, C)
    ad = cross1(A, D)
    bc = cross1(B, C)
    bd = cross1(B, D)
    if isinstance(ac, (int, np.int64)):
        return Fraction(ac, ad) / Fraction(bc, bd)
    else:
        return ac*bd/(ad*bc)


def isharmonic(A, B, C, D):
    ac = cross1(A, C)
    ad = cross1(A, D)
    bc = cross1(B, C)
    bd = cross1(B, D)
    return ac*bd + ad*bc == 0


if __name__ == "__main__":
    p = pl_point([1-2j, 3-1j])
    q = pl_point([-2+1j, 1-3j])
    r = pl_point([2-1j, -2+1j])
    s = pl_point([2j, 2-2j])
    t = pl_point([2, -2j])
