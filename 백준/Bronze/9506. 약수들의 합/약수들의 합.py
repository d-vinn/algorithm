import sys
input = sys.stdin.readline

while True:
    A = int(input())

    if A == -1:
        break ##-1 입력되면 그만

    lis = [] ##약수 리스트

    for i in range(1, A):
        if A % i == 0:
            lis.append(i)
        ## 1부터 A-1까지 수들이 A를 나눌 수 있으면 i를 lis에 집어넣기

    if sum(lis) == A:
        # print(A, "=", " + ".join(str(i) for i in list), sep="")
        temp = " + ".join(str(i) for i in lis)
        print(A, "=", temp)
    else:
        print(A, "is NOT perfect.")


