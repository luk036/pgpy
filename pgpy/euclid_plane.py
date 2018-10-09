# -*- coding: utf-8 -*-
import numpy as np
from fractions import Fraction
from .proj_plane import pg_point, pg_line, join, tri_dual, involution, tri_func, plucker
from .pg_common import cross2, dot1


def fB(l):
    [a, b] = l[:2]
    return pg_point([a, b, 0])


def is_perpendicular(l, m):
    return dot1(l, m) == 0


def is_parallel(l, m):
    return cross2(l, m) == 0


def altitude(a, l):
    return join(a, fB(l))


def tri_altitude(tri):
    l1, l2, l3 = tri_dual(tri)
    a1, a2, a3 = tri
    t1 = altitude(a1, l1)
    t2 = altitude(a2, l2)
    t3 = altitude(a3, l3)
    return t1, t2, t3


def orthocenter(tri):
    a1, a2, a3 = tri
    t1 = altitude(a1, a2*a3)
    t2 = altitude(a2, a1*a3)
    return t1*t2


def reflect(m):
    return involution(m, fB(m))


def midpoint(a, b):
    return plucker(b[2], a, a[2], b)

# Angle Bisector???


def quad1(P):
    x1, z1, x2, z2 = P
    for v in P:
        if not isinstance(v, int):
            return (x1/z1 - x2/z2)**2
    return (Fraction(x1, z1) - Fraction(x2, z2))**2


def quadrance(a1, a2):
    return quad1((a1[0], a1[2], a2[0], a2[2])) + \
        quad1((a1[1], a1[2], a2[1], a2[2]))


def sbase(l1, l2, d):
    if isinstance(d, int):
        return Fraction(d, dot1(l1, l1)) * Fraction(d, dot1(l2, l2))
    return (d * d) / (dot1(l1, l1) * dot1(l2, l2))


def spread(l1, l2):
    return sbase(l1, l2, cross2(l1, l2))


def tri_quadrance(triangle):
    return tri_func(quadrance, triangle)


def tri_spread(trilateral):
    return tri_func(spread, trilateral)


def cross(l1, l2):
    return sbase(l1, l2, dot1(l1, l2))


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


def Ptolemy(Q):
    Q12, Q23, Q34, Q14, Q13, Q24 = Q
    return Ar(Q12*Q34, Q23*Q14, Q13*Q24) == 0


def distance(a, b):
    return np.sqrt(float(quadrance(a, b)))


def angle(l, m):
    return np.arcsin(np.sqrt(float(spread(l, m))))
