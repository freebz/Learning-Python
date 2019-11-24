# 함수와 클래스 직접 관리하기

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


# py -3 registry-deco.py 
# Registry:
# spam => <function spam at 0x7f3c0aa6b620> <class 'function'>
# ham => <function ham at 0x7f3c0aa6bae8> <class 'function'>
# Eggs => <class '__main__.Eggs'> <class 'type'>

# Manual calls:
# 4
# 8
# 16

# Registry calls:
# spam => 4
# ham => 8
# Eggs => 16


# 데코레이트된 객체를 직접 보강하기

def decorate(func):
    func.marked = True                        # 나중에 사용하기 위해 함수 속성을 할당
    return func


@decorate
def spam(a, b):
    return a + b

spam.marked
# True

def annotate(text):                           # 동일하지만 값은 데코레이터 인수임
    def decorate(func):
        func.label = text
        return func
    return decorate

@annotate('spam data')
def spam(a, b):                               # spam = annotate(...)(spam)
    return a + b

spam(1, 2), spam.label
# (3, 'spam data')
