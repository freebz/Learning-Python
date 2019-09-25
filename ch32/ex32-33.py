# super의 기본 용도와 장단점

# 이상한 의미론: 파이썬 3.X에서의 마법의 프록시

class C:                        # 파이썬 3.X에서만(2.X의 super 형태: 이후 내용 참조)
    def act(self):
        print('spam')

class D(C):
    def act(self):
        super().act()           # 일반적으로 슈퍼클래스 참조, self 생략
        print('eggs')

X = D()
X.act()
# spam
# eggs


super                           # 나중에 호출을 라우팅하는 '마법'의 프록시 객체
# <class 'super'>
super()
# RuntimeError: super(): no arguments

class E(C):
    def method(self):           # self는 super에서만 암묵적!
        proxy = super()         # 이 형태는 메서드 외부에서는 의미가 없음
        print(proxy)            # 일반적으로 감춰진 프록시 객체를 보여 줌
        proxy.act()             # 인수가 없음: 암묵적으로 슈퍼클래스 메서드를 호출!
E().method()
# <super: <class 'E'>, <E object>>
# spam
