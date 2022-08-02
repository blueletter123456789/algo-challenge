class Edge(object):
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev

class FordFulkerson(object):
    def __init__(self, n):
        self.G = [list() for _ in range(n)]
        self.used = [False]*n
        self.n = n
    
    def add_edge(self, fro, to, cap):
        self.G[fro].append(Edge(to, cap, len(self.G[to])))
        self.G[to].append(Edge(fro, 0, len(self.G[fro])-1))
    
    def dfs(self, v, t, f):
        if v == t:
            return f
        
        self.used[v] = True

        for edge in self.G[v]:
            if not self.used[edge.to] and edge.cap > 0:
                d = self.dfs(edge.to, t, min(f, edge.cap))
                if d > 0:
                    edge.cap -= d
                    self.G[edge.to][edge.rev].cap += d
                    return d
        
        return 0
    
    def max_flow(self, s, t):
        flow = 0
        while True:
            self.used = [False]*self.n
            f = self.dfs(s, t, float('inf'))
            if f == 0:
                return flow
            flow += f


if __name__ == '__main__':
    n = 6
    m = 9
    s, t = 0, 5
    lst = [
        (0, 1, 5),
        (0, 3, 5),
        (1, 3, 37),
        (1, 2, 4),
        (3, 2, 3),
        (3, 4, 9),
        (2, 4, 56),
        (2, 5, 9),
        (4, 5, 2)
    ]
    ff = FordFulkerson(n)
    for e in lst:
        ff.add_edge(*e)
    
    print(ff.max_flow(s, t))
