# import bisect

# a, b = map(int, input().split())

# def sieve(n):
#     prime = list()
#     is_prime = [True]*(n+1)
#     is_prime[0], is_prime[1] = False, False
#     for i in range(2, n+1):
#         if is_prime[i]:
#             prime.append(i)
#             for j in range(2*i, n+1, i):
#                 is_prime[j] = False
#     return prime

# primes = sieve(b)
# idx_l = bisect.bisect_left(primes, a)
# idx_r = bisect.bisect_left(primes, b)
# print(idx_r-idx_l)

# Sample code
MAX_L = 10 ** 6
MAX_SQRT_B = 10 ** 6

is_prime = [True] * MAX_L
is_prime_small = [True] * MAX_SQRT_B

def segment_sieve(a, b):
    i = 0
    while i * i < b:
        is_prime_small[i] = True
        i += 1
    for i in range(b-a):
        is_prime[i] = True

    i = 2
    while i * i < b:
        if is_prime_small[i]:
            j = 2 * i
            while j * j < b:
                is_prime_small[j] = False
                j += i
            for j in range(max(2, (a+i-1)//i)*i, b, i):
                is_prime[j-a] = False
        i += 1

a, b = map(int, input().split())

segment_sieve(a, b)
ans = sum(is_prime[:b - a])
print(ans)
