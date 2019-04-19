# 루프 else

x = y // 2                      # y > 1 값
while x > 1:
    if y % x == 0:              # 나머지
        print(y, 'has factor', x)
        break                   # else의 실행을 건너뜀
    x -= 1
else:                           # 일반적인 종료
    print(y, 'is prime')
