# class Spam:
#     numInstances = 0            # 정적 메서드 대신에 클래스 메서드 사용
#     def __init__(self):
#         Spam.numInstances += 1
#     def printNumInstances(cls):
#         print("Number of instances: %s" % cls.numInstances)
#     printNumInstances = classmethod(printNumInstances)


class Spam:
    numInstances = 0                    # 전달된 클래스 추적
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances(cls):
        print("Number of instances: %s %s" % (cls.numInstances, cls))
    printNumInstances = classmethod(printNumInstances)

class Sub(Spam):
    def printNumInstances(cls):         # 클래스 메서드 재정의
        print("Extra stuff...", cls)    # 하지만 원래 버전을 재호출
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)

class Other(Spam): pass                 # 말 그대로 클래스 메서드 상속
