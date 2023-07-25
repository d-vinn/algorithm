S = input()
sum = 0

for i in S:
    if i==' ':
        sum += 1

if S[0]==' ':
    sum -= 1

if S[len(S)-1]==' ':
    sum -= 1

print(sum+1)