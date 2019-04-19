# continue

x = 10
while x:
    x = x - 1                   # 또는 x -= 1
    if x % 2 != 0: continue     # 홀수는 건너뜀
    print(x, end=' ')


x = 10
while x:
    x = x - 1
    if x % 2 == 0:              # 짝수인 경우 출력
        print(x, end=' ')
