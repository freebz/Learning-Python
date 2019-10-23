# 연산 속성

class DescSquare:
    def __init__(self, start):             # 각 디스크립터는 자신만의 상태를 가짐
        self.value = start
    def __get__(self, instance, owner):    # 속성 가져올 때
        return self.value ** 2
    def __set__(self, instance, value):    # 속성 할당 시
        self.value = value                 # delete나 docs는 없음

class Client1:
    X = DescSquare(3)           # 디스크립터 인스턴스를 클래스 속성에 할당

class Client2:
    X = DescSquare(32)          # 다른 클라이언트 클래스 안의 다른 인스턴스
                                # 두 개의 인스턴스를 동일한 클래스 안에 위치하도록 작성할 수도 있음
c1 = Client1()
c2 = Client2()

print(c1.X)                     # 3 ** 2
c1.X = 4
print(c1.X)                     # 4 ** 2
print(c2.X)                     # 32 ** 2(1024)


# py -3 desc-computed.py
# 9
# 16
# 1024
