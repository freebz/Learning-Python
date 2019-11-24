# 클래스 실수 I: 메서드 데코레이트하기

class tracer:
    def __init__(self, func):                 # @ 데코레이터에서
        self.calls = 0                        # 나중 호출을 위해 func을 저장
        self.func = func
    def __call__(self, *args, **kwargs):      # 원래 함수를 호출할 때
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


@tracer
def spam(a, b, c):                            # spam = tracer(spam)
    print(a + b + c)                          # trace.__init__을 작동시킴

spam(1, 2, 3)                                 # trace.__call__을 실행
# call 1 to spam
# 6
spam(a=4, b=5, c=6)                           # spam은 인스턴스 속성에 저장됨
# call 2 to spam
# 15


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):             # giveRaise = tracer(giveRaise)
        self.pay *= (1.0 + percent)

    @tracer
    def lastName(self):                       # lastName = tracer(lastName)
        return self.name.split()[-1]

bob = Person('Bob Smith', 50000)              # tracer는 메서드 함수를 기억함
bob.giveRaise(.25)                            # tracer.__call__(???, .25) 실행
# call 1 to giveRaise
# TypeError: giveRaise() missing 1 required positional argument: 'percent'

print(bob.lastName())                         # tracer.__call__(???)를 실행
# call 1 to lastName
# TypeError: lastName() missing 1 required positional argument: 'self'


bob.giveRaise(.25)
# <__main__.tracer object at 0x02A486D8> (0.25,) {}
# call 1 to giveRaise
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 9, in __call__
# TypeError: giveRaise() missing 1 required positional argument: 'percent'
