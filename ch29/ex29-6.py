# 상속된 메서드 특수화하기

class Super:
    def method(self):
        print('in Super.method')

class Sub(Super):
    def method(self):                   # 메서드 오버라이드
        print('starting Sub.method')    # 여기에 동작 추가
        Super.method(self)              # 기본 동작 실행
        print('ending Sub.method')


x = Super()                     # Super 인스턴스를 만듦
x.method()                      # Super.method를 실행
# in Super.method

x = Sub()                       # Sub 인스턴스를 만듦
x.method()                      # Sub.method를 호출하면 Super.method가 실행
# starting Sub.method
# in Super.method
# ending Sub.method
