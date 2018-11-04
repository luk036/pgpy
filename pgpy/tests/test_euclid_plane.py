from __future__ import print_function

from ..euclid_plane import *
from ..proj_plane import tri_dual, join, meet, coincident, harm_conj, R, cross
from pytest import approx


def test_float():
    a1 = pg_point([3., -5., 2.])
    a2 = pg_point([6., 2., 2.])
    a3 = pg_point([5., -4., 3.])

    triangle = [a1, a2, a3]
    trilateral = tri_dual(triangle)
    l1, l2, l3 = trilateral
    assert cross2(l1, l2) != approx(0)
    assert cross2(l2, l3) != approx(0)

    t1, t2, t3 = tri_altitude(triangle)
    assert dot1(t1, l1) == approx(0)
    assert spread(t1, l1) == approx(1)  # get 1
    assert t1.dot(t2 * t3) == approx(0)

    t4 = harm_conj(t1, t2, t3)
    assert R(t1, t2, t3, t4) == approx(-1)

    o = orthocenter(triangle)
    assert cross(o, meet(t2, t3)) == approx((0, 0, 0))
    assert cross(a1, orthocenter([o, a2, a3])) == approx((0, 0, 0))

    tau = reflect(l1)
    assert cross(tau(tau(a1)), a1) == approx((0, 0, 0))

    m12 = midpoint(a1, a2)
    m23 = midpoint(a2, a3)
    m13 = midpoint(a1, a3)
    t1 = a1 * m23
    t2 = a2 * m13
    t3 = a3 * m12
    assert t1.dot(t2 * t3) == approx(0)

    q1, q2, q3 = tri_quadrance(triangle)
    s1, s2, s3 = tri_spread(trilateral)
    # print(q1/s1, q2/s2, q3/s3)

    tqf = ((q1 + q2 + q3)**2) - 2*(q1*q1 + q2*q2 + q3*q3)
    assert approx(tqf) == Ar(q1, q2, q3)

    assert spread(l1, l1) == approx(0)
    assert quadrance(a1, a1) == approx(0)
    assert angle(l1, l1) == approx(0)
    assert distance(a1, a1) == approx(0)

    c3 = ((q1 + q2 - q3)**2) / (4*q1*q2)
    assert cross_s(l1, l2) == approx(c3)
    assert c3 + s3 == approx(1)  # get the same

    tsf = (s1 + s2 + s3)**2 - 2*(s1*s1 + s2*s2 + s3*s3) - 4*s1*s2*s3
    assert tsf == approx(0)

    a3 = pg_point(3*a1 + 4*a2)
    q1 = quadrance(a2, a3)
    q2 = quadrance(a1, a3)
    q3 = quadrance(a1, a2)
    tqf = (q1 + q2 + q3)**2 - 2*(q1*q1 + q2*q2 + q3*q3)  # get 0
    assert tqf == approx(0)

    a1 = uc_point(1., 2.)
    a2 = uc_point(3., 4.)
    a3 = uc_point(-1., 2.)
    a4 = uc_point(-5., 1.)
    q12 = quadrance(a1, a2)
    q23 = quadrance(a2, a3)
    q34 = quadrance(a3, a4)
    q14 = quadrance(a1, a4)
    q24 = quadrance(a2, a4)
    q13 = quadrance(a1, a3)
    # print(q12, q23, q34, q14, q24, q13)
    t = Ar(q12*q34, q23*q14, q13*q24)
    # t = sympy.simplify(t)
    assert t == approx(0)


def test_int():
    a1 = pg_point([3451, -5673, 241])
    a2 = pg_point([644, 2423, 2341])
    a3 = pg_point([544, -4333, 341])

    triangle = [a1, a2, a3]
    trilateral = tri_dual(triangle)
    l1, l2, l3 = trilateral
    assert not is_parallel(l1, l2)
    assert not is_parallel(l2, l3)

    t1, t2, t3 = tri_altitude(triangle)
    assert is_perpendicular(t1, l1)
    assert spread(t1, l1) == 1  # get 1
    assert coincident(t1, t2, t3)

    t4 = harm_conj(t1, t2, t3)
    assert R(t1, t2, t3, t4) == -1

    o = orthocenter(triangle)
    assert o == meet(t2, t3)
    assert a1 == orthocenter([o, a2, a3])

    tau = reflect(l1)
    assert tau(tau(a1)) == a1

    m12 = midpoint(a1, a2)
    m23 = midpoint(a2, a3)
    m13 = midpoint(a1, a3)
    t1 = a1 * m23
    t2 = a2 * m13
    t3 = a3 * m12
    assert coincident(t1, t2, t3)

    q1, q2, q3 = tri_quadrance(triangle)
    s1, s2, s3 = tri_spread(trilateral)
    # print(q1/s1, q2/s2, q3/s3)

    tqf = ((q1 + q2 + q3)**2) - 2*(q1*q1 + q2*q2 + q3*q3)
    assert tqf == Ar(q1, q2, q3)

    assert spread(l1, l1) == 0
    assert quadrance(a1, a1) == 0

    c3 = ((q1 + q2 - q3)**2) / (4*q1*q2)
    assert cross_s(l1, l2) == c3
    assert c3 + s3 == 1  # get the same

    tsf = (s1 + s2 + s3)**2 - 2*(s1*s1 + s2*s2 + s3*s3) - 4*s1*s2*s3
    assert tsf == 0

    a3 = pg_point(3*a1 + 4*a2)
    q1 = quadrance(a2, a3)
    q2 = quadrance(a1, a3)
    q3 = quadrance(a1, a2)
    tqf = (q1 + q2 + q3)**2 - 2*(q1*q1 + q2*q2 + q3*q3)  # get 0
    assert tqf == 0

    a1 = uc_point(1, 2)
    a2 = uc_point(3, 4)
    a3 = uc_point(-1, 2)
    a4 = uc_point(-5, 1)
    q12 = quadrance(a1, a2)
    q23 = quadrance(a2, a3)
    q34 = quadrance(a3, a4)
    q14 = quadrance(a1, a4)
    q24 = quadrance(a2, a4)
    q13 = quadrance(a1, a3)
    # print(q12, q23, q34, q14, q24, q13)
    t = Ar(q12*q34, q23*q14, q13*q24)
    # t = sympy.simplify(t)
    assert t == 0
    t = Ptolemy([q12, q23, q34, q14, q24, q13])
    assert t == True

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
