# Sample code
dir = list()
turned = list()

def calc(k):
    """機械の使用回数計算
    同一区間を複数回回転させる必要がないため、
    一番左側が1の場合は必ず回転させる。
    残りの区間も同様に回転させていく。

    Args:
        k (int): 一度に回転できる数

    Returns:
        int: 使用回数
    """
    turned = [0]*n
    res = 0
    # 区間[i-k+1, i]の合算
    # 偶数：初期の向き、奇数：初期と反対の向き
    sum_turn = 0
    i = 0
    while i + k <= n:
        # 先頭の向きを判定
        # もともとの向きと操作回数を加算
        if (dir[i] + sum_turn) % 2:
            res += 1
            turned[i] = 1
        
        # iが先頭の区間
        sum_turn += turned[i]
        if i - k + 1 >= 0:
            # i-k+1が先頭の区間
            sum_turn -= turned[i - k + 1]
        i += 1
    for i in range(n - k + 1, n):
        # 反対の向きがある場合
        if (dir[i] + sum_turn) % 2:
            return -1
        if i - k + 1 >= 0:
            sum_turn -= turned[i - k + 1]
    return res

def solved():
    global dir
    dir = [0 if j == 'F' else 1 for j in direction]
    K = 1
    M = n
    for k in range(1, n+1):
        m = calc(k)
        if m >= 0 and M > m:
            M = m
            K = k
    return K, M

if __name__ == '__main__':
    n = int(input())
    direction = input()
    print(solved())

# def solved():
#     k = n+1
#     m = 1 << 30
#     for i in range(n):
#         d = [True if j == 'F' else False for j in direction]
#         if all(d):
#             return 1, 0
#         s = 0
#         for t in range(n-i):
#             if d[t]:
#                 continue
#             for j in range(t, t+i+1):
#                 d[j] = not d[j]
#             s += 1
#         if all(d) and m > s:
#             m = s
#             k = i+1
#     return k, m

# if __name__ == '__main__':
#     n = int(input())
#     direction = input()

#     print(solved())
