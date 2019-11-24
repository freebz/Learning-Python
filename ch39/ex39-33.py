# 3.X에서 연산자 오버로딩 메서드를 재정의하는 방식

def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kargs):
                self.__wrapped = aClass(*args, **kargs)

            # 내장 연산을 구체적으로 잡아내고 위임함
            def __str__(self):
                return str(self.__wrapped)
            def __add__(self, other):
                return self.__wrapped + other            # 또는 getattr(x.'__add__')(y)
            def __getitem__(self, index):
                return self.__wrapped[index]             # 필요한 경우
            def __call__(self, *args, **kargs):
                return self.__wrapped(*args, **kargs)    # 필요한 경우
            # 필요한 내용은 무엇이라도 여기에 추가

            # 일반적으로 이름에 의한 접근을 가로채고 위임함
            def __getattr__(self, attr): ...
            def __setattr__(self, attr, value): ...
        return onInstance
    return onDecorator
