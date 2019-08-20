# -*- coding: utf-8 -*-
# person-department.py 파일
# 내장 객체들을 하나의 컴포지트로 모음

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

class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Jones', 50000)

    development = Department(bob, sue)  # 객체들을 하나의 컴포지트로 내장시킴
    development.addMember(tom)
    development.giveRaises(.10)         # 내장 객체의 giveRaise를 실행
    development.showAll()               # 내장 객체의 __repr__을 실행
