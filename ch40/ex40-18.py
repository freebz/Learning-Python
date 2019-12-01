# 메타클래스 메서드

class A(type):
    def x(cls): print('ax', cls)        # A 메타클래스(인스턴스 = 클래스)
    def y(cls): print('ay', cls)        # y는 인스턴스 B에 의해 오버라이드됨

class B(metaclass=A):
    def y(self): print('by', self)      # A 일반클래스(일반 인스턴스)
    def z(self): print('bz', self)      # 네임스페이스 딕셔너리는 y와 z를 보유

B.x                                     # 메타클래스로부터 획득한 x
# <bound method A.x of <class '__main__.B'>>
B.y                                     # y와 z는 클래스 자체에서 정의됨
# <function B.y at 0x7f85a6d236a8>
B.z
# <function B.z at 0x7f85a6d23730>
B.x()                                   # 메타클래스 메서드 호출: gets cls
# ax <class '__main__.B'>

I = B()                                 # 인스턴스 메서드 호출: get inst
I.y()
# by <__main__.B object at 0x7f85a6d04ba8>
I.z()
# bz <__main__.B object at 0x7f85a6d04ba8>
I.x()                                   # 인스턴스는 메타클래스 이름들을 보지 못함
# AttributeError: 'B' object has no attribute 'x'
