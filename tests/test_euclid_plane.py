from __future__ import print_function

from pytest import approx

from pgpy.euclid_plane import (
    Ar,
    Ptolemy,
    angle,
    cross2,
    cross_s,
    distance,
    dot1,
    is_parallel,
    is_perpendicular,
    orthocenter,
    quad_quadrance,
    quadrance,
    reflect,
    spread,
    tri_altitude,
    tri_midpoint,
    tri_quadrance,
    tri_spread,
    uc_point
)
from pgpy.proj_plane import (
    R,
    coincident,
    cross,
    harm_conj,
    meet,
    pg_point,
    plucker,
    tri_dual
)


def chk_euclid(K):
    """[summary]

    Arguments:
        K (type): [description]

    Raises:
        NotImplementedError -- [description]
        NotImplementedError -- [description]
    """
    if K == int:
        a1 = pg_point([31, -53, 1])
        a2 = pg_point([6, 23, 21])
        a3 = pg_point([5, -43, 31])
    elif K == float:
        a1 = pg_point([3., -5., 2.])
        a2 = pg_point([6., 2., 2.])
        a3 = pg_point([5., -4., 3.])
    else:
        raise NotImplementedError()

    triangle = [a1, a2, a3]
    trilateral = tri_dual(triangle)
    l1, l2, l3 = trilateral
    t1, t2, t3 = tri_altitude(triangle)
    t4 = harm_conj(t1, t2, t3)
    o = orthocenter(triangle)
    tau = reflect(l1)
    m23, m13, m12 = tri_midpoint(triangle)
    mt1 = a1 * m23
    mt2 = a2 * m13
    mt3 = a3 * m12
    q1, q2, q3 = tri_quadrance(triangle)
    s1, s2, s3 = tri_spread(trilateral)
    tqf = ((q1 + q2 + q3)**2) - 2 * (q1 * q1 + q2 * q2 + q3 * q3)
    tsf = (s1 + s2 +
           s3)**2 - 2 * (s1 * s1 + s2 * s2 + s3 * s3) - 4 * s1 * s2 * s3
    c3 = ((q1 + q2 - q3)**2) / (4 * q1 * q2)
    a4 = plucker(3, a1, 4, a2)
    qq1, qq2, qq3 = tri_quadrance([a1, a2, a4])
    tqf2 = Ar(qq1, qq2, qq3)  # get 0

    if K == int:
        assert not is_parallel(l1, l2)
        assert not is_parallel(l2, l3)
        assert is_perpendicular(t1, l1)
        assert spread(t1, l1) == 1  # get 1
        assert coincident(t1, t2, t3)
        assert R(t1, t2, t3, t4) == -1
        assert o == meet(t2, t3)
        assert a1 == orthocenter([o, a2, a3])
        assert tau(tau(a1)) == a1
        assert coincident(mt1, mt2, mt3)
        assert spread(l1, l1) == 0
        assert quadrance(a1, a1) == 0
        assert cross_s(l1, l2) == c3
        assert c3 + s3 == 1  # get the same
        assert tqf == Ar(q1, q2, q3)
        assert tsf == 0
        assert tqf2 == 0
    elif K == float:
        assert cross2(l1, l2) != approx(0)
        assert cross2(l2, l3) != approx(0)
        assert dot1(t1, l1) == approx(0)
        assert spread(t1, l1) == approx(1)  # get 1
        assert t1.dot(t2 * t3) == approx(0)
        assert R(t1, t2, t3, t4) == approx(-1)
        assert cross(o, meet(t2, t3)) == approx((0, 0, 0))
        assert cross(a1, orthocenter([o, a2, a3])) == approx((0, 0, 0))
        assert cross(tau(tau(a1)), a1) == approx((0, 0, 0))
        assert mt1.dot(mt2 * mt3) == approx(0)
        assert spread(l1, l1) == approx(0)
        assert quadrance(a1, a1) == approx(0)
        assert angle(l1, l1) == approx(0)
        assert distance(a1, a1) == approx(0)
        assert cross_s(l1, l2) == approx(c3)
        assert c3 + s3 == approx(1)  # get the same
        assert approx(tqf) == Ar(q1, q2, q3)
        assert tsf == approx(0)
        assert tqf2 == approx(0)
    else:
        raise NotImplementedError()


def chk_circle(K):
    """[summary]

    Arguments:
        K (type): [description]

    Raises:
        NotImplementedError -- [description]
        NotImplementedError -- [description]
    """
    if K == int:
        ca1 = uc_point(1, 2)
        ca2 = uc_point(3, 4)
        ca3 = uc_point(-1, 2)
        ca4 = uc_point(-5, 1)
    elif K == float:
        ca1 = uc_point(1., 2.)
        ca2 = uc_point(3., 4.)
        ca3 = uc_point(-1., 2.)
        ca4 = uc_point(-5., 1.)
    else:
        raise NotImplementedError()

    quadr = quad_quadrance([ca1, ca2, ca3, ca4])
    q12, q23, q34, q14, q24, q13 = quadr

    if K == int:
        assert Ar(q12 * q34, q23 * q14, q13 * q24) == 0
        assert Ptolemy(quadr)
    elif K == float:
        assert Ar(q12 * q34, q23 * q14, q13 * q24) == approx(0)
    else:
        raise NotImplementedError()


def test_euclid():
    chk_euclid(int)
    chk_euclid(float)
    chk_circle(int)
    chk_circle(float)


# def no_test_symbolic():
#     import sympy
#     sympy.init_printing()
#     lambda1, mu1 = sympy.symbols("lambda1 mu1", integer=True)
#     lambda2, mu2 = sympy.symbols("lambda2 mu2", integer=True)
#     lambda3, mu3 = sympy.symbols("lambda3 mu3", integer=True)
#     lambda4, mu4 = sympy.symbols("lambda4 mu4", integer=True)
#     a1 = uc_point(lambda1, mu1)
#     a2 = uc_point(lambda2, mu2)
#     a3 = uc_point(lambda3, mu3)
#     a4 = uc_point(lambda4, mu4)
#     q12 = quadrance(a1, a2)
#     q23 = quadrance(a2, a3)
#     q34 = quadrance(a3, a4)
#     q14 = quadrance(a1, a4)
#     q24 = quadrance(a2, a4)
#     q13 = quadrance(a1, a3)
#     #print(q12, q23, q34, q14, q24, q13)
#     t = Ar(q12*q34, q23*q14, q13*q24)
#     t = sympy.simplify(t)
#     assert t == 0
