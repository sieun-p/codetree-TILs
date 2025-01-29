N, M = map(int,input().split())
dist_a = [0]
dist_b = [0]
for _ in range(N):
    v, t = map(int,input().split())
    for _ in range(t):
        dist_a.append(v+dist_a[-1])
for _ in range(M):
    v, t = map(int,input().split())
    for _ in range(t):
        dist_b.append(v+dist_b[-1])

del dist_a[0]
del dist_b[0]
c = []

for a,b in zip(dist_a,dist_b):
    if a>=b:
        c.append(0)
    else:
        c.append(1)

cnt = 0
for i in range(1,len(c)):
    if c[i-1]!=c[i]:
        cnt+=1
print(cnt)

