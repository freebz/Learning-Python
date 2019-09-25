# 속성 가로채기에 미치는 영향

class C:
    data = 'spam'
    def __getattr__(self, name):        # 2.X 고전 형식: 내장된 연산을 잡아냄
        print(name)
        return getattr(self.data, name)

X = C()
X[0]
# __getitem__
# 's'
print(X)                                # 고전 모델은 기본값을 상속받지 않음
# __str__
# spam


class C(object):                        # 2.X와 3.X의 새 형식 클래스
    ...클래스와 나머지 부분은 변경되지 않음...

X = C()
X[0]                                    # 내장된 연산은 getattr로 라우팅되지 않음
# TypeError: 'C' object does not support indexing
print(X)
# <__main__.C object at 0x7f498559ffd0>


class C: pass                   # 2.X 고전 클래스
X = C()
X.normal = lambda: 99
X.normal()
# 99
X.__add__ = lambda y: 88 + y
X.__add__(1)
# 89
X + 1
# 89

class C(object): pass           # 2.X/3.X 새 형식 클래스
X = C()
X.normal = lambda: 99          
X.normal()                      # 일반적인 이름은 여전히 인스턴스로부터
# 99
X.__add__ = lambda y: 88 + y
X.__add__(1)                    # 명시적인 내장된 이름의 경우에도 상동
# 89
X + 1
# TypeError: unsupported operand type(s) for +: 'C' and 'int'


class C(object):
    def __getattr__(self, name): print(name)

X = C()
X.normal                        # 일반적인 이름은 여전히 getattr로 라우팅
# normal
X.__add__                       # 이름으로 직접 호출하는 경우도 동일, 하지만 표현식은 아니다!
# __add__
X + 1
# TypeError: unsupported operand type(s) for +: 'C' and 'int'
