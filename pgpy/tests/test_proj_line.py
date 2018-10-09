from __future__ import print_function

from ..proj_line import pl_point
# import gmpy2
# from gmpy2 import mpz

def test_complex_point():
    p = pl_point([1-2j, 3-1j])  # complex number
    assert p == p

# def test_mpz_point():
#     p = pl_point([mpz(1000), mpz(30000)])  # complex number
#     assert(p == p)
