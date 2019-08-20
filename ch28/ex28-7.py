# 메서드 코딩하기

# 유지보수성을 위해 연산을 캡슐화하도록 메서드를 추가

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay
    def lastName(self):                             # 행위 메서드
        return self.name.split()[-1]                # self는 암묵적 대상
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))    # 여기에서만 바꾸면 됨

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.lastName(), sue.lastName())           # 새 메서드 사용
    sue.giveRaise(.10)                              # 하드코딩 대신에
    print(sue.pay)


# Bob Smith 0
# Sue Jones 100000
# Smith Jones
# 110000


@rangetest(percent=(0.0, 1.0))      # 검증을 위해 데코레이터를 사용
def giveRaise(self, percent):
    self.pay = int(self.pay * (1 + percent))
