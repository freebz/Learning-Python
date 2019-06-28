# 제너레이터 표현식 vs 맵

list(map(abs, (-1, -2, 3, 4)))              # 튜플에 함수 적용
# [1, 2, 3, 4]
list(abs(x) for x in (-1, -2, 3, 4))        # 제너레이터 표현식
# [1, 2, 3, 4]
list(map(lambda x: x * 2, (1, 2, 3, 4)))    # 함수가 아닌 경우
# [2, 4, 6, 8]
list(x * 2 for x in (1, 2, 3, 4))           # 제너레이터가 더 단순한가?
# [2, 4, 6, 8]


line = 'aaa,bbb,ccc'
''.join([x.upper() for x in line.split(',')]) # 무의미한 리스트 생성
# 'AAABBBCCC'

''.join(x.upper() for x in line.split(','))   # 반복 상황을 이용한 결과 생성
# 'AAABBBCCC'
''.join(map(str.upper, line.split(',')))      # 반복 상황을 이용한 결과 생성
# 'AAABBBCCC'

''.join(x * 2 for x in line.split(','))       # 제너레이터가 더 단순한가?
# 'aaaaaabbbbbbcccccc'
''.join(map(lambda x: x * 2, line.split(',')))
# 'aaaaaabbbbbbcccccc'


[x * 2 for x in [abs(x) for x in (-1, -2, 3, 4)]]        # 중첩된 컴프리헨션
# [2, 4, 6, 8]

list(map(lambda x: x * 2, map(abs, (-1, -2, 3, 4))))     # 중첩된 map
# [2, 4, 6, 8]

list(x * 2 for x in (abs(x) for x in (-1, -2, 3, 4)))    # 중첩된 제너레이터
# [2, 4, 6, 8]


import math
list(map(math.sqrt, (x ** 2 for x in range(4))))       # 중첩된 조합
# [0.0, 1.0, 2.0, 3.0]


list(map(abs, map(abs, map(abs, (-1, 0, 1)))))         # 잘못된 중첩?
# [1, 0, 1]
list(abs(x) for x in (abs(x) for x in (abs(x) for x in (-1, 0, 1))))
# [1, 0, 1]


list(abs(x) * 2 for x in (-1, -2, 3, 4))     # 중첩되지 않은 방법
# [2, 4, 6, 8]
list(math.sqrt(x ** 2) for x in range(4))    # 단층 구조가 종종 더 나음
# [0.0, 1.0, 2.0, 3.0]
list(abs(x) for x in (-1, 0, 1))
# [1, 0, 1]
