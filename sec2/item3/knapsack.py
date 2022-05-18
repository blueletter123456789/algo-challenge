n = int(input())
items = [tuple(map(int, input().split())) for _ in range(n)]
w = int(input())

dp = [[0]*(w+1) for _ in range(n+1)]
for i in range(n):
    weight, value = items[i]
    for j in range(w+1):
        if weight > j:
            dp[i+1][j] = dp[i][j]
            continue
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        dp[i+1][j] = max(dp[i+1][j], dp[i][j-weight]+value)

ans = 0
for val in dp[n]:
    ans = max(ans, val)
print(ans)

