table = [list(map(int, input().split())) for _ in range(9)]

maxrow, maxcol, max = 0, 0, -1

for i in range(9):
    for j in range(9):
        if table[i][j] > max:
            max = table[i][j]
            maxrow = i+1
            maxcol = j+1

print(max)
print(maxrow, maxcol)