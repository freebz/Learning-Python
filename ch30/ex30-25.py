# 제자리 덧셈

class Number:
    def __init__(self, val):
        self.val = val
    def __iadd__(self, other):    # 명시적으로 __iadd__: x += y
        self.val += other         # 일반적으로 self를 반환
        return self

x = Number(5)
x += 1
x += 1
x.val
# 7


y = Number([1])                 # 직접 변경이 +보다 빠름
y += [2]
y += [3]
y.val
# [1, 2, 3]


class Number:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):              # __add__ 폴백: x = (x + y)
        return Number(self.val + other)    # 클래스 타입 전파

x = Number(5)
x += 1
x += 1                                     # 그리고 +=는 연결을 수행
x.val
# 7
