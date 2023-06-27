N = int(input())
money = []

for i in range(N):
    a, b, c = map(int, input().split())
    if a==b==c:
        money.append(10000+a*1000)
    elif a!=b and a!=c and b!=c:
        money.append(max(a, b, c)*100)
    else:
        if a==b:
            money.append(1000+a*100)
        elif a==c:
            money.append(1000+a*100)
        else:
            money.append(1000+b*100)
            
print(max(money))
        