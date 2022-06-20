def subsequence(n, s, lst):
    part_sum = [0]*(n+1)
    for i in range(1, n+1):
        part_sum[i] = part_sum[i-1] + lst[i-1]
    
    for i in range(1, n):
        for j in range(i, n+1):
            if part_sum[j] - part_sum[j-i] >= s:
                return i
    return 0

if __name__ == '__main__':
    n = int(input())
    s = int(input())
    lst = list(map(int, input().split()))
    print(subsequence(n, s, lst))


# Sample code
# import bisect

# def solved():
#     for i in range(1, n+1):
#         sum_a[i] = sum_a[i-1] + a[i-1]
    
#     if sum_a[n] < S:
#         print(0)
#         return
    
#     res = n
#     s = 0
#     while sum_a[s] + S <= sum_a[n]:
#         t = bisect.bisect_left(sum_a, sum_a[s]+S)
#         res = min(res, t-s)
#         s += 1
#     print(res)
#     return

# def solved2():
#     res = n + 1
#     s = t = sum = 0
#     for i in range(n):
#         while t < n and sum < S:
#             sum += a[t]
#             t += 1
#         if sum < S:
#             break
#         res = min(res, t-s)
#         sum -= a[s]
#         s += 1
#     if res > n:
#         res = 0
    # print(res)

# n = int(input())
# S = int(input())
# a = list(map(int, input().split()))
# sum_a = [0]*(n+1)

# solved()

