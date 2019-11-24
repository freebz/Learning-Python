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
