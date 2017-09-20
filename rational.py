# -*- coding: utf-8 -*-
from __future__ import print_function

from pprint import pprint
import numpy as np
import fractions
import math

def dot(p, q):
    return p.x * q.x + p.y * q.y

def cross(p, q):
    return p.x * q.y - p.y * q.x

class rat:
    def __init__(self, p):
        if type(p) is int:
            self.x = p
            self.y = 1
        elif type(p) is type(self):
            self.x = p.x
            self.y = p.y
        else:
            raise NotImplementedError()


    def __eq__(self, other):
        if type(other) is type(self):
            return cross(self, other) == 0
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __mul__(self, other):
        res = rat(0)
        if type(other) is int:
            res.x = self.x * other
            res.y = self.y
        else:
            res.x = self.x * other.y
            res.y = self.y * other.x
        return res

    def __div__(self, other):
        res = rat(0)
        if type(other) is int:
            res.x = self.x
            res.y = self.y * other
        else:
            res.x = self.x * other.y
            res.y = self.y * other.x
        return res

    def __str__(self):
        return "%s/%s" % (self.x, self.y)

if __name__ == "__main__":
    r = rat(3)/4
    q = rat(r)/3
    print(r)
    print(q)
    f = fractions.Fraction(4, 5)
    print(f)
