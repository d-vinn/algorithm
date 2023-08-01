N = int(input())
def piv(n):
    if n==1:
        return 2
    else:
        return(piv(n-1)*2 - 1)
print(piv(N+1)**2)

