# 변경: 메서드 교체

class A:
    def method(self): print('A.method'); super().method()
class B(A):
    def method(self): print('B.method'); super().method()
class C:
    def method(self): print('C.method')    # super가 없음: 체인의 닻 역할을 해야!
class D(B, C):
    def method(self): print('D.method'); super().method()
X = D()
X.method()
# D.method
# B.method
# A.method                        # 자동으로 MRO에 따라 모두에게 전달
# C.method


# 만약 클래스가 super의 기본값을 완전히 교체해야 한다면 어떻게 될까?

class B(A):
    def method(self): print('B.method')    # super를 버리고 A의 메서드를 교체
class D(B, C):
    def method(self): print('D.method'); super().method()
X = D()
X.method()
# D.method
# B.method                        # 하지만 이 교체는 호출 체인을 깨뜨림...

class D(B, C):
    def method(self): print('D.method'); B.method(self); C.method(self)
D().method()
# D.method
# B.method
# C.method                        # 명시적 호출로 회귀...
