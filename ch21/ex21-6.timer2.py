# 또 다른 타이머 모듈들

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


import sys, timer2
...
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (total, result) = timer2.bestoftotal(test, _reps1=5, _reps=1000)

# 또는:
#   (total, result) = timer2.bestoftotal(test)
#   (total, result) = timer2.bestof(test, _reps = 5)
#   (total, result) = timer2.total(test, _reps = 1000)
#   (bestof, (total, result)) = timer2.bestof(timer2.total, test, _reps = 5)

    print ('%-9s: %.5f => [%s...%s]' %
           (test.__name__, total, result[0], result[-1]))


from timer2 import total, bestof, bestoftotal
total(pow, 2, 1000)[0]          # 2 ** 1000, 기본 1,000회 반복
# 0.0029562534118596773
total(pow, 2, 1000, _reps=1000)[0] # 2 ** 1000, 1,000회 반복
# 0.0029733585316193967
total(pow, 2, 1000, _reps=1000000)[0] # 2 ** 1000, 1백만회 반복
# 1.245167814889865

bestof(pow, 2, 100000)[0]       # 2 ** 100K, 기본 5회 반복
# 0.0007550688578703557
bestof(pow, 2, 100000, _reps=30)[0] # 2 ** 1M, 최고 30
# 0.004040229286800923

bestoftotal(str.upper, 'spam', _reps1=30, _reps=1000) # 최고 30, 총 1K
# (0.0004945823198454491, 'SPAM')
bestof(total, str.upper, 'spam', _reps=30) # 중첩된 호출 또한 동작
# (0.0005463863968202531, (0.0004994694969298052, 'SPAM'))


def spam(a, b, c, d): return a + b + c + d

total(spam, 1, 2, c=3, d=4, _reps=1000)
# (0.0009730369554290519, 10)
bestof(spam, 1, 2, c=3, d=4, _reps=1000)
# (9.774353202374186e-07, 10)
bestoftotal(spam, 1, 2, c=3, d=4, _reps1=1000, _reps=1000)
# (0.00037289161070930277, 10)
bestoftotal(spam, *(1, 2), _reps1=1000, _reps=1000, **dict(c=3, d=4))
# (0.00037289161070930277, 10)
