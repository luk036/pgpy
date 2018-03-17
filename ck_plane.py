# -*- coding: utf-8 -*-
from __future__ import print_function
from pprint import pprint
import numpy as np
from fractions import *
from .proj_plane import * 

class ck:
    def __init__(self, dual):
        self.dual = dual

    def is_perpendicular(self, l, m):
        return m.incident(self.dual(l))

    def altitude(self, p, l):
        return p * self.dual(l)

    def orthocenter(self, a1, a2, a3):
        t1 = self.altitude(a1, a2*a3)
        t2 = self.altitude(a2, a1*a3)
        return t1*t2

    def omega(self, l):
        return dot(l, self.dual(l))

    def measure(self, a1, a2):
        """test"""
        omg = dot(a1, self.dual(a2))
        if isinstance(omg, (int, np.int64) ):
            return 1 - Fraction(omg, self.omega(a1)) * Fraction(omg, self.omega(a2))
        else:
            return 1 - (omg * omg) / (self.omega(a1) * self.omega(a2))

    # def measure(self, a1, a2):
    #     omg = self.omega(a1*a2)
    #     if isinstance(omg, (int, np.int64) ):
    #         return Fraction(omg, self.omega(a1) * self.omega(a2))
    #     else:
    #         return omg / (self.omega(a1) * self.omega(a2))

    def quadrance(self, a1, a2):
        return self.measure(a1, a2)

    def spread(self, l1, l2):
        return self.measure(l1, l2)

if __name__ == "__main__":
    def mydual(v):
        [x, y, z] = v
        if isinstance(v, pg_point):
            return pg_line([-x, y, -z])
        elif isinstance(v, pg_line):
            return pg_point([-x, y, -z])
        else:
            raise NotImplementedError()

    import sympy
    sympy.init_printing()

    myck = ck(mydual)

    # i1 = sympy.Integer(1)
    # i2 = sympy.Integer(3)
    # i3 = sympy.Integer(1)
    # i4 = sympy.Integer(4)
    # i5 = sympy.Integer(2)
    # i6 = sympy.Integer(1)
    # i7 = sympy.Integer(4)
    # i8 = sympy.Integer(-2)
    # i9 = sympy.Integer(1)    
    a1 = pg_point([1, 2, 3])
    a2 = pg_point([4, -5, 6])
    a3 = pg_point([-7, 8, 9])
    l1 = join(a2, a3)
    assert l1.incident(a2)
    l2 = join(a1, a3)
    l3 = join(a1, a2)
    q1 = myck.quadrance(a2,a3)
    q2 = myck.quadrance(a1,a3)
    q3 = myck.quadrance(a1,a2)
    s1 = myck.spread(l2, l3)
    s2 = myck.spread(l1, l3)
    s3 = myck.spread(l1, l2)
    # print(q1, s1, q2, s2, q3, s3)
    print(q1/s1, q2/s2, q3/s3)
    assert myck.spread(l1,l1) == 0
    assert myck.quadrance(a1,a1) == 0

    # import sympy
    # sympy.init_printing()
    # a1x = sympy.Symbol("a1x", integer=True)
    # a1y = sympy.Symbol("a1y", integer=True)
    # a1z = sympy.Symbol("a1z", integer=True)
    # a2x = sympy.Symbol("a2x", integer=True)
    # a2y = sympy.Symbol("a2y", integer=True)
    # a2z = sympy.Symbol("a2z", integer=True)
    # a3x = sympy.Symbol("a3x", integer=True)
    # a3y = sympy.Symbol("a3y", integer=True)
    # a3z = sympy.Symbol("a3z", integer=True)
    # a1 = pg_point([a1x, a1y, a1z])
    # a2 = pg_point([a2x, a2y, a2z])
    # a3 = pg_point([a3x, a3y, a3z])
    # l1 = join(a2, a3)
    # l2 = join(a1, a3)
    # l3 = join(a1, a2)
    t1 = myck.altitude(a1, l1)
    t2 = myck.altitude(a2, l2)
    t3 = myck.altitude(a3, l3)
    ans = dot(t1, meet(t2, t3))
    # ans = sympy.simplify(ans)
    print(ans) # get 0
