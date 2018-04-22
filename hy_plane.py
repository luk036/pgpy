# -*- coding: utf-8 -*-
from pgpy.ck_plane import ck
from pgpy.proj_plane import pg_point, pg_line


def hydual(v):
    [x, y, z] = v
    if isinstance(v, pg_point):
        return pg_line([x, y, -z])
    elif isinstance(v, pg_line):
        return pg_point([x, y, -z])
    raise NotImplementedError()


class hyck(ck):

    def __init__(self):
        ck.__init__(self, hydual)
