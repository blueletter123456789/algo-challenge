# n = int(input())
# cut_cost = list(map(int, input().split()))
# cut_cost.sort()
# ans = 0
# cost = cut_cost[0]
# for i in range(1, n):
#     cost += cut_cost[i]
#     ans += cost
# print(ans)

n = int(input())
L = list(map(int, input().split()))

ans = 0
while n > 1:
    mil1, mil2 = 0, 1
    if L[mil1] > L[mil2]:
        mil1, mil2 = mil2, mil1
    for i in range(2, n):
        if L[i] < L[mil1]:
            mil2 = mil1
            mil1 = i
        elif L[i] < L[mil2]:
            mil2 = i
    t = L[mil1] + L[mil2]
    ans += t
    if mil1 == n-1:
        mil1, mil2 = mil2, mil1
    L[mil1] = t
    L[mil2] = L[n-1]
    n -= 1
print(ans)
