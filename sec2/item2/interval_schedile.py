n = int(input())
schedules = [(s, t) for s, t in 
    zip(list(map(int, input().split())), 
    list(map(int, input().split())))]

schedules.sort(key=lambda x: x[1])
ans = 1
ps, pt = schedules[0]

for i in range(1, n):
    s, t = schedules[i]
    if s > pt:
        ans += 1
        pt = t

print(ans)
