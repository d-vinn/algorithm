a = []
for i in range(10):
    a.append(int(input()))
count = 0
b = []

for i in range(42):
    b.append(0)

for i in range(10):
    b[a[i] % 42] += 1
    if b[a[i] % 42] == 2:
        b[a[i] % 42] -= 1

print(sum(b))
