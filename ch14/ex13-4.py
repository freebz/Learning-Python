# 전체 반복 프로토콜

L = [1, 2, 3]
I = iter(L)                     # 반복 객체로부터 반복자 객체 얻기
I.__next__()                    # 다음 아이템으로 나아가기 위해 반복자의 next 호출
# 1
I.__next__()                    # 또는 2.X에서 I.next(), 두 버전 모두에서 next(I) 호출
# 2
I.__next__()
# 3
I.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration


f = open('script2.py')
iter(f) is f
# True
iter(f) is f.__iter__()
# True
f.__next__()
# 'import sys\n'


L = [1, 2, 3]
iter(L) is L
# False
L.__next__()
# AttributeError: 'list' object has no attribute '__next__'

I = iter(L)
I.__next__()
# 1
next(I)                         # I.__next__()와 같음
# 2
