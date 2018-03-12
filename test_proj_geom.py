from proj_geom import * 

def test_incident():
    p = pg_point([1-2j, 3-1j, 2+1j]) # complex number
    q = pg_point([-2+1j, 1-3j, -1-1j])
    assert p.incident(p*q)
