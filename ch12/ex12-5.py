# 블록 구분자: 들어쓰기 규칙

x = 1
if x:
    y = 2
    if y:
        print('block2')
    print('block1')
print('block0')


  x = 'SPAM'                    # 에러: 첫 라인이 들여쓰기
if 'rubbery' in 'shrubbery':
    print(x * 9)
        x += 'NI'               # 에러: 예기치 않은 들여쓰기
        if x.endswith('NI'):
                x *= 2
            print(x)            # 에러: 일관성 없는 들여쓰기


x = 'SPAM'
if 'rubbery' in 'shrubbery':
    print(x * 8)                # "SPAM"을 8번 출력
    x += 'NI'
    if x.endswith('NI'):
        x *= 2
        print(x)                # "SPAMNISPAMNI" 출력
