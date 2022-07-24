# Sample code
M = 10**9 + 7

def solved():
    dp = [[0]*(1 << m) for _ in range(2)]

    # dp[crt][S]の状態になるにはdp[nxt][S']のいずれかにある
    crt, nxt = 0, 1
    dp[crt][0] = 1

    i = n - 1
    while i >= 0:
        j = m - 1
        while j >= 0:
            for used in range(1 << m):
                # (i,j)が空でない場合
                if (used >> j) & 1 or color[i][j]:
                    dp[nxt][used] = dp[crt][used & ~(1 << j)]
                # (i,j)が空の場合
                else:
                    res = 0
                    # 横置き
                    if j+1 < m and not ((used >> (j+1)) & 1) and not color[i][j+1]:
                        res += dp[crt][used | 1 << (j+1)]
                    # 縦置き
                    if i+1 < n and not color[i+1][j]:
                        res += dp[crt][used | 1 << j]
                    dp[nxt][used] = res % M
            crt, nxt = nxt, crt
            j -= 1
        i -= 1
    
    return dp[crt][0]

# def solved():
#     dp = [[float('inf')]*(1 << m) for _ in range(n)]
#     dp[0][0] = 0

#     for S in range(1 << m):
#         for i in range(n):
#             s = S
#             for k, val in enumerate(G[i]):
#                 if val == 'x':
#                     s |= (1 << k)
#             for j in range(m):
#                 if s & (1 << j):
#                     continue

#                 if s & (1 << (j+1)):
#                     continue
                


if __name__ == '__main__':
    n, m = map(int, input().split())
    color = [[False]*m for _ in range(n)]
    for i in range(n):
        for j, s in enumerate(input()):
            if s == 'x':
                color[i][j] = True

    print(solved())
