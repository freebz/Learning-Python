# 다른 활용 사례: 타입 테스팅(반드시 해야 한다면!)

def typetest(**argchecks):
    def onDecorator(func):
        ...
        def onCall(*pargs, **kargs):
            positionals = list(allargs)[:len(pargs)]
            for (argname, type) in argchecks.items():
                if argname in kargs:
                    if not isinstance(kargs[argname], type):
                        ...
                        raise TypeError(errmsg)
                    elif argname in positionals:
                        positon = positionals.index(argname)
                        if not isinstance(pargs[position], type):
                            ...
                            raise TypeError(errmsg)
                    else:
                        # 전달되지 않은 것으로 가정: 기본 인수
                return func(*pargs, **kargs)
            return onCall
    return onDecorator

@typetest(a=int, c=float)
def func(a, b, c, d):                   # func = typetest(...)(func)
    ...

func(1, 2, 3.0, 4)                      # OK
func('spam', 2, 99, 4)                  # 예외를 정확하게 일으킴


@typetest
def func(a: int, b, c: float, d):       # func = typetest(func)
    ...                                 # 헉!...
