import heapq


class Edge(object):
    def __init__(self, to, cap, cost, rev):
        self.to = to
        self.cap = cap
        self.cost = cost
        self.rev = rev

class MinimumCostFlow(object):
    """
    参考
    http://www.bunkyo.ac.jp/~nemoto/lecture/network/2015/mincostflow2011.pdf
    """
    def __init__(self, n):
        self.n = n
        self.G = [list() for _ in range(n)]
        self.h = list()
        self.dist = list()
        self.prevv = [0]*n
        self.preve = [0]*n
    
    def add_edge(self, fro, to, cap, cost):
        self.G[fro].append(Edge(to, cap, cost, len(self.G[to])))
        self.G[to].append(Edge(fro, 0, -cost, len(self.G[fro])-1))
    
    def min_cost_flow(self, s, t, f):
        res = 0
        self.h = [0]*self.n
        while f > 0:
            que = list()
            self.dist = [float('inf') for _ in range(self.n)]
            self.dist[s] = 0
            heapq.heappush(que, (0, s))
            while len(que):
                nd, nv = heapq.heappop(que)
                if self.dist[nv] < nd:
                    continue
                for i, e in enumerate(self.G[nv]):
                    if e.cap > 0 and self.dist[e.to] > self.dist[nv] + e.cost + self.h[nv] - self.h[e.to]:
                        self.dist[e.to] = self.dist[nv] + e.cost + self.h[nv] - self.h[e.to]
                        self.prevv[e.to] = nv
                        self.preve[e.to] = i
                        heapq.heappush(que, (self.dist[e.to], e.to))
            
            if self.dist[t] == float('inf'):
                return -1
            
            for v in range(self.n):
                self.h[v] += self.dist[v]
            
            d = f
            v = t
            while v != s:
                d = min(d, self.G[self.prevv[v]][self.preve[v]].cap)
                v = self.prevv[v]
            
            f -= d
            res += d * self.h[t]

            v = t
            while v != s:
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
    
    print(mcf.min_cost_flow(s, t, f))
