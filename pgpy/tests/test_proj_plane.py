from __future__ import print_function

from ..proj_plane import *


def chk_complex(pg_object):
    p = pg_object([1-2j, 3-1j, 2+1j])  # complex number
    q = pg_object([-2+1j, 1-3j, -1-1j])
    l = p*q
    assert l == q*p
    assert l.incident(p)
    assert l.incident(q)

    r = plucker(2, p, 3, q)
    assert l.incident(r)

    s = harm_conj(p, q, r)
    assert isharmonic(p, q, r, s)
    assert coI(p, q, r, s)

    r = pg_object([2-1j, -2+1j, 1+1j])
    s = pg_object([2j, 2-2j, 3])
    t = pg_object([2, -2j, 2])

    assert not persp([p, q, p + q], [r, p + r, p])

    O = (p * s) * (q * t)
    # r = join(p, q)
    u = O - r  # ???
    check_desargue((p, q, r), (s, t, u))


def test_complex():
    chk_complex(pg_point)
    chk_complex(pg_line)


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
