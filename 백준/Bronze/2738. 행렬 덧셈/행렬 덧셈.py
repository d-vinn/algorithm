N, M = map(int, input().split())
A = []
B = []
for i in range(N):
    S = list(map(int, input().split()))
    A.append(S)

for i in range(N):
    S = list(map(int, input().split()))
    B.append(S)

C = []

for i in range(N):
    for j in range(M):
        print(A[i][j]+B[i][j], end = ' ')
    print()