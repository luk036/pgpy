# -*- coding: utf-8 -*-
from __future__ import print_function
from pprint import pprint
import numpy as np
from fractions import *
from .proj_plane import *


def dot1(x, y):
    return x[0] * y[0] + x[1] * y[1]


def cross1(x, y):
    return x[0] * y[1] - x[1] * y[0]


def dot2(x, y):
    return x[0] * y[0] + x[2] * y[2]


def fB(l):
    [a, b] = l[0:2]
    return pg_point([a, b, 0])


def is_perpendicular(l, m):
    return dot1(l, m) == 0


def is_parallel(l, m):
    return cross1(l, m) == 0


def altitude(a, l):
    return join(a, fB(l))


def orthocenter(a1, a2, a3):
    t1 = altitude(a1, a2*a3)
    t2 = altitude(a2, a1*a3)
    return t1*t2


def line_reflect(m):
    return involution(m, fB(m))


def omgB(x, y):
    return x[0] * y[0] + x[1] * y[1]


def det(x, y):
    return x[0] * y[1] - x[1] * y[0]


def midpoint(a, b):
    return plucker(b[2], a, a[2], b)

# Angle Bisector???


def quad1(x1, z1, x2, z2):
    if isinstance(x1, (int, np.int64)):
        return (Fraction(x1, z1) - Fraction(x2, z2))**2
    else:
        return (x1/z1 - x2/z2)**2


def quadrance(a1, a2):
    return quad1(a1[0], a1[2], a2[0], a2[2]) + \
        quad1(a1[1], a1[2], a2[1], a2[2])


def spread(l1, l2):
    d = det(l1, l2)
    if isinstance(d, (int, np.int64)):
        return Fraction(d, omgB(l1, l1)) * Fraction(d, omgB(l2, l2))
    else:
        return d * d / (omgB(l1, l1) * omgB(l2, l2))


def cross(l1, l2):
    d = omgB(l1, l2)
    if isinstance(d, (int, np.int64)):
        return Fraction(d, omgB(l1, l1)) * Fraction(d, omgB(l2, l2))
    else:
        return d * d / (omgB(l1, l1) * omgB(l2, l2))


def uc_point(lambda1, mu1):
    return pg_point([lambda1**2 - mu1**2,
                     2*lambda1*mu1, lambda1**2 + mu1**2])


def Ar(a, b, c):
    ''' Archimedes's function '''
    return (4*a*b) - (a + b - c)**2


def cqq(a, b, c, d):
    ''' Cyclic quadrilateral quadrea theorem '''
    t1 = 4*a*b
    t2 = 4*c*d
    m = (t1 + t2) - (a + b - c - d)**2
    p = m*m - 4*t1*t2
    return m, p


def Ptolemy(Q12, Q23, Q34, Q14, Q13, Q24):
    return Ar(Q12*Q34, Q23 * Q14, Q13*Q24) == 0


def distance(a, b):
    return np.sqrt(float(quadrance(a, b)))


def angle(l, m):
    return np.arcsin(np.sqrt(spread(l, m)))
