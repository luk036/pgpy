# -*- coding: utf-8 -*-
from __future__ import print_function
 
from pprint import pprint
import numpy as np

M = 6

def pg_eq(p,q):
    return (np.cross(p,q) % M == 0).all()

def incident(p, l):
    return not (np.dot(p,l) % M)

def join(p,q):
    return np.cross(p, q) % M

def meet(l,m):
    return np.cross(l, m) % M

def collinear(p, q, r):
    return incident(join(p,q), r)

def concurrent(l, m, n):
    return incident(meet(l,m), n)

def coI(L):
    if len(L) < 3: return True
    p , q = L[0], L[1]
    assert not pg_eq(p,q)
    for r in L[2:]:
        if not collinear(p,q,r): return False
    return True

def persp(L, M):
    if len(L) != len(M): return False
    if len(L) < 3: return True
    pL , qL = L[0], L[1]
    pM , qM = M[0], M[1]
    assert not pg_eq(pL,qL)
    assert not pg_eq(pM,qM)
    assert not pg_eq(pL,pM)
    assert not pg_eq(qL,qM)
    O = meet(join(pL,pM), join(qL,qM))
    for rL, rM in zip(L[2:],M[2:]):
        if not collinear(rL, rM, O): return False
    return True

def check_pappus(A, B, C, D, E, F):
    G = meet(join(A,E), join(B,D))
    H = meet(join(A,F), join(C,D))
    I = meet(join(B,F), join(C,E))
    assert collinear(G, H, I)

def check_desargue(A, B, C, D, E, F):
    a = join(B,C)
    b = join(A,C)
    c = join(B,A)
    d = join(E,F)
    e = join(D,F)
    f = join(E,D)
    
    b1 = persp([A,B,C],[D,E,F])
    b2 = persp([a,b,c], [d,e,f])
    if b1: assert b2
    else: assert not b2

if __name__ == "__main__":
    p = np.array([1, 3, 2])
    q = np.array([-2, 1, -1])
    r = np.array([2, -2, 1])
    s = np.array([2, 2, 3])
    t = np.array([2, -2, 2])
    assert incident(p,join(p,q))
    print(coI([p,q,p+q,p-q])) # True
    print(persp([p,q,p+q], [r, p+r, p])) # False
    check_pappus(p, q, p+q, r, s, r-s)
    O = meet(join(p,s), join(q,t))
    r = join(p,q)
    u = O - r
    # check_desargue(p,q,r,s,t,u)
    # l = np.array([1,2,1])
    cnt = 0
    for i in range(M):
        for j in range(M):
            for k in range(M):
                p = np.array([i,j,k])
                count = 0
                for i2 in range(M):
                    for j2 in range(M):
                        for k2 in range(M):
                            q = np.array([i2,j2,k2])
                            if (np.cross(p,q) % M == 0).all():
                                count += 1
                if count != M: 
                    print(count,p)
                    cnt += 1
    print(cnt)
    p = np.array([0,3,0])
    for i in range(M):
        for j in range(M):
            for k in range(M):
                q = np.array([i,j,k])
                if (np.cross(p,q) % M == 0).all():
                    print(q)


