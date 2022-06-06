def extgcd(a, b):
    d = a
    if b != 0:
        d, y, x = extgcd(b, a%b)
        y -= (a // b) * x
    else:
        x, y = 1, 0
    return d, x, y

a, b = map(int, input().split())
d, x, y = extgcd(a, b)
if d == 1:
    ans = [0]*4
    if x > 0:
        ans[0] = x
    else:
        ans[2] = -x
    if y > 0:
        ans[1] = y
    else:
        ans[3] = -y
    print(*ans)
else:
    print(-1)
