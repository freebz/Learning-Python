class Spam:
    numInstances = 0            # 클래스 데이터를 위해 static 메서드 사용
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances():
        print("Number of instances: %s" % Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)


class Sub(Spam):
    def printNumInstances():    # 정적 메서드 재정의
        print("Extra stuff...") # 하지만 원래 버전을 재호출
        Spam.printNumInstances()
    printNumInstances = staticmethod(printNumInstances)
