N = int(input())
alist = list(map(int, input().split()))

maxa = max(alist)
sum = 0

for i in alist:
    sum += (i/maxa)*100

print(sum/N)