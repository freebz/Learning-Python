# 외부 인스턴스 속성 가져오기를 추적하는 클래스 데코레이터

def Tracer(aClass):                                   # @ 데코레이션할 때
    class Wrapper:
        def __init__(self, *args, **kargs):           # 인스턴스 생성할 때
            self.wrapped = aClass(*args, **kargs)     # 유효 범위 이름 사용
        def __getattr__(self, attrname):
            print('Trace:' , attrname)                # .wrapped를 제외한 모든 이름을 잡아냄
            return getattr(self.wrapped, attrname)    # wrapped객체에 위임
    return Wrapper

@Tracer
class Person:                                         # Person = Tracer(Person)
    def __init__(self, name, hours, rate):            # Wrapper는 Person을 기억
        self.name = name
        self.hours = hours
        self.rate = rate                # 메서드 내에서 가져오는 것은 추적되지 않음
    def pay(self):
        return self.hours * self.rate

bob = Person('Bob', 40, 50)             # bob이 실제로 Wrapper
print(bob.name)                         # Wrapper는 Person을 내장
print(bob.pay())                        # __getattr__를 작동시킴
