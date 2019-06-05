# 함수의 일반화에 적용하기

if sometest:
    action, args = func1, (1,)         # 이 경우, 하나의 인수로 func1 호출
else:
    action, args = func2, (1, 2, 3)    # 여기에서는 세 개의 인수로 func2 호출
...등등...
action(*args)                          # 일반적으로 처리


...func3를 정의하거나 임포트함...
args = (2,3)
args += (4,)
args
# (2, 3, 4)
func3(*args)


def tracer(func, *pargs, **kargs):    # 임의의 인수를 받아들임
    print('calling:', func.__name__)
    return func(*pargs, **kargs)      # 임의의 인수를 전달함

def func(a, b, c, d):
    return a + b + c + d

print(tracer(func, 1, 2, c=3, d=4))


# calling: func
# 10
