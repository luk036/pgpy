from __future__ import print_function

from ..proj_plane import * 

def test_complex():
    p = pg_point([1-2j, 3-1j, 2+1j]) # complex number
    q = pg_point([-2+1j, 1-3j, -1-1j])
    l = p*q
    assert l == q*p
    assert l.incident(p)
    assert l.incident(q)

    assert coI([p, q, pk_point(1, p, 1, q), pk_point(1, p, -1, q)])

    r = pg_point([2-1j, -2+1j, 1+1j])
    s = pg_point([2j, 2-2j, 3])
    t = pg_point([2, -2j, 2])

    assert not persp([p, q, p + q], [r, p + r, p])

    O = meet(join(p, s), join(q, t))
    r = join(p, q)
    u = O - r
    check_desargue(p, q, r, s, t, u)
