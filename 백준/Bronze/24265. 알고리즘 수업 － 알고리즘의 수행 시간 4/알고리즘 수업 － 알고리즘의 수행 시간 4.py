n = int(input())
## j의 반복횟수를 보자면, i가 1에서 n-1까지 증가하는 동안
## j는 n-1번, n-2번, ..., n-6번 반복.
## 즉 n*(n-1) - (n-1)*n/2
print(int(n*(n-1) - (n-1)*n/2))
print(2)