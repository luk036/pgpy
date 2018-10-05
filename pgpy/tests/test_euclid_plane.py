from __future__ import print_function

from ..euclid_plane import *
from ..proj_plane import tri, join, meet


def test_int():
    a1 = pg_point([1, 3, 1])
    a2 = pg_point([4, 2, 1])
    a3 = pg_point([4, -3, 1])

    l1, l2, l3 = tri([a1, a2, a3])
    t1, t2, t3 = tri_altitude(a1, a2, a3)
    assert is_perpendicular(t1, l1)
    assert not is_parallel(t1, l1)

    t4 = harm_conj(t1, t2, t3)
    assert R(t1, t2, t3, t4) == -1

    o = orthocenter(a1, a2, a3)
    assert o == meet(t2, t3)
    assert a1 == orthocenter(o, a2, a3)

    tau = reflect(l1)
    assert(tau(tau(a1)) == a1)

    q1, q2, q3 = tri_quadrance(a1, a2, a3)
    s1, s2, s3 = tri_spread(l1, l2, l3)
    # print(q1/s1, q2/s2, q3/s3)
    assert spread(t1, l1) == 1.0  # get 1.0
    assert coincident(t1, t2, t3)

    tqf = ((q1 + q2 + q3)**2) - 2*(q1*q1 + q2*q2 + q3*q3)
    assert tqf == Ar(q1, q2, q3)

    assert spread(l1, l1) == 0
    assert quadrance(a1, a1) == 0

    c3 = ((q1 + q2 - q3)**2) / (4*q1*q2)
    assert c3 + s3 == 1  # get the same

    tsf = (s1 + s2 + s3)**2 - 2*(s1*s1 + s2*s2 + s3*s3) - 4*s1*s2*s3
    assert tsf == 0

    a3 = pg_point(3*a1 + 4*a2)
    q1 = quadrance(a2, a3)
    q2 = quadrance(a1, a3)
    q3 = quadrance(a1, a2)
    tqf = (q1 + q2 + q3)**2 - 2*(q1*q1 + q2*q2 + q3*q3)  # get 0
    assert tqf == 0

    a1 = uc_point(1, 0)
    a2 = uc_point(3, 4)
    a3 = uc_point(-1, 2)
    a4 = uc_point(0, 1)
    q12 = quadrance(a1, a2)
    q23 = quadrance(a2, a3)
    q34 = quadrance(a3, a4)
    q14 = quadrance(a1, a4)
    q24 = quadrance(a2, a4)
    q13 = quadrance(a1, a3)
    #print(q12, q23, q34, q14, q24, q13)
    t = Ar(q12*q34, q23*q14, q13*q24)
    # t = sympy.simplify(t)
    assert t == 0


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