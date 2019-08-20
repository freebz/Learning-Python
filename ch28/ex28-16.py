# 클래스를 결합하는 다른 방식

# person-composite.py 파일
# 내장 기반의 Manager 구현 방식

class Person:
    ...동일...

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
    ...동일...


# person-department.py 파일
# 내장 객체들을 하나의 컴포지트로 모음

class Person:
    ...동일...

class Manager(Person):
    ...동일...

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


# [Person: Bob Smith, 0]
# [Person: Sue Jones, 110000]
# [Person: Tom Jones, 60000]
