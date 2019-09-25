# 파이썬 2.X에서는 용법이 다름: 장황한 호출

class C(object):                # 파이썬 2.X: 새 형식 클래스에서만
    def act(self):
        print('spam')

class D(C):
    def act(self):
        super(D, self).act()    # 2.X: 상이한 호출 형태(너무 복잡해 보임)
        print('eggs')           # 'D'는 'C'의 타입 변경 수준!

X = D()
X.act()
# spam
# eggs


class D(C):
    def act(self):
        super().act()           # 더 단순한 3.X 호출 형태가 2.X에서는 실패
        print('eggs')

X = D()
X.act()
# TypeError: super() takes at least 1 argument (0 given)


class D(C):
    def act(self):
        C.act(self)             # 하지만 전형적인 패턴은 이식성이 좋음
        print('eggs')           # 그리고 2.X 코드에서 종종 더 단순해지기도 함

X = D()
X.act()
# spam
# eggs
