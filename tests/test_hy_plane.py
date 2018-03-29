from __future__ import print_function

from ..hy_plane import *


def test_int():
    a1 = pg_point([1, 3, 1])
    a2 = pg_point([4, 2, 1])
    a3 = pg_point([1, 1, -1])

    assert(dual(dual(a1)) == a1)

    l1 = join(a2, a3)
    l2 = join(a1, a3)
    l3 = join(a1, a2)
    # a3 = pg_point([sx, sy, sz])

    t1 = altitude(a1, l1)
    assert is_perpendicular(t1, l1)
    t2 = altitude(a2, l2)
    t3 = altitude(a3, l3)
    o = orthocenter(a1, a2, a3)
    assert o == meet(t2, t3)
    assert a1 == orthocenter(o, a2, a3)

    tau = line_reflect(l1)
    assert(tau(tau(a1)) == a1)

    s1 = spread(l2, l3)
    s2 = spread(l1, l3)
    s3 = spread(l1, l2)

    q1 = quadrance(a2, a3)
    q2 = quadrance(a1, a3)
    q3 = quadrance(a1, a2)

    # print(s1, s2, s3, q1, q2, q3)

    t12 = q1*s2 - q2*s1
    # t12 = sympy.simplify(t12)
    assert t12 == 0

    cl = (s1*s2*q3 - (s1+s2+s3)+2)**2 - 4*(1 - s1)*(1 - s2)*(1 - s3)
    # cld = (q1*q2*s3 - (q1+q2+q3)+2)**2 - 4*(1 - q1)*(1 - q2)*(1 - q3)
    # cld = sympy.simplify(cld)
    assert cl == 0
    cld = (q1*q2*s3 - (q1+q2+q3)+2)**2 - 4*(1 - q1)*(1 - q2)*(1 - q3)
    assert cld == 0


def test_symbolic():
    import sympy
    sympy.init_printing()
    pv = sympy.symbols("p:3", integer=True)
    qv = sympy.symbols("q:3", integer=True)

    a1 = pg_point(pv)
    a2 = pg_point(qv)

    lambda1, mu1 = sympy.symbols("lambda1 mu1", integer=True)
    a3 = plucker(lambda1, a1, mu1, a2)

    q1 = quadrance(a2, a3)
    q2 = quadrance(a1, a3)
    q3 = quadrance(a1, a2)
    tqf = (q1 + q2 + q3)**2 - 2*(q1*q1 + q2*q2 + q3*q3) - 4*q1*q2*q3
    tqf = sympy.simplify(tqf)
    assert tqf == 0

    sv = sympy.symbols("s:3", integer=True)
    a3 = pg_point(sv)
    l1 = join(a2, a3)
    l2 = join(a1, a3)
    l3 = join(a1, a2)
    t1 = altitude(a1, l1)
    t2 = altitude(a2, l2)
    t3 = altitude(a3, l3)
    o = t1*t2
    ans = t3.dot(o)
    ans = sympy.simplify(ans)
    assert ans == 0