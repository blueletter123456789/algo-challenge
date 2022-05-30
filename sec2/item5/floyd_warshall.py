INF = 10**5

n, m, s = map(int, input().split())
dist = [[INF]*n for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split())
    dist[u][v] = c
    # dist[v][u] = c

for i in range(n):
    dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

for row in dist:
    for el in row:
        print('{:<7}'.format(el), end='')
    print()
