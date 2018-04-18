# -*- coding: utf-8 -*-
from .ck_plane import ck
from .proj_plane import pg_point, pg_line, join, meet


def dual(v):
    [x, y, z] = v
    if isinstance(v, pg_point):
        return pg_line([x, y, -z])
    elif isinstance(v, pg_line):
        return pg_point([x, y, -z])
    else:
        raise NotImplementedError()


__hyck = ck(dual)


def is_perpendicular(l, m):
    return __hyck.is_perpendicular(l, m)


def line_reflect(m):
    return __hyck.line_reflect(m)


def altitude(p, l):
    return __hyck.altitude(p, l)


def orthocenter(a1, a2, a3):
    return __hyck.orthocenter(a1, a2, a3)


def quadrance(a1, a2):
    return __hyck.quadrance(a1, a2)


def spread(l1, l2):
    return __hyck.spread(l1, l2)
