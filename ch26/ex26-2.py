# 연산자 오버로드

class C2: ...                   # 슈퍼클래스 객체를 생성함
class C3: ...

class C1(C2, C3):
    def __init__(self, who):    # 생성 시에 name을 설정
        self.name = who         # self는 I1 또는 I2

I1 = C1('bob')                  # I1.name을 'bob'으로 설정
I2 = C1('sue')                  # I2.name을 'sue'로 설정
print(I1.name)                  # 'bob'이 출력됨
