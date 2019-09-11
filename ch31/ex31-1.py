# 다형성은 호출 서명이 아니라 인터페이스를 의미

class C:
    def meth(self, x):
        ...
    def meth(self, x, y, z):
        ...


class C:
    def meth(slef, *args):
        if len(args) == 1:            # 숫자 인수 분기
            ...
        elif type(arg[0]) == int:     # 인수 타입(또는 isinstance()) 분기
            ...


class C:
    def meth(self, x):
        x.operation()                 # x가 적절한 일을 한다고 가정
