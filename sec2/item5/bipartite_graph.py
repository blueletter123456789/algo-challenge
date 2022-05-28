from collections import deque

n, m = map(int, input().split())
al = [list() for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    al[a].append(b)
    al[b].append(a)

colors = [-1]*n
for i in range(n):
    if colors[i] != -1:
        continue
    que = deque([i])
    colors[i] = 0
    ans = True
    while len(que):
        current = que.popleft()
        for v in al[current]:
            if colors[v] == colors[current]:
                ans = False
                break
            if colors[v] < 0:
                colors[v] = (colors[current]+1)%2
                que.append(v)

if ans:
    print('Yes')
else:
    print('No')

# Sample code by DFS
# n, m = map(int, input().split())
# G = [list() for _ in range(n)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     G[a].append(b)
#     G[b].append(a)

# colors = [0]*n
# def dfs(v, c):
#     colors[v] = c
#     for i in G[v]:
#         if colors[i] == c:
#             return False
#         if colors[i] == 0 and not dfs(i, -c):
#             return False
#     return True

# flg = True
# for i in range(n):
#     if colors[i] != 0:
#         continue
#     if not dfs(i, 1):
#         flg = False
#         break

# if flg:
#     print('Yes')
# else:
#     print('No')
