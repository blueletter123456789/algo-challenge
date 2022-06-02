import heapq

INF = 10**5

n, m = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    al[u-1].append({'to': v-1, 'wei': w})
    al[v-1].append({'to': u-1, 'wei': w})

s = 0
dist = [INF]*n
dist2 = [INF]*n
dist[s] = 0
que = [(0, s)]
while len(que):
    cost, current = heapq.heappop(que)
    if dist2[current] < cost:
        continue
    for e in al[current]:
        tgt = dist[current] + e['wei']
        if dist[e['to']] > tgt:
            dist[e['to']], tgt = tgt, dist[e['to']]
            heapq.heappush(que, (dist[e['to']], e['to']))
        if dist2[e['to']] > tgt and dist[e['to']] < tgt:
            dist2[e['to']] = tgt
            heapq.heappush(que, (dist2[e['to']], e['to']))

print(dist2[n-1])
