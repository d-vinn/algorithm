A = 100
B = 100

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        B -= a
    elif b > a:
        A -= b

print(A)
print(B)