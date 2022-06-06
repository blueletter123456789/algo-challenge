x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

if x1 == x2 and y1 == y2:
    print(0)
else:
    print(gcd(abs(x1-x2), abs(y1-y2))-1)
