from __future__ import print_function

from ..ck_plane import ellck, check_cross_TQF, check_cross_law, check_sine_law
from ..proj_plane import pg_point, pg_line, tri_dual, join, plucker
from .test_ck_plane import chk_int


def test_int():
    chk_int(ellck(), pg_point)
    chk_int(ellck(), pg_line)


def chk_tri(myck):
    a1 = pg_point([1, 3, 1])
    a2 = pg_point([4, 2, 1])
    a3 = pg_point([1, 1, -1])

    temp = myck.perp(a1)
    assert(myck.perp(temp) == a1)

    triangle = [a1, a2, a3]
    trilateral = tri_dual(triangle)

    l1, l2, _ = trilateral
    assert(myck.perp(myck.perp(l1)) == l1)

    Q = myck.tri_quadrance(triangle)
    S = myck.tri_spread(trilateral)

    assert check_cross_law(S, Q[2])
    assert check_cross_law(Q, S[2])

    a3 = plucker(2, a1, 3, a2)
    collin = [a1, a2, a3]
    Q = myck.tri_quadrance(collin)
    assert check_cross_TQF(Q) == 0


def test_ell():
    chk_tri(ellck())

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
