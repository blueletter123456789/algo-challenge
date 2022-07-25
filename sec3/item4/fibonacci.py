M = 10**4

def multi(a, b):
    res = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += (a[i][k] * b[k][j]) % M
                res[i][j] %= M
    return res

def power(a, r):
    p = a.copy()
    ans = None
    for i in range(35):
        if r & (1 << i):
            if ans is None:
                ans = p
            else:
                ans = multi(ans, p)
        p = multi(p, p)
    return ans

def solved():
    a = [[1, 1], [1, 0]]

    ans = power(a, n-1)

    return sum(ans[1]) % M

# Smaple code
# M = 10**4


# def mul(A, B):
#     C = [[0]*len(B) for _ in range(len(A))]
#     for i in range(len(A)):
#         for k in range(len(B)):
#             # 列数分
#             for j in range(len(B[0])):
#                 C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % M
    
#     return C


# def pow(A, n):
#     B = [[0]*len(A) for _ in range(len(A))]
#     for i in range(len(A)):
#         B[i][i] = 1

#     while n > 0:
#         if n & 1:
#             B = mul(B, A)
#         A = mul(A, A)
#         n >>= 1
    
#     return B

# def solved():

#     A = [[1, 1], [1, 0]]

#     A = pow(A, n)

#     # a0: 0, a1: 1のため
#     return A[1][0]


if __name__ == '__main__':
    n = int(input())

    print(solved())
