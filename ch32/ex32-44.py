# 커스터마이즈: 동일 인자 제약 조건

class Employee:
    def __init__(self, name, salary):           # 공통의 슈퍼클래스
        self.name = name
        self.salary = salary

class Chef1(Employee):
    def __init__(self, name):                   # 상이한 인수
        Employee.__init__(self, name, 50000)    # 직접 호출로 불러옴

class Server1(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)

bob = Chef1('Bob')
sue = Server1('Sue')
bob.salary, sue.salary
# (50000, 40000)


class Chef2(Employee):
    def __init__(self, name):
        super().__init__(name, 50000)    # super()로 불러옴

class Server2(Employee):
    def __init__(self, name):
        super().__init__(name, 40000)

bob = Chef2('Bob')
sue = Server2('Sue')
bob.salary, sue.salary
# (50000, 40000)


class TwoJobs(Chef2, Server2): pass

tom = TwoJobs('Tom')
# TypeError: __init__() takes 2 positional arguments but 3 were given


TwoJobs.__mro__
# (<class '__main__.TwoJobs'>, <class '__main__.Chef2'>, <class '__main__.Server2'>, <class '__main__.Employee'>, <class 'object'>)

Chef2.__mro__
# (<class '__main__.Chef2'>, <class '__main__.Employee'>, <class 'object'>)


class TwoJobs(Chef1, Server1): pass

tom = TwoJobs('Tom')
tom.salary
# 50000


class TwoJobs(Chef1, Server1):
    def __init__(self, name): Employee.__init__(self, name, 70000)

tom = TwoJobs('Tom')
tom.salary
# 70000

class TwoJobs(Chef2, Server2):
    def __init__(self, name): super().__init__(name, 70000)

tom = TwoJobs('Tom')
# TypeError: __init__() takes 2 positional arguments but 3 were given
