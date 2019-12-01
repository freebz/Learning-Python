# decotools.py 파일: 데코레이터 도구들을 하나로 모음
import time

def tracer(func):                       # __call__을 가진 클래스가 아니라 함수를 사용
    calls = 0                           # 그렇지 않으면 self는 데코레이터 인스턴스만
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall

def timer(label='', trace=True):        # 데코레이터 인수에 대해: 인수를 저장
    def onDecorator(func):              # @ 데코레이션 시: 데코레이트된 함수를 저장
        def onCall(*args, **kargs):     # 호출 시: 원래 버전을 호출
            start = time.clock()        # 상태 정보는 범위 + 함수 속성
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
