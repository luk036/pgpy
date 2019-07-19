from pgpy.proj_line import pl_point


def test_complex_point():
    p = pl_point([1 - 2j, 3 - 1j])  # complex number
    q = pl_point([2 - 1j, 4 - 1j])  # complex number
    assert p == p
    assert not p == q
    assert p != q
