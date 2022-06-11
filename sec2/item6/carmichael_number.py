def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return n != 1

def mod_pow(x, m):
    p = x
    ans = 1
    for i in range(60):
        if m & 1 << i:
            ans *= p
            ans %= m
        p *= p
        p %= m
    return ans

def is_carmichael(n):
    if is_prime(n):
        return False
    
    for i in range(n):
        # if mod_pow(i, n, n) != i % n:
        if mod_pow(i, n) != i % n:
            return False
    return True

# Sample code1
# def mod_pow(x, n, mod):
#     res = 1
#     while n > 0:
#         if n & 1:
#             res = (res * x) % mod
#         x = (x * x) % mod
#         n >>= 1
#     return res

# Sample code2
# def mod_pow(x, n, mod):
#     if n == 0:
#         return 1
#     res = mod_pow((x*x) % mod, n // 2, mod)
#     if n & 1:
#         res = (res * x) % mod
#     return res

if __name__ == '__main__':
    n = int(input())
    if is_carmichael(n):
        print('Yes')
    else:
        print('No')

