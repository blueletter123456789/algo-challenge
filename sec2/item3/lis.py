n = int(input())
lst = list(map(int, input().split()))

dp = [0]*(n+1)
dp[1] = 1
ans = 0
for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i+1] = max(dp[i+1], dp[j+1]+1)
            ans = max(ans, dp[i+1])
    if dp[i+1] == 0:
        dp[i+1] = dp[0]+1

print(ans)

# Sample code 1
dp = [0]*n
res = 0
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j]+1)
    res = max(res, dp[i])

print(res)


# Sample code 2
import bisect

INF = 10**6+10
dp = [INF]*n
for i in range(n):
    idx = bisect.bisect_left(dp, lst[i])
    dp[idx] = lst[i]

ans = bisect.bisect_left(dp, INF)
print(ans)
