# 재귀 함수

# 재귀를 이용한 더하기

def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:]) # 자신을 재귀적으로 호출
mysum([1, 2, 3, 4, 5])
# 15


def mysum(L):
    print(L)                    # 재귀 단계 추적
    if not L:                   # 각 단계에서 L은 점점 짧아짐
        return 0
    else:
        return L[0] + mysum(L[1:])

mysum([1, 2, 3, 4, 5])
# [1, 2, 3, 4, 5]
# [2, 3, 4, 5]
# [3, 4, 5]
# [4, 5]
# [5]
# []
# 15
