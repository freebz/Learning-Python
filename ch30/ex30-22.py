# 오른쪽 기준 연산과 제자리 연산: __radd__와 iadd__

# 오른쪽 기준 덧셈

class Adder:
    def __init__(self, value=0):
        self.data = value
    def __add__(self, other):
        return self.data + other

x = Adder(5)
x + 2
# 7
2 + x
# TypeError: unsupported operand type(s) for +: 'int' and 'Adder'


class Commuter1:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val

from commuter import Commuter1
x = Commuter1(88)
y = Commuter1(99)

x + 1                           # __add__: 인스턴스 + 비인스턴스
# add 88 1
# 89
1 + y                           # __radd__: 비인스턴스 + 인스턴스
# radd 99 1
# 100
x + y                           # __add__: 인스턴스 + 인스턴스, __radd__ 작동
# add 88 <__main__.Commuter1 object at 0x7f351076d710>
# radd 99 88
# 187
