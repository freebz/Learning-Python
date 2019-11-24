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
