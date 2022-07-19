class BIT(object):
    def __init__(self, n):
        self.lst = [0]*(n+2)
        self.n = n+1
    
    def sum(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.lst[i]
            i -= (i & -i)
        return s
    
    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.lst[i] += x
            i += (i & -i)
    
    def part(self, i, j):
        return self.sum(j) - self.sum(i-1)


def solved():
    ans = 0
    bt = BIT(n)
    
    for j in range(n):
        ans += j - bt.sum(A[j])
        bt.add(A[j], 1)
    
    return ans



if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))

    print(solved())
