# 다중 인스턴스 지원

class Decorator:
    def __init__(self, C):              # @ 데코레이션 시
        self.C = C
    def __call__(self, *args):          # 인스턴스 생성할 때
        self.wrapped = self.C(args)
        return self
    def __getattr__(self, attrname):    # 속성 가져올 때
        return getattr(self.wrapped, attrname)

@Decorator
class C: ...                            # C = Decorator(C)

x = C()
y = C()                                 # x를 덮어씀!


def decorator(C):                       # @ 데코레이션할 때
    class Wrapper:
        def __init__(self, *args):      # 인스턴스 생성할 때: 새로운 Wrapper
            self.wrapped = C(*args)     # 인스턴스에 인스턴스를 내장시킴
    return Wrapper

class Wrapper: ...
def decorator(C):                       # @ 데코레이션할 때
    def onCall(*args):                  # 인스턴스 생성할 때: 새로운 Wrapper
        return Wrapper(C(*args))        # 인스턴스에 인스턴스를 내장시킴
    return onCall
