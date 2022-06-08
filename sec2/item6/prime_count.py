n = int(input())

factors = {1}
for i in range(2, int(n**0.5)+1):
    if i in factors:
        continue
    for j in range(i*2, n+1, i):
        factors.add(j)

print(n - len(factors))
# print(factors)

# Sample code
# def sieve(n):
#     prime = list()
#     is_prime = [True]*(n+1)
#     is_prime[0], is_prime[1] = False, False
#     for i in range(2, n+1):
#         if is_prime[i]:
#             prime.append(i)
#             for j in range(2*i, n+1, i):
#                 is_prime[j] = False
#     return len(prime)

# print(sieve(n))
