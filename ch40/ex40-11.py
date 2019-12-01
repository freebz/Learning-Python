# 클래스 생성 호출을 일반 클래스로 오버로딩

# 일반 클래스도 메타클래스 역할을 할 수 있음

class MetaObj:
    def __call__(self, classname, supers, classdict):
        print('In MetaObj.call: ', classname, supers, classdict, sep='\n...')
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class

    def __New__(self, classname, supers, classdict):
        print('In MetaObj.new: ', classname, supers, classdict, sep='\n...')
        return type(classname, supers, classdict)

    def __Init__(self, Class, classname, supers, classdict):
        print('In MetaObj.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))

class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass=MetaObj()):    # MetaObj는 일반 클래스 인스턴스
    data = 1                              # 문장 마지막에서 호출됨
    def meth(self, arg):
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))


# py -3 metaclass4.py 
# making class
# In MetaObj.call: 
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meth': <function Spam.meth at 0x7fc3d8b11a60>}
# In MetaObj.new: 
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meth': <function Spam.meth at 0x7fc3d8b11a60>}
# In MetaObj.init:
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meth': <function Spam.meth at 0x7fc3d8b11a60>}
# ...init class object: ['__module__', 'data', 'meth', '__doc__']
# making instance
# data: 1 3


# 인스턴스는 클래스와 그 클래스의 슈퍼클래스로부터 일반적으로 상속받음

class SuperMetaObj:
    def __call__(self, classname, supers, classdict):
        print('In SuperMetaObj.call: ', classname, supers, classdict, sep='\n...')
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class

class SubMetaObj(SuperMetaObj):
    def __New__(self, classname, supers, classdict):
        print('In SubMetaObj.new: ', classname, supers, classdict, sep='\n...')
        return type(classname, supers, classdict)

    def __Init__(self, Class, classname, supers, classdict):
        print('In SubMetaObj.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))

class Spam(Eggs, metaclass=SubMetaObj()):      # Super.__call__을 통해 Sub 인스턴스 호출
    ...파일 나머지 부분은 동일함...


# py -3 metaclass4-super.py
# making class
# In SuperMetaObj.call:
# ...이전과 동일...
# In SubMetaObj.new: 
# ...이전과 동일...
# In SubMetaObj.init:
# ...이전과 동일...
# making instance
# data: 1 3
