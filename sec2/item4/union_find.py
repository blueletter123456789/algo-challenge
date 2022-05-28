class UnionFind(object):
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0]*n
    
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

if __name__ == '__main__':
    uf = UnionFind(5)
    uf.unite(0, 3)
    uf.unite(2, 4)
    print(uf.same(0, 3))
    print(uf.same(0, 2))
    uf.unite(0, 2)
    print(uf.same(3, 4))
