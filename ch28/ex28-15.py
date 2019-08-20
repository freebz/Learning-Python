# 단계 5: 생성자도 커스터마이즈하기

# person.py 파일
# 서브클래스에서 생성자 커스터마이즈 버전을 추가함

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
    def __init__(self, name, pay):                 # 생성자 재정의
        Person.__init__(self, name, 'mgr', pay)    # 'mgr'로 원래 버전 호출
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)              # 직업명은 필요 없음
    tom.giveRaise(.10)                             # 클래스에 의해 설정됨
    print(tom.lastName())
    print(tom)


# [Person: Bob Smith, 0]
# [Person: Sue Jones, 100000]
# Smith Jones
# [Person: Sue Jones, 110000]
# Jones
# [Person: Tom Jones, 60000]
