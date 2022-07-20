import bisect


class SegmentTree(object):
    INF = (1 << 18) - 1

    def __init__(self, n) -> None:
        self.dat = [list() for _ in range(self.INF)]
        self.n = n

        self.create_tree(0, 0, n)
    
    def create_tree(self, k, l, r):
        if r - l == 1:
            self.dat[k].append(A[l])
        else:
            lch, rch = k*2+1, k*2+2
            self.create_tree(lch, l, (l+r)//2)
            self.create_tree(rch, (l+r)//2, r)
            
            self.dat[k] = self.merge(self.dat[lch], self.dat[rch])
    
    def merge(self, lst1, lst2):
        lst = list()
        i = j = 0
        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                lst.append(lst1[i])
                i += 1
            else:
                lst.append(lst2[j])
                j += 1
        while i < len(lst1):
            lst.append(lst1[i])
            i += 1
        while j < len(lst2):
            lst.append(lst2[j])
            j += 1
        return lst
    
    def query(self, i, j, x):
        def _query(i, j, x, k, l, r):
            if j <= l or i >= r:
                return 0
            elif i <= l and r <= j:
                return bisect.bisect(self.dat[k], x)
            else:
                lc = _query(i, j, x, k*2+1, l, (l+r)//2)
                rc = _query(i, j, x, k*2+2, (l+r)//2, r)
                return lc + rc
        
        return _query(i, j, x, 0, 0, self.n)


def solved():
    nums = A.copy()
    nums.sort()

    st = SegmentTree(n)

    for i in range(m):
        l, r, k = I[i], J[i], K[i]
        lb, ub = -1, n-1
        while ub - lb > 1:
            md = (lb + ub)//2
            c = st.query(l, r, nums[md])
            if c >= k:
                ub = md
            else:
                lb = md
        print(nums[ub-1])

if __name__ == '__main__':
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    I, J, K = [0]*m, [0]*m, [0]*m
    for i in range(m):
        I[i], J[i], K[i] = map(int, input().split())
    
    solved()

