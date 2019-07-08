# 3.X에서 키워드 전용 인수 사용하기

# timer3.py 파일(3.X에서만 동작한다)
"""
timer2.py와 사용법이 같지만, 단순한 코드에 대해 딕셔너리의 pop 대신 3.X 키워드 전용 기본 인수를 사용한다.
이 코드는 range()가 제너레이터인 3.X에서만 정상 동작한다.
"""
import time, sys
timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(func, *pargs, _reps=1000, **kargs):
    start = timer()
    for i in range(_reps):
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(func, *pargs, _reps=5, **kargs):
    best = 2 ** 32
    for i in range(_reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

def bestoftotal(func, *pargs, _reps1=5, **kargs):
    return min(total(func, *pargs, **kargs) for i in range(_reps1))
