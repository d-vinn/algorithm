alist = []

for i in range(ord('a'), ord('z')+1):
    alist.append(-1)

S = input()

for i in range(len(S)):
    if alist[ord(S[i])-ord('a')] == -1:
        alist[ord(S[i]) - ord('a')] = i

for i in alist:
    print(i, end = ' ')