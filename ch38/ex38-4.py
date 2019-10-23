# 계산된 속성

class PropSquare:
    def __init__(self, start):
        self.value = start
    def getX(self):             # 속성 반환 시
        return self.value ** 2
    def setX(self, value):      # 속성 할당 시
        self.value = value
    X = property(getX, setX)    # delete와 docs 없음

P = PropSquare(3)               # 프로퍼티를 가진 두 개의 인스턴스
Q = PropSquare(32)              # 각각의 인스턴스는 다른 상태 정보를 가짐

print(P.X)                      # 3 ** 2
P.X = 4
print(P.X)                      # 4 ** 2
print(Q.X)                      # 32 ** 2(1024)


# py -3 prop-computed.py
# 9
# 16
# 1024
