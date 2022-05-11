# import math

# n = int(input())
# in_lst = list(map(int, input().split()))
# search_set = set(in_lst)
# ans = 0

# for i in range(n):
#     for j in range(i+1, n):
#         tgt = math.sqrt(in_lst[i]**2 + in_lst[j]**2)
#         if tgt in search_set:
#             ans = max(ans, in_lst[i] + in_lst[j] + tgt)
# print(int(ans))

n = int(input())
in_lst = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            len_a = in_lst[i] + in_lst[j] + in_lst[k]
            max_a = max(in_lst[i], in_lst[j], in_lst[k]) 
            rest = len_a - max_a
            if max_a < rest:
                ans = max(ans, len_a)
print(ans)
