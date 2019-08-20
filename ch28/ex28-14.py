# 상속, 커스터마이즈, 그리고 확장

class Person:
    def lastName(self): ...
    def giveRaise(self): ...
    def __repr__(self): ...

class Manager(Person):                   # 상속
    def giveRaise(self, ...): ...        # 커스터마이즈
    def someThingElse(self, ...): ...    # 확장

tom = Manager()
tom.lastName()                  # 그대로 상속된 메서드
tom.giveRaise()                 # 커스터마이즈된 메서드
tom.someThingElse()             # 클래스 확장
print(tom)                      # 상속된 오버로드 메서드
