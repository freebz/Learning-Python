# 연산 속성

class AttrSquare:
    def __init__(self, start):
        self.value = start                 # __setattr__ 촉발!

    def __getattr__(self, attr):           # 정의되지 않은 속성 가져오기
        if attr == 'X':
            return self.value ** 2         # value는 정의되지 않음
        else:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):    # 모든 attr에 대한 할당
        if attr == 'X':
            attr = 'value'
        self.__dict__[attr] = value

A = AttrSquare(3)                          # 두 개의 오버로드된 클래스 인스턴스
B = AttrSquare(32)                         # 각각은 다른 상태 정보를 가짐

print(A.X)                                 # 3 ** 2
A.X = 4
print(A.X)                                 # 4 ** 2
print(B.X)                                 # 32 ** 2(1024)


# py -3 getattr-computed.py
# 9
# 16
# 1024
