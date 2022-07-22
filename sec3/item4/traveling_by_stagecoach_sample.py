def solved():
    # dp[S][v]: 残りの乗車券がS, 現在のノードがv
    dp = [[float('inf')]*m for _ in range(1 << n)]
    dp[(1 << n)-1][s] = 0
    res = float('inf')

    for S in range((1<<n)-1, -1, -1):
        res = min(res, dp[S][t])
        for v in range(m):
            for i in range(n):
                if (S >> i) & 1:
                    for u in range(m):
                        if G[v][u] >= 0:
                            # 乗車券iを使用してvからuへ移動
                            # 集合Sから要素iを取り除いた集合に対して更新
                            dp[S & ~(1 << i)][u] = min(dp[S & ~(1 << i)][u], 
                                dp[S][v] + G[v][u]/T[i])
    
    if res == float('inf'):
        return 'Impossible'
    else:
        return res

def to_zero(a):
    return int(a)-1

if __name__ == '__main__':
    n, m = map(int, input().split())
    s, t = map(to_zero, input().split())

    T = list(map(int, input().split()))
    G = [[float('inf')]*m for _ in range(m)]
    while True:
        try:
            u, v, c = map(int, input().split())
            u -= 1
            v -= 1
            G[u][v] = c
            G[v][u] = c
        except EOFError:
            break
    
    print(solved())
