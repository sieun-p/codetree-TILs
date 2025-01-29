# MAX_iter = 100000
# n, m = map(int,input().split())
# loc_a = [0]*(MAX_iter+1)
# loc_b = [0]*(MAX_iter+1)

# time_a = 1
# for _ in range(n):
#     t, d = tuple(input().split())
#     for _ in range(int(t)):
#         if d=='R': loc_a[time_a] = loc_a[time_a-1]+1
#         else: loc_a[time_a] = loc_a[time_a-1]-1
#         time_a += 1
# time_b = 1
# for _ in range(m):
#     t, d = tuple(input().split())
#     for _ in range(int(t)):
#         if d=='R': loc_b[time_b] = loc_b[time_b-1]+1
#         else: loc_b[time_b] = loc_b[time_b-1]-1
#         time_b += 1

# cnt = 0
# loc_ab = 0
# for a,b in zip(loc_a, loc_b):
#     if a==b and a!=loc_ab:
#         cnt+=1
#         loc_ab = a
# print(cnt-1)

n,m = map(int,input().split())
loc_a = [0]
loc_b = [0]

for _ in range(n):
    t, d = tuple(input().split())
    for _ in range(int(t)):
        if d == 'R': loc_a.append(loc_a[-1]+1)
        else: loc_a.append(loc_a[-1]-1)
for _ in range(m):
    t, d =tuple(input().split())
    for _ in range(int(t)):
        if d == 'R': loc_b.append(loc_b[-1]+1)
        else: loc_b.append(loc_b[-1]-1)

del loc_a[0]
del loc_b[0]
cnt = 0
loc_ab = 0
for a,b in zip(loc_a, loc_b):
    if a==b and a!=loc_ab:
        cnt += 1
        loc_ab = a

print(cnt)