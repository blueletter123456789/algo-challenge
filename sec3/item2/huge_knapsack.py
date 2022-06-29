# Sample code
import bisect
import pprint

INF = float('inf')

def solved():
    m = n // 2
    ps = list()
    for i in range(1 << m):
        sw = sv = 0
        for j in range(m):
            if i & (1 << j):
                sw += w[j]
                sv += v[j]
        ps.append((sw, sv))
    ps.sort()
    # pprint.pprint(ps)

    min_num = 1
    for i in range(1, 1 << m):
        if ps[min_num-1][1] < ps[i][1]:
            ps[min_num] = ps[i]
            min_num += 1
    # pprint.pprint(ps)
    res = 0
    for i in range(1 << (n-m)):
        sw = sv = 0
        for j in range(n-m):
            if i & (1 << j):
                sw += w[m+j]
                sv += v[m+j]
        if sw <= W:
            tv = ps[bisect.bisect_left(ps[:min_num],  (W - sw, INF))-1][1]
            res = max(res, sv + tv)
    return res

if __name__ == '__main__':
    n, W = map(int, input().split())
    v = [0]*n
    w = [0]*n
    for i in range(n):
        v[i], w[i] = map(int, input().split())
    
    print(solved())



# def solved():
#     dp = [(0, 0)]
#     for i in range(n):
#         row = list()
#         for d in dp:
#             dw, dv = d
#             if w[i]+dw > W:
#                 continue
#             row.append((w[i]+dw, v[i]+dv))
#         dp += row
    
#     dp.sort(key=lambda x: x[1])
#     ans = dp[-1][1]
#     return ans


# if __name__ == '__main__':
#     n, W = map(int, input().split())
#     v = [0]*n
#     w = [0]*n
#     for i in range(n):
#         v[i], w[i] = map(int, input().split())

#     print(solved())
