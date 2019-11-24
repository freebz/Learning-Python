# 클래스 데코레이터를 내장 타입에 적용하기

from interfacetracer import Tracer

@Tracer
class MyList(list): pass        # MyList = Tracer(MyList)

x = MyList([1, 2, 3])           # Wrapper() 실행
x.append(4)                     # __getattr__, append 실행
# Trace: append
x.wrapped
# [1, 2, 3, 4]

WrapList = Tracer(list)         # 또는 직접 데코레이션함
x = WrapList([4, 5, 6])         # 아니면 subclass문이 필요
x.append(7)
# Trace: append
x.wrapped
# [4, 5, 6, 7]


@Tracer                                 # 데코레이터를 사용하는 방식
class Person: ...
bob = Person('Bob', 40, 50)
sue = Person('Sue', rate=100, hours=60)

class Person: ...                       # 데코레이터를 사용하지 않는 방식
bob = Wrapper(Person('Bob', 40, 50))
sue = Wrapper(Person('Sue', rate=100, hours=60))


x                               # 2.X
# Trace: __repr__
# [4, 5, 6, 7]
x                               # 3.X
# <interfacetracer.Tracer.<locals>.Wrapper object at 0x7ffab0dfc6a0>
