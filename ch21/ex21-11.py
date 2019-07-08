# 또 다른 사용 모드

python -m timeit -n 1000 -r 3 "L = [1,2,3,4,5]" "M = [x + 1 for x in L]"
1000 loops, best of 3: 0.956 usec per loop

python -m timeit -n 1000 -r 3 -s "L = [1,2,3,4,5]" "M = [x + 1 for x in L]"
1000 loops, best of 3: 0.775 usec per loop


from timeit import repeat

min(repeat(number=1000, repeat=3,
           setup='from mins import min1, min2, min3\n'
           'vals=list(range(10000))',
    stmt = min3(*vals))
#0.0387865921275079

min(repeat(number=1000, repeat=3,
    setup='from mins import min1, min2, min3\n'
           'import random\nvals=[random.random() for i in range(10000)]',
    stmt = 'min3(*vals)'))
# 0.275656482278373


# py -3
import timeit
timeit.timeit(stmt='[x ** 2 for x in range(1000)]', number=1000) # 전체시간
# 0.5238125259325834

timeit.Timer(stmt='[x ** 2 for x in range(1000)]').timeit(1000) # 클래스 API
# 0.5282652329644009

timeit.repeat(stmt='[x ** 2 for x in range(1000)]', number=1000, repeat=3)
# [0.5299034147194845, 0.5082454007998365, 0.5095136232504416]

def testcase():
    y = [x ** 2 for x in range(1000)] # 호출 가능한 객체 또는 코드 문자열

min(timeit.repeat(stmt=testcase, number=1000, repeat=3))
# 0.5073828140463377
