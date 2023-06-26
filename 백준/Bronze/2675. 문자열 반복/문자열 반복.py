T = int(input())
for i in range(T):
    R, S = input().split()
    S = list(S)
    for j in range(len(S)):
        print(S[j]*int(R), end="")
    print('')

