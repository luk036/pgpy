from pgpy.proj_plane import *


def chk_complex(pg_object):
    """[summary]

    Arguments:
        pg_object (type): [description]
    """
    p = pg_object([1 - 2j, 3 - 1j, 2 + 1j])  # complex number
    q = pg_object([-2 + 1j, 1 - 3j, -1 - 1j])
    l = p * q
    assert l == q * p
    assert not l == q
    assert l.incident(p)
    assert l.incident(q)

    pq = plucker(2 + 1j, p, 3 + 0j, q)
    assert l.incident(pq)

    h = harm_conj(p, q, pq)
    assert is_harmonic(p, q, pq, h)
    assert coI(p, q, pq, h)

    r = pg_object([2 - 1j, -2 + 1j, 1 + 1j])
    s = pg_object([2j, 2 - 2j, 3])
    t = pg_object([2, -2j, 2])

    assert not coI(p, q, r, s)

    co1 = [p, q, plucker(1, p, 1, q)]
    co2 = [r, plucker(1, p, 1, r), p]
    assert not persp(co1, co2)
    assert not persp(co1[:2], co2)
    assert persp(co1[:2], co2[:2])

    O = (p * s) * (q * t)
    # r = join(p, q)
    u = plucker(1, O, -1, r)  # ???
    check_desargue((p, q, r), (s, t, u))
    check_desargue((p, q, O), (s, t, u))

    check_pappus(co1, [u, O, r])


def test_complex():
    chk_complex(pg_point)
    chk_complex(pg_line)


def test_special_case():
    p = pg_point([1, 3, 2])
    l = pg_line([-2, 3, 1])
    # l_inf = pg_line([0, 0, 1])
    l_nan = pg_line([0, 0, 0])
    p_nan = pg_point([0, 0, 0])

    assert l_nan == l_nan
    assert l_nan == p * p  # join two equal points
    assert p_nan == l * l
    assert l_nan == p_nan * p
    assert p_nan == l_nan * l
    assert p.incident(l_nan)
    assert l.incident(p_nan)
    assert p_nan.incident(l_nan)


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
