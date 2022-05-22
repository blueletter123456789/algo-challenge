# Sample code
# http://techtipshoge.blogspot.com/2011/01/blog-post_28.html
n = int(input())
m = int(input())
M = int(input())

dp = [[0]*(n+1) for _ in range(m+1)]
dp[0][0] = 1
for i in range(1, m+1):
    for j in range(n+1):
        if j - i >= 0:
            dp[i][j] = (dp[i-1][j] + dp[i][j-i]) % M
        else:
            dp[i][j] = dp[i-1][j]

print(dp[m][n])

# n = int(input())
# m = int(input())
# M = int(input())

# dp = [[0]*(n+1) for _ in range(m+1)]
# for i in range(m):
#     for j in range(1, n+1):
#         if i < j:
#             dp[i+1][j] = (dp[i][j-1]+1) + dp[i+1][j-1]
#         else:
#             dp[i+1][j] = dp[i][j]
