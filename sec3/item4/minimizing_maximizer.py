class SegmentTreeRMQ(object):
    # INF = 1 << 17

    def __init__(self, length):
        self.n = 1
        self.dat = list()
        self.length = length

        while self.n < length:
            self.n *= 2
        
        # self.dat = [self.INF]*(2 * self.n - 1)
        self.dat = [float('inf') for _ in range(2 * self.n - 1)]
    
    def update(self, k, a):
        k += self.n - 1
        self.dat[k] = a

        while k > 0:
            k = (k - 1) // 2
            self.dat[k] = min(self.dat[k*2+1], self.dat[k*2+2])
    
    def query(self, a, b):
        l = k = 0
        r = self.n
        def _query(a, b, k, l, r):
            if r <= a or b <= l:
                return float('inf')
                # return self.INF
            
            if a <= l and r <= b:
                return self.dat[k]
            else:
                vl = _query(a, b, k*2+1, l, (l+r)//2)
                vr = _query(a, b, k*2+2, (l+r)//2, r)
                return min(vl, vr)
        return _query(a, b, k, l, r)

def solved():
    st = SegmentTreeRMQ(n)

    dp = [float('inf') for _ in range(n+1)]
    dp[1] = 0

    st.update(1, 0)
    for i in range(m):
        v = min(dp[T[i]], st.query(S[i], T[i]+1)+1)
        dp[T[i]] = v
        st.update(T[i], v)
    
    return dp[n]



if __name__ == '__main__':
    n, m = map(int, input().split())
    S, T = [0]*m, [0]*m
    for i in range(m):
        S[i], T[i] = map(int, input().split())
    
    print(solved())
