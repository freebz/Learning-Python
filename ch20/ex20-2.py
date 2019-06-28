# 테스트와 중첩된 루프 추가하기: filter

[x for x in range(5) if x % 2 == 0]
# [0, 2, 4]

list(filter((lambda x: x % 2 == 0), range(5)))
# [0, 2, 4]

res = []
for x in range(5):
    if x % 2 == 0:
        res.append(x)

res
# [0, 2, 4]


[x ** 2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]


list(map((lambda x: x**2), filter((lambda x: x % 2 == 0), range(10))))
# [0, 4, 16, 36, 64]
