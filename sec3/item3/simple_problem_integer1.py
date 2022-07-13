class SegmentTree(object):
    INF = (1 << 18) - 1

    def __init__(self, n):
        # 節点の区間全体に一様に加えられた値
        self.dat = [0]*self.INF
        # 節点の区間に一様でなく加えられた値の和
        self.datb = [0] * self.INF
        self.n = n
    
    def add(self, a, b, x):
        # [a, b)区間を加算
        def _add(a, b, x, k, l, r):
            # 節点kの区間は[l, r)に対応

            if a <= l and r <= b:
                # 節点の区間全体に与えられた場合は加算
                # 親に一様に加えられたら子の節点は加算しない
                self.dat[k] += x
            elif l < b and a < r:
                # 親の節点で一様に加算できない場合は子の節点に遷移
                self.datb[k] += (min(b, r) - max(a, l))*x
                _add(a, b, x, k*2+1, l, (l+r)//2)
                _add(a, b, x, k*2+2, (l+r)//2, r)
        
        _add(a, b, x, 0, 0, self.n)
    
    def sum(self, a, b):
        # [a, b)区間を合計
        def _sum(a, b, k, l, r):
            # 節点kの区間は[l, r)に対応

            # 区間外
            if b <= l or r <= a:
                return 0
            # 節点全体に加算した値 + 
            # 一様ではないが区間内に該当する節点の合計値
            elif a <= l and r <= b:
                return self.dat[k] * (r-l) + self.datb[k]
            else:
                # 親区間で加算されていた分を計算
                res = (min(b, r) - max(a, l))*self.dat[k]
                res += _sum(a, b, k*2+1, l, (l+r)//2)
                res += _sum(a, b, k*2+2, (l+r)//2, r)
                return res
        
        return _sum(a, b, 0, 0, self.n)

def solved():
    seg_tree = SegmentTree(N)
    for i, a in enumerate(A):
        seg_tree.add(i, i+1, a)

    for i in range(Q):
        # 0-indexedでl, rが格納されている想定
        q = T[i]
        if len(q) == 3:
            l, r, x = q
            seg_tree.add(l, r+1, x)
        elif len(q) == 2:
            l, r = q
            print(seg_tree.sum(l, r+1))


if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    T = list()
    for _ in range(Q):
        T.append(list(map(int, input().split())))

    solved()
