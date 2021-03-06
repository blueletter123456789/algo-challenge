n = int(input())

ans = True
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        ans = False
        # print(i, n // i)
        break

if ans:
    print('Yes')
else:
    print('No')


# Sample code
# from collections import defaultdict

# def is_prime(n):
#     """
#     素数判定(O(√N))
#     """
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i += 1
#     return n != 1

# def divisor(n):
#     """
#     約数列挙(O√N)
#     """
#     res = list()
#     i = 1
#     while i * i <= n:
#         if n % i == 0:
#             res.append(i)
#             if i != n//i:
#                 res.append(n//i)
#         i += 1
#     return res

# def prime_factor(n):
#     res = defaultdict(int)
#     i = 2
#     while i * i <= n:
#         while n % i == 0:
#             res[i] += 1
#             n //= i
#         i += 1
#     if n != 1:
#         res[n] = 1
#     return res

# if __name__ == '__main__':
#     n = int(input())
#     print('is_prime: ', is_prime(n))
#     print('divisor: ', sorted(divisor(n)))
#     print('prime_factor: ', prime_factor(n))