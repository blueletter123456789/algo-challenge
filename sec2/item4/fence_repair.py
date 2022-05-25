import heapq

n = int(input())
lst = list(map(int, input().split()))
heapq.heapify(lst)

ans = 0
while len(lst) > 1:
    mil1 = heapq.heappop(lst)
    mil2 = heapq.heappop(lst)
    t = mil1 + mil2
    ans += t
    heapq.heappush(lst, t)

print(ans)
