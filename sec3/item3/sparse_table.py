import numpy as np
 
 
class SparseTable:
    def __init__(self, lst):
        n = len(lst)
        max_k = (n - 1).bit_length() - 1
        INF = 10 ** 18
        table = np.full((n, max_k + 1), INF, dtype=np.int64)
        table[:, 0] = lst
 
        for k in range(1, max_k + 1):
            k2 = 1 << (k - 1)
            k3 = (1 << k) - 1
            table[:n - k3, k] = np.minimum(
                table[:n - k3, k - 1], 
                table[k2:n - k3 + k2, k - 1]
            )
 
        self.table = table
 
    def query(self, l, r):
        """ min value of [l, r) """
        d = r - l
        if d == 1:
            return self.table[l, 0]
 
        k = (d - 1).bit_length() - 1
        k2 = 1 << k
        return min(self.table[l, k], self.table[r - k2, k])

if __name__ == '__main__':
    lst = [9, 6, 3, 5, 8, 2, 10, 1, 7, 2]
    st = SparseTable(lst)
    print(st.query(2, 8))