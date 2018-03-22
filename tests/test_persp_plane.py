from __future__ import print_function

from ..persp_plane import * 

def test_int():
    A_inf = pg_point([-1j, 1, 1])
    B_inf = pg_point([1j, 1, 1])
    P = persp_euclid_plane(A_inf, B_inf)

    a1 = pg_point([1, 3, 1])
    a2 = pg_point([4, 2, 1])
    a3 = pg_point([4, -3, 1])
    # a3 = pg_point([sx, sy, sz])
    l1 = join(a2, a3)
    l2 = join(a1, a3)
    l3 = join(a1, a2)
 
    t1 = P.altitude(a1, l1)
    assert P.is_perpendicular(t1, l1)
    t2 = P.altitude(a2, l2)
    t3 = P.altitude(a3, l3)
    o = P.orthocenter(a1, a2, a3)
    assert o ==  meet(t2, t3)
    assert a1 == P.orthocenter(o, a2, a3)

    # tau = P.line_reflect(l1)
    # assert(tau(tau(a1)) == a1)

    q1 = P.quadrance(a2, a3)
    q2 = P.quadrance(a1, a3)
    q3 = P.quadrance(a1, a2)
    s1 = P.spread(l2, l3)
    s2 = P.spread(l1, l3)
    s3 = P.spread(l1, l2)
    # print(q1/s1, q2/s2, q3/s3)
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
