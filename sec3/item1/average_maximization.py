from decimal import Decimal

def under_threshold(x, k, w, v):
    lst = list()
    # 貧欲法を使うため、ΣVk/ΣWk >= xを変形する
    for wi, vi in zip(w, v):
        lst.append(vi - (x*wi))
    lst.sort(reverse=True)

    sum = 0
    for i in range(k):
        sum += lst[i]
    return sum >= 0

def round_decimal(x, n=2):
    res = str(x).split('.')
    return res[0] + '.' + res[1][:n]

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    w = [0]*n
    v = [0]*n

    for i in range(n):
        w[i], v[i] = map(int, input().split())

    l, r = 0, 10**7
    # NOTE: 問題により小数点以下の判定を変える
    while r - l > 0.001:
        m = (l + r) / 2
        if under_threshold(m, k, w, v):
            l = m
        else:
            r = m

    print(round_decimal(r))
