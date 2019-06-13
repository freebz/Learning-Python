# 또 다른 방법

def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:])             # 삼중 표현식 사용

def mysum(L):
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:])    # 모든 타입, 최소 하나

def mysum(L):
    first, *rest = L
    return first if not rest else first + mysum(rest)  # 3.X 확장 시퀀스 할당 사용


mysum([1])                      # mysum([])은 위의 아래 둘에서 실패하지만
# 1
mysum([1, 2, 3, 4, 5])
# 15
mysum(('s', 'p', 'a', 'm'))     # 다양한 타입과 동작함
# 'spam'
mysum(['spam', 'ham', 'eggs'])
# 'spamhameggs'


def mysum(L):
    if not L: return 0
    return nonempty(L)          # 나를 호출하는 함수를 호출

def nonempty(L):
    return L[0] + mysum(L[1:])  # 간접 재귀

mysum([1.1, 2.2, 3.3, 4.4])
# 11.0
