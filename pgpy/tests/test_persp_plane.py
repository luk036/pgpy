from __future__ import print_function

from ..persp_plane import persp_euclid_plane
from ..proj_plane import pg_point, pg_line, tri_dual, meet, coincident
from .test_ck_plane import chk_int
from ..euclid_plane import Ar

def chk_degenerate(myck):
    a1 = pg_point([-1, 2, 3])
    a2 = pg_point([4, -1, 1])
    a3 = pg_point([0, -1, 1])

    triangle = [a1, a2, a3]
    trilateral = tri_dual(triangle)
    l1, l2, l3 = trilateral
    assert not myck.is_parallel(l1, l2)
    assert not myck.is_parallel(l2, l3)

    m12 = myck.midpoint(a1, a2)
    m23 = myck.midpoint(a2, a3)
    m13 = myck.midpoint(a1, a3)

    t1 = a1 * m23
    t2 = a2 * m13
    t3 = a3 * m12
    assert coincident(t1, t2, t3)

    q1, q2, q3 = myck.tri_quadrance(triangle)
    tqf = ((q1 + q2 + q3)**2) - 2*(q1*q1 + q2*q2 + q3*q3)
    assert tqf == Ar(q1, q2, q3)


def test_int():
    Ire = pg_point([0, 1, 1])
    Iim = pg_point([1, 0, 0])
    l_inf = pg_line([0, -1, 1])
    P = persp_euclid_plane(Ire, Iim, l_inf)
    chk_int(P, pg_point)
    chk_degenerate(P)
