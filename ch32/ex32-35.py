# 제약 사항: 연산자 오버로딩

class C:                        # 파이썬 3.X
    def __getitem__(self, ix):  # 인덱싱 오버로드 메서드
        print('C index')

class D(C):
    def __getitem__(self, ix):  # 여기에서 확장을 위해 재정의
        print('D index')
        C.__getitem__(self, ix) # 전형적인 호출 형태는 동작함
        super().__getitem__(ix) # 직접 이름 호출하는 방식도 동작함
        super()[ix]             # 하지만 연산자는 동작하지 않음!(__getattribute__)

X = C()
X[99]
# C index
X = D()
X[99]
# D index
# C index
# C index
# Traceback (most recent call last):
#   File "", line 1, in <module>
#   File "", line 6, in __getitem__
# TypeError: 'super' object is not subscriptable
