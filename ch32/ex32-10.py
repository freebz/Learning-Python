# 다이아몬드 속성 트리에 미치는 영향

class A: attr = 1               # 고전 형식의 클래스(파이썬 2.X)
class B(A): pass                # B와 C 모두 A를 슈퍼클래스로 가짐
class C(A): attr = 2
class D(B, C): pass             # C 전에 A를 먼저 검색

x = D()
x.attr                          # 검색 순서: x, D, B, A
# 1


class A(object): attr = 1       # 새로운 형식(3.X에서 'object'는 불필요)
class B(A): pass
class C(A): attr = 2
class D(B, C): pass             # A 전에 C를 검색

x = D()
x.attr                          # 검색 순서: x, D, B, C
# 2
