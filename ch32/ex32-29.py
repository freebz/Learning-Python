# 데코레이터와 메타클래스: 파트 1

# 함수 데코레이터의 기본

class C:
    @staticmethod               # 함수 데코레이션 구문
    def meth():
        ...


class C:
    def meth():
        ...
    meth = staticmethod(meth)   # 이름을 재결합하는 것과 동일


class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances +1

    @staticmethod
    def printNumInstances():
        print("Number of instances created: %s" % Spam.numInstances)

from spam_static_deco import Spam
a = Spam()
b = Spam()
c = Spam()
Spam.printNumInstances()        # 클래스와 인스턴스로부터 호출이 모두 가능함
# Number of instances created: 3
a.printNumInstances()
# Number of instances created: 3


# bothmethods_decorators.py 파일

class Methods(object):          # 2.X에서 프로퍼티 설정을 위해 object 필요
    def imeth(self, x):         # 일반 인스턴스 메서드: self를 전달
        print([self, x])

    @staticmethod
    def smeth(x):               # 정적 메서드: 인스턴스가 전달되지 않음
        print([x])

    @classmethod
    def cmeth(cls, x):          # 클래스 메서드: 인스턴스가 아닌 클래스를 받음
        print([cls, x])

    @property                   # 프로퍼티: 가져오는 시점에 연산
    def name(self):
        return 'Bob ' + self.__class__.__name__

from bothmethods_decorators import Methods
obj = Methods()
obj.imeth(1)
# [<bothmethods_decorators.Methods object at 0x7f0ef0f4bc50>, 1]
obj.smeth(2)
# [2]
obj.cmeth(3)
# [<class 'bothmethods_decorators.Methods'>, 3]
obj.name
# 'Bob Methods'
