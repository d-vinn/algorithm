N = int(input())
n = 2*N-1
m = n//2
for i in range(n):
    if i <= (n//2):
        print(' ' * m, end='')
        print('*' * (2*i+1))
    else:
        print(' ' * abs(m), end='')
        print('*' * (2*(n-i)-1))
    m -= 1
