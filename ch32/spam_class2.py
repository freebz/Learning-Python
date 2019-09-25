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
