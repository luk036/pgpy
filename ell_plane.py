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

    return v.dual()(v.base)

class ellck(ck):

    def __init__(self):
        ck.__init__(self, elldual)

