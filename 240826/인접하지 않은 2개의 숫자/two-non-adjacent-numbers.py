n = int(input())
n_list = list(map(int,input().split()))
take = []
for i in range(n-2):
    for j in range(i+2,n):
        take.append(n_list[i]+n_list[j])

print(max(take))