from __future__ import print_function

from ..ck_plane import *


def tstdual(v):
    [x, y, z] = v
    if isinstance(v, pg_point):
        return pg_line([-2*x, y, -2*z])
    elif isinstance(v, pg_line):
        return pg_point([-x, 2*y, -z])
    else:
        raise NotImplementedError()


def test_int():
    myck = ck(tstdual)
    a1 = pg_point([1, 2, 3])
    a2 = pg_point([4, -5, 6])
    a3 = pg_point([-7, 8, 9])

    assert(myck.dual(myck.dual(a1)) == a1)

    l1 = join(a2, a3)
    assert l1.incident(a2)
    l2 = join(a1, a3)
    l3 = join(a1, a2)

    assert(myck.dual(myck.dual(l1)) == l1)

    t1 = myck.altitude(a1, l1)
    assert myck.is_perpendicular(t1, l1)

    t2 = myck.altitude(a2, l2)
    t3 = myck.altitude(a3, l3)
    o = myck.orthocenter(a1, a2, a3)
    assert o == meet(t2, t3)
    assert a1 == myck.orthocenter(o, a2, a3)

    tau = myck.line_reflect(l1)
    assert(tau(tau(a1)) == a1)

    q1 = myck.quadrance(a2, a3)
    q2 = myck.quadrance(a1, a3)
    q3 = myck.quadrance(a1, a2)
    s1 = myck.spread(l2, l3)
    s2 = myck.spread(l1, l3)
    s3 = myck.spread(l1, l2)
    # print(q1/s1, q2/s2, q3/s3)
    assert myck.spread(l1, l1) == 0
    assert myck.quadrance(a1, a1) == 0
