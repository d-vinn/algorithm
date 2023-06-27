N= int(input())
Q1 = Q2 = Q3 = Q4 = AXIS = 0

for i in range(N):
    X, Y = map(int, input().split())
    if X == 0 or Y == 0:
        AXIS += 1
    elif X < 0:
        if Y < 0:
            Q3 += 1
        else:
            Q2 += 1
    elif X > 0:
        if Y < 0:
            Q4 += 1
        else:
            Q1 += 1


print("Q1: %d"%Q1)
print("Q2: %d"%Q2)
print("Q3: %d"%Q3)
print("Q4: %d"%Q4)
print("AXIS: %d"%AXIS)