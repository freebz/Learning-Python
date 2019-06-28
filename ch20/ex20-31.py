# 범위와 컴프리헨션 표현식 변수들

# py -3
(X for X in range(5))
# <generator object <genexpr> at 0x7f996c25a830>
X
# NameError: name 'X' is not defined

X = 99
[X for X in range(5)]           # 3.X에서 제너레이터, 집합, 딕셔너리, 그리고
# [0, 1, 2, 3, 4]               # 리스트는 이름을 지역화하지만
X
# 99

Y = 99
for Y in range(5): pass         # 루프문은 이름을 지역화하지 않음

Y
# 4


X = 'aaa'
def func():
    Y = 'bbb'
    print(''.join(Z for Z in X + Y)) # Z 컴프리헨션, Y지역, X전역

func()
# aaabbb


# py -2
(X for X in range(5))
# <generator object <genexpr> at 0x7f996c25a9e8>
X
# NameError: name 'X' is not defined

X = 99
[X for X in range(5)]           # 2.X: 리스트는 이름을 지역화하지 않음
# [0, 1, 2, 3, 4]
X
# 4

Y = 99
for Y in range(5): pass         # for 루프는 2.X, #.X에서 이름을 지역화하지 않음

Y
# 4
