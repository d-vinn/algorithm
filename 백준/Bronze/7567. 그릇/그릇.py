plate = input()
sum = 10
for i in range(len(plate)-1):
    if plate[i+1]!=plate[i]:
        sum += 10
    else:
        sum += 5
        
print(sum)