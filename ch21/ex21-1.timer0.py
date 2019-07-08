# 타이밍 모듈 직접 만들기

# timer0.py 파일
import time
def timer(func, *args):         # 단순한 타이밍 함수
    start = time.clock()
    for i in range(1000):
        func(*args)
    return time.clock() - start # 총 경과 시간(초)


from timer0 import timer
timer(pow, 2, 1000)             # pow(2, 1000)을 1,000번 호출한 시간
# 0.00296260674205626
timer(str.upper, 'spam')        # 'spam'.upper()을 1,000번 호출한 시간
# 0.0005165746166859719


# timer.py 파일
"""
함수 호출을 측정하기 위해 직접 만든 타이밍 도구.
함수를 반복 실행하는 전체 시간, 가장 빠른 시간, 함수를 반복 실행하는 전체 시간 중에 가장 빠른 시간을 측정
"""

import time, sys
timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(reps, func, *pargs, **kargs):
    """
    func()를 reps만큼 실행하는 전체 시간
    (전체 시간, 마지막 결과)를 반환
    """
    repslist = list(range(reps)) # 시간 측정 범위 밖으로 이동됐으며, 2.X, 3.X에서 동일하게 동작함
    start = timer()              # 또는 3.3+에서는 pref_counter를 사용
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(reps, func, *pargs, **kargs):
    """
    func()를 reps만큼 반복 실행하며 그중에 가장 빠른 시간
    (가장 빠른 시간, 마지막 결과)를 반환
    """
    best = 2 ** 32              # 136년이면 충분히 큼
    for i in range(reps):       # range는 여기서 측정되지 않음
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start # 또는 reps=1로 total() 호출
        if elapsed < best: best = elapsed # 또는 리스트에 추가하고 min() 호출
    return (best, ret)

def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    함수를 반복 실행하는 전체 시간 중에 가장 빠른 시간:
    (func를 reps2만큼 실행한 전체 시간)을 reps1만큼 실행한 것 중에 가장 빠른 시간
    """
    return bestof(reps1, total, reps2, func, *pargs, **kargs)


import timer
timer.total(1000, pow, 2, 1000)[0] # 이전 timer0 결과와 비교해 보자
# 0.0029542985410557776
timer.total(1000, str.upper, 'spam') # (시간, 마지막 호출의 결과) 반환
# 0.000504845391709686, 'SPAM')

timer.bestof(1000, str.upper, 'spam') # 총 시간의 1/1000
(4.887177027512735e-07, 'SPAM')
timer.bestof(1000, pow, 2, 1000000 )[0]
# 0.00393515497972885

timer.bestof(50, timer.total, 1000, str.upper, 'spam')
# (0.005468751145372153, (0.0005004469323637295, 'SPAM'))
timer.bestoftotal(50, 1000, str.upper, 'spam')
# (0.000566912540591602, (0.0005195069228989269, 'SPAM'))


min(timer.total(1000, str.upper, 'spam') for i in range(50))
# (0.0005155971812769167, 'SPAM')


((((2 ** 32) / 60) / 60) / 24) / 365 # 며칠이 남음
# 136.19251953323186
((((2 ** 32) // 60) // 60) // 24) // 365 # 반내림: 5장 참고
# 136
