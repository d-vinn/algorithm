N = int(input())
for i in range(N):
    M, T = input().split()
    for j in T:
        print(j*int(M), end = '')
    print()