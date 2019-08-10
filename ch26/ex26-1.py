# 클래스 트리 코드 작성하기

class C2: ...                   # 클래스 객체를 생성(타원형)
class C3: ...
class C1(C2, C3): ...           # 슈퍼 클래스에 연결(괄호 안의 순서대로)

I1 = C1()                       # 인스턴스 객체를 생성(그림 26-1의 사각형)
I2 = C1()                       # 클래스에 연결됨


class C2: ...                   # 슈퍼클래스 객체를 만듦
class C3: ...

class C1(C2, C3):               # 클래스 C1을 만들고 슈퍼클래스와 연결함
    def setname(self, who):     # 이름 할당: C1.setname
        self.name = who         # self는 I1 또는 I2

I1 = C1()                       # 두 개의 인스턴스를 만듦
I2 = C1()
I1.setname('bob')               # I1.name을 'bob'으로 설정
I2.setname('sue')               # I2.name을 'sue'로 설정
print(i1.name)                  # 'bob'이 출력됨
