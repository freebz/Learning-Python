# 존재하지 않는 키: if 테스트

D = {'a': 1, 'b': 2, 'c': 3}
D
# {'a': 1, 'b': 2, 'c': 3}

D['e'] = 99                     # 새 키 할당으로 딕셔너리 크기 증가
D
# {'a': 1, 'b': 2, 'c': 3, 'e': 99}

D['f']                          # 존재하지 않는 키 참조는 오류
# ...오류 메시지 생략...
# KeyError: 'f'


'f' in D
# False

if not 'f' in D:                # 파이썬의 단복 선택 구문
    print('missing')

# missing


if not 'f' in D:
    print('missing')
    print('no, really...')      # 들여쓰기된 구문 블록

# missing
# no, really...


value = D.get('x', 0)           # 기본값을 가지고 인덱스
value
# 0
value = D['x'] if 'x' in D else 0 # if/else 표현 형식
# 0
