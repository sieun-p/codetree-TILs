N, M = map(int,input().split())
a_loc = [0]
b_loc = [0]

for _ in range(N):
    d, t = input().split()
    if d == 'L':
        for _ in range(int(t)):
            a_loc.append(a_loc[-1]-1)
    else:
        for _ in range(int(t)):
            a_loc.append(a_loc[-1]+1)

for _ in range(M):
    d, t = input().split()
    if d == 'L':
        for _ in range(int(t)):
            b_loc.append(b_loc[-1]-1)
    else:
        for _ in range(int(t)):
            b_loc.append(b_loc[-1]+1)

del a_loc[0]
del b_loc[0]

ans = 0

for i,(a,b) in enumerate (zip(a_loc, b_loc)):
    if a==b:
        print(i+1)
        ans = 1
        break
if ans==0:
    print(-1)
