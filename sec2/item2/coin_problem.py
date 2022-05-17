coin_set = [1, 5, 10, 50, 100, 500]

coins = list(map(int, input().split()))

ans = 0
for i in range(5, -1, -1):
    t = min(coins[6]//coin_set[i], coins[i])
    coins[6] -= t * coin_set[i]
    ans += t

print(ans)

# c1, c5, c10, c50, c100, c500, a = map(int, input().split())

# ans = 0
# while a > 0:
#     if c500 and 500 <= a:
#         a -= 500
#         c500 -= 1
#     elif c100 and 100 <= a:
#         a -= 100
#         c100 -= 1
#     elif c50 and 50 <= a:
#         a -= 50
#         c50 -= 1
#     elif c10 and 10 <= a:
#         a -= 10
#         c10 -= 1
#     elif c5 and 5 <= a:
#         a -= 5
#         c5 -= 1
#     else:
#         a -= 1
#         c1 -= 1
#     ans += 1

# print(ans)
