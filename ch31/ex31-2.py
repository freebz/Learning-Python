# 객체 지향 프로그래밍과 상속: 'is-a' 관계

# employees.py 파일(2.X + 3.X)
from __future__ import print_function

class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)
    def work(self):
        print(self.name, "does stuff")
    def __repr__(self):
        return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)

class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)
    def work(self):
        print(self.name, "makes food")

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)
    def work(self):
        print(self.name, "interfaces with customer")

class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)
    def work(self):
        print(self.name, "makes pizza")

if __name__ == "__main__":
    bob = PizzaRobot('bob')     # bob이라는 이름의 로봇 생성
    print(bob)                  # 상속받은 __repr__ 실행
    bob.work()                  # 타입 특화된 동작 실행
    bob.giveRaise(0.20)         # bob에서 20% 급여 인상해 줌
    print(bob); print()

    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()


# python employees.py 
# <Employee: name=bob, salary=50000>
# bob makes pizza
# <Employee: name=bob, salary=60000.0>

# Employee does stuff
# Chef makes food
# Server interfaces with customer
# PizzaRobot makes pizza
