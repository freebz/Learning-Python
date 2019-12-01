# 클래스 생성 호출을 메타클래스로 오버로딩하기

# 클래스도 호출을 잡아냄(하지만 내장된 동작은 슈퍼클래스가 아니라 메타클래스를 조사함)

class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):
        print('In SuperMeta.call: ', classname, supers, classdict, sep='\n...')
        return type.__call__(meta,classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In SuperMeta init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))

print('making metaclass')
class SubMeta(type, metaclass=SuperMeta):
    def __new__(meta, classname, supers, classdict):
        print('In SubMeta.new: ', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In SubMeta init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))

class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass=SubMeta):    # SuperMeta.__call__을 통해 SubMeta 호출
    data = 1
    def meth(self, arg):
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))


# py -3 metaclass5.py 
# making metaclass
# In SuperMeta init:
# ...SubMeta
# ...(<class 'type'>,)
# ...{'__module__': '__main__', '__qualname__': 'SubMeta', '__new__': <function SubMeta.__new__ at 0x7f7e5494b950>, '__init__': <function SubMeta.__init__ at 0x7f7e5494b9d8>}
# ...init class object: ['__module__', '__new__', '__init__', '__doc__']
# making class
# In SuperMeta.call: 
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meth': <function Spam.meth at 0x7f7e5494ba60>}
# In SubMeta.new: 
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meth': <function Spam.meth at 0x7f7e5494ba60>}
# In SubMeta init:
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meth': <function Spam.meth at 0x7f7e5494ba60>}
# ...init class object: ['__module__', 'data', 'meth', '__doc__']
# making instance
# data: 1 3


class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):     # 내장된 동작이 아니라 이름으로
        print('In SuperMeta.call:', classname)
        return type.__call__(meta, classname, supers, classdict)

class SubMeta(SuperMeta):                                 # 타입에 의해 생성됨
    def __init__(Class, classname, supers, classdict):    # type.__init__ 오버라이드
        print('In SubMeta init:', classname)

print(SubMeta.__class__)
print([n.__name__ for n in SubMeta.__mro__])
print()
print(SubMeta.__call__)                     # 이름으로 발견된다면 데이터 디스크립터가 아님
print()
SubMeta.__call__(SubMeta, 'xxx', (), {})    # 명시적 호출은 동작: 클래스 상속
print()
SubMeta('yyy', (), {})                      # 그러나 암묵적 내장된 동작은 동작하지 않음: 타입

# py -3 metaclass5b.py
# <class 'type'>
# ['SubMeta', 'SuperMeta', 'type', 'object']

# <function SuperMeta.__call__ at 0x7f198c41c620>

# In SuperMeta.call: xxx
# In SubMeta init: xxx

# In SubMeta init: yyy
