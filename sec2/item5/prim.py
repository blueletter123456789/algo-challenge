INF = 10 ** 5

n, m = map(int, input().split())
min_cost = [INF]*n
used = [False]*n

# O(n^2)
am = [[INF]*n for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split())
    am[u][v] = c
    am[v][u] = c

def prim(s=0):
    min_cost[s] = 0
    res = 0
    while True:
        v = -1
        for u in range(n):
            if not used[u] and (v == -1 or min_cost[u] < min_cost[v]):
                v = u
        if v == -1:
            break
        used[v] = True
        res += min_cost[v]
        
        for u in range(n):
            min_cost[u] = min(min_cost[u], am[v][u])
    
    return res

print(prim())
print(min_cost)

# O(|E|log|V|)
# import heapq

# al = [list() for _ in range(n)]
# for _ in range(m):
#     u, v, c = map(int, input().split())
#     al[u].append({'to': v, 'cost': c})
#     al[v].append({'to': u, 'cost': c})

# def prim(s=0):
#     res = 0
#     que = [(0, s)]

#     while len(que):
#         cost, v = heapq.heappop(que)
#         if used[v]:
#             continue
#         used[v] = True
#         res += cost
#         for edge in al[v]:
#             if not used[edge['to']]:
#                 heapq.heappush(que, (edge['cost'], edge['to']))
#     return res

# print(prim())
