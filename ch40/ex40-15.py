# 상속: 이야기의 전모

class M1(type): attr1 = 1               # 메타클래스 상속 트리
class M2(M1): attr2 = 2                 # __bases__.__class__.__mro__를 얻음

class C1: attr3 = 3                     # 슈퍼클래스 상속 트리
class C2(C1,metaclass=M2): attr4 = 4    # __bases__.__class__.__mro__를 얻음

I = C2()                                # I는 __class__를 가지지만 나머지는 얻지 못함
I.attr3, I.attr4                        # 인스턴스는 슈퍼클래스 트리로부터 상속
# (3, 4)
C2.attr1, C2.attr2, C2.attr3, C2.attr4  # 클래스는 두 트리로부터 이름을 얻음!
# (1, 2, 3, 4)
M2.attr1, M2.attr2                      # 메타클래스도 이름을 상속받는다!
# (1, 2)


I.__class__                     # __bases__없이 인스턴스에서 따르는 링크
# <class '__main__.C2'>
C2.__bases__
# (<class '__main__.C1'>,)

C2.__class__                    # __bases__ 후에 클래스에서 따르는 링크
# <class '__main__.M2'>
M2.__bases__
# (<class '__main__.M1'>,)

I.__class__.attr1               # 상속을 클래스의 메타크래스 트리에 전달
# 1
I.attr1                         # 그러나 일반적으로 클래스의 __class__를 따르지 않음
# AttributeError: 'C2' object has no attribute 'attr1'

M2.__class__                    # 두 트리는 MRO와 인스턴스 링크를 가짐
# <class 'type'>
[x.__name__ for x in C2.__mro__]        # I.__class__로부터 __bases__ 트리
# ['C2', 'C1', 'object']
[x.__name__ for x in M2.__mro__]        # C2.__class__로부터 __bases__ 트리
# ['M2', 'M1', 'type', 'object']
