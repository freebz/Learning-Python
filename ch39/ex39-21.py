# 데코레이터 인수를 이용하여 시간 측정하기

import sys
from timerdeco2 import timer
force = list if sys.version_info[0] == 3 else (lambda X: X)

@timer(label='[CCC]==>')
def listcomp(N):                              # listcomp = timer(...)(listcomp)
    return [x * 2 for x in range(N)]          # listcomp(...)는 Timer.__call__ 실행

@timer(trace=True, label='[MMM]==>')
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))

for func in (listcomp, mapcall):
    result = func(5)                          # 이 호출과 모든 호출에 대한 시간 측정, 값을 반환
    func(50000)
    func(500000)
    func(1000000)
    print(result)
    print('allTime = %s\n' % func.alltime)    # 모든 호출에 대한 총 소요 시간

print('**map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))


# py -3 testseqs.py
# [CCC]==> listcomp: 0.00001, 0.00001
# [CCC]==> listcomp: 0.00492, 0.00493
# [CCC]==> listcomp: 0.04605, 0.05098
# [CCC]==> listcomp: 0.09322, 0.14420
# [0, 2, 4, 6, 8]
# allTime = 0.1442

# [MMM]==> mapcall: 0.00002, 0.00002
# [MMM]==> mapcall: 0.00721, 0.00723
# [MMM]==> mapcall: 0.07050, 0.07772
# [MMM]==> mapcall: 0.13717, 0.21489
# [0, 2, 4, 6, 8]
# allTime = 0.21489000000000003

# **map/comp = 1.49


from timerdeco2 import timer
@timer(trace=False)                 # 추적 X, 총 소요 시간 집계
def listcomp(N):
    return [x * 2 for x in range(N)]

x = listcomp(5000)
x = listcomp(5000)
x = listcomp(5000)
listcomp.alltime
# 0.0014610000000001566
listcomp
# <timerdeco2.timer.<locals>.Timer object at 0x7ffab495a208>

@timer(trace=True, label='\t=>')    # 추적 시작, 사용자 정의 레이블
def listcomp(N):
    return [x * 2 for x in range(N)]

x = listcomp(5000)
# 	=> listcomp: 0.00059, 0.00059
x = listcomp(5000)
# 	=> listcomp: 0.00063, 0.00122
x = listcomp(5000)
# 	=> listcomp: 0.00075, 0.00197
listcomp.alltime
# 0.0019689999999998875
