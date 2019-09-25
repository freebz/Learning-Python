# 클래스 메서드를 이용한 클래스별 인스턴스 개수 세기

class Spam:
    numInstances = 0
    def count(cls):             # 클래스별 인스턴스 카운터
        cls.numInstances += 1   # cls는 인스턴스 위 가장 낮은 클래스
    def __init__(self):
        self.count()            # self.__class__를 count에 전달
    count = classmethod(count)

class Sub(Spam):
    numInstances = 0
    def __init__(self):         # __init__을 재정의
        Spam.__init__(self)

class Other(Spam):              # __init__을 상속
    numInstances = 0

from spam_class2 import Spam, Sub, Other
x = Spam()
y1, y2 = Sub(), Sub()
z1, z2, z3 = Other(), Other(), Other()
x.numInstances, y1.numInstances, z1.numInstances    # 클래스별 데이터!
# (1, 2, 3)
Spam.numInstances, Sub.numInstances, Other.numInstances
# (1, 2, 3)
