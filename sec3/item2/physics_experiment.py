# Smaple code
import math

y = list()

def calc(T):
    if T < 0:
        return H
    t = math.sqrt(5*H)
    k = T // t
    if k % 2:
        d = k * t + t - T
        return H - 5 * (d**2)
    else:
        d = T - k * t
        return H - 5 * (d**2)

def solved():
    y = [0.0] * N
    for i in range(N):
        y[i] = calc(T - i)
    y.sort()
    for i, v in enumerate(y):
        print('{:.2f}'.format(v + 2 * R * i / 100.0))

if __name__ == '__main__':
    N = int(input())
    H = int(input())
    R = int(input())
    T = int(input())

    solved()


# import math

# def dist(t):
#     """変位計算

#     1/2gt^2
#     """
#     return 5*(t**2)

# def solved():
#     for i in range(1, in_n+1):
#         # ボールが落下する際の高さの初期値
#         ini_height = (in_h + 2*in_r*i)
#         # 地面に到着するまでの時間
#         t = math.sqrt(ini_height/ 5)
#         if t == in_t:
#             return 0
#         if t > in_t:
#             return ini_height - dist(t)
#         if (in_t // int(t)+1) % 2 == 0:
#             print(dist(in_t%t))
#         else:
#             print(ini_height-dist(in_t%t))

# if __name__ == '__main__':
#     in_n = int(input())
#     in_h = int(input())
#     in_r = int(input())/100
#     in_t = int(input())

#     solved()
