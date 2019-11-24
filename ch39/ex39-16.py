# 중첩 함수를 이용해 메서드 데코레이트하기

# 함수와 메서드 둘 모두를 위한 호출 추적 데코레이터

def tracer(func):                       # __call__을 가진 클래스가 아닌, 함수를 사용
    calls = 0                           # 아니면 "self"에는 데코레이터 인스턴스만!
    def onCall(*args, **kwargs):        # 또는 2.X+3.X에서: [onCall.calls += 1] 사용
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall

if __name__ == '__main__':

    # 단순 함수에 적용
    @tracer
    def spam(a, b, c):                       # spam = tracer(spam)
        print(a + b + c)                     # onCall은 spam을 기억
        
    @tracer
    def eggs(N):
        return 2 ** N

    spam(1, 2, 3)                            # onCall(1, 2, 3)를 실행
    spam(a=4, b=5, c=6)
    print(eggs(32))

    # 클래스 레벨의 메서드 함수에도 적용!
    class Person:
        def __init__(self, name, pay):
            self.name = name
            self.pay  = pay

        @tracer
        def giveRaise(self, percent):        # giveRaise = tracer(giveRaise)
            self.pay *= (1.0 + percent)      # onCall은 giveRaise를 기억

        @tracer
        def lastName(self):                  # lastName = tracer(lastName)
            return self.name.split()[-1]

    print('method...')
    bob = Person('Bob Smith', 50000)
    sue = Person('Sue Jones', 100000)
    print(bob.name, sue.name)
    sue.giveRaise(.10)                       # onCall(sue, .10) 실행
    print(int(sue.pay))
    print(bob.lastName(), sue.lastName())    # onCall(bob) 실행, lastName은 범위에 있음


# py -3 calltracer.py 
# call 1 to spam
# 6
# call 2 to spam
# 15
# call 1 to eggs
# 4294967296
# method...
# Bob Smith Sue Jones
# call 1 to giveRaise
# 110000
# call 1 to lastName
# call 2 to lastName
# Smith Jones
