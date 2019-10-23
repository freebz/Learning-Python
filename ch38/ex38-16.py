# 첫 번째 예제

class Person:                             # 2.X와 3.X에서 모두 실행됨
    def __init__(self, name):             # Person() 실행 시 호출됨
        self._name = name                 # __setattr__ 호출!

    def __getattr__(self, attr):          # obj.undefined 호출 시 실행됨
        print('get: ' + attr)
        if attr == 'name':                # name을 가로챈다. 저장되지 않음
            return self._name             # 실제 속성이므로 무한 루프에 빠지지 않음
        else:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):   # [obj.any = value] 실행 시 호출됨
        print('set: ' + attr)
        if attr == 'name':
            attr = '_name'                # 내부 이름 설정
        self.__dict__[attr] = value       # 루핑 방지

    def __delattr__(self, attr):          # [del obj.any] 실행 시 호출됨
        print('del: ' + attr)
        if attr == 'name':
            attr = '_name'                # 루핑 방지
        del self.__dict__[attr]           # 일반적으로 사용되지 않음

bob = Person('Bob Smith')                 # bob은 관리 속성을 가짐
print(bob.name)                           # __getattr__ 실행
bob.name = 'Robert Smith'                 # __setattr__ 실행
print(bob.name)
del bob.name                              # __delattr__ 실행

print('-'*20)
sue = Person('Sue Jones')                 # sue는 프로퍼티도 상속받음
print(sue.name)
#print(Person.name.__doc__)               # 여기에 해당하는 속성은 없음


# py -3 getattr-person.py
# set: _name
# get: name
# Bob Smith
# set: name
# get: name
# Robert Smith
# del: name
# --------------------
# set: _name
# get: name
# Sue Jones
