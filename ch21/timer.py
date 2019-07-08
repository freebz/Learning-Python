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
