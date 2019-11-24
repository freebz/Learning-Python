"""
timerdeco.py (3.X + 2.X) 파일
함수와 메서드 모두에 대한 타이머 데코레이터 호출
"""
import time

def timer(label='', trace=True):            # 데코레이터인수: 인수 유지
    def onDecorator(func):                  # @: 데코레이터 함수 유지
        def onCall(*args, **kargs):         # 원래 함수 호출
            start = time.clock()            # 상태는 범위 + 함수 속성임
            result = func(*args, **kargs)
            elapsed = time.clock() - start
            onCall.alltime += elapsed
            if trace:
                format = '%s%s: %.5f, %.5f'
                values = (label, func.__name__, elapsed, onCall.alltime)
                print(format % values)
            return result
        onCall.alltime = 0
        return onCall
    return onDecorator
