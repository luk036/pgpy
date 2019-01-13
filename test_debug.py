from __future__ import print_function

from pgpy.euclid_plane import *
from pgpy.proj_plane import tri_dual, join, meet, coincident, harm_conj, R


def test_int():
    a1 = uc_point(1, 2)
    a2 = uc_point(3, 4)
    a3 = uc_point(-1, 2)
    a4 = uc_point(-5, 1)
    q12 = quadrance(a1, a2)
    q23 = quadrance(a2, a3)
    q34 = quadrance(a3, a4)
    q14 = quadrance(a1, a4)
    q24 = quadrance(a2, a4)
    q13 = quadrance(a1, a3)
    print(q12, q23, q34, q14, q24, q13)
    t = Ar(q12*q34, q23*q14, q13*q24)
    # t = sympy.simplify(t)
    assert t == 0
    t = Ptolemy([q12, q23, q34, q14, q24, q13])
    assert t


if __name__ == "__main__":
    test_int()
