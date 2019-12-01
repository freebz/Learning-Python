# 클래스 대신 인스턴스 관리하기

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


# py -3 manage-inst-deco.py
# Trace: name
# Bob
# Trace: pay
# 2000


# 메타클래스를 이용하여 이전 예제처럼 인스턴스 관리하기

def Tracer(classname, supers, classdict):             # 클래스 생성 호출 시
    aClass = type(classname, supers, classdict)       # 클라이언트 클래스 생성
    class Wrapper:
        def __init__(self, *args, **kargs):           # 인스턴스 생성 시
            self.wrapped = aClass(*args, **kargs)
        def __getattr__(self, attrname):
            print('Trace:', attrname)                 # .wrapped를 뺀 모든 것을 잡아냄
            return getattr(self.wrapped, attrname)    # wrapped 객체에 위임
    return Wrapper

class Person(metaclass=Tracer):                       # Person을 Trace로 생성
    def __init__(self, name, hours, rate):            # Wrapper는 Person을 기억
        self.name = name
        self.hours = hours
        self.rate = rate                              # 메서드 내 호출은 추적되지 않음
    def pay(self):
        return self.hours * self.rate

bob = Person('Bob', 40, 50)                           # bob이 실제로 Wrapper
print(bob.name)                                       # Wrapper는 Person을 내장
print(bob.pay())                                      # __getattr__를 작동시킴


# py -3 manage-inst-meta.py 
# Trace: name
# Bob
# Trace: pay
# 2000
