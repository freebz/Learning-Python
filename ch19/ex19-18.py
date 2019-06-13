# 반복 객체에서 아이템 선택하기: filter

list(range(-5, 5))              # 3.X에서 반복 객체
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

list(filter((lambda x: x > 0), range(-5, 5))) # 3.X에서 반복 객체
# [1, 2, 3, 4]


res = []
for x in range(-5, 5):          # filter에 해당하는 문
    if x > 0:
        res.append(x)

res
# [1, 2, 3, 4]


[x for x in range(-5, 5) if x > 0] # ()를 사용하면 제네레이터 반환
# [1, 2, 3, 4]
