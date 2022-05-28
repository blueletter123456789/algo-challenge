INF = 10**5

n, m, s = map(int, input().split())
edge_lst = list()
for _ in range(m):
    u, v, c = map(int, input().split())
    edge_lst.append({'from': u, 'to': v, 'cost': c})

d = [INF]*n
d[s] = 0
while True:
    update = False
    for e in edge_lst:
        if d[e['from']] != INF and d[e['to']] > d[e['from']] + e['cost']:
            d[e['to']] = d[e['from']] + e['cost']
            update = True
    
    if not update:
        break

print(d)

# If exist negative roop and roop by vertex
# INF = 10**5

# n, m, s = map(int, input().split())
# G = [list() for _ in range(n)]

# for _ in range(m):
#     u, v, c = map(int, input().split())
#     G[u].append({'to': v, 'w': c})

# is_negative = False
# dist = [INF]*n
# dist[s] = 0
# for i in range(n):
#     update = False
#     for v in range(n):
#         if dist[v] == INF:
#             continue
#         for e in G[v]:
#             if dist[e['to']] > dist[v] + e['w']:
#                 dist[e['to']] = dist[v] + e['w']
#                 update = True
#     if not update:
#         break
#     if i == n-1 and update:
#         is_negative = True

# if is_negative:
#     print('negative circle')
# else:
#     print(dist)
