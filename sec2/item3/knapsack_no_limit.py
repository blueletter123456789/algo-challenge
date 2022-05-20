n = int(input())
in_lst = [tuple(map(int, input().split())) for _ in range(n)]
w = int(input())

dp = [0]*(w+1)

for i in range(w+1):
    for j in range(n):
        wj, vj = in_lst[j]
        if i < wj:
            continue
        dp[i] = max(dp[i], dp[i-wj]+vj)

print(dp[w])
