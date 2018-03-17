from __future__ import print_function

from ..ell_plane import * 

def test_int():
    a1 = pg_point([1, 3, 1])
    a2 = pg_point([4, 2, 1])
    a3 = pg_point([1, 1, -1])
    l1 = join(a2, a3)
    l2 = join(a1, a3)
    l3 = join(a1, a2)
    # a3 = pg_point([sx, sy, sz])

    s1 = spread(l2, l3)
    s2 = spread(l1, l3)
    s3 = spread(l1, l2)

    q1 = quadrance(a2,a3)
    q2 = quadrance(a1,a3)
    q3 = quadrance(a1,a2)

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
