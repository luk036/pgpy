from __future__ import print_function

from ..ck_plane import ellck, hyck, check_cross_TQF, check_cross_law
from ..proj_plane import pg_point, tri_dual, join, plucker, cross
from pytest import approx


# def test_int():
#     chk_int(ellck(), pg_point)
#     chk_int(ellck(), pg_line)

def chk_tri_float(myck):
    a1 = pg_point([34., 12., 563.])
    a2 = pg_point([345., 655., 34.])
    a3 = pg_point([3., 57., -68.])

    temp = myck.perp(a1)
    assert cross(myck.perp(temp), a1) == approx((0, 0, 0))

    triangle = [a1, a2, a3]
    trilateral = tri_dual(triangle)

    l1, _, _ = trilateral
    assert cross(myck.perp(myck.perp(l1)), l1) == approx((0, 0, 0))

    Q = myck.tri_quadrance(triangle)
    S = myck.tri_spread(trilateral)

    assert check_cross_law(S, Q[2]) == approx(0)
    assert check_cross_law(Q, S[2]) == approx(0)

    a3 = plucker(2, a1, 3, a2)
    collin = [a1, a2, a3]
    Q = myck.tri_quadrance(collin)
    assert check_cross_TQF(Q) == approx(0)


def chk_tri_int(myck):
    a1 = pg_point([3433, 12321, 5634])
    a2 = pg_point([3453, 65564, 344])
    a3 = pg_point([3454, 5764, -6862])

    temp = myck.perp(a1)
    assert(myck.perp(temp) == a1)

    triangle = [a1, a2, a3]
    trilateral = tri_dual(triangle)

    l1, _, _ = trilateral
    assert(myck.perp(myck.perp(l1)) == l1)

    assert(myck.quadrance(a1, a1) == 0)
    assert(myck.spread(l1, l1) == 0)

    Q = myck.tri_quadrance(triangle)
    S = myck.tri_spread(trilateral)

    assert check_cross_law(S, Q[2]) == 0
    assert check_cross_law(Q, S[2]) == 0

    a3 = plucker(2, a1, 3, a2)
    collin = [a1, a2, a3]
    Q = myck.tri_quadrance(collin)
    assert check_cross_TQF(Q) == 0


def test_ell_hy():
    chk_tri_int(ellck())
    chk_tri_int(hyck())

    chk_tri_float(ellck())
    chk_tri_float(hyck())

# def no_test_symbolic(myck):
#     import sympy
#     sympy.init_printing()
#     pv = sympy.symbols("p:3", integer=True)
#     qv = sympy.symbols("q:3", integer=True)

#     a1 = pg_point(pv)
#     a2 = pg_point(qv)

#     lambda1, mu1 = sympy.symbols("lambda1 mu1", integer=True)
#     a3 = plucker(lambda1, a1, mu1, a2)

#     q1 = myck.quadrance(a2, a3)
#     q2 = myck.quadrance(a1, a3)
#     q3 = myck.quadrance(a1, a2)
#     tqf = (q1 + q2 + q3)**2 - 2*(q1*q1 + q2*q2 + q3*q3) - 4*q1*q2*q3
#     tqf = sympy.simplify(tqf)
#     assert tqf == 0

#     sv = sympy.symbols("s:3", integer=True)
#     a3 = pg_point(sv)
#     l1 = join(a2, a3)
#     l2 = join(a1, a3)
#     l3 = join(a1, a2)
#     t1 = myck.altitude(a1, l1)
#     t2 = myck.altitude(a2, l2)
#     t3 = myck.altitude(a3, l3)
#     o = t1*t2
#     ans = t3.dot(o)
#     ans = sympy.simplify(ans)
#     assert ans == 0
