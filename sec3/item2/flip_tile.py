# Sample code
dx = [1, 0, 0, -1, 0]
dy = [0, 1, 0, 0, -1]
fliped = list()

def get(x, y):
    """マスの色を取得

    Args:
        x (int): 行インデックス
        y (int): 列インデックス

    Returns:
        int: 色（0: 白, 1: 黒）
    """
    c = tile[x][y]
    for d in range(5):
        nx, ny = x+dx[d], y+dy[d]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        # fliped[nx][ny]: フリップした回数
        c += fliped[nx][ny]
    return c % 2

def calc():
    """１行目以降でマスをフリップ

    Returns:
        int: フリップ回数
    """
    for i in range(1, m):
        for j in range(n):
            if get(i-1, j) != 0:
                # (i-1, j)が黒の場合は対象のマスをフリップ
                fliped[i][j] = 1
    
    # 最後の行に黒が存在する場合は成立しない
    for j in range(n):
        if get(m-1, j) != 0:
            return -1
    
    # フリップした回数を取得
    res = 0
    for i in range(m):
        for j in range(n):
            res += fliped[i][j]
    return res

def solved():
    global fliped

    opt = list()
    res = -1
    
    # １行目を辞書順で実行
    for i in range(1 << n):
        fliped = [[0]*n for _ in range(m)]
        for j in range(n):
            fliped[0][n-j-1] = i >> j & 1
        num = calc()

        if num >= 0 and (res < 0 or res > num):
            res = num
            # 最小回数をコピー
            opt = fliped.copy()
        
    return opt


if __name__ == '__main__':

    n = int(input())
    m = int(input())
    tile = [list(map(int, input().split())) for _ in range(m)]

    ans = solved()
    if ans:
        for i in range(m):
            print(' '.join(list(map(str, ans[i]))))
    else:
        print('IMPOSSIBLE')

# def solved():
#     dx = [1, 0]
#     dy = [0, 1]

#     ans = [[0]*n for _ in range(m)]
#     turned = [[0]*n for _ in range(m)]
#     sum = 0
#     for x in range(m):
#         for y in range(n):
#             if flip[x][y] == 0:
#                 continue
#             for i in range(2):
#                 nx, ny = flip[x], flip[y]
#     print(turned)
#     return ans

# if __name__ == '__main__':
#     n = int(input())
#     m = int(input())
#     flip = [list(map(int, input().split)) for _ in range(m)]
