from __future__ import print_function

from ..ck_plane import ck, ellck, hyck, check_sine_law
from ..proj_plane import pg_point, pg_line, tri_dual, x_ratio, coincident
from ..proj_plane import cross
from pytest import approx


def chk_float(myck, pg_obj=pg_point):
    a1 = pg_obj([3., 2., 7.])
    a2 = pg_obj([2., -2., 1.])
    a3 = pg_obj([-3., 4., 6.])

    triangle = [a1, a2, a3]
    trilateral = tri_dual(triangle)
    l1, _, _ = trilateral
    assert l1.dot(a2) == approx(0)

    t1, t2, t3 = myck.tri_altitude(triangle)
    assert l1.dot(myck.perp(t1)) == approx(0)
    assert t1.dot(t2 * t3) == approx(0)

    o = myck.orthocenter(triangle)
    assert cross(o, t2 * t3) == approx((0, 0, 0))
    assert cross(a1, myck.orthocenter([o, a2, a3])) == approx((0, 0, 0))

    tau = myck.reflect(l1)
    assert cross(tau(tau(a1)), a1) == approx((0, 0, 0))

    assert myck.measure(l1, l1) == approx(0)
    assert myck.measure(a1, a1) == approx(0)

    Q = myck.tri_measure(triangle)
    S = myck.tri_measure(trilateral)
    assert Q[0] * S[1] == approx(Q[1] * S[0])
    assert Q[1] * S[2] == approx(Q[2] * S[1])


def chk_int(myck, pg_obj=pg_point):
    a1 = pg_obj([23241, 2322, 2343])
    a2 = pg_obj([23234, -23420, 23346])
    a3 = pg_obj([-2347, 23431, 5652])

    triangle = [a1, a2, a3]
    trilateral = tri_dual(triangle)
    l1, _, _ = trilateral
    assert l1.incident(a2)

    t1, t2, t3 = myck.tri_altitude(triangle)
    assert myck.is_perpendicular(t1, l1)
    assert coincident(t1, t2, t3)

    o = myck.orthocenter(triangle)
    assert o == t2 * t3
    assert a1 == myck.orthocenter([o, a2, a3])

    tau = myck.reflect(l1)
    assert tau(tau(a1)) == a1

    assert myck.measure(l1, l1) == 0
    assert myck.measure(a1, a1) == 0

    Q = myck.tri_measure(triangle)
    S = myck.tri_measure(trilateral)
    assert check_sine_law(Q, S)


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

    def measure(self, a1, a2):
        return 1 - x_ratio(a1, a2, self.perp(a2), self.perp(a1))


def test_int():
    chk_int(myck(), pg_point)
    chk_int(myck(), pg_line)

    chk_int(ellck(), pg_point)
    chk_int(ellck(), pg_line)

    chk_int(hyck(), pg_point)
    chk_int(hyck(), pg_line)

    chk_float(myck(), pg_point)
    chk_float(myck(), pg_line)

    chk_float(ellck(), pg_point)
    chk_float(ellck(), pg_line)

    chk_float(hyck(), pg_point)
    chk_float(hyck(), pg_line)


# def no_test_symbolic():
#     import sympy
#     sympy.init_printing()
#     pv = sympy.symbols("p:3", integer=True)
#     qv = sympy.symbols("q:3", integer=True)
#     rv = sympy.symbols("r:3", integer=True)

#     tstck = myck()
#     a1 = pg_point(pv)
#     a2 = pg_point(qv)
#     a3 = pg_point(rv)
#     l1 = join(a2, a3)
#     l2 = join(a1, a3)
#     l3 = join(a1, a2)
#     t1 = tstck.altitude(a1, l1)
#     t2 = tstck.altitude(a2, l2)
#     t3 = tstck.altitude(a3, l3)
#     ans = t1.dot(meet(t2, t3))
#     ans = sympy.simplify(ans)
#     assert ans == 0
