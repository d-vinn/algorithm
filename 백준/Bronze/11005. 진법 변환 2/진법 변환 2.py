N, B = map(int, input().split())
i = 0
while True:
    if B**i>N:
        break
    else:
        i += 1

for j in range(i-1, -1, -1):
    if N // (B**j) > 9:
        print(chr((N//(B**j)) + 55), end = '')
    else:
        print(N // (B ** j), end='')
    N = N % (B**j)
