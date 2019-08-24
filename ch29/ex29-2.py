# 예제

class SharedData:
    spam = 42                   # 클래스 데이터 속성을 생성

x = SharedData()                # 클래스 인스턴스를 두 개 만듦
y = SharedData()
x.spam, y.spam                  # 두 인스턴스에서는 'spam'을 상속받고 공유함(SharedData.spam)
# (42, 42)


SharedData.spam = 99
x.spam, y.spam, SharedData.spam
# (99, 99, 99)


x.spam = 88
x.spam, y.spam, SharedData.spam
# (88, 99, 99)


class MixedNames:                            # 클래스 정의
    data = 'spam'                            # 클래스 속성 할당
    def __init__(self, value):               # 메서드 이름 할당
        self.data = value                    # 인스턴스 속성 할당
    def display(self):
        print(self.data, MixedNames.data)    # 인스턴스 속성, 클래스 속성


x = MixedNames(1)               # 두 개의 인스턴스 객체를 만든다
y = MixedNames(2)               # 각각의 인스턴스는 고유의 데이터를 가진다
x.display(); y.display()        # self.data는 다르지만, MixedNames.data는 같다
# 1 spam
# 2 spam
