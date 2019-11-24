"""
파일 rangetest.py: 어떤 함수나 메서드에 전달되는 인수들에 대한
범위 테스트 검증을 수행하는 함수 데코레이터

인수들은 데코레이터에 키워드에 의해 기술됨
실제 호출에서 인수들은 위치 또는 키워드로 전달될 수 있으며, 기본값은 생략됨
사례로 rangetest_test.py를 참조하자
"""
trace = True

def rangetest(**argchecks):             # 위치+키워드+기본값 인수에 대한 범위 검증
    def onDecorator(func):              # onCall은 func과 argchecks를 기억
        if not __debug__:               # "python -O main.py args..."가 True일 경우
            return func                 # 만약 디버깅이면 감싸고 아니면 원래 함수 사용
        else:
            code = func.__code__
            allargs = code.co_varnames[:code.co_argcount]
            funcname = func.__name__
            def onCall(*pargs, **kargs):
                # 모든 pargs는 위치에 의해 첫 N개의 인수에 매칭시킴
                # 나머지는 kargs에 있거나, 생략된 기본값
                expected = list(allargs)
                positionals = expected[:len(pargs)]

                for (argname, (low, high)) in argchecks.items():
                    # 검사할 모든 args에 대해
                    if argname in kargs:
                        # 이름에 의해 전달됨
                        if kargs[argname] < low or kargs[argname] > high:
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                    elif argname in positionals:
                        # 위치에 의해 전달됨
                        position = positionals.index(argname)
                        if pargs[position] < low or pargs[position] > high:
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                    else:
                        # 전달되지 않은 인수는 기본값으로 가정
                        if trace:
                            print('Argument "{0}" defaulted'.format(argname))

                return func(*pargs, **kargs)         # OK: 원래 호출 실행
            return onCall
    return onDecorator
