# 메서드 확장하기: 좋은 방법

class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)    # 좋은 방법: 원래 버전을 보안


instance.method(args...)

class.method(instance, args...)


# 서브클래스에서 한 행위에 대한 커스터마이즈 버전 추가

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

class Manager(Person):
    def giveRaise(self, percent, bonus=.10):       # 이 레벨에서 재정의
        Person.giveRaise(self, percent + bonus)    # Person의 버전을 호출

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 'mgr', 50000)    # Manager 생성: __init__
    tom.giveRaise(.10)                          # 사용자 정의 버전 실행
    print(tom.lastName())                       # 상속된 메서드 실행
    print(tom)                                  # 상속된 __repr__ 실행


# [Person: Bob Smith, 0]
# [Person: Sue Jones, 100000]
# Smith Jones
# [Person: Sue Jones, 110000]
# Jones
# [Person: Tom Jones, 60000]
