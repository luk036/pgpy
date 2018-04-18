# -*- coding: utf-8 -*-
from __future__ import print_function

from pprint import pprint
from .ck_plane import ck
from .proj_plane import pg_point, pg_line, join, meet


def dual(v):
    """pole/polar of v in elliptic geometry

    Arguments:
        v {pg_point/pg_line} -- projective point or plane 

    Raises:
        NotImplementedError

    Returns:
        [type] -- [description]
    """

    if isinstance(v, pg_point):
        return pg_line(v.base)
    elif isinstance(v, pg_line):
        return pg_point(v.base)
    raise NotImplementedError()


__ellck = ck(dual)


def is_perpendicular(l, m):
    return __ellck.is_perpendicular(l, m)


def line_reflect(m):
    return __ellck.line_reflect(m)


def altitude(p, l):
    return __ellck.altitude(p, l)


def orthocenter(a1, a2, a3):
    return __ellck.orthocenter(a1, a2, a3)


def quadrance(a1, a2):
    return __ellck.quadrance(a1, a2)


def spread(l1, l2):
    return __ellck.spread(l1, l2)
