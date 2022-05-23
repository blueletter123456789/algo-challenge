import heapq

n, l, p = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.append(l)
B.append(0)

que = list()
ans, pos, tank = 0, 0, p
for i in range(n+1):
    flg = False
    dis = A[i] - pos
    while tank - dis < 0:
        if len(que) == 0:
            ans = -1
            flg = True
            break
        tank += -heapq.heappop(que)
        ans += 1
    if flg:
        break
    tank -= dis
    pos = A[i]
    heapq.heappush(que, -B[i])

print(ans)



# n, l, p = map(int, input().split())
# gas_point = [(int(i), int(j)) for i, j in zip(input().split(), input().split())]
# gas_point.sort(key=lambda x: x[0])

# remaining = list()
# heapq.heappush(remaining, p)
# cnt = 0
# before = 0
# for i in range(n):
#     cur = 0
#     x, y = gas_point[i]
#     dis = x - before
#     while len(remaining):
#         cur += heapq.heappop(remaining)
#         if cur >= dis:
#             break
#     if cur < dis:
#         cnt = -1
#         break
#     else:
#         heapq.heappush(remaining, cur-dis)
#         heapq.heappush(remaining, y)
#         before = x
