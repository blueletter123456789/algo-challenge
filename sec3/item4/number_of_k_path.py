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

        G(k1+k2) = Gk1 * Gk2
        Gk = G1^k
    """
    pat = pow(G, k)

    # 各頂点から任意の頂点にパスが存在するため合計
    ans = 0
    for row in pat:
        ans += sum(row)
        ans %= M
    
    return ans

if __name__ == '__main__':
    n = int(input())
    k = int(input())

    G = list()
    for _ in range(n):
        G.append(list(map(int, input().split())))

    print(solved())
