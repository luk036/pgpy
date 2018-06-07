from __future__ import print_function

from ..proj_line import *


def test_complex_point():
    p = pl_point([1-2j, 3-1j])  # complex number
    assert(p == p)
