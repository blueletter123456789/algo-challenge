from collections import deque


class Edge(object):
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev


class Dinic(object):
    def __init__(self, n):
        self.G = [list() for _ in range(n)]
        self.level = list()
        self.iter = list()
        self.n = n
    
    def add_edge(self, fro, to, cap):
        self.G[fro].append(Edge(to, cap, len(self.G[to])))
        self.G[to].append(Edge(fro, 0, len(self.G[fro])-1))
    
    def bfs(self, s):
        self.level = [-1]*self.n
        self.level[s] = 0
        que = deque([s])
        while len(que):
            cur = que.popleft()
            for e in self.G[cur]:
                if e.cap > 0 and self.level[e.to] < 0:
                    self.level[e.to] = self.level[cur] + 1
                    que.append(e.to)

    def dfs(self, v, t, f):
        if v == t:
            return f
        iter_v = self.iter[v]
        for i in range(iter_v, len(self.G[v])):
            self.iter[v] = i
            e = self.G[v][i]
            if e.cap > 0 and self.level[e.to] > self.level[v]:
                d = self.dfs(e.to, t, min(f, e.cap))
                if d > 0:
                    e.cap -= d
                    self.G[e.to][e.rev].cap += d
                    return d
        return 0
    
    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                return flow
            self.iter = [0]*self.n
            f = 1
            while f > 0:
                f = self.dfs(s, t, float('inf'))
                flow += f

def solved():
    s = n + k
    t = s + 1

    di = Dinic(n + k + 2)
    for i in range(n):
        di.add_edge(s, i, 1)
    
    for i in range(k):
        di.add_edge(i + n, t, 1)
    
    for i in range(n):
        for j in range(k):
            if can[i][j]:
                di.add_edge(i, n + j, 1)
    
    return di.max_flow(s, t)


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
