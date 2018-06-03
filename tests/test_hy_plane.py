from __future__ import print_function

from ..ck_plane import hyck
from ..proj_plane import pg_point, pg_line
from .test_ck_plane import chk_int
from .test_ell_plane import chk_tri


def test_int():
    chk_int(hyck(), pg_point)
    chk_int(hyck(), pg_line)


def test_tri():
    chk_tri(hyck())
