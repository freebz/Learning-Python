# 데코레이터 vs 관리 함수

class Spam:                     # 데코레이터 없는 버전
    ...                         # 어떤 호출도 가능
food = Wrapper(Spam())          # 특별한 생성 구문

@Tracer
class Spam:                     # 데코레이터 사용하는 버전
    ...                         # 클래스에 @ 구문이 필요
food = Spam()                   # 일반적인 생성 구문


instances = {}
def getInstance(aClass, *args, **kwargs):
    if aClass not in instances:
        instances[aClass] = aClass(*args, **kwargs)
    return instances[aClass]

bob = getInstance(Person, 'Bob', 40, 10)    # 대조: bob = Person('Bob', 40, 10)


instances = {}
def getInstance(object):
    aClass = object.__class__
    if aClass not in instances:
        instances[aClass] = object
    return instances[aClass]

bob = getInstance(Person('Bob', 40, 10))    # 대조: bob = Person('Bob', 40, 10)


def func(x, y):                 # 데코레이터를 사용하지 않는 버전
    ...                         # def tracer(func, args): ... func(*args)
result = tracer(func, (1, 2))   # 특별한 호출 구문

@tracer
def func(x, y):                 # 데코레이터 사용 버전
    ...                         # 이름 재결합: func = tracer(func)
result = func(1, 2)             # 일반 호출 구문
