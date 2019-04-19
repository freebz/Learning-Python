# for 루프에서 튜플 할당

T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:                # 튜플 할당
    print(a, b)

# 1 2
# 3 4
# 5 6


D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(key, '=>', D[key])    # 딕셔너리 키를 반복자와 인덱스로 사용

# a => 1
# b => 2
# c => 3

list(D.items())
# [('a', 1), ('b', 2), ('c', 3)]

for (key, value) in D.items():
    print(key, '=>', value)     # 키와 값을 모두 반복

# a => 1
# b => 2
# c => 3



T
# [(1, 2), (3, 4), (5, 6)]

for both in T:
    a, b = both                 # 동일한 수동 할당
    print(a, b)                 # 2.X: 튜플을 '()'로 둘러싸서 출력

# 1 2
# 3 4
# 5 6


((a, b), c) = ((1, 2), 3)       # 중첩된 시퀀스 또한 동작함
a, b, c
# (1, 2, 3)

for ((a, b), cJ) in [((1, 2), 3), ['XY', 6]]: print(a, b, c)

# 1 2 3
# X Y 3
