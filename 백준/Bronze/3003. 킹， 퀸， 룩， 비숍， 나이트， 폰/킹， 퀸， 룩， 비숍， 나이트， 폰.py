alist = [1, 1, 2, 2, 2, 8]
blist = list(map(int, input().split()))

for i in range(6):
    print(alist[i]-blist[i], end = ' ')
