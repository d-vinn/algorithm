N = int(input())
alist = [list(0 for i in range(100)) for j in range(100)]
for i in range(N):
    n, m = map(int, input().split())
    
    for j in range(n, n+10):
        for k in range(m, m+10):
            alist[j][k] = 1

sum = 0

for i in alist:
    sum += i.count(1)

print(sum)
