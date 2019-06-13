# 왜 람다를 사용하는가?

L = [lambda x: x ** 2,          # 인라인 함수 정의
     lambda x: x ** 3,
     lambda x: x ** 4]          # 세 개의 호출 가능한 함수의 리스트

for f in L:
    print(f(2))                 # 4, 8, 16 출력

print(L[0](3))                  # 9 출력


def f1(x): return x ** 2
def f2(x): return x ** 3        # 명명된 함수 정의
def f3(x): return x ** 4

L = [f1, f2, f3]                # 이름으로 참조

for f in L:
    print(f(2))                 # 4, 8, 16 출력

print(L[0](3))                  # 9 출력
