# T = int(input())
# for i in range(T):
#     a, b = map(int, input().split())
#     for j in range(max(a, b), a*b+1):
#         if i%a == 0 and i%b == 0:
#             print(i)
#             break

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    A, B = max(a, b), min(a,b)
    
    while B!=0:
        A = A % B
        A, B = B, A
        
    print(a*b//A)