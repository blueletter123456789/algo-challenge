M = 10007

def mul(A, B):
    C = [[0]*len(B) for _ in range(len(A))]
    for i in range(len(A)):
        for k in range(len(B)):
            for j in range(len(B[0])):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % M
    
    return C


def pow(A, n):
    B = [[0]*len(A) for _ in range(len(A))]
    for i in range(len(A)):
        B[i][i] = 1

    while n > 0:
        if n & 1:
            B = mul(B, A)
        A = mul(A, A)
        n >>= 1
    
    return B


def solved():
    B = [[0]*(n*2) for _ in range(n*2)]
    for i in range(n):
        for j in range(n):
            B[i][j] = A[i][j]
        B[n+i][n+i], B[n+i][i] = 1, 1
    B = pow(B, k+1)

    ans = list()
    for i in range(n):
        row = list()
        for j in range(n):
            a = B[n+i][j] % M
            # Iを引く
            if i == j:
                a = (a + M - 1) % M
            row.append(a)
        ans.append(row)
    return ans


# 全探索
# def solved():
#     ans = [[0]*n for _ in range(n)]
#     for i in range(k):
#         ans = sum_matrix(ans, pow(A, i+1))
#     return ans


# def sum_matrix(a, b):
#     ret = [[0]*n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             ret[i][j] = a[i][j] + b[i][j]
#             ret[i][j] %= M
#     return ret

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    M = int(input())
    A = list()
    for _ in range(n):
        A.append(list(map(int, input().split())))
    
    print(solved())

