# 클래스는 객체: 일반적인 객체 팩토리

def factory(aClass, *pargs, **kargs):          # 가변 길이의 튜플, 딕셔너리
    return aClass(*pargs, **kargs)

class Spam:
    def doit(self, message):
        print(message)

class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job

object1 = factory(Spam)                        # Spam 객체 생성
object2 = factory(Person, "Arthur", "King")    # Person 객체 생성
object3 = factory(Person, name='Brian')        # 상동, 키워드와 기본 인수로


object1.doit(99)
# 99
object2.name, object2.job
# ('Arthur', 'King')
object3.name, object3.job
# ('Brian', None)
