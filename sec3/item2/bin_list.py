def sec_lst(sup):
    res = list()

    sub = (sup - 1) & sup

    while sub != sup:
        res.append(sub)
        sub = (sub - 1) & sup
    return sorted(res)

def comb_lst(n, k):
    res = list()
    comb = (1 << k) - 1
    while comb < (1 << n):
        res.append(comb)
        # 最下位の１を取り出す
        x = comb & -comb
        # １が連続する最下位の箇所から繰り上がりを取り出す
        y = comb + x
        # comb & ~y: １が連続する最下位の箇所
        comb = ((comb & ~y) // x >> 1) | y
    return res


if __name__ == '__main__':
    n = int(input())

    sec = sec_lst(n)
    for i in sec:
        print(bin(i)[2:].zfill(n))
    
    print('=================')
    
    comb = comb_lst(5, 2)
    for i in comb:
        print(bin(i)[2:].zfill(5))

