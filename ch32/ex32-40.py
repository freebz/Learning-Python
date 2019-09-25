# 범위: 양자택일형 모델(전체이거나 아무것도 아니거나)

class B:
    def __init__(self): print('B.__init__'); super().__init__()
class C:
    def __init__(self): print('C.__init__'); super().__init__()
class D(B, C):
    def __init__(self): print('D.__init__'); super().__init__()
X = D()
# D.__init__
# B.__init__
# C.__init__
D.__mro__
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)

# 만약 super를 호출하지 않는 클래스를 사용해야 한다면 어떻게 될까?

class B:
    def __init__(self): print('B.__init__')
class D(B, C):
    def __init__(self): print('D.__init__'); super().__init__()
X = D()
# D.__init__
# B.__init__                      # 이것은 양자택일형 도구임...
