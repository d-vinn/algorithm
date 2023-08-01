money = [25, 10, 5, 1]
T = int(input())
for i in range(T):
    N = int(input())
    for j in range(4):
        print(N // money[j], end=' ')
        N = N%money[j]
    print()