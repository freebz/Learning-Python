def Tracer(aClass):                                  # @ 데코레이션할 때
    class Wrapper:
        def __init__(self, *args, **kargs):          # 인스턴스 생성할 때
            self.fetches = 0
            self.wrapped = aClass(*args, **kargs)    # 유효 범위 이름 사용
        def __getattr__(self, attrname):
            print('Trace: ' + attrname)              # 자신의 속성을 제외한 모든 것을 잡아냄
            self.fetches += 1
            return getattr(self.wrapped, attrname)   # 내장 객체에 위임
    return Wrapper

if __name__ == '__main__':

    @Tracer
    class Spam:                                      # Spam = Tracer(Spam)
        def display(self):                           # Spam은 Wrapper에 재결합
            print('Spam!' * 8)

    @Tracer
    class Person:                                    # Person = Tracer(Person)
        def __init__(self, name, hours, rate):       # Wrapper는 Person을 기억
            self.name = name
            self.hours = hours
            self.rate = rate
        def pay(self):                               # 클래스 외부에서의 접근을 추적
            return self.hours * self.rate            # 메서드 내부 접근은 추적되지 않음

    food = Spam()                                    # Wrapper() 실행
    food.display()                                   # __getattr__ 실행
    print([food.fetches])

    bob = Person('Bob', 40, 50)                      # bob이 실제로 Wrapper임
    print(bob.name)                                  # Wrapper는 Person을 내장함
    print(bob.pay())

    print('')
    sue = Person('Sue', rate=100, hours=60)          # sue는 다른 Wrapper임
    print(sue.name)                                  # sue는 다른 Person을 가짐
    print(sue.pay())

    print(bob.name)                                  # bob은 다른 상태를 가짐
    print(bob.pay())
    print([bob.fetches, sue.fetches])                # Wrapper 속성은 추적되지 않음
