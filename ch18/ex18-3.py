# 출력 인자와 다수의 결괏값 흉내내기

def multiple(x, y):
    x = 2                       # 지역 이름만 변경
    y = [3, 4]
    return x, y                 # 다수의 새로운 값을 튜플로 반환

X = 1
L = [1, 2]
X, L = multiple(X, L)           # 결과를 호출자의 이름에 할당
X, L
# (2, [3, 4])
