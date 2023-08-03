M = int(input())
N = int(input())
alist = []
for i in range(M, N+1):
    summ = 0
    for j in range(1, i):
        if i % j == 0:
            summ += 1
    if summ == 1:
        alist.append(i)

if len(alist) == 0:
    print(-1)
else:
    print(sum(alist))
    print(alist[0])