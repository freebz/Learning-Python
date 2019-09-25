# 내장 함수 super: 나아진 것인가 악화된 것인가?

# super에 대한 엄청난 논쟁

# 전형적인 슈퍼클래스 호출 형태: 이식성이 있으며 일반적임

class C:                        # 파이썬 2.X와 3.X에서
    def act(self):
        print('spam')

class D(C):
    def act(self):
        C.act(self)             # 슈퍼클래스의 이름을 명명하고 self를 전달
        print('eggs')

X = D()
X.act()
# spam
# eggs
