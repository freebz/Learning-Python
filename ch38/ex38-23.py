# 위임 기반 Manager 클래스 다시 살펴보기

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
        self.person = Person(name, 'mgr', pay)    # Person 객체 내포
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)    # 가로채기와 위임
    def __getattr__(self, attr):
        return getattr(self.person, attr)         # 모든 다른 속성을 위임
    def __repr__(self):
        return str(self.person)                   # 다시 오버로드해야 함(3.X에서)

if __name__ == '__main__':
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tome Jones', 50000)    # Manager.__init__
    print(tom.lastName())                 # Manager.__getattr__ -> Person.lastName
    tom.giveRaise(.10)                    # Manager.giveRaise -> Person.giveRaise
    print(tom)                            # Manager.__repr__ -> Person.__repr__


# py -3 getattr-delegate.py
# Jones
# [Person: Sue Jones, 110000]
# Jones
# [Person: Tome Jones, 60000]


# Manager의 __str__ 메서드 삭제

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)    # Person 객체를 내장함
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)    # 가로채고 위임
    def __getattr__(self, attr):
        return getattr(self.person, attr)         # 다른 모든 속성을 위임함


# py -3 getattr-delegate.py
# Jones
# [Person: Sue Jones, 110000]
# Jones
# <__main__.Manager object at 0x7fb35afb7e80>


# py -2 getattr-delegate.py
# Jones
# [Person: Sue Jones, 110000]
# Jones
# [Person: Tome Jones, 60000]


# __getattr__을 __getattribute__로 대체함

class Manager(object):                            # 2.X에서는 (object)를 사용
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)    # Person 객체 내장
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)    # 가로채기와 위임
    def __getattribute__(self, attr):
        print('**', attr)
        if attr in ['person', 'giveRaise']:
            return object.__getattribute__(self, attr)    # 내 속성 가져오기
        else:
            return getattr(self.person, attr)             # 다른 속성 위임


# py -3 getattr-delegate.py
# Jones
# [Person: Sue Jones, 110000]
# ** lastName
# ** person
# Jones
# ** giveRaise
# ** person
# <__main__.Manager object at 0x7fef2aef0fd0>


# __getattribute__를 다른 방식으로 코딩하여 추가 호출을 최소화함

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)
    def __getattribute__(self, attr):
        print('**', attr)
        person = object.__getattribute__(self, 'person')
        if attr == 'giveRaise':
            return lambda percent: person.giveRaise(percent+.10)
        else:
            return getattr(person, attr)
    def __repr__(self):
        person = object.__getattribute__(self, 'person')
        return str(person)


# Jones
# [Person: Sue Jones, 110000]
# ** lastName
# Jones
# ** giveRaise
# [Person: Tome Jones, 60000]
