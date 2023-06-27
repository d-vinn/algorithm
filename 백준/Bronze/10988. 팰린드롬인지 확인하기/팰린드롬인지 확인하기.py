word = input() ##입력받고
flag = True


for i in range(len(word) // 2): ##i의 범위는 0부터 문자열 나누기 2의 몫까지
    if word[i] != word[len(word) - 1 - i]:
        flag = False
        break

if flag:
    print(1)
else:
    print(0)