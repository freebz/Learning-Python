# 첫 번째 예제

class FirstClass:               # 클래스 객체 정의
    def setdata(self, value):   # 클래스의 메서드 정의
        self.data = value       # self는 인스턴스
    def display(self):
        print(self.data)        # self.data: 인스턴스마다 존재함


x = FirstClass()                # 두 개의 인스턴스를 만듦
y = FirstClass()                # 각각은 새로운 네임스페이스임


x.setdata("King Arthur")        # 메서드 호출: self는 x
y.setdata(3.14159)              # FirstClass.setdata(y, 3.14159)를 실행


x.display()                     # self.data는 각 인스턴스마다 다름
# King Arthur
y.display()                     # FirstClass.display(y)를 실행
# 3.14159


x.data = "New value"            # 속성을 가져오거나 설정할 수 있음
x.display()
# New value


x.anothername = "spam"          # 여기서 새로운 속성을 설정할 수도 있음
