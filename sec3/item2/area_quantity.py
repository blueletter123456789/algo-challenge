import bisect
from collections import deque
from pprint import pprint

def compress(lst1, lst2, n):
    comp = list()
    seen = set()
    for a, b in zip(lst1, lst2):
        for j in range(2):
            a2 = a + j
            b2 = b + j
            if a2 not in seen and a2 < n:
                comp.append(a2)
                seen.add(a2)
            if b2 not in seen and b2 < n:
                comp.append(b2)
                seen.add(b2)
    
    comp.sort()

    for i, (a, b) in enumerate(zip(lst1, lst2)):
        lst1[i] = bisect.bisect_left(comp, a)
        lst2[i] = bisect.bisect_left(comp, b)

    return lst1, lst2, len(comp)


def solved():
    cx1, cx2, vals_x = compress(x1, x2, W)
    cy1, cy2, vals_y = compress(y1, y2, H)

    area = [[False]*(vals_x) for _ in range(vals_y)]
    for i in range(N):
        for y in range(cy1[i], cy2[i]+1):
            for x in range(cx1[i], cx2[i]+1):
                area[y][x] = True
    # pprint(area)

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    que = deque([])
    ans = 0
    for y in range(vals_y):
        for x in range(vals_x):
            if area[y][x]:
                continue
            ans += 1
            que.append((y, x))
            while len(que):
                qy, qx = que.popleft()
                for i, j in zip(dy, dx):
                    ny, nx = qy+i, qx+j
                    if ny < 0 or ny >= vals_y or nx < 0 or nx >= vals_x:
                        continue
                    if area[ny][nx]:
                        continue
                    area[ny][nx] = True
                    que.append((ny, nx))

    return ans

if __name__ == '__main__':
    W = int(input()) #幅(個)
    H = int(input()) #高さ(個)
    N = int(input())
    x1 = [int(i)-1 for i in input().split()]
    x2 = [int(i)-1 for i in input().split()]
    y1 = [int(i)-1 for i in input().split()]
    y2 = [int(i)-1 for i in input().split()]

    # W, H = map(int, input().split())
    # N = int(input())
    # x1 = [0]*N
    # x2 = [0]*N
    # y1 = [0]*N
    # y2 = [0]*N
    # for i in range(N):
    #     x1[i], y1[i], x2[i], y2[i] = map(int, input().split())
    #     x2[i] -= 1
    #     y2[i] -= 1

    print(solved())
