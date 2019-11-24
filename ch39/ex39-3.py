# 메서드 데코레이션 지원

class decorator:
    def __init__(self, func):         # func은 인스턴스가 없는 메서드
        self.func = func
    def __call__(self, *args):        # self는 데코레이터 인스턴스
        # self.func(*args)는 실패!    # C 인스턴스는 args에 없다!

class C:
    @decorator
    def method(self, x, y):           # method = decorator(method)
        ...                           # 데코레이터 인스턴스에 재결합


def decorator(F):               # F는 함수 또는 인스턴스가 없는 메서드
    def wrapper(*args):         # 메서드를 위해 args[0]에 클래스 인스턴스
        # F(*args)는 함수 또는 메서드를 실행
    return wrapper

@decorator
def func(x, y):                 # func = decorator(func)
    ...
func(6, 7)                      # 실제로 wrapper(6, 7)를 호출

class C:
    @decorator
    def method(self, x, y):     # method = decorator(method)
        ...                     # 단순 함수에 재결합

X = C()
X.method(6, 7)                  # 실제로 wrapper(X, 6, 7)를 호출
