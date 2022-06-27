import bisect

def solved():
    CD = [0]*(n**2)
    for i in range(n):
        for j in range(n):
            CD[i*n + j] = C[i] + D[j]
    
    cnt = 0
    CD.sort()
    for i in range(n):
        for j in range(n):
            ab = -(A[i] + B[j])
            idx1 = bisect.bisect_left(CD, ab)
            idx2 = bisect.bisect_right(CD, ab)
            cnt += idx2-idx1
    return cnt

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))

    print(solved())
