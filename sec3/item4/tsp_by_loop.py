def solved():
    dp = [[float('inf')]*n for _ in range(2**n)]
    dp[(1 << n)-1][0] = 0

    # 2^n - 1から遷移した状態からスタート
    S = (1 << n) - 2
    while S >= 0:
        for v in range(n):
            for u in range(n):
                if ((S >> u) & 1) == 0:
                    dp[S][v] = min(dp[S][v], 
                        dp[S | 1 << u][u] + G[v][u])
        S -= 1
    return dp[0][0]

def solved2():
    dp = [[float('inf')]*n for _ in range(2**n)]
    dp[0][0] = 0

    for S in range(2**n):
        for v in range(n):
            for u in range(n):
                # Sが０の時は例外として処理
                if not (S >> u) & 1 and S != 0:
                    continue
                if (S >> v) & 1 == 0:
                    if dp[S | (1 << v)][v] > dp[S][u] + G[u][v]:
                        dp[S | (1 << v)][v] = dp[S][u] + G[u][v]
    
    return dp[2**n-1][0]

if __name__ == '__main__':
    n = int(input())
    G = [[float('inf')]*n for _ in range(n)]
    for i in range(n):
        row = input().split()
        for j, c in enumerate(row):
            if c == 'INF':
                continue
            G[i][j] = int(c)
    
    print(solved())
    print(solved2())
