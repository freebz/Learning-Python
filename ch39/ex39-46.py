"""
access.py 파일(3.X + 2.X)
Private과 Public 속성 선언을 가진 클래스 데코레이터
인스턴스에 저장된 또는 이를 어떤 방식으로든 인스턴스의 클래스로부터 상속된 속성에 대한 외부 접근을 제어함

Private은 데코레이트된 클래스 외부에서 가져오거나 할당할 수 없는 속성 이름을 선언하며,
Public은 이것이 가능한 속성 이름을 선언함

경고: 3.X에서는 BuiltinMixins에만 코딩된 내장을 잡아냄(확장해 보자)
코딩된 대로 Public은 연산자 오버로딩을 위해 Private보다 덜 유용함
"""
from access_builtins import BuiltinsMixin         # 부분 집합임!

traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):
    def onDecorator(aClass):
        if not __debug__:
            return aClass
        else:
            class onInstance(BuiltinsMixin):
                def __init__(self, *args, **kargs):
                    self.__wrapped = aClass(*args, **kargs)

                def __getattr__(self, attr):
                    trace('get:', attr)
                    if failIf(attr):
                        raise TypeError('private attribute fetch: ' + attr)
                    else:
                        return getattr(self.__wrapped, attr)

                def __setattr__(self, attr, value):
                    trace('set:', attr, value)
                    if attr == '_onInstance__wrapped':
                        self.__dict__[attr] = value
                    elif failIf(attr):
                        raise TypeError('private attribute change: ' + attr)
                    else:
                        setattr(self.__wrapped, attr, value)
            return onInstance
    return onDecorator

def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))


"""
파일 access_builtins.py(from access2_builtins2b.py)
일부 내장 연산을 프록시 클래스의 __getattr__에 전달하여,
3.X에서도 직접적인 이름 호출과 2.X의 기본 고전 클래스처럼 동일하게 동작하도록 함
이를 요구대로 프록시된 객체가 사용하는 다른 __X__이름들을 포함하도록 확장해 보자
"""

class BuiltinsMixin:
    def reroute(self, attr, *args, **kargs):
        return self.__class__.__getattr__(self, attr)(*args, **kargs)

    def __add__(self, other):
        return self.reroute('__add__', other)
    def __str__(self):
        return self.reroute('__str__')
    def __getitem__(self, index):
        return self.reroute('__getitem__', index)
    def __call__(self, *args, **kargs):
        return self.reroute('__call__', *args, **kargs)

    # 3.X에서만 래퍼 객체에 의해 사용되는 다른 내용들 추가


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


# py -3 access-test.py 
# ---------------------------------------------------
# Bob
# Sue
# Sue: 50
# private attribute fetch: age
# private attribute change: age
# ---------------------------------------------------
# bob
# sue
# sue: 50
# private attribute fetch: age
# private attribute change: age

# py -3 -O access-test.py               # 네 개의 접근 에러 메시지는 생략함
