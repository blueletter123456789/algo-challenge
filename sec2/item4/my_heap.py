class Heap(object):
    def __init__(self, ini_size=1):
        self.heap = [None]*ini_size
        self.size = 0
    
    def push(self, x):
        if self.size == len(self.heap):
            self.heap.append(None)
        
        # 最後のノードから親を比較していく
        i = self.size
        self.size += 1
        while i > 0:
            p = (i - 1) // 2
            if self.heap[p] <= x:
                break
            self.heap[i] = self.heap[p]
            i = p
        self.heap[i] = x
    
    def pop(self):
        if self.heap[0] is None:
            raise ValueError('heap size is zero')

        ret = self.heap[0]

        # 最後のノードの値を取得してルートから比較していく
        x = self.heap[self.size-1]
        self.size -= 1
        i = 0
        while (i*2 + 1) < self.size:
            a, b = i*2+1, i*2+2
            if b < self.size and self.heap[b] < self.heap[a]:
                a = b
            if self.heap[a] >= x:
                break
            self.heap[i] = self.heap[a]
            i = a
        self.heap[i] = x
        self.heap[self.size] = None
        return ret

if __name__ == '__main__':
    import time
    print('my heap')
    h = Heap()
    h.push(8)
    h.push(1)
    h.push(4)
    h.push(9)
    h.push(7)
    print(h.heap)
    h.pop()
    h.push(3)
    h.pop()
    print(h.heap)

    print('heapq')
    import heapq
    lst = list()
    heapq.heappush(lst, 8)
    heapq.heappush(lst, 1)
    heapq.heappush(lst, 4)
    heapq.heappush(lst, 9)
    heapq.heappush(lst, 7)
    print(lst)
    heapq.heappop(lst)
    heapq.heappush(lst, 3)
    heapq.heappop(lst)
    print(lst)
