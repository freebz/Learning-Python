# 클래스 메서드를 이용하여 인스턴스 개수 세기

class Spam:
    numInstances = 0            # 정적 메서드 대신에 클래스 메서드 사용
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances(cls):
        print("Number of instances: %s" % cls.numInstances)
    printNumInstances = classmethod(printNumInstances)


from spam_class import Spam
a, b = Spam(), Spam()
a.printNumInstances()           # 첫 번째 인수에 클래스를 전달
# Number of instances: 2
Spam.printNumInstances()        # 역시 첫 번째 인수에 클래스를 전달
# Number of instances: 2


from spam_class import Spam, Sub, Other
x = Sub()
y = Spam()
x.printNumInstances()           # 서브클래스 인스턴스로부터 호출
# Extra stuff... <class 'spam_class.Sub'>
# Number of instances: 2 <class 'spam_class.Spam'>
Sub.printNumInstances()         # 서브클래스 자체로부터 호출
# Extra stuff... <class 'spam_class.Sub'>
# Number of instances: 2 <class 'spam_class.Spam'>
y.printNumInstances()           # 슈퍼클래스 인스턴스로부터 호출
# Number of instances: 2 <class 'spam_class.Spam'>


z = Other()                     # 더 낮은 서브클래스의 인스턴스로부터 호출
z.printNumInstances()
# Number of instances: 3 <class 'spam_class.Other'>
