n, m = map(int, input().split())
s = input()
t = input()

dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)

ans = ''
tgt = dp[0][0]
for i in range(n):
    for j in range(m):
        if dp[i+1][j+1] - tgt == 1:
            ans += t[j]
            tgt += 1
            break
print(dp[n][m])
print(ans)

# Sample code
# n, m = map(int, input().split())
# s = input()
# t = input()

# dp = [[0]*(m+1) for _ in range(n+1)]
# for i in range(n):
#     for j in range(m):
#         if s[i] == t[j]:
#             dp[i+1][j+1] = dp[i][j] + 1
#         else:
#             dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
# print(dp[n][m])
