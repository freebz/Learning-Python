# 딕셔너리를 사용하여 유연한 리스트 흉내 내기: 정수 키

L = []
L[99] = 'spam'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list assignment index out of range


D = {}
D[99] = 'spam'
D[99]
# 'spam'
D
# {99: 'spam'}


table = {1975: 'Holy Grail',
         1979: 'Life of Brian', # 키는 문자열이 아닌 정수
         1973: 'The Meaning of Life'}
table[1975]
# 'Holy Grail'
list(table.items())
# [(1975, 'Holy Grail'), (1979, 'Life of Brian'), (1973, 'The Meaning of Life')]
