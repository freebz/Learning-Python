# 슬롯과 네임스페이스 딕셔너리

class C:                        # 2.X에서만 '(object)'가 필요
    __slots__ = ['a', 'b']      # __slots__은 기본적으로 __dict__가 없음을 의미

X = C()
X.a = 1
X.a
# 1
X.__dict__
# AttributeError: 'C' object has no attribute '__dict__'


getattr(X, 'a')
# 1
setattr(X, 'b', 2)              # 하지만 getattr()과 setattr()은 여전히 동작함
X.b
# 2
'a' in dir(X)                   # 그리고 dir() 또한 슬롯 속성을 발견함
# True
'b' in dir(X)
# True


class D:                        # 2.X에서 동일 결과를 얻으려면 D(object)를 사용
    __slots__ = ['a', 'b']
    def __init__(self):
        self.d = 4              # __dict__가 없다면 새로운 이름을 추가할 수 없음
        
X = D()
# AttributeError: 'D' object has no attribute 'd'


class D:
    __slots__ = ['a', 'b', '__dict__']    # 이름 __dict__ 도 포함
    c = 3                                 # 클래스 속성은 일반적으로 동작
    def __init__(self):
        self.d = 4                        # d는 __dict__에 저장, a는 슬롯임

X = D()
X.d
# 4
X.c
# 3
X.a                             # 모든 인스턴스의 속성은 할당될 때까지는 미정의 상태임
# AttributeError: a
X.a = 1
X.b = 2


X.__dict__                      # 일부 객체는 __dict__와 슬롯 이름 모두를 가짐
# {'d': 4}
X.__slots__                     # getattr()는 두 형태의 속성 모두 가져올 수 있음
# ['a', 'b', '__dict__']
getattr(X, 'a'), getattr(X, 'c'), getattr(X, 'd')        # 세 형태 모두 불러옴
# (1, 3, 4)


for attr in list(X.__dict__) + X.__slots__:    # 잘못된 코드
    print(attr, '=>', getattr(X, attr))


for attr in list(getattr(X, '__dict__', [])) + getattr(X, '__slots__', []):
    print(attr, '=>', getattr(X, attr))

# d => 4
# a => 1                          # 덜 잘못된 코드
# b => 2
# __dict__ => {'d': 4}
