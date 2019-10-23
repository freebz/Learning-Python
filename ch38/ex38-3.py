# 첫 번째 예제

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


# py -3 prop-person.py
# fetch...
# Bob Smith
# change...
# fetch...
# Robert Smith
# remove...
# --------------------
# fetch...
# Sue Jones
# name property docs


class Super:
    ...원래의 Person 클래스 코드...
    name = property(getName, setName, delName, 'name property docs')

class Person(Super):
    pass                        # 프로퍼티는 상속된다(클래스 속성)

bob = Person('Bob Smith')
...나머지는 같음...
