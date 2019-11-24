def rangetest(*argchecks):              # 위치적 인수의 범위 적용
    def onDecorator(func):
        if not __debug__:               # 만약 "python -O main.py args..."이라면
            return func                 # 아무 작업도 하지 않음: 원래 함수를 직접 호출
        else:
            def onCall(*args):
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        errmsg = 'Argument %s not in %s..%s' % (ix, low, high)
                        raise TypeError(errmsg)
                return func(*args)
            return onCall
    return onDecorator
