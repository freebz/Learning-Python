# 공유 참조와 등가 비교

x = 42
x = 'shrubbery'                 # 42는 지금 바로 반환될까?


L = [1, 2, 3]
M = L                           # M과 L은 같은 객체를 참조함
L == M                          # 값이 같음
# True
L is M                          # 객체가 같음
# True


L = [1, 2, 3]
M = [1, 2, 3]                   # M과 L은 다른 객체를 참조함
L == M                          # 값이 같음
# True
L is M                          # 객체가 다름
# False


X = 42
Y = 42                          # 두 개의 서로 다른 객체여야 함
X == Y
# True
X is Y                          # 같은 객체: 캐시가 동작한 것이다!
# True


import sys
sys.getrefcount(1)              # 1의 공유된 메모리에 대해 647개의 포인터가 있음
# 647
