class Person:                   # 2.X에서는 (object) 추가
    def __init__(self, name):
        self._name = name
    def getName(self):
        print('fetch...')
        return self._name
    def setName(self, value):
        print('change...')
        self._name = value
    def delName(self):
        print('remove...')
        del self._name
    name = property(getName, setName, delName, "name property docs")

bob = Person('Bob Smith')       # bob은 관리 속성을 가짐
print(bob.name)                 # getName을 실행함
bob.name = 'Robert Smith'       # setName을 실행함
print(bob.name)
del bob.name                    # delName을 실행힘

print('-'*20)
sue = Person('Sue Jones')       # sue도 프로퍼티를 상속받음
print(sue.name)
print(Person.name.__doc__)      # 또는 help(Person.name)
