# 제너레이터와 함수의 활용

def f(a, b, c): print('%s, %s, and %s' % (a, b, c))

f(0, 1, 2)                      # 일반적인 위치 인수
# 0, 1, and 2
f(*range(3))                    # range 값을 풀어냄. 3.X에서 반복 객체
# 0, 1, and 2
f(*(i for i in range(3)))       # 제너레이터 표현식 값을 풀어냄
# 0, 1, and 2


D = dict(a='Bob', b='dev', c=40.5); D
# {'a': 'Bob', 'b': 'dev', 'c': 40.5}
f(a='Bob', b='dev', c=40.5)     # 일반적인 키워드
# Bob, dev, and 40.5
f(**D)                          # 딕셔너리 풀어내기: 키 = 값
# Bob, dev, and 40.5
f(*D)                           # 키 반복자 풀어내기
# a, b, and c
f(*D.values())                  # 뷰 반복자 풀어내기: 3.X에서 반복 객체
# Bob, dev, and 40.5


for x in 'spam': print(x.upper(), end= ' ')
# S P A M

list(print(x.upper(), end=' ') for x in 'spam')
# S P A M [None, None, None, None]

print(*(x.upper() for x in 'spam'))
# S P A M
