from types import FunctionType
from decotools import tracer, timer

def decorateAll(decorator):
    def DecoDecorate(aClass):
        for attr, attrval in aClass.__dict__.items():
            if type(attrval) is FunctionType:
                setattr(aClass, attr, decorator(attrval))    # __dict__가 아님
        return aClass
    return DecoDecorate

@decorateAll(timer(label='@@'))         # 클래스 데코레이터 사용
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


# 만약 타이머를 사용한다면: 메서드당 총 소요 시간 출력

print('-'*40)
print('%.5f' % Person.__init__.alltime)
print('%.5f' % Person.giveRaise.alltime)
print('%.5f' % Person.lastName.alltime)
