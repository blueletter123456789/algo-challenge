import bisect
import math


B = 1000

def solved():
    # MAX_N = 10**5
    # nums = [0]*MAX_N
    nums = [0]*n
    # buckets = [list()]*(MAX_N//B)
    buckets = [list()]*math.ceil(n/B)
    
    for i in range(n):
        buckets[i//B].append(A[i])
        nums[i] = A[i]
    nums.sort()
    for i in range(math.ceil(n/B)):
        buckets[i].sort()
    
    for i in range(m):
        # [l, r)のk番目を求める
        l, r, k = I[i], J[i], K[i]
        lb, ub = -1, n-1
        while ub - lb > 1:
            md = (lb + ub) // 2
            x = nums[md]
            tl, tr, c = l, r, 0

            # バケットをはみ出す部分
            while tl < tr and tl % B:
                if A[tl] <= x:
                    c += 1
                tl += 1
            
            while tl < tr and tr % B:
                if A[tr] <= x:
                    c += 1
                tr -= 1
            
            while tl < tr:
                b = tl // B
                c += bisect.bisect(buckets[b], x)
                tl += B
            
            if c >= k:
                ub = md
            else:
                lb = md
        print(nums[ub-1])


if __name__ == '__main__':
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    I, J, K = [0]*m, [0]*m, [0]*m
    for i in range(m):
        I[i], J[i], K[i] = map(int, input().split())
    
    solved()
