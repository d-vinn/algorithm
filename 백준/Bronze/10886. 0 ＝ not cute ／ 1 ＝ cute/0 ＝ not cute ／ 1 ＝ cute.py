N = int(input())
sum = 0

for i in range(N):
    a = int(input())
    sum += a

if sum > (N//2):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")