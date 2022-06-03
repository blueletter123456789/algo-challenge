INF = 10**10
base = 10000

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

n, m, r = map(int, input().split())
edge_lst = list()

for i in range(r):
    x, y, d = map(int, input().split())
    edge_lst.append((-d, x, y+n))

def kruskal():
    edge_lst.sort()
    uf = UnionFind(n+m)
    res = 0
    for edge in edge_lst:
        c, u, v = edge
        if not uf.is_same(u, v):
            uf.unite(u, v)
            res += c
    return res

# 森だった場合、各木の最初の人の費用を加算するため、全体からひく
ans = base*(n+m)
ans += kruskal()

print(ans)
