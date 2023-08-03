N, K = map(int, input().split())
alist = []
for i in range(N):
    if N % (i+1) == 0:
        alist.append(i+1)

if len(alist) >= K:
    print(alist[K - 1])
else:
    print(0)