from collections import defaultdict

def solved():
    s = t = 0
    res = p + 1

    m_cnt = defaultdict(int)
    S = len(set(matters))

    for _ in range(p):
        while t < p and len(m_cnt) < S:
            m_cnt[matters[t]] += 1
            t += 1

        if len(m_cnt) < S:
            break
        
        res = min(res, t-s)
        m_cnt[matters[s]] -= 1

        if m_cnt[matters[s]] == 0:
            del m_cnt[matters[s]]
        s += 1

    return res


p = int(input())
matters = list(map(int, input().split()))

print(solved())

