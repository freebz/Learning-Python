# 임의 인수 예제

# 헤더: 인수 수집

def f(*args): print(args)


f()
# ()
f(1)
# (1,)
f(1, 2, 3, 4)
# (1, 2, 3, 4)


def f(**args): print(args)

f()
# {}
f(a=1, b=2)
# {'a': 1, 'b': 2}


def f(a, *pargs, **kargs): print(a, pargs, kargs)

f(1, 2, 3, x=1, y=2)
# 1 (2, 3) {'x': 1, 'y': 2}
