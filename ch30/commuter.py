# -*- coding: utf-8 -*-
#!python
from __future__ import print_function    # 2.X/3.X 호환성
# ...클래스들은 여기에 정의됨...

class Commuter1:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val

class Commuter2:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    def __radd__(self, other):
        return self.__add__(other)      # __add__를 명시적으로 호출

class Commuter3:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    def __radd__(self, other):
        return self + other             # 순서를 바꾸어 다시 덧셈

class Commuter4:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    __radd__ = __add__                  # 별칭: 중간 매개자 제거
    
class Commuter5:                              # 결과에 클래스 타입 전파
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        if isinstance(other, Commuter5):      # 객체 중첩을 피하기 위해 타입 캐스팅
            other = other.val
        return Commuter5(self.val + other)    # Else + result는 또 다른 Commuter
    def __radd__(self, other):
        return Commuter5(other + self.val)
    def __str__(self):
        return '<Commuber5: %s>' % self.val


if __name__ == '__main__':
    for klass in (Commuter1, Commuter2, Commuter3, Commuter4, Commuter5):
        print('-' * 60)
        x = klass(88)
        y = klass(99)
        print(x + 1)
        print(1 + y)
        print(x + y)
