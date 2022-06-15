# Sample code
def solved(q, lst):
    total = len(lst)
    dp = [[0]*total for _ in range(q+1)]
    
    # 開放する対象の幅
    for width in range(2, total):
        # 区間の左端
        for left in range(total-width):
            # 区間の右端
            right = left + width
            # 必要な金貨
            t = 10**5

            # 区間内で開放する囚人の最小を探索
            for tgt in range(left+1, right):
                t = min(t, dp[left][tgt] + dp[tgt][right])
            
            dp[left][right] = t + lst[right] - lst[left] - 2
    return dp[0][q+1]

if __name__ == '__main__':
    p = int(input())
    q = int(input())
    lst = [0]*(q+2)
    for i, num in enumerate(map(int, input().split())):
        lst[i+1] = num
    lst[q+1] = p+1
    print(solved(q, lst))


# import bisect

# def bin_search(n, lst):
#     if len(lst) <= 1:
#         return n-len(lst)
#     res = n-1
#     m = n // 2
#     idx = bisect.bisect(lst, m)-1
#     tgt = lst[idx]
#     res += bin_search(tgt-1, lst[:idx])
#     res += bin_search(n-tgt, lst[idx+1:])
#     return res

# if __name__ == '__main__':
#     p = int(input())
#     q = int(input())
#     lst = list(map(int, input().split()))

#     print(bin_search(p, lst))
