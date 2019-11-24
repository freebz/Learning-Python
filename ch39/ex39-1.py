# 데코레이터 기초

# 함수 데코레이터

# 사용법

@decorator                      # 함수를 데코레이트함
def F(arg):
    ...

F(99)                           # 함수 호출


def F(arg):
    ...
F = decorator(F)                # 함수 이름을 데코레이터 결과에 재결합

F(99)                           # 근본적으로 decorator(F)(99)를 호출


func(6, 7)
decorator(func)(6, 7)


class C:
    @staticmethod
    def meth(...): ...          # meth = staticmethod(meth)

class C:
    @property
    def name(self): ...         # name = property(name)
