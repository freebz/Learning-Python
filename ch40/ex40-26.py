# 예제: 데코레이터를 메서드에 적용하기

# 직접 데코레이션을 이용하여 추적하기

# decotools.py 파일: 데코레이터 도구들을 하나로 모음
import time

def tracer(func):                       # __call__을 가진 클래스가 아니라 함수를 사용
    calls = 0                           # 그렇지 않으면 self는 데코레이터 인스턴스만
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall

def timer(label='', trace=True):        # 데코레이터 인수에 대해: 인수를 저장
    def onDecorator(func):              # @ 데코레이션 시: 데코레이트된 함수를 저장
        def onCall(*args, **kargs):     # 호출 시: 원래 버전을 호출
            start = time.clock()        # 상태 정보는 범위 + 함수 속성
            result = func(*args, **kargs)
            elapsed = time.clock() - start
            onCall.alltime += elapsed
            if trace:
                format = '%s%s: %.5f, %.5f'
                values = (label, func.__name__, elapsed, onCall.alltime)
                print(format % values)
            return result
        onCall.alltime = 0
        return onCall
    return onDecorator


from decotools import tracer

class Person:
    @tracer
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):       # giveRaise = tracer(giveRaise)
        self.pay *= (1.0 + percent)     # onCall이 giveRaise를 기억

    @tracer
    def lastName(self):                 # lastName = tracer(lastName)
        return self.name.split()[-1]

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10) # Runs onCall(sue, .10)
print('%.2f' % sue.pay)
print(bob.lastName(), sue.lastName())   # onCall(bob)을 실행, lastName을 기억


# py -3 decoall-manual.py 
# call 1 to __init__
# call 2 to __init__
# Bob Smith Sue Jones
# call 1 to giveRaise
# 110000.00
# call 1 to lastName
# call 2 to lastName
# Smith Jones
