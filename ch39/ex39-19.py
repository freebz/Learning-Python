# 데코레이터 vs 호출당 시간 측정

def listcomp(N): [x * 2 for x in range(N)]

import timer                               # 21장의 기법
timer.total(1, listcomp, 1000000)
# (0.1311631202697754, None)

import timeit
timeit.timeit(number=1, stmt=lambda: listcomp(1000000))
# 0.12949147200561129
