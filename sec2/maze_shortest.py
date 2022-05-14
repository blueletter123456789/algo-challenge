from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
field = list()

sx, sy = 0, 0
gx, gy = 0, 0

for i in range(n):
    row = input()
    for j in range(m):
        if row[j] == 'S':
            sx, sy = i, j
        if row[j] == 'G':
            gx, gy = i, j
    field.append(row)
# -1に設定。重み付きグラフの場合はINFの値を設定
dist = [[-1]*m for _ in range(n)]
que = deque([(sx, sy)])
dist[sx][sy] = 0

while len(que):
    x, y = que.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if dist[nx][ny] != -1:
            continue
        if field[nx][ny] != '#':
            dist[nx][ny] = dist[x][y] + 1
            que.append((nx, ny))

print(dist[gx][gy])
