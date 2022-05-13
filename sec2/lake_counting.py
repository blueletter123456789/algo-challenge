def dfs(i, j):
    seen[i*m+j] = True
    for fi in range(-1, 2):
        for fj in range(-1, 2):
            ni, nj = i+fi, j+fj
            if ni < 0 or ni >= n or nj < 0 or nj >= m or seen[ni*m + nj]:
                continue
            if field[ni][nj] == 'W':
                dfs(ni, nj)

n, m = map(int, input().split())
field = [input() for _ in range(n)]

ans = 0
seen = [False]*(n*m)
for i in range(n):
    for j in range(m):
        if field[i][j] == 'W' and not seen[i*m+j]:
            dfs(i, j)
            ans += 1

print(ans)

# Sample source
# def dfs(i, j):
#     field[i][j] = '.'
#     for fi in range(-1, 2):
#         for fj in range(-1, 2):
#             ni, nj = i+fi, j+fj
#             if ni < 0 or ni >= n or nj < 0 or nj >= m:
#                 continue
#             if field[ni][nj] == 'W':
#                 dfs(ni, nj)

# n, m = map(int, input().split())
# field = [list(input()) for _ in range(n)]

# ans = 0
# for i in range(n):
#     for j in range(m):
#         if field[i][j] == 'W':
#             dfs(i, j)
#             ans += 1

# print(ans)

