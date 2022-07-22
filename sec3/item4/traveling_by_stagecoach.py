def rec(S, v):
    if dp[S][v] >= 0:
        return dp[S][v]
    
    # 到達している場合
    if v == t:
        return 0
    
    res = float('inf')    
    # 次のノードを探索
    for u in range(m):
        if G[v][u] == float('inf'):
            continue
        # 使用する乗車券を探索
        for i in range(n):
            # 対象の乗車券を使用していない場合
            if (S >> i) & 1 == 0:
                res = min(res, rec(S | (1 << i), u) + G[v][u]/T[i])
        dp[S][v] = res
    return res


def solved():
    return rec(0, s)

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
    
    dp = [[-1]*m for _ in range(2**n)]
    ans = solved()

    if ans > 0 and ans < float('inf'):
        print(ans)
    else:
        print('Impossible')
