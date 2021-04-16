from __future__ import print_function

from pgpy.ck_plane import check_cross_law, check_cross_TQF, ellck, hyck
from pgpy.proj_plane import pg_point, plucker, tri_dual


def chk_tri_ell_hy(myck):
    """[summary]

    Arguments:
        myck (type): [description]
        K (type): [description]

    Raises:
        NotImplementedError -- [description]
        NotImplementedError -- [description]
    """
    a1 = pg_point([33, 121, 54])
    a2 = pg_point([33, 564, 34])
    a3 = pg_point([34, 64, -62])

    temp = myck.perp(a1)
    triangle = [a1, a2, a3]
    trilateral = tri_dual(triangle)
    l1, _, _ = trilateral
    Q = myck.tri_quadrance(triangle)
    S = myck.tri_spread(trilateral)
    a4 = plucker(2, a1, 3, a2)
    collin = [a1, a2, a4]
    Q2 = myck.tri_quadrance(collin)

    assert myck.perp(temp) == a1
    assert myck.perp(myck.perp(l1)) == l1
    assert myck.quadrance(a1, a1) == 0
    assert myck.spread(l1, l1) == 0
    assert check_cross_law(S, Q[2]) == 0
    assert check_cross_law(Q, S[2]) == 0
    assert check_cross_TQF(Q2) == 0


def test_ell_hy():
    chk_tri_ell_hy(ellck())
    chk_tri_ell_hy(hyck())

    chk_tri_ell_hy(ellck())
    chk_tri_ell_hy(hyck())


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
