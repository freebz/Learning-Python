# 또 다른 내장 타입의 반복 객체들

D = {'a':1, 'b':2, 'c':3}
for key in D.keys():
    print(key, D[key])

# a 1
# b 2
# c 3


I = iter(D)
next(I)
# 'a'
next(I)
# 'b'
next(I)
# 'c'
next(I)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration


for key in D:
    print(key, D[key])

# a 1
# b 2
# c 3


import os
P = os.popen('dir')
P.__next__()
# ' Volume in drive C has no label.\n'
P.__next__()
# ' Volume Serial Number is D093-D1F7\n'
next(P)
# TypeError: _wrap_close_object is not an iterator


P = os.popen('dir')
I = iter(P)
next(I)
# ' Volume in drive C has no label.\n'
I.__next__()
# ' Volume Serial Number is D093-D1F7\n'


R = range(5)
R                               # 3.X에서 range는 반복 객체
# range(0, 5)
I = iter(R)                     # 결과를 생성하기 위해 반복 프로토콜 사용
next(I)
# 0
next(I)
# 1
list(range(5))                  # 또는 모든 결과를 한 번에 받기 위해 list 사용
# [0, 1, 2, 3, 4]


E = enumerate('spam')           # enumerate 또한 반복 객체
E
# <enumerate object at 0x7fac2a0ac240>
I = iter(E)
next(I)                         # 반복 프로토콜을 이용하여 결과 생성
# (0, 's')
next(I)                         # 또는 결과를 강제 생성하기 위해 list 사용
# (1, 'p')
list(enumerate('spam'))
# [(0, 's'), (1, 'p'), (2, 'a'), (3, 'm')]
