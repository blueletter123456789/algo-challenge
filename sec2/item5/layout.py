INF = 10**8

n, ml, md = map(int, input().split())
al, bl, dl = [0]*ml, [0]*ml, [0]*ml
ad, bd, dd = [0]*md, [0]*md, [0]*md

for i in range(ml):
    al[i], bl[i], dl[i] = map(int, input().split())
for i in range(md):
    ad[i], bd[i], dd[i] = map(int, input().split())

def bellman_ford():
    for k in range(n+1):
        updated = False
        for i in range(n-1):
            if dist[i+1] < INF:
                if dist[i] > dist[i+1]:
                    dist[i] = dist[i+1]
                    updated = True
        for i in range(ml):
            if dist[al[i]-1] < INF:
                if dist[bl[i]-1] > dist[al[i]-1]+dl[i]:
                    dist[bl[i]-1] = dist[al[i]-1]+dl[i]
                    updated = True
        for i in range(md):
            if dist[bd[i]-1] < INF:
                if dist[ad[i]-1] > dist[bd[i]-1]-dd[i]:
                    dist[ad[i]-1] = dist[bd[i]-1]-dd[i]
                    updated = True

dist = [0]*n
updated = False
bellman_ford()
if updated:
    print(-1)

dist = [INF]*n
dist[0] = 0
bellman_ford()
if dist[n-1] == INF:
    print(-2)
else:
    print(dist[n-1])

