from collections import defaultdict
import sys

sys.setrecursionlimit(1 << 30)

def part_sum(lst, k, i):
    if k in memo[i]:
        return memo[i][k]

    if i == 0:
        return k == 0
    
    memo[i-1][k] = part_sum(lst, k, i-1)
    if memo[i-1][k]:
        return True
    
    memo[i-1][k-lst[i-1]] = part_sum(lst, k-lst[i-1], i-1)
    if memo[i-1][k-lst[i-1]]:
        return True
    
    return False

n = int(input())
in_lst = [int(i) for i in input().split()]
k = int(input())

memo = [defaultdict(int) for _ in range(n+1)]

if part_sum(in_lst, k, n):
    print('Yes')
else:
    print('No')


# Sample function
# def part_num_all(lst, k, i):
#     if i < 0:
#         return k == 0
    
#     if part_num_all(lst, k, i-1):
#         return True
    
#     if part_num_all(lst, k-lst[i], i-1):
#         return True
    
#     return False
# print(part_num_all(in_lst, k, n-1))
