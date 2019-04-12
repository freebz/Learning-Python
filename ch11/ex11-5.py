# 유용한 편의 기능

seq
# [1, 2, 3, 4]

a, *b = seq                     # 첫 번째, 나머지
a, b
# (1, [2, 3, 4])

a, b = seq[0], seq[1:]          # 첫 번째, 나머지: 기존 방식
a, b
# (1, [2, 3, 4])


*a, b = seq                     # 나머지, 마지막
a, b
# ([1, 2, 3], 4)

a, b = seq[:-1], seq[-1]        # 나머지, 마지막: 기존 방식
a, b
# ([1, 2, 3], 4)
