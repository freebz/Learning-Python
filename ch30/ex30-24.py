# 클래스 타입 전파

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

from commuter import Commuter5
x = Commuter5(88)
y = Commuter5(99)
print(x +10)                    # 결과는 또 다른 Commuter 인스턴스
# <Commuber5: 98>
print(10 + y)
# <Commuber5: 109>

z = x + y                       # 중첩되지 않음: __radd__를 재실행하지 않음
print(z)
# <Commuber5: 187>
print(z + 10)
# <Commuber5: 197>
print(z + z)
# <Commuber5: 374>
print(z + z + 1)
# <Commuber5: 375>


z = x + y                       # 인스턴스 테스트를 주석 처리한 경우
print(z)
# <Commuber5: <Commuber5: 187>>
print(z + 10)
# <Commuber5: <Commuber5: 197>>
print(z + z)
# <Commuber5: <Commuber5: <Commuber5: <Commuber5: 374>>>>
print(z + z + 1)
# <Commuber5: <Commuber5: <Commuber5: <Commuber5: 375>>>>
