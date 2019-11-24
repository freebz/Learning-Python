# 데코레이트된 객체를 API에 등록
from __future__ import print_function         # 2.X

registry = {}
def register(obj):                            # 클래스와 함수 데코레이터 모두
    registry[obj.__name__] = obj              # registry에 추가
    return obj                                # wrapper가 아니라 obj 자체를 반환

@register
def spam(x):
    return(x ** 2)                            # spam = register(spam)

@register
def ham(x):
    return(x ** 3)

@register
class Eggs:                                   # Eggs = register(Eggs)
    def __init__(self, x):
        self.data = x ** 4
    def __str__(self):
        return str(self.data)

print('Registry:')
for name in registry:
    print(name, '=>', registry[name], type(registry[name]))

print('\nManual calls:')
print(spam(2))                                # 객체를 직접 호출
print(ham(2))                                 # 나중에 발생하는 호출은 가로채지지 않음
X = Eggs(2)
print(X)

print('\nRegistry calls:')
for name in registry:
    print(name, '=>', registry[name](2))      # registry로부터 호출
