# 데코레이터 중첩

@A
@B
@C
def f(...):
    ...


def f(...):
    ...
f = A(B(C(f)))


@spam
@eggs
class C:
    ...

X = C()


class C:
    ...
C = spam(eggs(C))

X = C()


def d1(F): return F
def d2(F): return F
def d3(F): return F

@d1
@d2
@d3
def func():                     # func = d1(d2(d3(func)))
    print('spam')

func()                          # "spam"을 출력


def d1(F): return lambda: 'X' + F()
def d2(F): return lambda: 'Y' + F()
def d3(F): return lambda: 'Z' + F()

@d1
@d2
@d3
def func():                     # func = d1(d2(d3(func)))
    return 'spam'

print(func())                   # "XYZspam"을 출력
