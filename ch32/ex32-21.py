# 프로퍼티: 속성 접근자

# 프로퍼티의 기본

class operators:
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError(name)

x = operators()
x.age                           # __getattr__를 실행
# 40
x.name                          # __getattr__를 실행
# AttributeError: name


class properties(object):                       # 2.X에서는 setters를 위해 object 필요
    def getage(self):
        return 40
    age = property(getage, None, None, None)    # (get,get,del,docs) 또는 @

x = properties()
x.age                                           # getage 실행
# 40
x.name                                          # 일반적인 가져오기
# AttributeError: 'properties' object has no attribute 'name'


class properties(object):     # 2.X에서는 setters를 위해 object가 필요
    def getage(self):
        return 40
    def setage(self, value):
        print('set age: %s' % value)
        self._age = value
    age = property(getage, setage, None, None)

x = properties()
x.age                           # getage 실행
# 40
x.age = 42                      # setage 실행
# set age: 42
x._age                          # 일반적인 가져오기: getage 호출 ✕
# 42
x.age                           # getage 실행
# 40
x.job = 'trainer'               # 일반적인 할당: setage 호출 ✕
x.job                           # 일반적인 가져오기: getage 호출 ✕
# 'trainer'


class operators:
    def __getattr__(self, name):             # 미정의 참조에 대해
        if name == 'age':
            return 40
        else:
            raise AttributeError(name)
    def __setattr__(self, name, value):      # 모든 할당에 대해
        print('set: %s %s' % (name, value))
        if name == 'age':
            self.__dict__['_age'] = value    # 또는 object.__setattr__()
        else:
            self.__dict__[name] = value

x = operators()
x.age                           # __getattr__ 실행
# 40
x.age = 41                      # __setattr__ 실행
# set: age 41
x._age                          # 정의됨: __getattr__ 호출 ✕
# 41
x.age                           # __getattr__ 실행
# 40
x.job = 'trainer'               # 다시 __setattr__ 실행
# set: job trainer
x.job                           # 정의됨: __getattr__ 호출 ✕
# 'trainer'


class properties(object):
    @property                   # 데코레이터로 프로퍼티 코딩하기: 앞으로 알아보겠음
    def age(self):
        ...
    @age.setter
    def age(self, value):
        ...
