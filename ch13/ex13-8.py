# 루프 else에 대한 자세한 내용

found = False
while x and not found:
    if match(x[0]):             # 가장 앞에 있는 값?
        print('Ni')
        found = True
    else:
        x = x[1:]               # 가장 앞에 있는 값을 잘라내고 반복
if not found:
    print('not found')


while x:                        # x가 비어 있을 때 종료
    if match(x[0]):
        print('Ni')
        break                   # 종료. else 다음으로 이동
    x = x[1:]
else:
    print('Not found')          # x가 바닥날 때만 여기로 진입
