arr = []
max = 0
index = -1

for i in range(9):
    a = int(input())
    arr.append(a)
    if a > max:
        max = a
        index = i+1

print(max)
print(index)

