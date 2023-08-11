N = int(input())
iss = 1
for i in range(N):
    alist=[]
    tmp = i
    while True:
        alist.append(i%10)
        i = i//10
        if i == 0:
            break
    if sum(alist)+tmp == N:
        iss = 0
        print(tmp)
        break
if iss == 1:
    print(0)