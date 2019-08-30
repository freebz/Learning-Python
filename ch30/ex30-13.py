# 다른 코딩 방식: __iter__ + yield

def gen(x):
    for i in range(x): yield i ** 2

G = gen(5)                      # __iter__와 __next__를 갖는 제너레이터 생성
G.__iter__() == G               # 두 메서드는 동일 객체에 존재
# True
I = iter(G)                     # __iter__ 실행: 제너레이터는 자기 자신을 반환
next(I), next(I)                # __next(2.X에서는 next) 실행
# (0, 1)
list(gen(5))                    # 반복 맥락은 자동으로 iter와 next를 실행
# [0, 1, 4, 9, 16]


# squares_yield.py 파일

class Squares:                          # __iter__ + yield 제너레이터
    def __init__(self, start, stop):    # __next__는 자동으로/암묵적으로 존재
        self.start = start
        self.stop = stop
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2


# python
from squares_yield import Squares
for i in Squares(1, 5): print(i, end=' ')
# 1 4 9 16 25


S = Squares(1, 5)               # __init__ 실행: 클래스는 인스턴스 상태 저장
S
# <squares_yield.Squares object at 0x7fa8ff2c1320>

I = iter(S)                     # __iter__ 실행: 제너레이터 반환
I
# <generator object Squares.__iter__ at 0x7fa8fb98bb48>
next(I)
# 1
next(I)                         # 제너레이터의 __next__ 실행
# 4
# ...등등...
next(I)                         # 제너레이터는 인스턴스와 지역 범위의 상태 모두 가짐
# StopIteration


class Squares:                  # __iter__에 대응하는 것이 없음(squares_manual.py)
    def __init__(...):
        ...
    def gen(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2


# python
from squares_manual import Squares
for i in Squares(1, 5).gen(): print(i, end=' ')
# ...동일한 결과가 표시됨...

S = Squares(1, 5)
I = iter(S.gen())               # 반복 객체와 반복자를 위해 직접 제너레이터를 호출
next(I)
# ...동일한 결과가 표시됨...
