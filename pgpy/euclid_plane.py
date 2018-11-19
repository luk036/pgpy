# -*- coding: utf-8 -*-
import numpy as np
from fractions import Fraction
from .proj_plane import pg_point, tri_dual, involution, tri_func, quad_func, plucker
from .pg_common import cross2, dot1


def fB(l):
    """[summary]

    Arguments:
            l {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    [a, b] = l[:2]
    return pg_point([a, b, 0])


def is_perpendicular(l, m):
    """[summary]

    Arguments:
            l {[type]} -- [description]
            m {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    return dot1(l, m) == 0


def is_parallel(l, m):
    """[summary]

    Arguments:
            l {[type]} -- [description]
            m {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    return cross2(l, m) == 0


def altitude(a, l):
    """[summary]

    Arguments:
            a {[type]} -- [description]
            l {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    return a * fB(l)


def tri_altitude(tri):
    """[summary]

    Arguments:
            tri {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    l1, l2, l3 = tri_dual(tri)
    a1, a2, a3 = tri
    t1 = altitude(a1, l1)
    t2 = altitude(a2, l2)
    t3 = altitude(a3, l3)
    return t1, t2, t3


def orthocenter(tri):
    """[summary]

    Arguments:
            tri {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    a1, a2, a3 = tri
    t1 = altitude(a1, a2*a3)
    t2 = altitude(a2, a1*a3)
    return t1*t2


def reflect(m):
    """[summary]

    Arguments:
            m {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    return involution(m, fB(m))


def midpoint(a, b):
    """[summary]

    Arguments:
            a {[type]} -- [description]
            b {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    return plucker(b[2], a, a[2], b)


def tri_midpoint(triangle):
    """[summary]

    Arguments:
            triangle {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    return tri_func(midpoint, triangle)

# Angle Bisector???


def quad1(P):
    """[summary]

    Arguments:
            P {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    x1, z1, x2, z2 = P
    for v in P:
        if not isinstance(v, int):
            return (x1/z1 - x2/z2)**2
    return (Fraction(x1, z1) - Fraction(x2, z2))**2


def quadrance(a1, a2):
    """[summary]

    Arguments:
            a1 {[type]} -- [description]
            a2 {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    return quad1((a1[0], a1[2], a2[0], a2[2])) + \
        quad1((a1[1], a1[2], a2[1], a2[2]))


def sbase(l1, l2, d):
    """[summary]

    Arguments:
            l1 {[type]} -- [description]
            l2 {[type]} -- [description]
            d {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    if isinstance(d, int):
        return Fraction(d, dot1(l1, l1)) * Fraction(d, dot1(l2, l2))
    return (d * d) / (dot1(l1, l1) * dot1(l2, l2))


def spread(l1, l2):
    """[summary]

    Arguments:
            l1 {[type]} -- [description]
            l2 {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    return sbase(l1, l2, cross2(l1, l2))


def tri_quadrance(triangle):
    """[summary]

    Arguments:
            triangle {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    return tri_func(quadrance, triangle)


def tri_spread(trilateral):
    """[summary]

    Arguments:
            trilateral {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    return tri_func(spread, trilateral)


def quad_quadrance(quadrangle):
    """[summary]

    Arguments:
            quadrangle {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    return quad_func(quadrance, quadrangle)


def cross_s(l1, l2):
    """[summary]

    Arguments:
            l1 {[type]} -- [description]
            l2 {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    return sbase(l1, l2, dot1(l1, l2))


def uc_point(lambda1, mu1):
    """[summary]

    Arguments:
            lambda1 {[type]} -- [description]
            mu1 {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    return pg_point([lambda1**2 - mu1**2,
                     2*lambda1*mu1, lambda1**2 + mu1**2])


def Ar(a, b, c):
    """Archimedes's function

    Arguments:
            a {[type]} -- [description]
            b {[type]} -- [description]
            c {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    return (4*a*b) - (a + b - c)**2


# def cqq(a, b, c, d):
#     ''' Cyclic quadrilateral quadrea theorem '''
#     t1 = 4*a*b
#     t2 = 4*c*d
#     m = (t1 + t2) - (a + b - c - d)**2
#     p = m*m - 4*t1*t2
#     return m, p


def Ptolemy(Q):
    """[summary]

    Arguments:
            Q {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    Q12, Q23, Q34, Q14, Q13, Q24 = Q
    return Ar(Q12*Q34, Q23*Q14, Q13*Q24) == 0


def distance(a, b):
    """[summary]

    Arguments:
            a {[type]} -- [description]
            b {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    return np.sqrt(float(quadrance(a, b)))


def angle(l, m):
    """[summary]

    Arguments:
            l {[type]} -- [description]
            m {[type]} -- [description]

    Returns:
            [type] -- [description]
    """
    return np.arcsin(np.sqrt(float(spread(l, m))))
