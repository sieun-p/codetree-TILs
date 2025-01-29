N, M, K = map(int,input().split())
N_list = [0]*(N+1)
ans = -1

for _ in range(M):
    student_num = int(input())
    N_list[student_num] += 1
    if N_list[student_num] >= K:
        ans = student_num
        break


print(ans)
