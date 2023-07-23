N, M = map(int, input().split())

a = []

for i in range(N):
    a.append(i+1)

for l in range(M):
    i, j = map(int, input().split())
    if j - i == 0:
        continue
    elif (j-i) % 2 == 1:
        while j > i:
            a[j-1], a[i-1] = a[i-1], a[j-1]
            j -= 1
            i += 1
    else:
        while j > i+1:
            a[j-1], a[i-1] = a[i-1], a[j-1]
            j -= 1
            i += 1

for i in range(len(a)):
    print(a[i], end = ' ')

