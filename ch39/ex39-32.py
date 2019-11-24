# 경고: 암묵적으로 실행되는 연산자 오버로딩 메서드는 3.X에서 위임을 할 수 없음

# py -2
from access2 import Private
@Private('age')
class Person:
    def __init__(self):
        self.age = 42
    def __str__(self):
        return 'Person: ' + str(self.age)
    def __add__(self, yrs):
        self.age += yrs

X = Person()
X.age                               # 이름 검증이 제대로 실패함
# TypeError: private attribute fetch: age
print(X)                            # __getattr__ => Person.__str__ 실행
# Person: 42
X + 10                              # __getattr__ => Person.__add__ 실행
print(X)                            # __getattr__ => Person.__str__ 실행
# Person: 52


# py -3
from access2 import Private
@Private('age')
class Person:
    def __init__(self):
        self.age = 42
    def __str__(self):
        return 'Person: ' + str(self.age)
    def __add__(self, yrs):
        self.age += yrs

X = Person()                        # 이름 검증이 여전히 동작함
X.age                               # 하지만 3.X 내장을 위임하는 데에는 실패!
# TypeError: private attribute fetch: age
print(X)
# <access2.accessControl.<locals>.onDecorator.<locals>.onInstance object at 0x7ffab0dfcf28>
X + 10
# TypeError: unsupported operand type(s) for +: 'onInstance' and 'int'
print(X)
# <access2.accessControl.<locals>.onDecorator.<locals>.onInstance object at 0x7ffab0dfcf28>


X.__add__(10)                   # 비록 이름에 의한 호출이 정상적으로 동작하지만,
X._onInstance__wrapped.age      # 결과를 보기 위해 프라이버시가 훼손됨
# 52
