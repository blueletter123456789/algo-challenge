from collections import deque

class Edge(object):
    def __init__(self, to, cap, cost, rev):
        self.to = to
        self.cap = cap
        self.cost = cost
        self.rev = rev

class MinimumCostFlow(object):
    def __init__(self, n):
        self.n = n
        self.G = [list() for _ in range(n)]
        self.dist = list()
        self.prevv = [0]*n
        self.preve = [0]*n
    
    def add_edge(self, fro, to, cap, cost):
        self.G[fro].append(Edge(to, cap, cost, len(self.G[to])))
        self.G[to].append(Edge(fro, 0, -cost, len(self.G[fro])-1))
    
    def min_cost(self, s, t, f):
        res = 0
        while f > 0:
            # ベルマンフォードよりs-t間のコストを元に最短路を求める
            self.dist = [float('inf') for _ in range(self.n)]
            self.dist[s] = 0
            update = True
            while update:
                update = False
                for v in range(self.n):
                    if self.dist[v] == float('inf'):
                        continue
                    for i, e in enumerate(self.G[v]):
                        if e.cap > 0 and self.dist[e.to] > self.dist[v] + e.cost:
                            self.dist[e.to] = self.dist[v] + e.cost
                            self.prevv[e.to] = v
                            self.preve[e.to] = i
                            update = True
            if self.dist[t] == float('inf'):
                return -1
            
            d = f

            v = t
            while v != s:
                # コストベースでの最短経路でフローの量をゴールから計算する
                d = min(d, self.G[self.prevv[v]][self.preve[v]].cap)
                v = self.prevv[v]
            
            f -= d
            # (流れたフロー)×(s-t間コストの合計)
            res += d * self.dist[t]
            
            v = t
            while v != s:
                # 実際にフローを流す
                e = self.G[self.prevv[v]][self.preve[v]]
                e.cap -= d
                self.G[v][e.rev].cap += d
                v = self.prevv[v]
        
        return res


if __name__ == '__main__':
    n, m = map(int, input().split())
    f = int(input())
    s, t = map(int, input().split())
    
    mcf = MinimumCostFlow(n)
    for _ in range(m):
        u, v, c, d = map(int, input().split())
        mcf.add_edge(u, v, c, d)
    
    print(mcf.min_cost(s, t, f))

