from __future__ import print_function

from ..proj_plane import *


def test_complex_point():
    p = pg_point([1-2j, 3-1j, 2+1j])  # complex number
    q = pg_point([-2+1j, 1-3j, -1-1j])
    l = p*q
    assert l == q*p
    assert l.incident(p)
    assert l.incident(q)

    r = plucker(2, p, 3, q)
    assert l.incident(r)

    assert coI([p, q, plucker(1, p, 1, q), plucker(1, p, -1, q)])

    r = pg_point([2-1j, -2+1j, 1+1j])
    s = pg_point([2j, 2-2j, 3])
    t = pg_point([2, -2j, 2])

    assert not persp([p, q, p + q], [r, p + r, p])

    O = meet(join(p, s), join(q, t))
    # r = join(p, q)
    u = O - r  # ???
    check_desargue((p, q, r), (s, t, u))


def test_complex_line():
    l = pg_line([1-2j, 3-1j, 2+1j])  # complex number
    m = pg_line([-2+1j, 1-3j, -1-1j])
    A = l*m
    assert A == m*l
    assert A.incident(l)
    assert A.incident(m)

    r = plucker(2, l, 3, m)
    assert A.incident(r)

    assert coI([l, m, plucker(1, l, 1, m), plucker(1, l, -1, m)])

    r = pg_line([2-1j, -2+1j, 1+1j])
    s = pg_line([2j, 2-2j, 3])
    t = pg_line([2, -2j, 2])

    assert not persp([l, m, l + m], [r, l + r, l])

    o = join(meet(l, s), meet(m, t))
    # r = meet(l, m)
    u = o - r  # ???
    check_desargue((l, m, r), (s, t, u))


# def no_test_symbolic():
#     import sympy
#     sympy.init_printing()
#     pv = sympy.symbols("p:3", integer=True)
#     qv = sympy.symbols("q:3", integer=True)
#     lambda1, mu1 = sympy.symbols("lambda1 mu1", integer=True)
#     p = pg_point(pv)
#     q = pg_point(qv)
#     r = plucker(lambda1, p, mu1, q)
#     sv = sympy.symbols("s:3", integer=True)
#     tv = sympy.symbols("t:3", integer=True)
#     lambda2, mu2 = sympy.symbols("lambda2 mu2", integer=True)
#     s = pg_point(sv)
#     t = pg_point(tv)
#     u = plucker(lambda2, s, mu2, t)

#     # Prove Pappus Theorem
#     G = meet(join(p, t), join(q, s))
#     H = meet(join(p, u), join(r, s))
#     I = meet(join(q, u), join(r, t))
#     ans = G.dot(join(H, I))
#     ans = sympy.simplify(ans)
#     assert ans == 0

#     # p, q, s, t
#     lambda3, mu3 = sympy.symbols("lambda3 mu3", integer=True)
#     p2 = plucker(lambda1, p, mu1, t)
#     q2 = plucker(lambda2, q, mu2, t)
#     s2 = plucker(lambda3, s, mu3, t)

#     # Prove Desargue Theorem
#     G = meet(join(p, q), join(p2, q2))
#     H = meet(join(q, s), join(q2, s2))
#     I = meet(join(s, p), join(s2, p2))
#     ans = G.dot(join(H, I))
#     ans = sympy.simplify(ans)
#     assert ans == 0
