# -*- coding: utf-8 -*-
from .ck_plane import *


def dual(v):
    [x, y, z] = v
    if isinstance(v, pg_point):
        return pg_line([x, y, z])
    elif isinstance(v, pg_line):
        return pg_point([x, y, z])
    else:
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


