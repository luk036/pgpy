# -*- coding: utf-8 -*-
from pgpy.ck_plane import ck
from pgpy.proj_plane import pg_point, pg_line


def elldual(v):
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


class ellck(ck):

    def __init__(self):
        ck.__init__(self, elldual)

