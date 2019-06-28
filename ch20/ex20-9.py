# 제너레이터 표현식: 반복 객체와 컴프리헨션의 만남

[x ** 2 for x in range(4)]      # 리스트 컴프리헨션: 리스트 생성
# [0, 1, 4, 9]

(x ** 2 for x in range(4))      # 제너레이터 표현식: 반복 객체 생성
# <generator object <genexpr> at 0x7f60689b9ba0>


list(x ** 2 for x in range(4))  # 리스트 컴프리헨션과 같음
# [0, 1, 4, 9]


G = (x ** 2 for x in range(4))
iter(G) is G                    # iter(G) 호출은 옵션: __iter__는 자신을 반환함
# True
next(G)                         # 제너레이터 객체: 자동으로 호출되는 메서드
# 0
next(G)
# 1
next(G)
# 4
next(G)
# 9
next(G)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

G
# <generator object <genexpr> at 0x7f60689b9ba0>


for num in (x ** 2 for x in range(4)): # 자동으로 next() 호출
    print('%s, %s' % (num, num / 2.0))

# 0, 0.0
# 1, 0.5
# 4, 2.0
# 9, 4.5


''.join(x.upper() for x in 'aaa,bbb,ccc'.split(','))
# 'AAABBBCCC'

a, b, c = (x + '\n' for x in 'aaa,bbb,ccc'.split(','))
a, c
# ('aaa\n', 'ccc\n')


sum(x ** 2 for x in range(4))   # 선택적인 괄호
# 14
sorted(x ** 2 for x in range(4)) # 선택적인 괄호
# [0, 1, 4, 9]
sorted((x ** 2 for x in range(4)), reverse=True) # 필수적인 괄호
# [9, 4, 1, 0]
