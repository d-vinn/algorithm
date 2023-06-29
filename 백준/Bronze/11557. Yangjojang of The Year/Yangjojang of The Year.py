T = int(input())
for i in range(T):
    N = int(input())
    max = 0
    for j in range(N):
        S, L = input().split()
        if int(L) > max:
            max = int(L)
            s = S
    print(s)
        