from __future__ import print_function

from ..proj_plane import * 

def test_complex_point():
    p = pg_point([1-2j, 3-1j, 2+1j]) # complex number
    q = pg_point([-2+1j, 1-3j, -1-1j])
    l = p*q
    assert l == q*p
    assert l.incident(p)
    assert l.incident(q)

    r = pk_point(2, p, 3, q)
    assert l.incident(r)

    assert coI([p, q, pk_point(1, p, 1, q), pk_point(1, p, -1, q)])

    r = pg_point([2-1j, -2+1j, 1+1j])
    s = pg_point([2j, 2-2j, 3])
    t = pg_point([2, -2j, 2])

    assert not persp([p, q, p + q], [r, p + r, p])

    O = meet(join(p, s), join(q, t))
    r = join(p, q)
    u = O - r # ???
    check_desargue(p, q, r, s, t, u)

def test_complex_line():
    l = pg_line([1-2j, 3-1j, 2+1j]) # complex number
    m = pg_line([-2+1j, 1-3j, -1-1j])
    A = l*m
    assert A == m*l
    assert A.incident(l)
    assert A.incident(m)

    r = pk_line(2, l, 3, m)
    assert A.incident(r)

    assert coI([l, m, pk_line(1, l, 1, m), pk_line(1, l, -1, m)])

    r = pg_line([2-1j, -2+1j, 1+1j])
    s = pg_line([2j, 2-2j, 3])
    t = pg_line([2, -2j, 2])

    assert not persp([l, m, l + m], [r, l + r, l])

    o = join(meet(l, s), meet(m, t))
    r = meet(l, m)
    u = o - r # ???
    check_desargue(l, m, r, s, t, u)
