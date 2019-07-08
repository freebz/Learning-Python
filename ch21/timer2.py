# timer2.py 파일(2.X 그리고 3.X)
"""
total(spam, 1, 2, a = 3, b = 4, _reps = 1000)은 spam(1, 2, a = 3, b =4)을 _reps 횟수만큼 호출하고
시간을 측정하여 마지막 실행 결과와 함께 실행하는 데 걸린 전체 시간을 반환한다.
bestof(spam, 1, 2, a = 3, b = 4, _reps = 5)는 시스템 부하에 의한 영향을 제거하기 위해 N번 반복 호출을 통해
가장 빠른 결과를 찾는 타이머를 실행하며, _reps 횟수만큼 테스트를 수행하고 가장 빠른 시간을 반환한다.

bestoftotal(spam, 1, 2, a = 3, b = 4, _reps1 = 5, _reps = 1000)는 함수를 반복 실행하는 전체 시간 중에 가장 빠른
시간을 구하는테스트를 실행하며. (_reps 횟수만큼 반복 실행하는데 걸린 시간)을 _reps1 횟수만큼 반복 실행하여
가장 빠른 시간을 구한다
"""

import time, sys
timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000) # 전달 또는 기본 반복 횟수
    repslist = list(range(_reps))    # 2.X 리스트 호환을 위한 부분
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 5)
    best = 2 ** 32
    for i in range(_reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

def bestoftotal(func, *pargs, **kargs):
    _reps1 = kargs.pop('_reps1', 5)
    return min(total(func, *pargs, **kargs) for i in range(_reps1))
