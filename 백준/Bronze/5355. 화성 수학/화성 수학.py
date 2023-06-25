T = int(input())
for i in range(T):
  list = input().split()
  tn = float(list[0])
  for j in range(1, len(list)):
    if list[j]=="@":
      tn *= 3
    elif list[j]=="%":
      tn += 5
    else:
      tn -= 7
  print("%.2f"%tn)
