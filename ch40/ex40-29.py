# 메타클래스 vs 클래스 데코레이터: 라운드3(최종 라운드)

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


# py -3 decoall-deco-any.py 
# call 1 to __init__
# call 2 to __init__
# Bob Smith Sue Jones
# call 1 to giveRaise
# 110000.00
# call 1 to lastName
# call 2 to lastName
# Smith Jones


@decorateAll(tracer)                    # 모든 메서드를 tracer로 데코레이션

@decorateAll(timer())                   # 모든 메서드를 timer와 기본 인수로 데코레이션
@decorateAll(timer(label='@@'))         # 동일하지만 데코레이터 인수를 전달


# 만약 타이머를 사용한다면: 메서드당 총 소요 시간 출력

print('-'*40)
print('%.5f' % Person.__init__.alltime)
print('%.5f' % Person.giveRaise.alltime)
print('%.5f' % Person.lastName.alltime)


# py -3 decoall-deco-any2.py 
# @@__init__: 0.00001, 0.00001
# @@__init__: 0.00001, 0.00001
# Bob Smith Sue Jones
# @@giveRaise: 0.00002, 0.00002
# 110000.00
# @@lastName: 0.00002, 0.00002
# @@lastName: 0.00002, 0.00004
# Smith Jones
# ----------------------------------------
# 0.00001
# 0.00002
# 0.00004


@decorateAll(tracer(timer(label='@@')))    # timer를 적용하는 것을 추적
class Person:

@decorateAll(tracer)                       # onCall 래퍼를 추적, 메서드의 시간을 측정
@decorateAll(timer(label='@@'))
class Person:

@decorateAll(timer(label='@@'))
@decorateAll(tracer)                       # onCall 래퍼의 시간 측정, 메서드를 추적
class Person:
