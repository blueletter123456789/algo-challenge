from collections import namedtuple


EPS = 1e-10

P = namedtuple('Point', ['x', 'y'])

class Point(P):
    def __add__(self, other):
        return Point(add(self.x, other.x), add(self.y, other.y))
    
    def __sub__(self, other):
        return Point(add(self.x, -other.x), add(self.y, -other.y))
    
    def __mul__(self, d):
        return Point(self.x*d, self.y*d)
    
    # 内積
    def dot(self, other):
        return add(self.x*other.x, self.y*other.y)
    
    # 外積
    def det(self, other):
        return add(self.x*other.y, -self.y*other.x)

def add(ai, bi):
    if abs(ai + bi) < (EPS * (abs(ai) + abs(bi))):
        return 0
    return ai + bi

def on_seg(p1, p2, q):
    # p1, p2にてなす角が90度以上かつ一直線上
    # →p2, p2間でqが線上かを判定
    return ((p1 - q).det(p2 - q) == 0) and ((p1 - q).dot(p2 - q) <= 0)

def intersection(p1, p2, q1, q2):
    # 交点を計算
    return p1 + (p2 - p1) * ((q2 - q1).det(q1 - p1) / (q2 - q1).det(p2 - p1))

def sovled():
    g = [[False]*n for _ in range(n)]

    for i in range(n):
        g[i][i] = True
        for j in range(i):
            # 外積が0となるということは一直線上
            if (p[i] - q[i]).det(p[j] - q[j]) == 0:
                g[i][j] = g[j][i] = (on_seg(p[i], q[i], p[j])
                                  or on_seg(p[i], q[i], q[j])
                                  or on_seg(p[j], q[j], p[i])
                                  or on_seg(p[j], q[j], q[i]))
            else:
                # 交点を求め各線で線上か判定
                r = intersection(p[i], q[i], p[j], q[j])
                g[i][j] = g[j][i] = on_seg(p[i], q[i], r) and on_seg(p[j], q[j], r)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] |= (g[i][k] and g[k][j])
    
    for i, j in zip(a, b):
        print('CONNECTED' if g[i-1][j-1] else 'NOT CONNECTED')


if __name__ == '__main__':
    n = int(input())
    
    p = list()
    q = list()

    for _ in range(n):
        x, y = map(int, input().split())
        p.append(Point(x, y))
    
    for _ in range(n):
        x, y = map(int, input().split())
        q.append(Point(x, y))
    
    m = int(input())

    a = [0]*m
    b = [0]*m

    for i in range(m):
        a[i], b[i] = map(int, input().split())

    sovled()
