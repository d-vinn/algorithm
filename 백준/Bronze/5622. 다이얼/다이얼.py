S = input()
sum = 0

for i in S:
    if ord(i)-ord('A')<15:
        sum += (((ord(i)-ord('A'))//3) + 3)
    elif ord(i)-ord('A')<19:
        sum += 8
    elif ord(i)-ord('A')<22:
        sum += 9
    else:
        sum += 10

print(sum)
