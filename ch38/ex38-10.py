# 첫 번째 예제

class Name:                     # 2.X에서는 (object)를 사용
    "name descriptor docs"
    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name
    def __set__(self, instance, value):
        print('change...')
        instance._name = value
    def __delete__(self, instance):
        print('remove...')
        del instance._name

class Person:                   # 2.X에서는 (object)를 사용
    def __init__(self, name):
        self._name = name
    name = Name()               # 디스크립터를 속성에 할당

bob = Person('Bob Smith')       # bot도 관리 속성을 가지고 있음
print(bob.name)                 # Name.__get__을 실행
bob.name = 'Robert Smith'       # Name.__set__을 실행
print(bob.name)
del bob.name                    # Name.__delete__를 실행

print('-'*20)
sue = Person('Sue Jones')       # sue도 디스크립터를 상속
print(sue.name)
print(Name.__doc__)             # 또는 help(Name)를 실행


# py -3 desc-person.py
# fetch...
# Bob Smith
# change...
# fetch...
# Robert Smith
# remove...
# --------------------
# fetch...
# Sue Jones
# name descriptor docs


...
class Super:
    def __init__(self, name):
        self._name = name
    name = Name()

class Person(Super):            # 디스크립터가 상속됨(클래스 속성)
    pass
...


class Person:
    def __init__(self, name):
        self._name = name

    class Name:                 # 중첩된 클래스
        "name descriptor docs"
        def __get__(self, instance, owner):
            print('fetch...')
            return instance._name
        def __set__(self, instance, value):
            print('change...')
            instance._name = value
        def __delete__(self, instance):
            print('remove...')
            del instance._name
    name = Name()


...
print(Person.Name.__doc__)    # Person.Name은 클래스 외부의 Name.__doc__과 다름
