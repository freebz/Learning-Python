# 클래스 데코레이터 팩토리: 어떤 데코레이터도 클래스의 모든 메서드에 적용

from types import FunctionType
from decotools import tracer, timer

def decorateAll(decorator):
    def DecoDecorate(aClass):
        for attr, attrval in aClass.__dict__.items():
            if type(attrval) is FunctionType:
                setattr(aClass, attr, decorator(attrval))    # __dict__가 아님
        return aClass
    return DecoDecorate

@decorateAll(tracer)                    # 클래스 데코레이터 사용
class Person:                           # 함수 데코레이터를 메서드에 적용
    def __init__(self, name, pay):      # Person = decorateAll(...)(Person)
        self.name = name                # Person = DecoDecorate(Person)
        self.pay  = pay
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
