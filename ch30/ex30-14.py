# yield를 이용한 다중 반복자

# python
from squares_yield import Squares # __iter__/yield Squares 사용
S = Squares(1, 5)
I = iter(S)
next(I); next(I)
# 1
# 4
J = iter(S)                     # yield를 사용하면, 다중 반복자는 자동
next(J)
# 1
next(I)
# 9


S = Squares(1, 3)
for i in S:                     # 각각의 for는 __iter__를 호출함
    for j in S:
        print('%s:%s' % (i, j), end=' ')

# 1:1 1:4 1:9 4:1 4:4 4:9 9:1 9:4 9:9


# squares_nonyield.py 파일

class Squares:
    def __init__(self, start, stop): # yield가 없는 제너레이터
        self.start = start           # 다중 스캔: 추가 객체 필요
        self.stop = stop
    def __iter__(self):
        return SquaresIter(self.start, self.stop)

class SquaresIter:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


# python
from squares_nonyield import Squares
for i in Squares(1, 5): print(i, end=' ')

# 1 4 9 16 25

S = Squares(1, 5)
I = iter(S)
next(I); next(I)
# 1
# 4
J = iter(S)                     # yield 없는 다중 반복자
next(J)
# 1
next(I)
# 9

S = Squares(1, 3)
for i in S:                     # 각각의 for는 __iter__를 호출
    for j in S:
        print('%s:%s' % (i, j), end=' ')

# 1:1 1:4 1:9 4:1 4:4 4:9 9:1 9:4 9:9


# skipper_yield.py 파일

class SkipObject:                       # 또 다른 __iter__ + yield 제너레이터
    def __init__(self, wrapped):        # 일반적으로 인스턴스 범위에 기록됨
        self.wrapped = wrapped          # 지역 범위 상태는 자동으로 저장됨
    def __iter__(self):
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset += 2
            yield item


# python
from skipper_yield import SkipObject
skipper = SkipObject('abcdef')
I = iter(skipper)
next(I); next(I); next(I)
# 'a'
# 'c'
# 'e'
for x in skipper:               # 각 for는 __iter__를 호출: 새로운 자동 제너레이터
    for y in skipper:
        print(x + y, end=' ')

# aa ac ae ca cc ce ea ec ee
