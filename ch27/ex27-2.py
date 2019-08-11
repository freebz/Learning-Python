# 두 번째 예제

class SecondClass(FirstClass):  # setdata를 상속
    def display(self):          # display 메서드를 변경
        print('Current value = "%s"' % self.data)


z = SecondClass()
z.setdata(42)                   # FirstClass에서 setdata를 찾음
z.display()                     # SecondClass에서 오버라이드된 메서드를 찾음
# Current value = "42"


x.display()                     # x는 여전히 FirstClass 인스턴스임(예전 메시지)
# New value
