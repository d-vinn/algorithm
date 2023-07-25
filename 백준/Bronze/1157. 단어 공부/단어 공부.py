S = input()
S = S.upper()
# alist = [chr(i) for i in range(ord('A'), ord('Z')+1)]
blist = [0 for i in range(ord('A'), ord('Z')+1)]

max = 0
index = 0

for i in S:
    blist[ord(i)-ord('A')] += 1
    if blist[ord(i)-ord('A')] > max:
        max = blist[ord(i)-ord('A')]
        index = ord(i)-ord('A')

check = 0

for i in range(len(blist)):
    if blist[i] == max:
        check += 1

if check > 1:
    print("?")
else:
    print(chr(index+ord('A')))




