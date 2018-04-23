from __future__ import print_function

from ..persp_plane import persp_euclid_plane
from ..proj_plane import pg_point, pg_line, tri, join, meet

def chk_degenerate(myck):
    a1 = pg_point([1, 2, 3])
    a2 = pg_point([4, -5, 6])
    a3 = pg_point([-7, 8, 9])

    l1, l2, l3 = tri(a1, a2, a3)
    assert l1.incident(a2)

    t1, t2, t3 = myck.tri_altitude(a1, a2, a3)
    assert myck.is_perpendicular(t1, l1)

    o = myck.orthocenter(a1, a2, a3)
    assert o == meet(t2, t3)
    assert a1 == myck.orthocenter(o, a2, a3)

    #tau = myck.reflect(l1)
    #assert(tau(tau(a1)) == a1)

    q1, q2, q3 = myck.tri_quadrance(a1, a2, a3)
    s1, s2, s3 = myck.tri_spread(l1, l2, l3)
    print(q1/s1, q2/s2, q3/s3)
    assert myck.spread(l1, l1) == 0
    assert myck.quadrance(a1, a1) == 0

    tqf = ((q1 + q2 + q3)**2) - 2*(q1*q1 + q2*q2 + q3*q3)
    assert tqf == myck.Ar(q1, q2, q3)


def test_int():
    A_inf = pg_point([-1j, 1, 1])
    B_inf = pg_point([1j, 1, 1])
    l_inf = pg_line([0, -1, 1])
    P = persp_euclid_plane(A_inf, B_inf, l_inf)
    chk_degenerate(P)
