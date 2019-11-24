# 학습 테스트: 정답

"""
timerdeco.py (3.X + 2.X) 파일
함수와 메서드 모두에 대한 타이머 데코레이터 호출
"""
import time

def timer(label='', trace=True):            # 데코레이터인수: 인수 유지
    def onDecorator(func):                  # @: 데코레이터 함수 유지
        def onCall(*args, **kargs):         # 원래 함수 호출
            start = time.clock()            # 상태는 범위 + 함수 속성임
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


"""
timerdeco-test.py 파일
"""
from __future__ import print_function       # 2.X
from timerdeco import timer
import sys
force = list if sys.version_info[0] == 3 else (lambda X: X)

print('---------------------------------------------------')
# 함수에 대한 테스트

@timer(trace=True, label='[CCC]==>')
def listcomp(N):                            # listcomp = timer(...)(listcomp)와 유사함
    return [x * 2 for x in range(N)]        # listcomp(...)는 onCall을 호출함

@timer('[MMM]==')
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))    # 3.X 관점에서는 list()임

for func in (listcomp, mapcall):
    result = func(5)                        # 이 호출과 모든 호출에 대한 시간과 결괏값 출력
    func(5000000)
    print(result)
    print('allTime = %s\n' % func.alltime)    # 모든 호출에 대한 전체 시간

print('---------------------------------------------------')
# 메서드에 테스트

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @timer()
    def giveRaise(self, percent):           # giveRaise = timer()(giveRaise)
        self.pay *= (1.0 + percent)         # 추적자는 giveRaise를 기억함

    @timer(label='**')
    def lastName(self):                     # lastName = timer(...)(lastName)
        return self.name.split()[-1]        # 항상 인스턴스가 아닌 클래스임

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
bob.giveRaise(.10)
sue.giveRaise(.20)                          # onCall(sue, .10) 실행
print(int(bob.pay), int(sue.pay))
print(bob.lastName(), sue.lastName())       # onCall(bob) 실행, lastName을 기억함
print('%.5f %.5f' % (Person.giveRaise.alltime, Person.lastName.alltime))


# py -3 timerdeco-test.py 
# ---------------------------------------------------
# [CCC]==>listcomp: 0.00001, 0.00001
# [CCC]==>listcomp: 0.42827, 0.42827
# [0, 2, 4, 6, 8]
# allTime = 0.42827299999999996

# [MMM]==mapcall: 0.00002, 0.00002
# [MMM]==mapcall: 0.70572, 0.70574
# [0, 2, 4, 6, 8]
# allTime = 0.7057439999999999

# ---------------------------------------------------
# giveRaise: 0.00001, 0.00001
# giveRaise: 0.00000, 0.00001
# 55000 120000
# **lastName: 0.00001, 0.00001
# **lastName: 0.00000, 0.00001
# Smith Jones
