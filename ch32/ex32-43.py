# 결합: 혼합 클래스에의 적용

# 혼합 클래스는 메서드 집합들 간에 공통 요소가 없을 때 동작함

class A:
    def other(self): print('A.other')
class Mixin(A):
    def other(self): print('Mixin.other'); super().other()

class B:
    def method(self): print('B.method')
class C(Mixin, B):
    def method(self): print('C.method'); super().other(); super().method()

C().method()
# C.method
# Mixin.other
# A.other
# B.method

C.__mro__
# (<class '__main__.C'>, <class '__main__.Mixin'>, <class '__main__.A'>,
# <class '__main__.B'>, <class 'object'>)


class C(B, Mixin):
    def method(self): print('C.method'); super().other(); super().method()

C().method()
# C.method
# Mixin.other
# A.other
# B.method

C.__mro__
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.Mixin'>,
# <class '__main__.A'>, <class 'object'>)


# 명시적인 다이아몬드에서도 동작함

class A:
    def other(self): print('A.other')
class Mixin(A):
    def other(self): print('Mixin.other'); super().other()
class B(A):
    def method(self): print('B.method')
class C(Mixin, B):
    def method(self): print('C.method'); super().other(); super().method()

C().method()
# C.method
# Mixin.other
# A.other
# B.method

C.__mro__
# (<class '__main__.C'>, <class '__main__.Mixin'>, <class '__main__.B'>,
# <class '__main__.A'>, <class 'object'>)

# 혼합 클래스의 순서를 섞어도 동작함

class C(B, Mixin):
    def method(self): print('C.method'); super().other(); super().method()
C().method()
# C.method
# Mixin.other
# A.other
# B.method

C.__mro__
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.Mixin'>,
# <class '__main__.A'>, <class 'object'>)


# 하지만 직접적인 호출도 동작함. 명시적인 것이 암묵적인 것보다 더 나음

class C(Mixin, B):
    def method(self): print('C.method'); Mixin.other(self); B.method(self)

X = C()
X.method()
# C.method
# Mixin.other
# A.other
# B.method


# 하지만 비독자적인 메서드의 경우, super는 지나치게 강한 결합을 생성함

class A:
    def method(self): print('A.method')
class Mixin(A):
    def method(self): print('Mixin.method'); super().method()
Mixin().method()
# Mixin.method
# A.method

class B(A):
    def method(self): print('B.method')    # 여기에서 super는 B 다음에 A를 호출
class C(Mixin, B):
    def method(self): print('C.method'); super().method()
C().method()
# C.method
# Mixin.method
# B.method                        # 이 맥락에서만 A를 누락!


# 하지만 직접 호출은 그렇지 않다. 사용 맥락에 영향을 받지 않음

class A:
    def method(self): print('A.method')
class Mixin(A):
    def method(self): print('Mixin.method'); A.method(self)    # C는 무관함

class C(Mixin, B):
    def method(self): print('C.method'); Mixin.method(self)
C().method()
# C.method
# Mixin.method
# A.method
