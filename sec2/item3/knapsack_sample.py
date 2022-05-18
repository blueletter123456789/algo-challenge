n = int(input())
w, v = [0]*n, [0]*n
for i in range(n):
    w[i], v[i] = map(int, input().split())
wei = int(input())

# 再帰全探索
def rec(i, j):
    res = 0
    if i == n:
        res = 0
    elif j < w[i]:
        res = rec(i+1, j)
    else:
        res = max(rec(i+1, j), rec(i+1, j-w[i])+v[i])
    return res

print(rec(0, wei))


# 再帰動的計画法
def rec(i, j):
    if dp[i][j] >= 0:
        return dp[i][j]
    res = 0
    if i == n:
        res = 0
    elif j < w[i]:
        res = rec(i+1, j)
    else:
        res = max(rec(i+1, j), rec(i+1, j-w[i])+v[i])
    dp[i][j] = res
    return res

dp = [[-1]*(wei+1) for _ in range(n+1)]
print(rec(0, wei))


# 二重ループ動的計画法（逆向き）
dp = [[0]*(wei+1) for _ in range(n+1)]
for i in range(n-1, -1, -1):
    for j in range(wei+1):
        if j < w[i]:
            dp[i][j] = dp[i+1][j]
        else:
            dp[i][j] = max(dp[i+1][j], dp[i+1][j-w[i]] + v[i])

print(dp[0][wei])


# 二重ループ動的計画法（貰う）
dp = [[0]*(wei+1) for _ in range(n+1)]
for i in range(n):
    for j in range(wei+1):
        if j < w[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]] + v[i])

print(dp[n][wei])


# 二重ループ動的計画法（配る）
dp = [[0]*(wei+1) for _ in range(n+1)]
for i in range(n):
    for j in range(wei+1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if j+w[i] <= wei:
            dp[i+1][j+w[i]] = max(dp[i][j+w[i]], dp[i][j]+v[i])

print(dp[n][wei])
