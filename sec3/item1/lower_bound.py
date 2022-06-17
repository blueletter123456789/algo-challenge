import bisect
import random

def lower_bound(lst, x, l=-1, r=-1):
    if r == -1:
        r = len(lst)
    while r - l > 1:
        m = (l + r) // 2
        if lst[m] >= x:
            r = m
        else:
            l = m
    return r

if __name__ == '__main__':
    n = int(input())
    # lst = list(map(int, input().split()))
    lst = [random.randint(0, 100) for i in range(n-3)]
    k = int(input())
    lst += [k]*3
    lst.sort()
    
    print(lst)
    print(lower_bound(lst, k))
    print(bisect.bisect_left(lst, k))
