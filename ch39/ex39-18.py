# 호출 시간 측정하기

# timerdeco1.py 파일
# 경고: 범위는 여전히 다름(2.X에서는 리스트, 3.X에서는 반복 객체)
# 경고: 타이머는 메서드에서 코딩된 대로 동작하지 않음(퀴즈의 해답 참조)

import time, sys
force = list if sys.version_info[0] == 3 else (lambda X: X)

class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0
    def __call__(self, *args, **kargs):
        start = time.clock()
        result = self.func(*args, **kargs)
        elapsed = time.clock() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result

@timer
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))

result = listcomp(5)            # 이 호출과 모든 호출에 대해 시간을 측적하고 값을 반환
listcomp(50000)
listcomp(500000)
listcomp(1000000)
print(result)
print('allTime = %s' % listcomp.alltime)    # 모든 listcomp 호출에 대한 총 소요 시간

print('')
result = mapcall(5)
mapcall(50000)
mapcall(500000)
mapcall(1000000)
print(result)
print('allTime = %s' % mapcall.alltime)     # 모든 mapcall 호출에 대한 총 소요 시간

print('\n**map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))


# py -3 timerdeco1.py 
# listcomp: 0.00002, 0.00002
# listcomp: 0.00949, 0.00951
# listcomp: 0.05872, 0.06823
# listcomp: 0.09277, 0.16100
# [0, 2, 4, 6, 8]
# allTime = 0.16100099999999998

# mapcall: 0.00002, 0.00002
# mapcall: 0.00640, 0.00642
# mapcall: 0.06709, 0.07351
# mapcall: 0.13819, 0.21170
# [0, 2, 4, 6, 8]
# allTime = 0.211698

# **map/comp = 1.315
