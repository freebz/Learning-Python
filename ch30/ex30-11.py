# 하나의 객체에 대한 다중 반복자

S = 'ace'
for x in S:
    for y in S:
        print(x + y, end=' ')

# aa ac ae ca cc ce ea ec ee


# !python3
# skipper.py 파일

class SkipObject:
    def __init__(self, wrapped):                # 사용될 아이템 저장
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)       # 매회 새로운 반복자

class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped                  # 반복자 상태 정보
        self.offset = 0
    def __next__(self):
        if self.offset >= len(self.wrapped):    # 반복 종료
            raise StopIteration
        else:
            item = self.wrapped[self.offset]    # 아니면 반환하고 하나 누락
            self.offset += 2
            return item

        
if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)         # 컨테이너 객체 생성
    I = iter(skipper)                   # 컨테이너에 대한 반복자 생성
    print(next(I), next(I), next(I))    # 오프셋 0, 2, 4 방문

    for x in skipper:                   # for는 자동으로 __iter__를 호출
        for y in skipper:               # 내부의 for는 __iter__를 매회 다시 호출
            print(x + y, end=' ')       # 각 반복자는 자신만의 상태 정보와 오프셋을 가짐


#!python
from __future__ import print_function   # 2.X/3.X 호환성
...
class SkipIterator:
    ...
    def __next__(self):
        ...
    next = __next__                     # 2.X/3.X 호환성


# python skipper.py
# a c e
# aa ac ae ca cc ce ea ec ee
