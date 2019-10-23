# 데코레이터로 프로퍼티 코딩하기

@decorator
def func(args): ...


def func(args): ...
func = decorator(func)


class Person:
    @property
    def name(self): ...         # 다시 바인드: name = property(name)


class Person:
    def name(self): ...
    name = property(name)
