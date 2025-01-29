N = int(input())
n = map(int,input().split())

n_list = list(n)
n_list.sort()
sum_list = []

while len(n_list)!=0:
    sum_list.append(n_list[0]+n_list[-1])
    del(n_list[0])
    del(n_list[-1])

print(max(sum_list))