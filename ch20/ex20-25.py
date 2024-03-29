# 제너레이터를 남용하지 말자: EIBTI

# 또 다른 측면에서: 메모리, 지연 시간, 간결성, 표현력

import math
math.factorial(10)              # 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
# 3628800
from permute import permute1, permute2
seq = list(range(10))
p1 = permute1(seq)              # 2GHz 쿼드 코어 장비에서 37초가 걸리며,
                                # 360만 수를 가진 리스트를 만듦
len(p1), p1[0], p1[1]
# (3628800, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 9, 8])


p2 = permute2(seq)              # 제너레이터를 즉시 반환하며,
next(p2)                        # 요청 시에 각각의 결과를 빠르게 생성함
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
next(p2)
# [0, 1, 2, 3, 4, 5, 6, 7, 9, 8]

p2 = list(permute2(seq))        # 비록 비현실적이지만 약 28초가 걸림
p1 == p2
# True


math.factorial(50)
# 30414093201713378043612608166064768844377641568960512000000000000
p3 = permute2(list(range(50)))
next(p3)                        # permute1은 여기서 고려 대상이 아님!
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]


import random
math.factorial(20)              # 여기서 permute1은 고려 대상이 아님
# 2432902008176640000
seq = list(range(20))

random.shuffle(seq)             # 먼저 시퀀스를 무작위로 뒤섞음
p = permute2(seq)
next(p)
# [10, 17, 4, 14, 11, 3, 16, 19, 12, 8, 6, 5, 2, 15, 18, 7, 1, 0, 13, 9]
next(p)
# [10, 17, 4, 14, 11, 3, 16, 19, 12, 8, 6, 5, 2, 15, 18, 7, 1, 0, 9, 13]

random.shuffle(seq)
p = permute2(seq)
next(p)
# [16, 1, 5, 14, 15, 12, 0, 2, 6, 19, 10, 17, 11, 18, 13, 7, 4, 9, 8, 3]
next(p)
# [16, 1, 5, 14, 15, 12, 0, 2, 6, 19, 10, 17, 11, 18, 13, 7, 4, 9, 3, 8]
