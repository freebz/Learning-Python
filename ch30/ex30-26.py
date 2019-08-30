# 호출식: __call__

class Callee:
    def __call__(self, *pargs, **kargs):    # 인스턴스 호출 가로채기
        print('Called:', pargs, kargs)      # 임의의 인수 받아들이기

C = Callee()
C(1, 2, 3)                                  # C는 호출 가능한 객체
# Called: (1, 2, 3) {}
C(1, 2, 3, x=4, y=5)
# Called: (1, 2, 3) {'x': 4, 'y': 5}


class C:
    def __call__(self, a, b, c=5, d=6): ...  # 일반이면서 기본

class C:
    def __call__(self, *pargs, **kargs): ... # 임의의 인수들과 키워드 인수들을 수집

class C:
    def __call__(self, *pargs, d=6, **kargs): ... # 3.X 의 키워드 전용 인수


X = C()
X(1, 2)                         # 기본값 생략
X(1, 2, 3, 4)                   # 위치적 인수
X(a=1, b=2, d=4)                # 키워드
X(*[1, 2], **dict(c=3, d=4))    # 임의의 인수 풀어내기
X(1, *(2,), c=3, **dict(d=4))   # 혼합 방식


class Prod:
    def __init__(self, value):  # 단 하나의 인수만 받아들임
        self.value = value
    def __call__(self, other):
        return self.value * other

x = Prod(2)                     # 상태 정보에 2를 '기억'
x(3)                            # 3(전달된 인수) * 2(상탯값)
# 6
x(4)
# 8


class Prod:
    def __init__(self, value):
        self.value = value
    def comp(self, other):
        return self.value * other

x = Prod(3)
x.comp(3)
# 9
x.comp(4)
# 12
