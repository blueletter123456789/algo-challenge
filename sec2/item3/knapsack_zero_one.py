n = int(input())
w, v = [0]*n, [0]*n
for i in range(n):
    w[i], v[i] = map(int, input().split())
wei = int(input())

max_val = 10**4
INF = 10**9 + 10
dp = [[INF]*(max_val+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(max_val+1):
        if j < v[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]]+w[i])

ans = 0
for i in range(max_val+1):
    if dp[n][i] <= wei:
        ans = i
print(ans)
