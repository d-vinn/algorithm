N = int(input())
xlist = []
ylist = []
for i in range(N):
    a, b = map(int, input().split())
    xlist.append(a)
    ylist.append(b)
print((max(xlist)-min(xlist))*(max(ylist)-min(ylist)))