M = 10**9 + 7

def rec(i, j, used):
    # 対象の列に全て置いた場合
    if j == m:
        return rec(i+1, 0, used)
    # 全て置いた場合
    if i == n:
        return 1
    
    # 隣の列を探索
    if used[i][j] or color[i][j]:
        return rec(i, j+1, used)
    
    res = 0
    used[i][j] = True

    # 横に置いた場合
    if j+1 < m and not used[i][j+1] and not color[i][j+1]:
        used[i][j+1] = True
        res += rec(i, j+1, used)
        used[i][j+1] = False
    
    # 縦に置いた場合
    if i+1 < n and not used[i+1][j] and not color[i+1][j]:
        used[i+1][j] = True
        res += rec(i, j+1, used)
        used[i+1][j] = False
    
    used[i][j] = False

    return res % M


def solved():
    used = [[0]*m for _ in range(n)]
    return rec(0, 0, used)


if __name__ == '__main__':
    n, m = map(int, input().split())
    color = [[False]*m for _ in range(n)]
    for i in range(n):
        for j, s in enumerate(input()):
            if s == 'x':
                color[i][j] = True
    
    print(solved())
