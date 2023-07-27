alist = []

for i in range(5):
    alist.append(input())

j = 0
i = 0

while j < 15:
    try:
        print(alist[i][j], end = '')
        i += 1
    except:
        if i>4:
            i = 0
            j += 1
        else:
            i += 1


