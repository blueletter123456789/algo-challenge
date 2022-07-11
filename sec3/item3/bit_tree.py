class BIT(object):
    # [1, n]
    def __init__(self, n):
        # [0, a1, a2 ... an]までの区間を管理
        self.lst = [0]*(n+2)
        # 0を初期に入れているためn+1
        self.n = n+1
    
    def sum(self, i):
        # 1からlist[i-1]までの和
        s = 0
        i += 1
        while i > 0:
            s += self.lst[i]
            i -= (i & -i)
        return s
    
    def add(self, i, x):
        # list[i]に加算
        i += 1
        while i <= self.n:
            self.lst[i] += x
            i += (i & -i)
    
    def part(self, i, j):
        # [i, j]の区間和
        return self.sum(j) - self.sum(i-1)

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7]
    bit_tree = BIT(len(lst))
    for i, val in enumerate(lst):
        bit_tree.add(i, val)
    
    print(bit_tree.sum(3))
    print(bit_tree.sum(5))

    print(bit_tree.part(3, 4))
