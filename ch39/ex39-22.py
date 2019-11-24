# 클래스 데코레이터 코딩하기

# 싱글톤 클래스

# 3.X와 2.X: 전역 레이블

instances = {}

def singleton(aClass):                  # @ 데코레이션 시
    def onCall(*args, **kwargs):        # 인스턴스 생성 시
        if aClass not in instances:     # 클래스당 딕셔너리 아이템 하나
            instances[aClass] = aClass(*args, **kwargs)
        return instances[aClass]
    return onCall


@singleton                                    # Person = singleton(Person)
class Person:                                 # Person을 onCall에 재결합
    def __init__(self, name, hours, rate):    # onCall은 Person을 기억함
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate

@singleton                                    # Spam = singleton(Spam)
class Spam:                                   # Spam을 onCall에 다시 바인드함
    def __init__(self, val):                  # onCall은 Sapm을 기억함
        self.attr = val

bob = Person('Bob', 40, 10)                   # 실제로 onCall 호출
print(bob.name, bob.pay())

sue = Person('Sue', 50, 20)                   # 동일, 단일 객체
print(sue.name, sue.pay())

X = Spam(val=42)                              # 하나의 Person, 하나의 Spam
Y = Spam(99)
print(X.attr, Y.attr)


# python singletons.py 
# Bob 400
# Bob 400
# 42 42
