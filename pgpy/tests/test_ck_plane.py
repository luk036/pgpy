from __future__ import print_function

from ..ck_plane import ck
from ..proj_plane import pg_point, pg_line, tri_dual


def chk_int(myck, pg_obj=pg_point):
    a1 = pg_obj([1, 2, 3])
    a2 = pg_obj([4, -5, 6])
    a3 = pg_obj([-7, 8, 9])

    temp = myck.perp(a1)
    assert(myck.perp(temp) == a1)

    triangle = [a1, a2, a3]
    trilateral = tri_dual(triangle)
    l1, _, _ = trilateral
    assert l1.incident(a2)
    assert(myck.perp(myck.perp(l1)) == l1)

    t1, t2, t3 = myck.tri_altitude(triangle)
    assert myck.is_perpendicular(t1, l1)

    o = myck.orthocenter(triangle)
    assert o == t2 * t3
    assert a1 == myck.orthocenter([o, a2, a3])

    tau = myck.reflect(l1)
    assert(tau(tau(a1)) == a1)

    q1, q2, q3 = myck.tri_measure(triangle)
    s1, s2, s3 = myck.tri_measure(trilateral)
    print(q1/s1, q2/s2, q3/s3)
    assert(q1*s2 == q2*s1)
    assert myck.measure(l1, l1) == 0
    assert myck.measure(a1, a1) == 0


class myck(ck):
    @classmethod
    def perp(cls, v):
        [x, y, z] = v
        if isinstance(v, pg_point):
            return pg_line([-2*x, y, -2*z])
        elif isinstance(v, pg_line):
            return pg_point([-x, 2*y, -z])
        else:
            raise NotImplementedError()


def test_int():
    chk_int(myck(), pg_point)
    chk_int(myck(), pg_line)


# def no_test_symbolic():
#     import sympy
#     sympy.init_printing()
#     myck = ck(tstperp)
#     pv = sympy.symbols("p:3", integer=True)
#     qv = sympy.symbols("q:3", integer=True)
#     rv = sympy.symbols("r:3", integer=True)

#     a1 = pg_point(pv)
#     a2 = pg_point(qv)
#     a3 = pg_point(rv)
#     l1 = join(a2, a3)
#     l2 = join(a1, a3)
#     l3 = join(a1, a2)
#     t1 = myck.altitude(a1, l1)
#     t2 = myck.altitude(a2, l2)
#     t3 = myck.altitude(a3, l3)
#     ans = t1.dot(meet(t2, t3))
#     ans = sympy.simplify(ans)
#     assert ans == 0
