# 메타클래스 vs 슈퍼클래스

class A(type): attr = 1
class B(metaclass=A): pass      # B는 메타클래스의 인스턴스. 메타의 속성을 얻음
I = B()                         # I는 메타가 아니라 클래스로부터 상속!
B.attr
# 1
I.attr
# AttributeError: 'B' object has no attribute 'attr'
'attr' in B.__dict__, 'attr' in A.__dict__
# (False, True)


class A: attr = 1
class B(A): pass                # I는 클래스와 슈퍼클래스로부터 상속받음
I = B()
B.attr
# 1
I.attr
# 1
'attr' in B.__dict__, 'attr' in A.__dict__
# (False, True)


class M(type): attr = 1
class A: attr = 2
class B(A, metaclass=M): pass   # 슈퍼클래스는 메타클래스에 우선함
I = B()
B.attr, I.attr
# (2, 2)
'attr' in B.__dict__, 'attr' in A.__dict__, 'attr' in M.__dict__
# (False, True, True)


class M(type): attr = 1
class A: attr = 2
class B(A): pass
class C(B, metaclass=M): pass       # Super는 meta보다 2레벨 위: 여전히 이김!
I = C()
I.attr, C.attr
# (2, 2)
[x.__name__ for x in C.__mro__]     # MRO에 대한 모든 것은 32장 참조
# ['C', 'B', 'A', 'object']


I.__class__                     # 상속에 의해 따름: 인스턴스의 클래스
# <class '__main__.C'>
C.__bases__                     # 상속에 의해 따름: 클래스의 슈퍼클래스
# (<class '__main__.B'>,)
C.__class__                     # 인스턴스 획득에 의해 따름: 메타클래스
# <class '__main__.M'>
C.__class__.attr                # 메타클래스 속성을 가져오는 다른 방식
# 1
