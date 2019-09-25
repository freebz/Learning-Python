# 협조적 다중 상속 메서드 할당

# 기본: 실제 협조적 super 호출

class B:
    def __init__(self): print('B.__init__') # 독자적인 클래스 트리의 가지들
class C:
    def __init__(self): print('C.__init__')
class D(B, C): pass

x = D()                         # 기본으로 가장 왼쪽의 것만 실행
# B.__init__


class D(B, C):
    def __init__(self):         # 전형적인 형태
        B.__init__(self)        # 이름으로 슈퍼클래스 호출
        C.__init__(self)

x = D()
# B.__init__
# C.__init__


class A:
    def __init__(self): print('A.__init__')
class B(A):
    def __init__(self): print('B.__init__'); A.__init__(self)
class C(A):
    def __init__(self): print('C.__init__'); A.__init__(self)

x = B()
# B.__init__
# A.__init__
x = C()                         # 각 슈퍼클래스는 독자적으로 동작함
# C.__init__
# A.__init__

class D(B, C): pass             # 여전히 가장 왼쪽 것만 실행
x = D()
# B.__init__
# A.__init__

class D(B, C):
    def __init__(self):         # 전형적인 형태
        B.__init__(self)        # 이름으로 양쪽 슈퍼클래스 모두 호출
        C.__init__(self)

x = D()                         # 하지만 이로써 A를 두 번 호출!
# B.__init__
# A.__init__
# C.__init__
# A.__init__


class A:
    def __init__(self): print('A.__init__')
class B(A):
    def __init__(self): print('B.__init__'); super().__init__()
class C(A):
    def __init__(self): print('C.__init__'); super().__init__()

x = B()   # B.__init__실행, self인 B의 MRO에서는 A가 다음 슈퍼클래스임
# B.__init__
# A.__init__
x = C()
# C.__init__
# A.__init__

class D(B, C): pass
x = D()  # B.__init__실행, self인 D MRO에 의하면 C가 다음 슈퍼클래스임
# B.__init__
# C.__init__
# A.__init__


B.__mro__
# (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

D.__mro__
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
# <class '__main__.A'>, <class 'object'>)
