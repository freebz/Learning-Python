# 클래스 실수 II: 다중 인스턴스 유지하기

class Tracer:
    def __init__(self, aClass):              # @ 데코레이터가 나올 때
        self.aClass = aClass                 # 인스턴스 속성 사용
    def __call__(self, *args):               # 인스턴스 생성할 때
        self.wrapped = self.aClass(*args)    # 클래스당 하나의(마지막) 인스턴스!
        return self
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)

@Tracer                         # __init__을 작동시킴
class Spam:                     # Spam = Tracer(Spam)와 같음
    def display(self):
        print('Spam!' * 8)

...
food = Spam()                   # __call__ 작동시킴
food.display()                  # __getattr__을 작동시킴


@Tracer
class Person:                   # Person = Tracer(Person)
    def __init__(self, name):   # Wrapper는 Person에 바인드됨
        self.name = name

bob = Person('Bob')             # bob은 실제로 Wrapper임
print(bob.name)                 # Wrapper는 Person을 내장시킴
sue = Person('Sue')
print(sue.name)                 # sue는 bob을 덮어씀
print(bob.name)                 # 아뿔사 이제 bob의 이름은 'Sue'다!


# Trace: name
# Bob
# Trace: name
# Sue
# Trace: name
# Sue
