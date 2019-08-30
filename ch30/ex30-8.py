# 반복 객체: __iter__와 __next__

# 사용자 정의 반복 객체

# squares.py 파일

class Squares:
    def __init__(self, start, stop):    # 생성될 때 상태 정보 저장
        self.value = start - 1
        self.stop = stop
    def __iter__(self):                 # iter 호출 시, 반복자 객체 가져오기
        return self
    def __next__(self):                 # 매 반복 때마다 제곱값 반환
        if self.value == self.stop:     # 또한 내장된 next에 의해 호출됨
            raise StopIteration
        self.value += 1
        return self.value ** 2


# python
from squares import Squares
for i in Squares(1, 5):         # __iter__를 호출함 iter를 호출
    print(i, end=' ')           # 매 반복 시, __next__호출

# 1 4 9 16 25


X = Squares(1, 5)               # 직접 반복: 루프가 하는 일
I = iter(X)                     # iter는 __iter__를 호출
next(I)                         # next는 __next__를 호출(3.X의 경우)
# 1
next(I)
# 4
# ...생략...
next(I)
# 25
next(I)                         # try문에서 이를 잡아냄
# StopIteration


X = Squares(1, 5)
X[1]
# TypeError: 'Squares' object does not support indexing
list(X)[1]
# 4
