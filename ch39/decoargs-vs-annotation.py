# 데코레이터 인수 사용(3.X + 2.X)

def rangetest(**argchecks):
    def onDecorator(func):
        def onCall(*pargs, **kargs):
            print(argchecks)
            for check in argchecks:
                pass                    # 여기에 검증 코드 추가
            return func(*pargs, **kargs)
        return onCall
    return onDecorator

@rangetest(a=(1, 5), c=(0.0, 1.0))
def func(a, b, c):                      # func = rangetest(...)(func)
    print(a + b + c)

func(1, 2, c=3)                         # onCall 실행, argchecks는 범위에

# 함수 어노테이션 사용(3.X only)

def rangetest(func):
    def onCall(*pargs, **kargs):
        argchecks = func.__annotations__
        print(argchecks)
        for check in argchecks:
            pass                        # 여기에 검증 코드 추가
        return func(*pargs, **kargs)
    return onCall

@rangetest
def func(a:(1, 5), b, c:(0.0, 1.0)):    # func = rangetest(func)
    print(a + b + c)

func(1, 2, c=3)                         # onCall 실행, 함수에 어노테이션
