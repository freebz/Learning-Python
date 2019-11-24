# Public 선언도 혀용하도록 일반화하기

"""
파일 access2.py(3.X + 2.X)
Private과 Public 속성 선언을 가진 클래스 데코레이터

인스턴스에 저장되었거나 또는 그 인스턴스가 자신의 클래스로부터 상속받은 속성에 대하여
외부로부터의 접근을 제어함. Private은 데코레이트된 클래스 외부에서 가져올 수도 할당할 수도 없는
속성 이름을 선언하고 Public은 이 모든 것이 가능한 이름을 선언함

경고: 이는 3.X에서 명시적으로 지정된 속성에 대해서만 동작함
내장 연산을 위해 암묵적으로 실행되는 __X__ 연산자 오버로딩 메서드는 새 형식 클래스에서
__getattr__ 또는 __getattribute__ 모두 동작시키지 않음. 여기에서 내장을 가로채고 위임하기 위해
__X__ 메서드를 추가함
"""

traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance:
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


from access2 import Private, Public

@Private('age')                     # Person = Private('age')(Person)
class Person:                       # Person = 상태 정보를 잦는 onInstance
    def __init__(self, name, age):
        self.name = name
        self.age = age              # 내부에서의 접근은 정상적으로 동작

X = Person('Bob', 40)
X.name                              # 외부에서의 접근은 검증됨
# 'Bob'
X.name = 'Sue'
X.name
# 'Sue'
X.age
# TypeError: private attribute fetch: age
X.age = 'Tom'
# TypeError: private attribute change: age

@Public('name')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

X = Person('bob', 40)               # X는 onInstance
X.name                              # onInstance는 Person을 내장시킴
# 'bob'
X.name = 'Sue'
X.name
# 'Sue'
X.age
# TypeError: private attribute fetch: age
X.age = 'Tom'
# TypeError: private attribute change: age
