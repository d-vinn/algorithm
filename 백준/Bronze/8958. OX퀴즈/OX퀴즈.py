N = int(input())

for i in range(N):
    score = 0
    sum = 0
    A = input()
    for j in range(len(A)):
        if A[j]=="O":
            sum += 1
            score += sum
        else:
            sum = 0
    print(score)
            