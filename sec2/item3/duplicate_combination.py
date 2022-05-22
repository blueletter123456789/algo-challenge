n = int(input())
m = int(input())
lst = list(map(int, input().split()))
M = int(input())

dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1

for i in range(n):
    for j in range(1, m+1):
        if j - 1 - lst[i] >= 0:
            dp[i+1][j] = (dp[i+1][j-1] + dp[i][j] - dp[i][j-1-lst[i]]+M) % M
        else:
            dp[i+1][j] = (dp[i+1][j-1] + dp[i][j]) % M

print(dp[n][m])
