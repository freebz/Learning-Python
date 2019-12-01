# 메타클래스와 데코레이터로 추적하기

# 추적 데코레이터를 클라이언트 클래스의 모든 메서드에 추가하는 메타클래스

from types import FunctionType
from decotools import tracer

class MetaTrace(type):
    def __new__(meta, classname, supers, classdict):
        for attr, attrval in classdict.items():
            if type(attrval) is FunctionType:                      # 메서드?
                classdict[attr] = tracer(attrval)                  # 데코레이션할 것
        return type.__new__(meta, classname, supers, classdict)    # 클래스 생성

class Person(metaclass=MetaTrace):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    def lastName(self):
        return self.name.split()[-1]

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print('%.2f' % sue.pay)
print(bob.lastName(), sue.lastName())


# py -3 decoall-meta.py
# call 1 to __init__
# call 2 to __init__
# Bob Smith Sue Jones
# call 1 to giveRaise
# 110000.00
# call 1 to lastName
# call 2 to lastName
# Smith Jones
