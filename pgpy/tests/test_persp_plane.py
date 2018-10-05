from __future__ import print_function

from ..persp_plane import persp_euclid_plane
from ..proj_plane import pg_point, pg_line, tri_dual, meet


def chk_degenerate(myck):
    a1 = pg_point([-1, 2, 3])
    a2 = pg_point([4, -1, 1])
    a3 = pg_point([0, -1, 1])

    triangle = [a1, a2, a3]
    trilateral = tri_dual(triangle)
    l1, _, _ = trilateral
    assert l1.incident(a2)

    t1, t2, t3 = myck.tri_altitude(triangle)
    assert myck.is_perpendicular(t1, l1)

    o = myck.orthocenter(triangle)
    assert o == meet(t2, t3)
    assert a1 == myck.orthocenter([o, a2, a3])

    q1, q2, q3 = myck.tri_quadrance(triangle)
    s1, s2, s3 = myck.tri_spread(trilateral)
    print(q1/s1, q2/s2, q3/s3)
    assert q1*s2 == q2*s1
    assert myck.spread(l1, l1) == 0
    assert myck.quadrance(a1, a1) == 0

    tqf = ((q1 + q2 + q3)**2) - 2*(q1*q1 + q2*q2 + q3*q3)
    assert tqf == myck.Ar(q1, q2, q3)


def test_int():
    Ire = pg_point([0, 1, 1])
    Iim = pg_point([1, 0, 0])
    l_inf = pg_line([0, -1, 1])
    P = persp_euclid_plane(Ire, Iim, l_inf)
    chk_degenerate(P)
