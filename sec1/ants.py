l = int(input())
n = int(input())
in_lst = [int(i) for i in input().split()]

min_ans, max_ans = 0, 0
for i in range(n):
    tgt_min = min(in_lst[i], l - in_lst[i])
    min_ans = max(min_ans, tgt_min)
    tgt_max = max(in_lst[i], l - in_lst[i])
    max_ans = max(max_ans, tgt_max)

print('min =', min_ans)
print('max =', max_ans)
