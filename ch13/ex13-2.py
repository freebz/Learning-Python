# 예제

while True:
    print('Type Ctrl+C to stop me!')


x = 'spam'
while x:                        # x가 비어 있지 않은 동안
    print(x, end=' ')           # 2.X에서는 print x
    x = x[1:]                   # x의 첫 번째 문자 제거

# spam pam am m


a = 0; b = 10
while a < b:                    # 카운터 루프를 작성하는 한 방법
    print(a, end=' ')
    a += 1                      # 또는 a = a + 1

# 0 1 2 3 4 5 6 7 8 9


while True:
    ...루프 본문...
    if exitTest(): break
