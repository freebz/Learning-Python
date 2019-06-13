# 반복 객체의 아이템들을 결합하기: reduce

from functools import reduce    # 3.X에서만 임포트
reduce((lambda x, y: x + y), [1, 2, 3, 4])
# 10
reduce((lambda x, y: x * y), [1, 2, 3, 4])
# 24


L = [1,2,3,4]
res = L[0]
for x in L[1:]:
    res = res + x

res
# 10


def myreduce(function, sequence):
    tally = sequence[0]
    for next in sequence[1:]:
        tally = function(tally, next)
    return tally

myreduce((lambda x, y: x + y), [1, 2, 3, 4, 5])
# 15
myreduce((lambda x, y: x * y), [1, 2, 3, 4, 5])
# 120


import operator, functools
functools.reduce(operator.add, [2, 4, 6]) # 함수 기반의 +
# 12
functions.reduce((lambda x, y: x + y), [2, 4, 6])
# 12
