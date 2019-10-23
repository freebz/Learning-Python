class Person:                             # 2.X와 3.X에서 모두 실행됨
    def __init__(self, name):             # Person() 실행 시 호출됨
        self._name = name                 # __setattr__ 호출!

# __getattr__을 이 코드로 대체

    def __getattribute__(self, attr):                 # 객체의 모든 속성에 대해 동작함
        print('get: ' + attr)
        if attr == 'name':                            # 모든 이름을 가로챔
            attr = '_name'                            # 내부 이름에 매핑
        return object.__getattribute__(self, attr)    # 루핑 방지

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
