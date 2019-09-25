# 제약 사항: 호출 체인상에 닻 역할이 필요함

class B:
    def __init__(self): print('B.__init__'); super().__init__()
class C:
    def __init__(self): print('C.__init__'); super().__init__()

x = B()                         # object는 MRO 마지막에 오는 암묵적 슈퍼클래스임
# B.__init__
x = C()
# C.__init__

class D(B, C): pass             # B.__init__을 상속, 하지만 B의 MRO는 D와 다름
x = D()                         # B.__init__을 실행, D의 MRO에서 다음 슈퍼클래스는 C
# B.__init__
# C.__init__


B.__mro__
# (<class '__main__.B'>, <class 'object'>)
D.__mro__
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)


class B:
    def __init__(self): print('B.__init__')
class C:
    def __init__(self): print('C.__init__')
class D(B, C):
    def __init__(self): B.__init__(self); C.__init__(self)

x = D()
# B.__init__
# C.__init__
