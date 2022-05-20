n = int(input())
w, v = [0]*n, [0]*n
for i in range(n):
    w[i], v[i] = map(int, input().split())
wei = int(input())

# sample code 1
dp = [[0]*(wei+1) for _ in range(n+1)]
for i in range(n):
    for j in range(wei+1):
        k = 0
        while k * w[i] <= j:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j-k*w[i]]+k*v[i])
            k += 1

print(dp[n][wei])

# sample code 2
dp = [[0]*(wei+1) for _ in range(n+1)]
for i in range(n):
    for j in range(wei+1):
        if j < w[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i+1][j-w[i]]+v[i])

print(dp[n][wei])

# 0-1 knapsack
dp = [0]*(wei+1)
for i in range(n):
    for j in range(wei, w[i]-1, -1):
        dp[j] = max(dp[j], dp[j-w[i]]+v[i])

print(dp[wei])

# sample code 3
dp = [0]*(wei+1)
for i in range(n):
    for j in range(w[i], wei+1):
        dp[j] = max(dp[j], dp[j-w[i]]+v[i])

print(dp[wei])

# sample code 4
dp = [[0]*(wei+1) for _ in range(2)]
for i in range(n):
    for j in range(wei+1):
        if j < w[i]:
            dp[(i+1) & 1][j] = dp[i & 1][j]
        else:
           dp[(i+1)&1][j] = max(dp[i&1][j], dp[(i+1)&1][j-w[i]]+v[i])

print(dp[n&1][wei])
