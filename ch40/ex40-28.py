# 어떤 데코레이터라도 메서드에 적용하기

# 메타클래스 팩토리: 클래스의 모든 메서드에 어떤 데코레이터라도 적용

from types import FunctionType
from decotools import tracer, timer

def decorateAll(decorator):
    class MetaDecorate(type):
        def __new__(meta, classname, supers, classdict):
            for attr, attrval in classdict.items():
                if type(attrval) is FunctionType:
                    classdict[attr] = decorator(attrval)
            return type.__new__(meta, classname, supers, classdict)
    return MetaDecorate

class Person(metaclass=decorateAll(tracer)):    # 데코레이터를 모든 메서드에 적용
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
print('%2.f' % sue.pay)
print(bob.lastName(), sue.lastName())


# py -3 decoall-meta-any.py 
# call 1 to __init__
# call 2 to __init__
# Bob Smith Sue Jones
# call 1 to giveRaise
# 110000
# call 1 to lastName
# call 2 to lastName
# Smith Jones


class Person(metaclass=decorateAll(tracer)):               # 추적 데코레이터 적용

class Person(metaclass=decorateAll(timer())):              # 타이머를 기본 인수로 적용
class Person(metaclass=decorateAll(timer(label='**'))):    # 데코레이터 인수 사용


# 만약 타이머를 사용하면: 메서드당 총 소요 시간 출력
print('-'*40)
print('%.5f' % Person.__init__.alltime)
print('%.5f' % Person.giveRaise.alltime)
print('%.5f' % Person.lastName.alltime)


# py -3 decoall-meta-any2.py 
# **__init__: 0.00001, 0.00001
# **__init__: 0.00000, 0.00001
# Bob Smith Sue Jones
# **giveRaise: 0.00002, 0.00002
# 110000
# **lastName: 0.00002, 0.00002
# **lastName: 0.00002, 0.00004
# Smith Jones
# ----------------------------------------
# 0.00001
# 0.00002
# 0.00004
