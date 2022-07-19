class TwodimBIT(object):
    def __init__(self, n, m):
        self.lst = [[0]*(m+1) for _ in range(n+1)]
        self.n = n
        self.m = m
    
    # (1, 1)から(x, y)までの累積和を求める
    def sum(self, x, y):
        s = 0
        i = x
        while i > 0:
            j = y
            while j > 0:
                s += self.lst[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return s
    
    def add(self, x, y, k):
        i = x
        while i <= self.n:
            j = y
            while j <= self.m:
                self.lst[i][j] += k
                j += j & (-j)
            i += i & (-i)
    
    def part(self, x1, y1, x2, y2):
        return (self.sum(x2, y2) - self.sum(x1-1, y2) - 
            self.sum(x2, y1-1) + self.sum(x1-1, y1-1))


if __name__ == '__main__':
    lst = [[1, 2], [3, 4]]
    bit_tree = TwodimBIT(2, 2)
    
    for i in range(2):
        for j in range(2):
            bit_tree.add(i+1, j+1, lst[i][j])
    
    print(bit_tree.sum(1, 2))
    print(bit_tree.sum(2, 1))
    print(bit_tree.part(1, 2, 2, 2))
