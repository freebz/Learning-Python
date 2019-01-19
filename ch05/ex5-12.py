# 다른 내장된 수치 도구들

import math
math.pi, math.e                 # 일반적인 상수
# (3.141592653589793, 2.718281828459045)

math.sin(2 * math.pi / 180)     # 사인, 탄젠트, 코사인
# 0.03489949670250097

math.sqrt(144), math.sqrt(2)    # 제곱근
# (12.0, 1.4142135623730951)

pow(2, 4), 2 ** 4, 2.0 ** 4.0   # 지수(거듭제곡)
# (16, 16, 16.0)

abs(-42.0), sum((1, 2, 3, 4))   # 절대값, 합계
# (42.0, 10)

min(3, 1, 2, 4), max(3, 1, 2, 4) # 최솟값, 최대값
# (1, 4)


math.floor(2.567), math.floor(-2.567) # 반내림(낮은 정수)
# (2, -3)

math.trunc(2.567), math.trunc(-2.567) # 버림(소수 자리 버림)
# (2, -2)

int(2.567), int(-2.567)         # 버림(정수 변환)
# (2, -2)

round(2.567), round(2.467), round(2.567, 2) # 반올림(파이썬 3.X 버전)
# (3, 2, 2.57)

'%.1f' % 2.567, '{0:.2f}'.format(2.567) # 출력을 위한 반올림(7장 참고)
# ('2.6', '2.57')


(1 / 3.0), round(1 / 3.0, 2), ('%.2f' % (1 / 3.0))
# (0.3333333333333333, 0.33, '0.33')


import math
math.sqrt(144)                  # 모듈
# 12.0
144 ** .5                       # 표현식
# 12.0
pow(144, .5)                    # 내장된 함수
# 12.0

math.sqrt(1234567890)           # 큰 수
# 35136.41828644462
1234567890 ** .5
# 35136.41828644462
pow(1234567890, .5)
# 35136.41828644462


import random
random.random()
# 0.556014960423105
random.random()                 # 임의 부동 소수점 수, 정수 선택
# 0.051308506597373515
random.randint(1, 10)
# 5
random.randint(1, 10)
# 9


random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life'])
# 'Holy Grail'
random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life'])
# 'Life of Brian'

suits = ['hearts', 'clubs', 'diamonds', 'spades']
random.shuffle(suits)
suits
# ['spades', 'hearts', 'diamonds', 'clubs']
random.shuffle(suits)
['clubs', 'diamonds', 'hearts', 'spades']
