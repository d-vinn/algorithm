V = int(input())
who = input()
A = 0
B = 0

for i in range(V):
    if who[i]=="A":
        A += 1
    else:
        B += 1
        
if A > B:
    print("A")
elif A < B:
    print("B")
else:
    print("Tie")