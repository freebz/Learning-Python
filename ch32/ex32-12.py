# MRO에 대해 더 알아보기: 메서드 검색 순서

# MRO 알고리즘

# MRO 추적하기

class A: pass
class B(A): pass                # 다이아몬드: 새로운 형식에서는 순서가 달라짐
class C(A): pass                # 낮은 레벨에서 휭 우선으로 검색
class D(B, C): pass
D.__mro__
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
# <class '__main__.A'>, <class 'object'>)


class A: pass
class B(A): pass              # 다이아몬드 패턴이 아닌 경우, 고전 형식과 동일한 순서
class C: pass                 # 위로 먼저 검색한 뒤, 왼쪽에서 오른쪽으로 검색
class D(B, C): pass
D.__mro__
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>,
# <class '__main__.C'>, <class 'object'>)


class A: pass
class B: pass                   # 다이아몬드 패턴이 아닌 다른 예제: DFLR
class C(A): pass
class D(B, C): pass
D.__mro__
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
# <class '__main__.A'>, <class 'object'>)


A.__bases__                     # 슈퍼클래스 링크: 두 개의 루트에 object가 있음
# (<class 'object'>,)
B.__bases__
# (<class 'object'>,)
C.__bases__
# (<class '__main__.A'>,)
D.__bases__
# (<class '__main__.B'>, <class '__main__.C'>)


class X: pass
class Y: pass
class A(X): pass            # 비다이아몬드: 깊이 우선, 이후 왼쪽에서 오른쪽으로
class B(Y): pass            # 하지만 암묵적인 'object'는 항상 다이아몬드를 생성한다.
class D(A, B): pass
D.mro()
# [<class '__main__.D'>, <class '__main__.A'>, <class '__main__.X'>,
# <class '__main__.B'>, <class '__main__.Y'>, <class 'object'>]

X.__bases__, Y.__bases__
# ((<class 'object'>,), (<class 'object'>,))
A.__bases__, B.__bases__
# ((<class '__main__.X'>,), (<class '__main__.Y'>,))


D.mro() == list(D.__mro__)
# True
[cls.__name__ for cls in D.__mro__]
# ['D', 'A', 'X', 'B', 'Y', 'object']
