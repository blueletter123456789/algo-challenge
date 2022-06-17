# Sample code
from decimal import Decimal

def solved(m, p, x):
    # n: 2^m
    n = 1 << m
    dp = [[0.0]*(n+1) for _ in range(2)]
    prev = 0
    nxt = 1
    dp[prev][n] = 1.0

    # 各ラウンドで見ていく
    for r in range(m):
        # 各区間を計算
        for i in range(n+1):

            # 区間の金額となりうる範囲を取得
            jub = min(i, n-i)
            t = 0.0
            for j in range(jub+1):
                # 残りrラウンドにてr-1ラウンドの状態から計算
                t = max(t, p*dp[prev][i+j] + (1-p)*dp[prev][i-j])
            dp[nxt][i] = t
        prev, nxt = nxt, prev
    
    # 初期値が属する区間
    i = x*n//1000000
    return dp[prev][i]

if __name__ == '__main__':
    m = int(input())
    p = Decimal(input())
    x = int(input())

    print(solved(m, p, x))

# import math

# def solved(m, p, x):
#     reward = 10**6
#     dp = [[0]*(reward+1) for _ in range(m+1)]
#     dp[0][x] = 1
#     for i in range(m):
#         for j in range(reward):
#             dp[i+1][j] = max(dp[i+1][j], dp[i][j])

#             less_amount = reward - j
#             less_cnt = m - i - 1
#             bet = math.ceil(less_amount / 2**less_cnt)
#             dp[i+1][j+bet] = max(dp[i+1][j+bet], dp[i][j]*p)
#             dp[i+1][j-bet] = max(dp[i+1][j-bet], dp[i][j]*(1-p))

#     return dp[m][reward]


# if __name__ == '__main__':
#     m = int(input())
#     p = float(input())
#     x = int(input())

#     print(solved(m, p, x))
