n = int(input())
s = input()

t = ''
i, j = 0, n-1
while i <= j:
    if s[i] < s[j]:
        t += s[i]
        i += 1
    elif s[i] > s[j]:
        t += s[j]
        j -= 1
    else:
        si, sj = i, j
        while s[si] == s[j]:
            si += 1
        while s[i] == s[sj]:
            sj -= 1
        if s[si] < s[sj]:
            t += s[i]
            i += 1
        else:
            t += s[j]
            j -= 1

print(t)

# Sample source code
# n = int(input())
# s = input()

# t = ''
# a, b = 0, n-1
# while a <= b:
#     left = False
#     i = 0
#     while a+i <= b:
#         if s[a+i] < s[b-i]:
#             left = True
#             break
#         elif s[a+i] > s[b-i]:
#             left = False
#             break
#         i += 1
#     if left:
#         t += s[a]
#         a += 1
#     else:
#         t += s[b]
#         b -= 1

# print(t)
