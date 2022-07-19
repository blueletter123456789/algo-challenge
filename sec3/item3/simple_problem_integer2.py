class BIT(object):
    INF = (1 << 18) - 1

    def __init__(self, n):
        self.bit0 = [0]*self.INF
        self.bit1 = [0] * self.INF
        self.n = n
    
    def add(self, b, i, v):
        while i <= self.n:
            b[i] += v
            i += (i & -i)
    
    def sum(self, b, i):
        s = 0
        while i > 0:
            s += b[i]
            i -= (i & -i)
        return s

def solved():
    bit_tree = BIT(N)
    for i, a in enumerate(A):
        bit_tree.add(bit_tree.bit0, i+1, a)

    for i in range(Q):
        # 1-indexedでl, rが格納されている想定
        q = T[i]
        if len(q) == 3:
            l, r, x = q
            bit_tree.add(bit_tree.bit0, l, -x*(l - 1))
            bit_tree.add(bit_tree.bit1, l, x)
            bit_tree.add(bit_tree.bit0, r+1, x*r)
            bit_tree.add(bit_tree.bit1, r+1, -x)
        elif len(q) == 2:
            l, r = q
            res = 0
            res += bit_tree.sum(bit_tree.bit0, r) + bit_tree.sum(bit_tree.bit1, r)*r
            res -= bit_tree.sum(bit_tree.bit0, l-1) + bit_tree.sum(bit_tree.bit1, l-1)*(l-1)
            print(res)


if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    T = list()
    for _ in range(Q):
        T.append(list(map(int, input().split())))

    solved()
