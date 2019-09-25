# 정적 메서드의 대안

def printNumInstances():
    print("Number of instances created: %s" % Spam.numInstances)

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

# py -3
import spam
a = spam.Spam()
b = spam.Spam()
c = spam.Spam()
spam.printNumInstances()            # 하지만 함수는 극단적으로 제거될 수 있음
# Number of instances created: 3    # 그리고 상속에 의해 변경될 수 없음
spam.Spam.numInstances
# 3


class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1
    def printNumInstances(self):
        print("Number of instances created: %s" % Spam.numInstances)


# py -3
from spam import Spam
a, b, c = Spam(), Spam(), Spam()
a.printNumInstances()
# Number of instances created: 3
Spam.printNumInstances(a)
# Number of instances created: 3
Spam().printNumInstances()      # 하지만 카운터를 가져오는 것은 카운터를 변경시킴!
# Number of instances created: 4
