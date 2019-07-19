from __future__ import print_function

from pytest import approx

from pgpy.ck_plane import check_sine_law
from pgpy.euclid_plane import Ar
from pgpy.persp_plane import persp_euclid_plane
from pgpy.proj_plane import coincident, cross, pg_line, pg_point, plucker, tri_dual


def chk_ck(myck, K, pg_obj=pg_point):
    """[summary]

    Arguments:
        myck (type): [description]
        K (type): [description]

    Keyword Arguments:
        pg_obj (type): [description] (default: {pg_point})

    Raises:
        NotImplementedError -- [description]
        NotImplementedError -- [description]
    """
    if K == int:
        a1 = pg_obj([2, 22, 3])
        a2 = pg_obj([4, -20, 26])
        a3 = pg_obj([-27, 21, 2])
    elif K == float:
        a1 = pg_obj([3., 2., 7.])
        a2 = pg_obj([2., -2., 1.])
        a3 = pg_obj([-3., 4., 6.])
    else:
        raise NotImplementedError()

    triangle = [a1, a2, a3]
    trilateral = tri_dual(triangle)
    l1, _, _ = trilateral
    t1, t2, t3 = myck.tri_altitude(triangle)
    o = myck.orthocenter(triangle)
    tau = myck.reflect(l1)
    Q = myck.tri_measure(triangle)
    S = myck.tri_measure(trilateral)

    if K == int:
        assert l1.incident(a2)
        assert myck.is_perpendicular(t1, l1)
        assert coincident(t1, t2, t3)
        assert o == t2 * t3
        assert a1 == myck.orthocenter([o, a2, a3])
        assert tau(tau(a1)) == a1
        assert myck.measure(l1, l1) == 0
        assert myck.measure(a1, a1) == 0
        assert check_sine_law(Q, S)
    elif K == float:
        assert l1.dot(a2) == approx(0)
        assert l1.dot(myck.perp(t1)) == approx(0)
        assert t1.dot(t2 * t3) == approx(0)
        assert cross(o, t2 * t3) == approx((0, 0, 0))
        assert cross(a1, myck.orthocenter([o, a2, a3])) == approx((0, 0, 0))
        assert cross(tau(tau(a1)), a1) == approx((0, 0, 0))
        assert myck.measure(l1, l1) == approx(0)
        assert myck.measure(a1, a1) == approx(0)
        assert Q[0] * S[1] == approx(Q[1] * S[0])
        assert Q[1] * S[2] == approx(Q[2] * S[1])
    else:
        raise NotImplementedError()


def chk_degenerate(myck, K):
    """[summary]

    Arguments:
        myck (type): [description]
        K (type): [description]

    Raises:
        NotImplementedError -- [description]
        NotImplementedError -- [description]
    """
    if K == int:
        a1 = pg_point([-1, 2, 3])
        a2 = pg_point([4, -1, 1])
        a3 = pg_point([0, -1, 1])
    elif K == float:
        a1 = pg_point([-1., 2., 3.])
        a2 = pg_point([4., -1., 1.])
        a3 = pg_point([0., -1., 1.])
    else:
        raise NotImplementedError()

    triangle = [a1, a2, a3]
    trilateral = tri_dual(triangle)
    l1, l2, l3 = trilateral
    m23, m13, m12 = myck.tri_midpoint(triangle)
    t1 = a1 * m23
    t2 = a2 * m13
    t3 = a3 * m12
    q1, q2, q3 = myck.tri_quadrance(triangle)
    s1, s2, s3 = myck.tri_spread(trilateral)
    tqf = ((q1 + q2 + q3)**2) - 2 * (q1 * q1 + q2 * q2 + q3 * q3)
    tsf = (s1 + s2 +
           s3)**2 - 2 * (s1 * s1 + s2 * s2 + s3 * s3) - 4 * s1 * s2 * s3
    a4 = plucker(3, a1, 4, a2)
    qq1, qq2, qq3 = myck.tri_quadrance([a1, a2, a4])
    tqf2 = Ar(qq1, qq2, qq3)  # get 0

    if K == int:
        assert not myck.is_parallel(l1, l2)
        assert not myck.is_parallel(l2, l3)
        assert coincident(t1, t2, t3)
        assert tqf == Ar(q1, q2, q3)
        assert tsf == 0
        assert tqf2 == 0
    elif K == float:
        assert myck.l_infty.dot(l1 * l2) != approx(0)
        assert myck.l_infty.dot(l2 * l3) != approx(0)
        assert t1.dot(t2 * t3) == approx(0)
        assert approx(tqf) == Ar(q1, q2, q3)
        assert tsf == approx(0)
        assert tqf2 == approx(0)
    else:
        raise NotImplementedError()


def test_persp():
    Ire = pg_point([0, 1, 1])
    Iim = pg_point([1, 0, 0])
    l_inf = pg_line([0, -1, 1])
    P = persp_euclid_plane(Ire, Iim, l_inf)

    chk_ck(P, int, pg_point)
    chk_ck(P, float, pg_point)

    chk_degenerate(P, int)
    chk_degenerate(P, float)
