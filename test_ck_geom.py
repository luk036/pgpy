from proj_geom import * 
from ck_geom import * 

def test_int():
    a1 = pg_point([1, 2, 3])
    a2 = pg_point([4, -5, 6])
    a3 = pg_point([-7, 8, 9])
    l1 = join(a2, a3)
    assert l1.incident(a2)
    l2 = join(a1, a3)
    l3 = join(a1, a2)
    q1 = quadrance(a2,a3)
    q2 = quadrance(a1,a3)
    q3 = quadrance(a1,a2)
    s1 = spread(l2, l3)
    s2 = spread(l1, l3)
    s3 = spread(l1, l2)
    # print(q1/s1, q2/s2, q3/s3)
    assert spread(l1,l1) == 0
    assert quadrance(a1,a1) == 0

    t1 = altitude(a1, l1)
    t2 = altitude(a2, l2)
    t3 = altitude(a3, l3)
    ans = dot(t1, meet(t2, t3))
    # ans = sympy.simplify(ans)
    assert ans == 0
