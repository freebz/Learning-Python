# 메타클래스와 클래스 데코레이터는 동일한가?

# 데코레이터는 메타클래스를 호출할 수 있으나, type() 없이는 메타클래스가 데코레이터를 호출할 수 없음

class Metaclass(type):
    def __new__(meta, clsname, supers, attrdict):
        print('In M.__new__:')
        print([clsname, supers, list(attrdict.keys())])
        return type.__new__(meta, clsname, supers, attrdict)

def decorator(cls):
    return Metaclass(cls.__name__, cls.__bases__, dict(cls.__dict__))

class A:
    x = 1

@decorator
class B(A):
    y = 2
    def m(self): return self.x + self.y

# In M.__new__:
# ['B', (<class '__main__.A'>,), ['__module__', 'y', 'm', '__doc__']]
B.x, B.y
# (1, 2)
I = B()
I.x, I.y, I.m()
# (1, 2, 3)


class B(A, metaclass=Metaclass): ...    # 동일 결과, 하지만 하나의 클래스만 생성


def Metaclass(clsname, supers, attrdict):
    return decorator(type(clsname, supers, attrdict))

def decorator(cls): ...
class B(A, metaclass=Metaclass): ...    # 역으로 메타클래스는 데코레이터를 호출할 수 있음


def func(name, supers, attrs):
    return 'spam'

class C(metaclass=func):        # 메타클래스가 클래스를 문자열로 만듦!
    attr = 'huh?'

C, C.upper()
# ('spam', 'SPAM')

def func(cls):
    return 'spam'

@func
class C:                        # 데코레이터가 클래스를 문자열로 만듦!
    attr = 'huh?'

C, C.upper()
# ('spam', 'SPAM')
