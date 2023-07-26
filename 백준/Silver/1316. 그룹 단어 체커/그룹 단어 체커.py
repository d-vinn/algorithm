N = int(input())
sum = 0

for i in range(N):
    S = input()
    k = 0
    alist = [0 for i in range(ord("A"), ord("Z")+1)]
    for j in range(len(S)):
        if ((ord(S[j])-ord("a")) != (ord(S[j-1])-ord("a"))) and (alist[(ord(S[j])-ord("a"))] != 0):
            k = 1
        else:
            alist[(ord(S[j]) - ord("a"))] += 1
    if k == 0:
        sum += 1

print(sum)
