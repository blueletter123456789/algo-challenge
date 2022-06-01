INF = 10**5

class UnionFind(object):
    def __init__(self, n):
        self.par = [-1]*n
        self.size = [1]*n
    
    def root(self, a):
        if self.par[a] == -1:
            return a
        self.par[a] = self.root(self.par[a])
        return self.par[a]
    
    def is_same(self, a, b):
        return self.root(a) == self.root(b)
    
    def unite(self, a, b):
        a, b = self.root(a), self.root(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.par[b] = a
        self.size[a] += self.size[b]
        return True

n, m = map(int, input().split())
edge_lst = list()
for _ in range(m):
    u, v, c = map(int, input().split())
    edge_lst.append((c, u, v))

def kruskal():
    edge_lst.sort()
    uf = UnionFind(n)
    res = 0
    for edge in edge_lst:
        c, u, v = edge
        if not uf.is_same(u, v):
            uf.unite(u, v)
            res += c
    return res

print(kruskal())
