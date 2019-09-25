# 정적 메서드를 이용하여 인스턴스 개수 세기

class Spam:
    numInstances = 0            # 클래스 데이터를 위해 static 메서드 사용
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances():
        print("Number of instances: %s" % Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)


from spam_static import Spam
a = Spam()
b = Spam()
c = Spam()
Spam.printNumInstances()        # 단순한 함수로 호출
# Number of instances: 3
a.printNumInstances()           # 인스턴스 인수가 전달되지 않음
# Number of instances: 3


class Sub(Spam):
    def printNumInstances():    # 정적 메서드 재정의
        print("Extra stuff...") # 하지만 원래 버전을 재호출
        Spam.printNumInstances()
    printNumInstances = staticmethod(printNumInstances)

from spam_static import Spam, Sub
a = Sub()
b = Sub()
a.printNumInstances()           # 서브클래스 인스턴스로부터 호출
# Extra stuff...
# Number of instances: 2
Sub.printNumInstances()         # 서브클래스 자체로부터 호출
# Extra stuff...
# Number of instances: 2
Spam.printNumInstances()        # 원래 버전을 호출
# Number of instances: 2


class Other(Spam): pass         # 말 그대로 정적 메서드를 상속

c = Other()
c.printNumInstances()
# Number of instances: 3
