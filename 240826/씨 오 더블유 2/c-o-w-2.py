N = int(input())
string = list(str(input()))
cnt = 0
for i in range(len(string)-2):
    if string[i]=='C':
        for j in range(i,len(string)-1):
            if string[j]=='O':
                for k in range(j,len(string)):
                    if string[k]=='W':
                        cnt+=1

print(cnt)