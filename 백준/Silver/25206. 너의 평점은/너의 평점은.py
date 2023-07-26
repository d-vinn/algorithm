sum_h = 0 ##학점의 총합
sum_p = 0 ##학점*평점의 총합

p = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0}

for i in range(20):
    S = input()
    if S[len(S)-1] == "P":
        continue
    elif S[len(S)-1] == "F":
        sum_h += int(S[len(S)-5])
    else:
        sum_h += int(S[len(S)-6])
        S_p = S[len(S)-2:]
        sum_p += p[S_p]*int(S[len(S)-6])

print(sum_p/sum_h)
