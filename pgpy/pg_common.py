def cross0(v, w):
    return cross2(v[1:], w[1:])


def cross1(v, w):
    return cross2(v[0:3:2], w[0:3:2])


def cross2(v, w):
    return v[0] * w[1] - w[0] * v[1]


def cross(v, w):
    return (cross0(v, w), -cross1(v, w), cross2(v, w))


def dot_c(v, w):
    x1, y1, z1 = v
    x2, y2, z2 = w
    return x1 * x2 + y1 * y2 + z1 * z2


def plucker_c(ld, v, mu, w):
    x1, y1, z1 = v
    x2, y2, z2 = w
    return (ld*x1 + mu*x2, ld*y1 + mu*y2, ld*z1 + mu*z2)


def dot1(v, w):
    return v[0] * w[0] + v[1] * w[1]


def dot2(v, w):
    return dot1(v[0:3:2], w[0:3:2])
