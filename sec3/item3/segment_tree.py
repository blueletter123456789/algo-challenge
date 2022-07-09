class SegmentTreeRMQ(object):
    INF = 1 << 17

    def __init__(self, length):
        self.n = 1
        self.dat = list()
        self.length = length

        # Segment treeの親の節点分
        while self.n < length:
            self.n *= 2
        
        # 子も含めた節点分
        self.dat = [self.INF]*(2 * self.n - 1)
    
    def update(self, k, a):
        # 挿入する葉インデックス
        k += self.n - 1
        self.dat[k] = a

        while k > 0:
            # 親の節点のインデックス
            k = (k - 1) // 2
            # 親から見て子の節点を比較
            self.dat[k] = min(self.dat[k*2+1], self.dat[k*2+2])
    
    def query(self, a, b):
        # [a, b)の最小値
        l = k = 0
        r = self.n
        def _query(a, b, k, l, r):
            # 節点の範囲が検索対象外
            if r <= a or b <= l:
                return self.INF
            
            # 節点の範囲が検索対象内
            if a <= l and r <= b:
                return self.dat[k]
            else:
                vl = _query(a, b, k*2+1, l, (l+r)//2)
                vr = _query(a, b, k*2+2, (l+r)//2, r)
                return min(vl, vr)
        return _query(a, b, k, l, r)

if __name__ == '__main__':
    import random
    n = 10
    lst = [0, 1, 2, 9, 8, 7, 6, 5, 4, 3]
    
    st = SegmentTreeRMQ(n)
    for i, val in enumerate(lst):
        st.update(i, val)
    
    print(st.query(3, 7))
