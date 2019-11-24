# 데코레이터 인수 추가하기

def timer(label=''):
    def decorator(func):
        def onCall(*args):      # 다중 레벨 상태 유지
            ...                 # args는 함수에 전달
            func(*args)         # func은 유효 범위에 유지
            print(label, ...    # label은 유효 범위에 유지
        return onCall
    return decorator            # 실제 데코레이터 반환

@timer('==>')                   # listcomp = timer('==>')(listcomp)
def listcomp(N): ...            # listcomp는 새로운 onCall과 재결합

listcomp(...)                   # 실제 onCall 호출


import time

def timer(label='', trace=True):               # 데코레이터 인수가 있을 때: 인수 유지
    class Timer:
        def __init__(self, func):              # @ 데코레이션 시: 데코레이트된 함수 유지
            self.func = func
            self.alltime = 0
        def __call__(self, *args, **kargs):    # 호출 시: 원래 함수 호출
            start = time.clock()
            result = self.func(*args, **kargs)
            elapsed = time.clock() - start
            self.alltime += elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(format % values)
            return result
    return Timer
