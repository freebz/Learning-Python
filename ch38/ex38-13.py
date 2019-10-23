# 프로퍼티와 디스크립터의 연관 관계

class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel              # 바인드되지 않은 메서드 저장
        self.__doc__ = doc            # 혹은 다른 호출 가능 객체

    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("can't get attribute")
        return self.fget(instance)    # 프로퍼티 엑세서에서 slef에 instance를 전달

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)

class Person:
    def getName(self): print('getName...')
    def setName(self, value): print('setName...')
    name = Property(getName, setName)    # property()처럼 사용

x = Person()
x.name
x.name = 'Bob'
del x.name


# py -3 prop-desc-equiv.py
# getName...
# setName...
# AttributeError: can't delete attribute
