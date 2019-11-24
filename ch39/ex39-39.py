# 키워드 인수와 기본값도 수용할 수 있도록 일반화하기

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


"""
파일 rangetest_test.py(3.X + 2.X)
주석 처리된 줄은 셸 명령 라인에서 "python -O"을 사용하지 않으면 TypeError 발생
"""
from __future__ import print_function # 2.X
from rangetest import rangetest

# 함수 테스트: 위치와 키워드 인수

@rangetest(arg=(0, 120))                # persinfo = rangetest(...)(persinfo)
def persinfo(name, age):
    print('%s is %s years old' % (name, age))

@rangetest(M=(1, 12), D=(1, 31), Y=(0, 2013))
def birthday(M, D, Y):
    print('birthday = {0}/{1}/{2}'.format(M, D, Y))

persinfo('Bob', 40)
persinfo(age=40, name='Bob')
birthday(5, D=1, Y=1963)
#persinfo('Bob', 150)
#persinfo(age=150, name='Bob')
#birthday(5, D=40, Y=1963)

# 메서드 테스트: 위치와 키워드 인수

class Person:
    def __init__(self, name, job, pay):
        self.job = job
        self.pay = pay
                                        # giveRaise = rangetest(...)(giveRaise)
    @rangetest(percent=(0.0, 1.0))      # 이름 또는 위치로 전달되는 퍼센트
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

bob = Person('Bob Smith', 'dev', 100000)
sue = Person('Sue Jones', 'dev', 100000)
bob.giveRaise(.10)
sue.giveRaise(percent=.20)
print(bob.pay, sue.pay)
#bob.giveRaise(1.10)
#bob.giveRaise(percent=1.20)

# 생략된 기본 인수 테스트: 생략
@rangetest(a=(1, 10), b=(1, 10), c=(1, 10), d=(1, 10))
def omitargs(a, b=7, c=8, d=9):
    print(a, b, c, d)

omitargs(1, 2, 3, 4)
omitargs(1, 2, 3)
omitargs(1, 2, 3, d=4)
omitargs(1, d=4)
omitargs(d=4, a=1)
omitargs(1, b=2, d=4)
omitargs(d=8, c=7, a=1)

#omitargs(1, 2, 3, 11)                  # 잘못된 d
#omitargs(1, 2, 11)                     # 잘못된 c
#omitargs(1, 2, 3, d=11)                # 잘못된 d
#omitargs(11, d=4)                      # 잘못된 a
#omitargs(d=4, a=11)                    # 잘못된 a
#omitargs(1, b=11, d=4)                 # 잘못된 b
#omitargs(d=8, c=7, a=11)               # 잘못된 a


# python rangetest_test.py
# Argument "arg" defaulted
# Bob is 40 years old
# Argument "arg" defaulted
# Bob is 40 years old
# birthday = 5/1/1963
# 110000 120000
# 1 2 3 4
# Argument "d" defaulted
# 1 2 3 9
# 1 2 3 4
# Argument "b" defaulted
# Argument "c" defaulted
# 1 7 8 4
# Argument "b" defaulted
# Argument "c" defaulted
# 1 7 8 4
# Argument "c" defaulted
# 1 2 8 4
# Argument "b" defaulted
# 1 7 7 8


# TypeError: giveRaise argument "percent" not in 0.0..1.0
