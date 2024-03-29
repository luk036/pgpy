from __future__ import print_function

from pgpy.ck_plane import check_sine_law, ck, ellck, hyck
from pgpy.proj_plane import coincident, pg_line, pg_point, tri_dual, x_ratio


def chk_ck(myck, pg_obj=pg_point):
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
    a1 = pg_obj([2133, 2232, 3322])
    a2 = pg_obj([2444, -2034, 2623])
    a3 = pg_obj([-2723, 2123, 2232])

    triangle = [a1, a2, a3]
    trilateral = tri_dual(triangle)
    l1, _, _ = trilateral
    t1, t2, t3 = myck.tri_altitude(triangle)
    o = myck.orthocenter(triangle)
    tau = myck.reflect(l1)
    Q = myck.tri_measure(triangle)
    S = myck.tri_measure(trilateral)

    assert l1.incident(a2)
    assert myck.is_perpendicular(t1, l1)
    assert coincident(t1, t2, t3)
    assert o == t2 * t3
    assert a1 == myck.orthocenter([o, a2, a3])
    assert tau(tau(a1)) == a1
    assert myck.measure(l1, l1) == 0
    assert myck.measure(a1, a1) == 0
    assert check_sine_law(Q, S)


class myck(ck):
    """[summary]

    Arguments:
        ck (type): [description]

    Raises:
        NotImplementedError -- [description]

    Returns:
        [type]: [description]
    """

    @classmethod
    def perp(cls, v):
        """[summary]

        Arguments:
            v (type): [description]

        Raises:
            NotImplementedError -- [description]

        Returns:
            [type]: [description]
        """
        [x, y, z] = v
        if isinstance(v, pg_point):
            return pg_line([-2 * x, y, -2 * z])
        elif isinstance(v, pg_line):
            return pg_point([-x, 2 * y, -z])
        else:
            raise NotImplementedError()

    def measure(self, a1, a2):
        """[summary]

        Arguments:
            a1 (type): [description]
            a2 (type): [description]

        Returns:
            [type]: [description]
        """
        return 1 - x_ratio(a1, a2, self.perp(a2), self.perp(a1))


def test_ck():
    chk_ck(myck(), pg_point)
    chk_ck(myck(), pg_line)

    chk_ck(ellck(), pg_point)
    chk_ck(ellck(), pg_line)

    chk_ck(hyck(), pg_point)
    chk_ck(hyck(), pg_line)


# def no_test_symbolic():
#     import sympy
#     sympy.init_printing()
#     pv = sympy.symbols("p:3", integer=True)
#     qv = sympy.symbols("q:3", integer=True)
#     rv = sympy.symbols("r:3", integer=True)

#     tstck = myck()
#     a1 = pg_point(pv)
#     a2 = pg_point(qv)
#     a3 = pg_point(rv)
#     l1 = join(a2, a3)
#     l2 = join(a1, a3)
#     l3 = join(a1, a2)
#     t1 = tstck.altitude(a1, l1)
#     t2 = tstck.altitude(a2, l2)
#     t3 = tstck.altitude(a3, l3)
#     ans = t1.dot(meet(t2, t3))
#     ans = sympy.simplify(ans)
#     assert ans == 0
