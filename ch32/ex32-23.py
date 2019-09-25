# 정적 메서드와 클래스 메서드

# 왜 특별한 메서드인가?

# 2.X와 3.X에서의 정적 메서드

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1
    def printNumInstances():
        print("Number of instances created: %s" % Spam.numInstances)


# py -2
from spam import Spam
a = Spam()                      # 2.X에서는 언바운드 클래스 메서드를 호출할 수 없음
b = Spam()                      # 기본적으로 메서드는 self 객체를 기대함
c = Spam()

Spam.printNumInstances()
# TypeError: unbound method printNumInstances() must be called with Spam instance as first argument (got nothing instead)
a.printNumInstances()
# TypeError: printNumInstances() takes no arguments (1 given)


# py -3
from spam import Spam
a = Spam()                      # 3.X에서는 클래스에서 함수를 호출할 수 있음
b = Spam()                      # 인스턴스를 통한 호출은 여전히 self를 전달함
c = Spam()

Spam.printNumInstances()        # 3.X에서는 다름
# Number of instances created: 3
a.printNumInstances()
# TypeError: printNumInstances() takes 0 positional arguments but 1 was given


Spam.printNumInstances()        # 2.X에서는 실패, 3.X에서는 정상 동작
instance.printNumInstances()    # 2.X와 3.X 모두에서 실패(static이 아니라면)
