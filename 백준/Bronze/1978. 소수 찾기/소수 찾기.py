N = int(input())
result = 0
alist = list(map(int, input().split()))
for i in range(N):
    sum = 0
    for j in range(alist[i]):
        if alist[i] % (j+1) == 0:
            sum += 1
    if sum == 2:
        result += 1

print(result)