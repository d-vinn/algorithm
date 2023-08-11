n = int(input())
sum = 0
for i in range(1, n-1):
    sum += (n-i)*(n-i-1)
sum = sum//2

print(sum)
print(3)