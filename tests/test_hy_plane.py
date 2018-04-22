from __future__ import print_function

from ..hy_plane import hyck
from .test_ck_plane import chk_int
from .test_ell_plane import chk_tri

def test_int():
    chk_int(hyck())

def test_tri():
    chk_tri(hyck())

