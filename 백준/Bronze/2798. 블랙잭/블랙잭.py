N , M = map(int, input().split())
alist = list(map(int, input().split()))
max = float("inf")
result = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and j != k and i != k:
                sum = alist[i] + alist[j] + alist[k]
                if abs(sum-M) < max and sum <= M:
                    max = abs(sum-M)
                    result = sum

print(result)

