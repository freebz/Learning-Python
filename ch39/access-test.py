"""
access-test.py 파일
테스트 코드: 데코레이터 재사용을 할 수 있도록 별도 파일로 저장
"""
import sys
from access import Private, Public

print('---------------------------------------------------')
# 테스트1: private이 아닌 이름은 public

@Private('age')                      # Person = Private('age')(Person)
class Person:                        # Person = onInstance + 상태
    def __init__(self, name, age):
        self.name = name
        self.age = age               # 내부에서의 접근은 정상적으로 동작
    def __add__(self, N):
        self.age += N                # 3.X에서 혼합 클래스에 의해 잡힌 내장
    def __str__(self):
        return '%s: %s' % (self.name, self.age)

X = Person('Bob', 40)
print(X.name)                        # 외부에서의 접근은 검증됨
X.name = 'Sue'
print(X.name)
X + 10
print(X)

try: t = X.age                       # "python -O"가 아니라면 실패
except: print(sys.exc_info()[1])
try: X.age = 999                     # 상동
except: print(sys.exc_info()[1])

print('---------------------------------------------------')
# 테스트 2: public이 아닌 이름은 private
# BuiltinMixin에서 연산자는 private이 아니거나 public이어야만 함

@Public('name', '__add__', '__str__', '__coerce__')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __add__(self, N):
        self.age += N                # 3.X에서 혼합 클래스가 잡아내는 내장
    def __str__(self):
        return '%s: %s' % (self.name, self.age)

X = Person('bob', 40)                # X는 onInstance
print(X.name)                        # onInstance는 Person을 내장시킴
X.name = 'sue'
print(X.name)
X + 10
print(X)

try: t = X.age                       # "python -O"이 아니라면 실패
except: print(sys.exc_info()[1])
try : X.age = 999                    # 상동
except: print(sys.exc_info()[1])
