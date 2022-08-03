class BipartiteMatching(object):
    def __init__(self, n):
        self.G = [list() for _ in range(n)]
        self.match = list()
        self.used = list()
        self.n = n
    
    def add_edge(self, u, v):
        self.G[u].append(v)
        self.G[v].append(u)
    
    def dfs(self, v):
        """増加パスをDFSで探索

        隣接するノードuとマッチングを作ることができるならそれを行いtrueを返す。
        隣接するノードuが使われていたらそこから探索を行い、
        uがフリーになるようにつなぎ変えてtrueを返す。
        以上の二つが行えない場合falseを返して何もしない。
        マッチングを増やせる時はtrueを返し、増やせない時にfalseを返す。

        Returns:
            _type_: _description_
        """
        self.used[v] = True
        for i in range(len(self.G[v])):
            u = self.G[v][i]
            w = self.match[u]
            if w < 0 or not self.used[w] and self.dfs(w):
                self.match[v] = u
                self.match[u] = v
                return True
        return False

    def biparite_matching(self):
        res = 0
        self.match = [-1]*self.n
        for v in range(self.n):
            if self.match[v] < 0:
                self.used = [False]*self.n
                if self.dfs(v):
                    res += 1
        return res


def solved():
    bm = BipartiteMatching(n+k)
    
    for i in range(n):
        for j in range(k):
            if can[i][j]:
                bm.add_edge(i, n+j)
    
    return bm.biparite_matching()

if __name__ == '__main__':
    n, k = map(int, input().split())
    m = int(input())

    can = [[0]*k for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        can[u][v] = 1
    
    print(solved())

