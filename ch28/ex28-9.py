# 프린트 디스플레이 제공하기

# 객체 출력을 위한 __repr__ 오버로딩 메서드 추가

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):                                      # 추가된 메서드
        return '[Person: %s, %s]' % (self.name, self.pay)    # 출력될 문자열

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)


# [Person: Bob Smith, 0]
# [Person: Sue Jones, 100000]
# Smith Jones
# [Person: Sue Jones, 110000]
