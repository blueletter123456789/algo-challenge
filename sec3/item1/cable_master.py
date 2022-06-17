from decimal import Decimal

def round_decimal(d, n=2):
    ans = str(d).split('.')
    return ans[0] + '.' + ans[1][:n]

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    lst = input().split()

    l = Decimal('0.0')
    r = Decimal('1000000.0')
    while r - l > 0.001:
        m = (l + r) / 2
        cnt = 0
        for t in lst:
            cnt += Decimal(t) // m
        if cnt < k:
            r = m
        else:
            l = m
    
    print(round_decimal(r))


# Sample code
# n, k = 0, 0
# L = list()
# INF = 10**6

# def C(x):
#     num = 0
#     for i in range(n):
#         num += int(L[i] // x)
    
#     return num >= k

# if __name__ == '__main__':
#     n = int(input())
#     k = int(input())
#     L = list(map(float, input().split()))
    
#     lb = 0
#     ub = INF
#     for i in range(100):
#         mid = (lb + ub) / 2
#         if C(mid):
#             lb = mid
#         else:
#             ub = mid
    
#     print(round_decimal(ub))
