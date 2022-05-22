n = int(input())
a_lst = [i for i in list(map(int, input().split()))]
m_lst = [i for i in list(map(int, input().split()))]
k = int(input())

INF = 10**5
dp = [[INF]*(k+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(k+1):
        if dp[i][j] < INF:
            dp[i+1][j] = 0
        if j == a_lst[i] or dp[i][j-a_lst[i]] < INF:
            dp[i+1][j] = min(dp[i+1][j], 1)
        if dp[i+1][j-a_lst[i]] < m_lst[i]:
            dp[i+1][j] = min(dp[i+1][j], dp[i+1][j-a_lst[i]]+1)

if dp[n][k] < INF:
    print('Yes')
else:
    print('No')

# Sample code 1
# dp = [[False]*(k+1) for _ in range(n+1)]
# dp[0][0] = True
# for i in range(n):
#     for j in range(k+1):
#         for m in range(m_lst[i]+1):
#             if m*a_lst[i] > j:
#                 break
#             dp[i+1][j] |= dp[i][j-(m*a_lst[i])]

# if dp[n][k]:
#     print('Yes')
# else:
#     print('No')

# Sample code 2
# dp = [-1]*(k+1)
# dp[0] = 0
# for i in range(n):
#     for j in range(k+1):
#         if dp[j] >= 0:
#             dp[j] = m_lst[i]
#         elif j < a_lst[i] or dp[j-a_lst[i]] <= 0:
#             dp[j] = -1
#         else:
#             dp[j] = dp[j-a_lst[i]]-1
# if dp[k] >= 0:
#     print('Yes')
# else:
#     print('No')
