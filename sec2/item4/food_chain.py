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
            return False
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        return True
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

n, k = map(int, input().split())

ans = 0
uf = UnionFind(n*3)
seen = set()
for _ in range(k):
    t, a, b = map(int, input().split())
    if a < 1 or a > n or b < 1 or b > n:
        ans += 1
        continue
    flg = True
    if t == 1:
        if a in seen and b in seen:
            for i in range(3):
                ai = a + n*i
                bi = b + n*i
                if not uf.same(ai, bi):
                    ans += 1
                    flg = False
                    break
        if flg:
            for i in range(3):
                ai = a + n*i
                bi = b + n*i
                uf.unite(ai, bi)
            seen.add(a)
            seen.add(b)
    elif t == 2:
        if a == b:
            ans += 1
            continue
        if a in seen and b in seen:
            for i in range(3):
                ai = a + i*n
                bi = b + ((i+1)%3)*n
                if not uf.same(ai, bi):
                    ans += 1
                    flg = False
                    break
        if flg:
            for i in range(3):
                ai = a + i*n
                bi = b + ((i+1)%3)*n
                uf.unite(ai, bi)
            seen.add(a)
            seen.add(b)

print(ans)

# Sample code
# n, k = map(int, input().split())

# ans = 0
# uf = UnionFind(n*3)
# for i in range(k):
#     t, x, y = map(int, input().split())
#     x -= 1
#     y -= 1
#     if x < 0 or x >= n or y < 0 or y >= n:
#         ans += 1
#         continue

#     if t == 1:
#         if uf.same(x, y+n) or uf.same(x, y+n*2):
#             ans += 1
#         else:
#             uf.unite(x, y)
#             uf.unite(x+n, y+n)
#             uf.unite(x+n*2, y+n*2)
#     else:
#         if uf.same(x, y) or uf.same(x, y+n*2):
#             ans += 1
#         else:
#             uf.unite(x, y+n)
#             uf.unite(x+n, y+n*2)
#             uf.unite(x+n*2, y)

# print(ans)
