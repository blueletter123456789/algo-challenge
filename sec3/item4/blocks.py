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
    """漸化式
        ai: R,G共に偶数
        bi: R,Gどちらか奇数
        ci: R,G共に奇数

        ai+1 = 2*ai + bi
        bi+1 = 2*ai * 2*bi + 2*ci
        ci+1 = bi + 2*ci

        |ai+1|   |2 1 0|   |ai|
        |bi+1| = |2 2 2| * |bi|
        |ci+1|   |0 1 2|   |ci|
    """
    A = [
        [2, 1, 0], 
        [2, 2, 2], 
        [0, 1, 2]
    ]

    ans = pow(A, n)

    return ans[0][0]


if __name__ == '__main__':
    n = int(input())

    print(solved())
