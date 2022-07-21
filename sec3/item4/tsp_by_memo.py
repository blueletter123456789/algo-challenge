import pprint

MAX_N = 15


def rec(S, v):
    if dp[S][v] >= 0:
        return dp[S][v]
    
    if S == (1 << n) - 1 and v == 0:
        # 全ての頂点を訪問し、戻ってきた場合
        dp[S][v] = 0
        return 0
    
    res = float('inf')
    for u in range(n):
        # まだSの中でuに到達していない場合のみ比較
        if (S >> u) & 1 == 0:
            res = min(res, rec(S | (1 << u), u) + G[v][u])
    dp[S][v] = res
    return res


def solved():
    return rec(0, 0)
    

if __name__ == '__main__':
    n = int(input())
    G = [[float('inf')]*n for _ in range(n)]
    for i in range(n):
        row = input().split()
        for j, c in enumerate(row):
            if c == 'INF':
                continue
            G[i][j] = int(c)

    dp = [[-1]*n for _ in range(2**n)]
    
    print(solved())

    