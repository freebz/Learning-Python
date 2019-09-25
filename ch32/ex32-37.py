# super의 장점: 트리를 변경하고 할당함

# 런타임 클래스 변경과 super

class X:
    def m(self): print('X.m')
class Y:
    def m(self): print('Y.m')
class C(X):                     # X로부터 상속받은 것으로 시작
    def m(self): super().m()    # 여기에 클래스 이름ㅇ르 하드코딩할 수 없음

i = C()
i.m()
# X.m
C.__bases__ = (Y,)              # 런타임에 클래스 이름을 변경!
i.m()
# Y.m


class C(X):
    def m(self): C.__bases__[0].m(self)    # 특별한 경우를 위한 특수 코드

i = C()
i.m()
# X.m
C.__bases__ = (Y,)                         # super() 없이도 동일한 결과
i.m()
# Y.m
