from __future__ import print_function

from ..persp_plane import *
from ..proj_plane import tri, join, meet


def test_int():
    A_inf = pg_point([-1j, 1, 1])
    B_inf = pg_point([1j, 1, 1])
    l_inf = pg_line([0, -1, 1])
    P = persp_euclid_plane(A_inf, B_inf, l_inf)

    a1 = pg_point([1, 3, 1])
    a2 = pg_point([4, 2, 1])
    a3 = pg_point([4, -3, 1])
    # a3 = pg_point([sx, sy, sz])
    # l1 = join(a2, a3)
    # l2 = join(a1, a3)
    # l3 = join(a1, a2)
    l1, l2, l3 = tri(a1, a2, a3)
    
    t1, t2, t3 = P.tri_altitude(a1, a2, a3)
    assert P.is_perpendicular(t1, l1)

    o = P.orthocenter(a1, a2, a3)
    assert o == meet(t2, t3)
    assert a1 == P.orthocenter(o, a2, a3)

    # tau = P.line_reflect(l1)
    # assert(tau(tau(a1)) == a1)

    q1, q2, q3 = P.tri_quadrance(a1, a2, a3)
    s1, s2, s3 = P.tri_spread(l1, l2, l3)
    print(q1/s1, q2/s2, q3/s3)
    # assert P.spread(t1, l1) == 1.0 # get 1.0
    assert coincident(t1, t2, t3)

    tqf = ((q1 + q2 + q3)**2) - 2*(q1*q1 + q2*q2 + q3*q3)
    assert tqf == P.Ar(q1, q2, q3)

    assert P.spread(l1, l1) == 0
    assert P.quadrance(a1, a1) == 0

    # c3 = ((q1 + q2 - q3)**2) / (4*q1*q2)
    # assert c3 + s3 == 1 # get the same

    # tsf = (s1 + s2 + s3)**2 - 2*(s1*s1 + s2*s2 + s3*s3) - 4*s1*s2*s3
    # tsf = sympy.simplify(tsf)
    #assert tsf == 0
