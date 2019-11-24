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
