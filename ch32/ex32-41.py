# 유연성: 호출 순서의 가정

# 만약 메서드 호출 순서의 요구 사항이 MRO와 다르면 어떻게 될까?

class B:
    def __init__(self): print('B.__init__'); super().__init__()
class C:
    def __init__(self): print('C.__init__'); super().__init__()
class D(B, C):
    def __init__(self): print('D.__init__'); C.__init__(self); B.__init__(self)
X = D()
# D.__init__
# C.__init__
# B.__init__
# C.__init__                      # MRO이거나 명시적 호출이거나 둘 중 하나...
