# Sample code
def solved(n):
    res = 0
    lst = [0]*n
    for i in range(n):
        lst[i] = -1
        input_row = input()
        for idx, s in enumerate(input_row):
            if s == '1':
                lst[i] = idx
    
    for i in range(n):
        pos = -1
        # 初めに対象となる値を見つけて、
        # 対象のインデックスから未定の値を逆順に並べる
        for j in range(i, n):
            if lst[j] <= i:
                pos = j
                break
        j = pos
        while i < j:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            res += 1
            j -= 1
    
    return res

if __name__ == '__main__':
    n = int(input())
    print(solved(n))


# def bubble_sort_cnt(lst):
#     len_lst = len(lst)
#     swapped = 0
#     for i in range(len_lst):
#         for j in range(n-1, i, -1):
#             if lst[j] < lst[j-1] and j+1 > lst[j]:
#                 lst[j], lst[j-1] = lst[j-1], lst[j]
#                 swapped += 1
#     return swapped

# n = int(input())
# lst = [n]*n

# for i in range(n):
#     row = list(input())
#     for j, val in enumerate(row[::-1]):
#         if val == '1':
#             lst[i] = n-j
#             break

# print(bubble_sort_cnt(lst))