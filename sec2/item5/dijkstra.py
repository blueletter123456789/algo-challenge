# O(v^2): 密グラフ
INF = 10**5

n, m, s = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split())
    al[u].append((v, c))

dist = [INF]*n
used = [False]*n
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
        dist[to] = min(dist[to], dist[v]+cost)

print(dist)

# O(|E|log|V|): 疎グラフ
import heapq

INF = 10**5

n, m, s = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split())
    al[u].append({'to': v, 'cost': c})

dist = [INF]*n
dist[s] = 0
que = [(0, s)]
while len(que):
    p, v = heapq.heappop(que)
    if dist[v] < p:
        continue
    for edge in al[v]:
        if dist[edge['to']] > dist[v] + edge['cost']:
            dist[edge['to']] = dist[v] + edge['cost']
            heapq.heappush(que, (dist[edge['to']], edge['to']))

print(dist)
