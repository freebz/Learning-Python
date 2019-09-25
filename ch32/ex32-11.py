# 충돌에 대한 명시적 해결

class A:       attr = 1         # 고전 클래스
class B(A):    pass
class C(A):    attr = 2
class D(B, C): attr = C.attr    # <== 오른쪽에 있는 C를 선택

x = D()
x.attr                          # 새로운 형식의 순서처럼 동작(모든 3.X)
# 2


class A(object): attr = 1       # 새 형식 클래스
class B(A):      pass
class C(A):      attr = 2
class D(B, C):   attr = B.attr  # <== 상위에 있는 A.attr를 선택

x = D()
x.attr                          # 고전 클래스처럼 동작(2.X 기본 클래스)
# 1


class A:
    def meth(s): print('A.meth')

class C(A):
    def meth(s): print('C.meth')

class B(A):
    pass

class D(B, C): pass             # 기본 검색 순서 사용
x = D()                         # 클래스 유형에 따라 달라짐
x.meth()                        # 2.X에서는 고전 형식의 순서가 기본임
# A.meth

class D(B, C): meth = C.meth    # <== C의 메서드 선택: 새로운 형식(3.X)
x = D()
x.meth()
# C.meth

class D(B, C): meth = B.meth    # <== B의 메서드 선택: 고전 형식
x = D()
x.meth()
# A.meth


class D(B, C):
    def meth(self):             # 더 낮은 메서드를 재정의
        ...
        C.meth(self)            # <== 호출에 의해 C의 메서드를 선택
