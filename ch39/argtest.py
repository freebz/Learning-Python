"""
파일 argtest.py: (3.X + 2.X) 임의의 함수 메서드에 전달된 인수를 위해
임의의 전달된 검증을 수행하는 함수 데코레이터. 범위와 타입 테스트가 두 사례임
valuetest는 인수의 값에 대해 더 읨의의 테스트를 수행함

인수들은 키워드에 의해 기술되어 데코레이터에 전달됨
실제 호출에서 인수들은 위치 또는 키워드에 의해 전달되고 기본 인수는 생략될 수 있음
이 예제의 사례는 다음 셀프 테스트 코드를 참조하자

경고: 호출 프록시의 인수들이 다르기 때문에 중첩 구조를 완전히 지원하지 않음
데코레이트된 함수의 *args에 전달된 추가 인수들은 검증하지 않음
그리고 사례를 하나의 단위로 포장했다는 점을 제외하고 assert보다 쉽지 않음
"""
trace = False


def rangetest(**argchecks):
    return argtest(argchecks, lambda arg, vals: arg < vals[0] or arg > vals[1])

def typetest(**argchecks):
    return argtest(argchecks, lambda arg, type: not isinstance(arg, type))

def valuetest(**argchecks):
    return argtest(argchecks, lambda arg, tester: not tester(arg))


def argtest(argchecks, failif):        # failif + criteria에 따라 인수 검증
    def onDecorator(func):             # onCall은 func, argchecks, failif를 유지함
        if not __debug__:              # "python -O main.py args..."라면 아무 동작을 하지 않음
            return func
        else:
            code = func.__code__
            expected = list(code.co_varnames[:code.co_argcount])
            def onError(argname, criteria):
                errfmt = '%s argument "%s" not %s'
                raise TypeError(errfmt % (func.__name__, argname, criteria))

            def onCall(*pargs, **kargs):
                positionals = expected[:len(pargs)]
                for (argname, criteria) in argchecks.items():   # 테스트할 모든 것에 대해
                    if argname in kargs:                        # 이름에 의해 전달
                        if failif(kargs[argname], criteria):
                            onError(argname, criteria)
                    elif argname in positionals:                # 위치에 의해 전달
                        position = positionals.index(argname)
                        if failif(pargs[position], criteria):
                            onError(argname, criteria)
                    else:                                  # 전달되지 않으면 기본 인수
                        if trace:
                            print('Argument "%s" defaulted' % argname)
                return func(*pargs, **kargs)               # OK: 원래 호출 실행
            return onCall
    return onDecorator

if __name__ == '__main__':
    import sys
    def fails(test):
        try:    result = test()
        except: print('[%s]' % sys.exc_info()[1])
        else:   print('?%s?' % result)

    print('---------------------------------------------------')
    # 활용 사례: 범위, 타입

    @rangetest(m=(1, 12), d=(1, 31), y=(1900, 2013))
    def date(m, d, y):
        print('date = %s/%s/%s' % (m, d, y))

    date(1, 2, 1960)
    fails(lambda: date(1, 2, 3))

    @typetest(a=int, c=float)
    def sum(a, b, c, d):
        print(a + b + c + d)

    sum(1, 2, 3.0, 4)
    sum(1, d=4, b=2, c=3.0)
    fails(lambda: sum('spam', 2, 99, 4))
    fails(lambda: sum(1, d=4, b=2, c=99))

    print('---------------------------------------------------')
    # 임의의/혼합된 테스트
    @valuetest(word1=str.islower, word2=(lambda x: x[0].isupper()))
    def msg(word1='mighty', word2='Larch', label='The'):
        print('%s %s %s' % (label, word1, word2))

    msg()                              # word1과 word2는 기본 인수
    msg('majestic', 'Moose')
    fails(lambda: msg('Giant', 'Redwood'))
    fails(lambda: msg('great', word2='elm'))

    print('---------------------------------------------------')
    # 수동으로 타입과 범위 테스트

    @valuetest(A=lambda x: isinstance(x, int), B=lambda x: x > 0 and x < 10)
    def manual(A, B):
        print(A + B)

    manual(100, 2)
    fails(lambda: manual(1.99, 2))
    fails(lambda: manual(100, 20))

    print('---------------------------------------------------')
    # 중첩: 원래 함수에 프록시를 중첩함으로써, 둘 모두 실행
    # 현안: 외부 계층은 위치적 인수가 받아야 할 검증을 하지 않음
    # 프록시 함수의 상이한 인수 시그니처 호출하기
    # trace=True이면, 이들 중 마지막을 제외한 모두에 "X"가 있음
    # 프록시의 시그니처로 인해 기본 인수로 분류됨

    @rangetest(X=(1, 10))
    @typetest(Z=str)                       # 가장 안쪽에서만 위치적 인수를 검증함
    def nester(X, Y, Z):
        return('%s-%s-%s' % (X, Y, Z))

    print(nester(1, 2, 'spam'))            # 원래의 함수는 적절하게 실행함
    fails(lambda: nester(1, 2, 3))         # 중첩된 타입 테스트가 실행됨: 위치적 인수
    fails(lambda: nester(1, 2, Z=3))       # 중첩된 타입 테스트가 실행됨: 키워드 인수
    fails(lambda: nester(0, 2, 'spam'))    # <== 외부 범위 테스트가 실행되지 않음: 위치적 인수
    fails(lambda: nester(X=0, Y=2, Z='spam'))     # 외부 범위 테스트는 실행됨: 키워드 임수
