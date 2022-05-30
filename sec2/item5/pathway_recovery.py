# Ex）Dijkstra
INF = 10**5

n, m, s = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split())
    al[u].append((v, c))

dist = [INF]*n
used = [False]*n
prev = [-1]*n
dist[s] = 0

while True:
    v = -1
    for u in range(n):
        if not used[u] and (v == -1 or dist[u] < dist[v]):
            v = u
    if v == -1:
        break
    used[v] = True
    
    for to, cost in al[v]:
        if dist[to] > dist[v]+cost:
            dist[to] = dist[v]+cost
            prev[to] = v

def get_path(t):
    path = list()
    v = t
    while v != -1:
        path.append(v)
        v = prev[v]
    path.reverse()
    return path
print(get_path(6))
