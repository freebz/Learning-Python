# -*- coding: utf-8 -*-
# person-composite.py 파일
# 내장 기반의 Manager 구현 방식

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

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)    # Person 객체를 내장시킴
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)    # 가로채고 위임함
    def __getattr__(self, attr):
        return getattr(self.person, attr)         # 모든 다른 속성들을 위임함
    def __repr__(self):
        return str(self.person)                   # 다시 오버로드해야 함(3.X)

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
