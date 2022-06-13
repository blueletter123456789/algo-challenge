n = int(input())
v1 = list(map(int, input().split()))
v2 = list(map(int, input().split()))

v1.sort()
v2.sort(reverse=True)

ans = 0
for x, y in zip(v1, v2):
    ans += x*y

print(ans)
